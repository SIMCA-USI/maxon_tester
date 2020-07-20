import os
import yaml
import queue
from queue import Queue
import socket
import threading
from time import sleep
import epos_motor
from traceback import format_exc
from pynput import keyboard


class Maxon:
    def __init__(self):
        self.ip = None
        self.port = None
        self.conexion_mode = None
        self.cobid = None
        self.socket = None
        self.queue = Queue()
        self.sender_tread = None
        self.freq = 0
        self.rel_speed = 10
        self.maxon_enabled = False
        self.dig_3 = False
        self.dig_4 = False
        self.dict_options = {
            '1': self.init_device,
            '2': self.enable,
            '3': self.disable,
            '4': self.turn_abs,
            '5': self.turn_rel,
            '6': self.fault_reset,
            '7': self.salidas_digitales,
            '0': self.no_function
        }

    def load_config(self, path: str):
        with open(path) as f:
            parameters = yaml.load(f, Loader=yaml.FullLoader)
        self.ip = parameters['ip']
        self.port = parameters['port']
        self.conexion_mode = parameters['conexion_mode']
        self.cobid = parameters['cobid']
        self.freq = parameters['freq']
        self.rel_speed = parameters['rel_speed']
        self.print_parameters()

    @staticmethod
    def select_config():
        os.system('cls')  # Clear console
        files = os.listdir('./config')
        yamlfiles = [n for n in files if n.__contains__('.yaml')]
        if len(yamlfiles) > 1:
            print('Selecciona fichero de configuración:')
            i = 0
            for file in yamlfiles:
                print('{}: {}'.format(i, file))
                i += 1
            try:
                value = input('Seleccione un fichero de configuración (0,1,2,...): ')
                return 'config/' + yamlfiles[int(value)]
            except Exception:
                raise ValueError('El fichero seleccionado no es correcto')
        elif len(yamlfiles) == 1:
            print('Archivo de configuración cargado automáticamente: {}'.format(yamlfiles[0]))
            return 'config/' + yamlfiles[0]
        else:
            raise ValueError('No se encontrarion ficheros de configuración')

    def manual_parameters(self):
        raise ValueError('Function not implemented')

    def print_parameters(self):
        os.system('cls')
        print('La configuracion cargada es:')
        print('ip: {}'.format(self.ip))
        print('port: {}'.format(self.port))
        print('conexion_mode: {}'.format(self.conexion_mode))
        print('cobid: {}'.format(self.cobid))
        print('freq: {}'.format(self.freq))
        print('rel_speed: {}'.format(self.rel_speed))
        input()

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('', self.port + 1))

    def start_sender(self):
        self.connect()
        self.sender_tread = threading.Thread(target=self.send, daemon=True, name='sender-thread')
        self.sender_tread.start()

    def send(self):
        while True:
            try:
                msg = self.queue.get_nowait()
                # if self._log_send.value:
                #     self.logger.debug(f"{hexlify(msg)} --> {self.ip.value}:{self.port.value}")
                assert len(msg) == 13
                self.socket.sendto(msg, (self.ip, self.port))
                sleep(1/self.freq)
            except queue.Empty:
                sleep(1/10)
            except socket.timeout:
                print('time out')
                # self.logger.warning(f"Could not send message after {self.time_out_s.value}s")
            except Exception as exc:
                print(exc.message)

    def init_device(self):
        [self.queue.put(frame) for frame in epos_motor.init_device(self.cobid)]

    def turn_abs(self):
        lis = keyboard.Listener(on_press=self.on_press_esc)
        lis.start()  # start to listen on a separate thread
        while lis.is_alive():
            target = input('Introduzca numero de grados: ') or 0
            if lis.is_alive():
                try:
                    target = int(target)
                    [self.queue.put(frame) for frame in epos_motor.set_angle_value(self.cobid, target, True)]
                except ValueError:
                    print('No es un valor válido')

    def turn_rel(self):
        os.system('cls')
        print('Utilice las flechas para girar <- ->')
        print('Press esc para salir')

        lis = keyboard.Listener(on_press=self.on_press)
        lis.start()  # start to listen on a separate thread
        while lis.is_alive():
            pass

    def on_press(self, key):
        if key == keyboard.Key.esc:
            return False  # stop listener
        elif key == keyboard.Key.left:
            [self.queue.put(frame) for frame in epos_motor.set_angle_value(self.cobid, -self.rel_speed)]
        elif key == keyboard.Key.right:
            [self.queue.put(frame) for frame in epos_motor.set_angle_value(self.cobid, self.rel_speed)]

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

    @staticmethod
    def no_function():
        print('Selecione una opcion valida')
        input()

    def menu(self):
        os.system('cls')  # Clear console
        print('Selecciona una opcion:')
        print('1: Init device')
        print('2: Enable device')
        print('3: Disable device')
        print('4: Girar motor a n grados (absolutos)')
        print('5: Girar motor a n grados (relativos)')
        print('6: Fault reset')
        print('7: Salidas digitales')
        option = input('==>') or '0'
        self.dict_options.get(option, self.dict_options['0'])()

