import os
import struct

import yaml
import queue
from queue import Queue
# import socket
import threading
from time import sleep
from traceback import format_exc
from pynput import keyboard
from connection import Connection
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from interface_maxon import Ui_InterfazMAXON
from PySide2.QtWidgets import *
from new_interface_maxon import Ui_InterfazMAXON
import utils.epos as maxon
import utils.epos4 as epos4
import random
import networkx as nx
from utils.utils import make_can_msg
from utils.filtro import Decoder


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

        self.window.ui.pushButton_openabled.clicked.connect(self.operation_mode)
        self.window.ui.pushButton_swon.clicked.connect(self.switch_on_mode)
        self.window.ui.pushButton_ready.clicked.connect(self.ready_mode)
        self.window.ui.pushButton_swondis.clicked.connect(self.switch_disable_mode)

        self.window.ui.frame_general.setVisible(False)
        self.window.ui.frame_control.setVisible(False)
        self.window.ui.frame_rel.setVisible(False)
        self.window.ui.frame_abs.setVisible(False)
        self.device_type = 'epos4'
        self.cobid = 2
        self.epos_dictionary = {}
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
        self.auto_fault_reset = False
        self.last_position_updated = 0
        self.op_mode = 'PPM'
        self.motor_graph = nx.read_graphml('utils/maxon.graphml')
        self.rpm = 5000
        self.shutdown_flag = False
        # self.decoder = Decoder(dictionary=self.get_parameter('dictionary').value, cobid=self.cobid)
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

    def get_device(self):
        if self.device_type == 'EPOS 4':
            return epos4
        elif self.device_type == 'Maxon':
            return maxon
        return epos4

    def operation_mode(self):
        self.update_state(target=self.get_device().EPOSStatus.Operation_enabled)
        self.change_frame_color(button=4)

    def switch_on_mode(self):
        self.update_state(target=self.get_device().EPOSStatus.Switched_on)
        self.change_frame_color(button=3)

    def switch_disable_mode(self):
        self.update_state(target=self.get_device().EPOSStatus.Switch_on_disabled)
        self.change_frame_color(button=1)

    def ready_mode(self):
        self.update_state(target=self.get_device().EPOSStatus.Ready_to_switch_on)
        self.change_frame_color(button=2)

    def change_frame_color(self, button=0):
        if button == 1:
            self.window.ui.frame_ready.setStyleSheet(u"background-color: rgb(244, 244, 244);")
            self.window.ui.frame_openabled.setStyleSheet(u"background-color: rgb(244, 244, 244);")
            self.window.ui.frame_swon.setStyleSheet(u"background-color: rgb(244, 244, 244);")
            self.window.ui.frame_swondis.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        elif button == 2:
            self.window.ui.frame_ready.setStyleSheet(u"background-color: rgb(85, 255, 127);")
            self.window.ui.frame_openabled.setStyleSheet(u"background-color: rgb(244, 244, 244);")
            self.window.ui.frame_swon.setStyleSheet(u"background-color: rgb(244, 244, 244);")
            self.window.ui.frame_swondis.setStyleSheet(u"background-color: rgb(244, 244, 244);")
        elif button == 3:
            self.window.ui.frame_ready.setStyleSheet(u"background-color: rgb(244, 244, 244);")
            self.window.ui.frame_openabled.setStyleSheet(u"background-color: rgb(244, 244, 244);")
            self.window.ui.frame_swon.setStyleSheet(u"background-color: rgb(85, 255, 127);")
            self.window.ui.frame_swondis.setStyleSheet(u"background-color: rgb(244, 244, 244);")
        elif button == 4:
            self.window.ui.frame_ready.setStyleSheet(u"background-color: rgb(244, 244, 244);")
            self.window.ui.frame_openabled.setStyleSheet(u"background-color: rgb(85, 255, 127);")
            self.window.ui.frame_swon.setStyleSheet(u"background-color: rgb(244, 244, 244);")
            self.window.ui.frame_swondis.setStyleSheet(u"background-color: rgb(244, 244, 244);")
        else:
            self.window.ui.frame_ready.setStyleSheet(u"background-color: rgb(244, 244, 244);")
            self.window.ui.frame_openabled.setStyleSheet(u"background-color: rgb(244, 244, 244);")
            self.window.ui.frame_swon.setStyleSheet(u"background-color: rgb(244, 244, 244);")
            self.window.ui.frame_swondis.setStyleSheet(u"background-color: rgb(244, 244, 244);")

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
            # ip = '127.0.0.1'
            port = self.window.ui.puerto.text()
            self.cobid = int(self.window.ui.comboBox.currentText())
            self.device_type = self.window.ui.comboBox_2.currentText()

            self.connection = Connection(name='Connection', mode='tcp', ip=ip, port=int(port),
                                         deco_function=self.decode_can)
            self.enable_send = True
            self.window.ui.Conectar.setText('Desconectar')
            self.window.ui.frame_general.setVisible(True)
            self.window.ui.frame_control.setVisible(True)
            self.enable_disable_conect(False)
            # self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # self.socket.bind(('', self.port + 1))
        else:
            self.update_state(target=self.get_device().EPOSStatus.Switched_on)
            sleep(0.5)
            self.enable_send = False
            self.connection.shutdown()
            self.connection = None
            self.window.ui.Conectar.setText('Conectar')
            self.window.ui.frame_general.setVisible(False)
            self.window.ui.frame_control.setVisible(False)
            self.enable_disable_conect(True)
            self.change_frame_color(button=0)

    def enable_disable_conect(self, enable):
        self.window.ui.comboBox.setEnabled(enable)
        self.window.ui.comboBox_2.setEnabled(enable)
        self.window.ui.ip.setEnabled(enable)
        self.window.ui.puerto.setEnabled(enable)

    def send(self):
        while not self.shutdown_flag:
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
        msg = self.get_device().init_device(node=self.cobid, rpm=self.rpm)
        [self.queue.put(frame) for frame in msg]

    def reset_position(self, data):
        msg = self.get_device().reset_position(node=self.cobid, position=data.data, prev_mode=self.op_mode,
                                               status_word=self.epos_dictionary.get('Statusword'))
        [self.queue.put(frame) for frame in msg]

    def print_dictionary(self):
        for key, value in self.epos_dictionary.items():
            print(f'{key}: {value}')

    # def read_dictionary(self):
    #     keys = list(self.decoder.dic_parameters.keys())
    #     next_key = (self.last_position_updated + 1) % len(keys)
    #     self.last_position_updated = next_key
    #     key = keys[next_key].split(':')
    #     if 500 < int(key[0]):
    #         key = key + ([0] * (
    #                 3 - len(key)))  # array de longitud 3 relleno de cobid index subindex y los 0's necesarios
    #         msg = [make_can_msg(node=self.cobid, index=int(key[1]), sub_index=int(key[2]), write=False)]
    #         [self.queue.put(frame) for frame in msg]
    #         # print(f'Read {hex(int(key[1]))}:{hex(int(key[2]))}')

    def update_state(self, target=None, fault=False, fault_reset=False):
        if target is None:
            target = self.get_device().EPOSStatus.Switched_on
        device = self.get_device()
        status = self.get_device().get_status_from_dict(self.epos_dictionary)
        fault_mode = (status == device.EPOSStatus.Fault or status == device.EPOSStatus.Fault_reaction_active)
        if self.auto_fault_reset or fault_reset or (not fault_mode and not fault):
            if fault_reset:
                print('Reset fault')
            msg = device.set_state(node=self.cobid, target_state=target, graph=self.motor_graph,
                                   status_word=self.epos_dictionary.get('Statusword') if not fault else None)
            if msg is not None:
                [self.queue.put(frame) for frame in msg]
            self.informed_fault = False

    def turn_abs(self):
        try:
            target = int(self.window.ui.giro_text.text())
            [self.queue.put(frame) for frame in self.get_device().set_angle_value(self.cobid, target, True)]
        except ValueError:
            print('No es un valor válido')

    def giro_izq(self):
        giro = self.dict_slider.get(self.window.ui.slider_giro.value(), self.dict_slider[0])
        self.giro_relativo -= giro
        [self.queue.put(frame) for frame in self.get_device().set_angle_value(self.cobid, -giro)]
        self.window.ui.label_giro_relativo.setText(str(self.giro_relativo))

    def giro_dch(self):
        giro = self.dict_slider.get(self.window.ui.slider_giro.value(), self.dict_slider[0])
        self.giro_relativo += giro
        [self.queue.put(frame) for frame in self.get_device().set_angle_value(self.cobid, giro)]
        self.window.ui.label_giro_relativo.setText(str(self.giro_relativo))

    def enderezar(self):
        [self.queue.put(frame) for frame in self.get_device().set_angle_value(self.cobid, -self.giro_relativo)]
        self.giro_relativo = 0
        self.window.ui.label_giro_relativo.setText(str(self.giro_relativo))

    def update_steering(self):
        while not self.shutdown_flag:
            self.window.ui.label_volante.setText(str(self.steering_value))
            sleep(1 / 10)

    def on_press_esc(self, key):
        if key == keyboard.Key.esc:
            return False  # stop listener

    def enable(self):
        if self.device_type == 'Maxon':
            try:
                [self.queue.put(frame) for frame in self.get_device().set_digital(self.cobid, {4: True})]
                # self.update_state(target=device.EPOSStatus.Operation_enabled)
                #     if not self.maxon_enabled:
                #         [self.queue.put(frame) for frame in epos_motor.init_device(self.cobid)]
                #         [self.queue.put(frame) for frame in epos_motor.enable(self.cobid)]
                #         [self.queue.put(frame) for frame in epos_motor.enable_digital_4(self.cobid)]
                #         self.maxon_enabled = True
            except Exception:
                print(format_exc())
        else:
            print('No se puede activar el electroiman con una epos4')

    def disable(self):
        try:
            [self.queue.put(frame) for frame in self.get_device().set_digital(self.cobid, {4: False})]
            # self.update_state(target=device.EPOSStatus.Switched_on)
            # if self.maxon_enabled:
            #     [self.queue.put(frame) for frame in epos_motor.disable(self.cobid)]
            #     [self.queue.put(frame) for frame in epos_motor.disable_digital_4(self.cobid)]
            #     self.maxon_enabled = False
        except Exception:
            print(format_exc())

    def fault_reset(self):
        try:
            print('Send fault reset')
            [self.queue.put(frame) for frame in self.get_device().fault_reset(self.cobid)]
        except Exception:
            print(format_exc())

    def reset_rel(self):
        self.giro_relativo = 0
        self.window.ui.label_giro_relativo.setText(str(self.giro_relativo))

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
