from maxon import Maxon, Window
from PyQt5 import QtWidgets
import sys


def main():
    try:
        app = QtWidgets.QApplication(sys.argv)
        gui = Window()
        maxon = Maxon(main_window=gui)
        gui.show()
        app.exec_()
    except KeyboardInterrupt:
        print('Keyboard interrupt')


if __name__ == '__main__':
    main()
