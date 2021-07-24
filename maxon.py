import os
import struct

import yaml
import queue
from queue import Queue
# import socket
import threading
from time import sleep
import epos_motor
from traceback import format_exc
from pynput import keyboard
from connection import Connection
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface_maxon import Ui_InterfazMAXON
import random


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_InterfazMAXON()
        self.ui.setupUi(self)


class Maxon:
    def __init__(self, main_window: Window = None):
        self.window = main_window
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

        self.cobid = 3
        # self.socket = None
        self.connection = None
        self.steering_value = 0
        self.queue = Queue()
        self.giro_relativo = 0
        self.enable_send = False
        self.freq = 50
        self.rel_speed = 10
        self.maxon_enabled = False
        self.dig_3 = False
        self.dig_4 = False
        self.rpm = 5000
        self.sender_thread = threading.Thread(target=self.send, daemon=True, name='sender-thread')
        self.sender_thread.start()
        self.update_volante = threading.Thread(target=self.update_steering, daemon=True, name='update-steering')
        self.update_volante.start()
        self.dict_slider = {
            0: 1,
            1: 5,
            2: 10,
            3: 20,
            4: 50,
            5: 360,
        }

    def decode_can(self, msg):
        try:
            COBID = (msg[2] << 8) + msg[3]
            if COBID == 0x305:
                # os.system('cls')
                data = struct.unpack('>h', msg[4:6])[0]
                # print(msg)
                value = data * 0.13
                self.steering_value = value
                # self.steering_value = random.randint(-350, 350) # Para pruebas
        except Exception as e:
            pass

    def connect(self):
        if self.connection is None:
            ip = self.window.ui.ip.text()
            ip = '127.0.0.1'
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

    def send(self):
        while True:
            try:
                if self.enable_send:
                    msg = self.queue.get_nowait()
                    # if self._log_send.value:
                    #     self.logger.debug(f"{hexlify(msg)} --> {self.ip.value}:{self.port.value}")
                    assert len(msg) == 13
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
        while(True):
            self.window.ui.label_volante.setText(str(self.steering_value))
            sleep(1/10)

    def on_press_esc(self, key):
        if key == keyboard.Key.esc:
            return False  # stop listener

    def enable(self):
        try:
            if not self.maxon_enabled:
                [self.queue.put(frame) for frame in epos_motor.init_device(self.cobid)]
                [self.queue.put(frame) for frame in epos_motor.enable(self.cobid)]
                [self.queue.put(frame) for frame in epos_motor.enable_digital_4(self.cobid)]
                self.maxon_enabled = True
        except Exception:
            print(format_exc())

    def disable(self):
        try:
            if self.maxon_enabled:
                [self.queue.put(frame) for frame in epos_motor.disable(self.cobid)]
                [self.queue.put(frame) for frame in epos_motor.disable_digital_4(self.cobid)]
                self.maxon_enabled = False
        except Exception:
            print(format_exc())

    def fault_reset(self):
        try:
            [self.queue.put(frame) for frame in epos_motor.fault_reset(self.cobid)]
        except Exception:
            print(format_exc())

    def reset_rel(self):
        self.giro_relativo = 0

    def rel(self):
        if not self.window.ui.frame_rel.isVisible():
            self.reset_rel()
            self.window.ui.frame_rel.setVisible(True)
            self.window.ui.frame_abs.setVisible(False)
        else:
            self.window.ui.frame_rel.setVisible(False)

    def abs(self):
        if not self.window.ui.frame_abs.isVisible():
            self.window.ui.frame_rel.setVisible(False)
            self.window.ui.frame_abs.setVisible(True)
        else:
            self.window.ui.frame_abs.setVisible(False)

    def salidas_digitales(self):
        lis = keyboard.Listener(on_press=self.on_press_esc)
        lis.start()  # start to listen on a separate thread
        while lis.is_alive():
            os.system('cls')  # Clear console
            print('Para encender o apagar una salida digital indique el numero de salida')
            print('Para salir pulse Esc')
            print('Estado de las salidas digitales:')
            print('Digital 3: {}'.format('on' if self.dig_3 else 'off'))
            print('Digital 4: {}'.format('on' if self.dig_4 else 'off'))
            target = input('Introduzca salida digital: ') or 0
            if lis.is_alive():
                try:
                    target = int(target)
                    if target == 3:
                        if self.dig_3:
                            [self.queue.put(frame) for frame in epos_motor.disable_digital_3(self.cobid)]
                            self.dig_3 = False
                        else:
                            [self.queue.put(frame) for frame in epos_motor.enable_digital_3(self.cobid)]
                            self.dig_3 = True
                    elif target == 4:
                        if self.dig_4:
                            [self.queue.put(frame) for frame in epos_motor.disable_digital_4(self.cobid)]
                            self.dig_4 = False
                        else:
                            [self.queue.put(frame) for frame in epos_motor.enable_digital_4(self.cobid)]
                            self.dig_4 = True
                    else:
                        raise ValueError('No existe esta salida digital')
                except ValueError as ve:
                    print(ve)
