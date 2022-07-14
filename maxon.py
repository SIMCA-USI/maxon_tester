import queue
import struct
import threading
from queue import Queue
from time import sleep
from traceback import format_exc

import yaml
from PyQt5.QtWidgets import QMainWindow

import epos_motor
from connection import Connection
from interface_maxon import Ui_InterfazMAXON
from common import make_can_frame
from pynput import keyboard
from binascii import hexlify
from typing import Tuple


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_InterfazMAXON()
        self.ui.setupUi(self)


def decoder_maxon(msg) -> Tuple[bytes, int, int, int, bytes]:
    msg = msg[2:-1]  # Se elimina el pad delantero (2) y trasero (1) de la trama
    COBID = struct.unpack('>H', msg[0:2])[0]
    b0 = msg[2:3]
    index = struct.unpack('<H', msg[3:5])[0]
    sub_index = struct.unpack('B', msg[5:6])[0]
    data = msg[6:]
    # print(f'{COBID} {index} {sub_index} {len(data)} {data}')
    return msg, COBID, index, sub_index, data


class Maxon:
    def __init__(self, main_window: Window = None):
        self.window = main_window
        self.window.ui.frame_general.setVisible(False)
        self.window.ui.frame_rel.setVisible(False)
        self.window.ui.frame_abs.setVisible(False)
        self.window.ui.Conectar.clicked.connect(self.connect)
        self.window.ui.init_button.clicked.connect(self.init_device)
        self.window.ui.fault_button.clicked.connect(self.fault_reset)
        self.window.ui.enable_button.clicked.connect(self.enable)
        self.window.ui.disable_button.clicked.connect(self.disable)
        self.window.ui.rel_button.clicked.connect(self.rel)
        self.window.ui.abs_button.clicked.connect(self.abs)
        self.window.ui.girar_button.clicked.connect(self.turn_abs)

        self.window.ui.giro_izq.clicked.connect(self.giro_izq)
        self.window.ui.giro_dch.clicked.connect(self.giro_dch)
        self.window.ui.enderezar.clicked.connect(self.enderezar)

        self.window.ui.reset_rel.clicked.connect(self.reset_rel)
        self.window.ui.speed_button.clicked.connect(self.change_speed)
        self.window.ui.following_button.clicked.connect(self.change_following)
        self.window.ui.reset_encoder_button.clicked.connect(self.ajustar_volante)

        self.window.ui.press.clicked.connect(self.press)
        self.window.ui.release.clicked.connect(self.release)

        with open('config/config.yaml') as f:
            parameters = yaml.load(f, Loader=yaml.FullLoader)
        self.error_encoder = parameters['error_encoder']
        self.window.ui.ip.setText(parameters['ip'])
        self.window.ui.puerto.setText(str(parameters['puerto']))

        self.listener_keyboard = None

        self.shutdown_flag = False
        self.cobid = parameters['cobid']

        self.connection = None
        self.steering_value = 0
        self.queue = Queue()
        self.giro_relativo = 0
        self.enable_send = False
        self.freq = 50
        self.maxon_enabled = False
        self.dig_3 = False
        self.dig_4 = False
        self.rpm = 5000
        self.sender_thread = threading.Thread(target=self.send, daemon=True, name='sender-thread')
        self.sender_thread.start()
        self.status_thread = threading.Thread(target=self.read_status, daemon=True, name='sender-thread')
        # self.status_thread.start()
        self.update_volante = threading.Thread(target=self.update_steering, daemon=True, name='update-steering')
        # self.update_volante.start()
        self.dict_slider = {
            0: 1,
            1: 5,
            2: 10,
            3: 20,
            4: 50,
            5: 360,
        }

    def read_status(self):
        while not self.shutdown_flag:
            if self.connection is not None and self.connection.connected:
                [self.queue.put(frame) for frame in [make_can_frame(self.cobid, 0x6041, 0, 0, write=False)]]
                [self.queue.put(frame) for frame in [make_can_frame(self.cobid, 0x6064, 0, 0, write=False)]]
                [self.queue.put(frame) for frame in [make_can_frame(self.cobid, 0x30D3, 0x01, 0, write=False)]]
            sleep(1 / 5)

    def change_speed(self):
        new_speed = self.window.ui.speed_text.text()
        self.rpm = int(new_speed)
        [self.queue.put(frame) for frame in [make_can_frame(self.cobid, 0x6081, 0, self.rpm)]]

    def change_following(self):
        new_following = int(self.window.ui.following_text.text())
        [self.queue.put(frame) for frame in [make_can_frame(self.cobid, 0x6065, 0, new_following)]]

    def decode_can(self, msg: bytes):
        try:
            COBID = struct.unpack('>h', msg[2:4])[0]
            print(hex(COBID))
            if COBID == 0x305:
                # os.system('cls')
                data = struct.unpack('>h', msg[4:6])[0]
                # print(msg)
                value = data * 0.13
                self.steering_value = round(value - self.error_encoder, 2)
                # self.steering_value = random.randint(-350, 350) # Para pruebas
            elif 0x580 < COBID < 0x590 or 0x80 < COBID < 0x90:
                # print(f'Maxon {COBID & 0xF}') #TODO
                msg, COBID, index, sub_index, data = decoder_maxon(msg)
                # print(f'COBID {hex(COBID)} {hexlify(msg)}')
                # print(f'COBID {hex(COBID)}')
                # print(f'index {hex(index)}')
                # print(f'sub_index {hex(sub_index)}')
                # print(f'data {hexlify(data)}\n')
                if index == 0x6041:
                    status = struct.unpack('>H', data[:2])[0]
                    print(status)
                elif index == 0x6064:
                    position = struct.unpack('<i', data)[0]
                    # print(f'Position {position}')
                    self.window.ui.label_position.setText(str(position))
                elif index == 0x30D3:
                    if sub_index == 0x01:
                        velocidad = struct.unpack('<i', data)[0]
                        self.window.ui.label_rpm.setText(str(velocidad))
                        # print(f'Velocidad {velocidad}')
            else:
                pass
                # print(f'COBID{hex(COBID)} {hexlify(msg)}')
        except Exception as e:
            print(e)

    def connect(self):
        if self.connection is None:
            ip = self.window.ui.ip.text()
            # ip = '127.0.0.1'
            port = self.window.ui.puerto.text()
            self.connection = Connection(name='Connection', mode='tcp', ip=ip, port=int(port),
                                         deco_function=self.decode_can)
            self.enable_send = True
            self.window.ui.Conectar.setText('Desconectar')
            self.window.ui.frame_general.setVisible(True)
            # self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # self.socket.bind(('', self.port + 1))
        else:
            self.enable_send = False
            self.connection.shutdown()
            self.connection = None
            self.window.ui.Conectar.setText('Conectar')
            self.window.ui.frame_general.setVisible(False)
            self.window.ui.frame_rel.setVisible(False)
            self.window.ui.frame_abs.setVisible(False)

    def send(self):
        while True:
            try:
                if self.enable_send:
                    msg = self.queue.get_nowait()
                    # if self._log_send.value:
                    #     self.logger.debug(f"{hexlify(msg)} --> {self.ip.value}:{self.port.value}")
                    assert len(msg) == 13
                    print('sent')
                    self.connection.send(msg)
                    # self.socket.sendto(msg, (self.ip, self.port))
                sleep(1 / self.freq)
            except queue.Empty:
                sleep(1 / 10)
            # except socket.timeout:
            #     print('time out')
            #     # self.logger.warning(f"Could not send message after {self.time_out_s.value}s")
            except Exception as exc:
                print('exception')
                print(exc)

    def init_device(self):
        [self.queue.put(frame) for frame in epos_motor.init_device(self.cobid, self.rpm)]
        self.window.ui.speed_text.setText('5000')
        self.window.ui.following_text.setText('2000')

    def press(self):
        try:
            [self.queue.put(frame) for frame in epos_motor.set_angle_value(self.cobid, 1200, True)]
        except Exception:
            pass

    def release(self):
        try:
            [self.queue.put(frame) for frame in epos_motor.set_angle_value(self.cobid, 0, True)]
        except Exception:
            pass

    def turn_abs(self):
        try:
            target = int(self.window.ui.giro_text.text())
            [self.queue.put(frame) for frame in epos_motor.set_angle_value(self.cobid, target, True)]
        except ValueError:
            print('No es un valor válido')

    def giro_izq(self):
        giro = self.dict_slider.get(self.window.ui.slider_giro.value(), self.dict_slider[0])
        self.giro_relativo -= giro
        [self.queue.put(frame) for frame in epos_motor.set_angle_value(self.cobid, -giro)]
        self.window.ui.label_giro_relativo.setText(str(self.giro_relativo))

    def giro_dch(self):
        giro = self.dict_slider.get(self.window.ui.slider_giro.value(), self.dict_slider[0])
        self.giro_relativo += giro
        [self.queue.put(frame) for frame in epos_motor.set_angle_value(self.cobid, giro)]
        self.window.ui.label_giro_relativo.setText(str(self.giro_relativo))

    def enderezar(self):
        [self.queue.put(frame) for frame in epos_motor.set_angle_value(self.cobid, -self.giro_relativo)]
        self.giro_relativo = 0
        self.window.ui.label_giro_relativo.setText(str(self.giro_relativo))

    def update_steering(self):
        while not self.shutdown_flag:
            self.window.ui.label_volante.setText(str(self.steering_value))
            sleep(1 / 10)

    def ajustar_volante(self):
        self.error_encoder += self.steering_value

    def enable(self):
        try:
            if not self.maxon_enabled:
                [self.queue.put(frame) for frame in epos_motor.init_device(self.cobid)]
                [self.queue.put(frame) for frame in epos_motor.enable(self.cobid)]
                [self.queue.put(frame) for frame in epos_motor.enable_digital_1(self.cobid)]
                self.maxon_enabled = True
        except Exception:
            print(format_exc())

    def disable(self):
        try:
            if self.maxon_enabled:
                [self.queue.put(frame) for frame in epos_motor.disable(self.cobid)]
                [self.queue.put(frame) for frame in epos_motor.disable_digital_1(self.cobid)]
                self.maxon_enabled = False
        except Exception:
            print(format_exc())

    def fault_reset(self):
        try:
            print(self.cobid)
            [self.queue.put(frame) for frame in epos_motor.fault_reset(self.cobid)]
            self.window.ui.speed_text.setText('5000')
            self.window.ui.following_text.setText('2000')
        except Exception:
            print(format_exc())

    def reset_rel(self):
        self.giro_relativo = 0
        self.window.ui.label_giro_relativo.setText(str(self.giro_relativo))

    def rel(self):
        if not self.window.ui.frame_rel.isVisible():
            self.reset_rel()
            self.listener_keyboard = keyboard.Listener(on_press=self.on_press)
            self.listener_keyboard.start()
            self.window.ui.frame_rel.setVisible(True)
            self.window.ui.frame_abs.setVisible(False)
        else:
            self.listener_keyboard.stop()
            self.window.ui.frame_rel.setVisible(False)

    def on_press(self, key):
        if key == keyboard.Key.left:
            self.giro_izq()
        elif key == keyboard.Key.right:
            self.giro_dch()
        elif key == keyboard.Key.down:
            self.enderezar()

    def abs(self):
        if not self.window.ui.frame_abs.isVisible():
            self.window.ui.frame_rel.setVisible(False)
            self.window.ui.frame_abs.setVisible(True)
            if self.listener_keyboard is not None:
                self.listener_keyboard.stop()
        else:
            self.window.ui.frame_abs.setVisible(False)

    # def salidas_digitales(self):
    #     lis = keyboard.Listener(on_press=self.on_press_esc)
    #     lis.start()  # start to listen on a separate thread
    #     while lis.is_alive():
    #         os.system('cls')  # Clear console
    #         print('Para encender o apagar una salida digital indique el numero de salida')
    #         print('Para salir pulse Esc')
    #         print('Estado de las salidas digitales:')
    #         print('Digital 3: {}'.format('on' if self.dig_3 else 'off'))
    #         print('Digital 4: {}'.format('on' if self.dig_4 else 'off'))
    #         target = input('Introduzca salida digital: ') or 0
    #         if lis.is_alive():
    #             try:
    #                 target = int(target)
    #                 if target == 3:
    #                     if self.dig_3:
    #                         [self.queue.put(frame) for frame in epos_motor.disable_digital_3(self.cobid)]
    #                         self.dig_3 = False
    #                     else:
    #                         [self.queue.put(frame) for frame in epos_motor.enable_digital_3(self.cobid)]
    #                         self.dig_3 = True
    #                 elif target == 4:
    #                     if self.dig_4:
    #                         [self.queue.put(frame) for frame in epos_motor.disable_digital_4(self.cobid)]
    #                         self.dig_4 = False
    #                     else:
    #                         [self.queue.put(frame) for frame in epos_motor.enable_digital_4(self.cobid)]
    #                         self.dig_4 = True
    #                 else:
    #                     raise ValueError('No existe esta salida digital')
    #             except ValueError as ve:
    #                 print(ve)

    def shutdown(self):
        self.shutdown_flag = True
        if self.connection is not None:
            self.connection.shutdown()
