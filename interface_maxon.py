# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_maxon.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InterfazMAXON(object):
    def setupUi(self, InterfazMAXON):
        InterfazMAXON.setObjectName("InterfazMAXON")
        InterfazMAXON.resize(784, 600)
        self.interfaz = QtWidgets.QWidget(InterfazMAXON)
        self.interfaz.setObjectName("interfaz")
        self.frame_general = QtWidgets.QFrame(self.interfaz)
        self.frame_general.setEnabled(True)
        self.frame_general.setGeometry(QtCore.QRect(20, 10, 761, 581))
        self.frame_general.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_general.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_general.setObjectName("frame_general")
        self.init_button = QtWidgets.QPushButton(self.frame_general)
        self.init_button.setGeometry(QtCore.QRect(20, 80, 151, 51))
        self.init_button.setObjectName("init_button")
        self.frame_12 = QtWidgets.QFrame(self.frame_general)
        self.frame_12.setGeometry(QtCore.QRect(0, 140, 191, 341))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_3.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fault_button = QtWidgets.QPushButton(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fault_button.sizePolicy().hasHeightForWidth())
        self.fault_button.setSizePolicy(sizePolicy)
        self.fault_button.setObjectName("fault_button")
        self.verticalLayout_3.addWidget(self.fault_button)
        self.enable_button = QtWidgets.QPushButton(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enable_button.sizePolicy().hasHeightForWidth())
        self.enable_button.setSizePolicy(sizePolicy)
        self.enable_button.setObjectName("enable_button")
        self.verticalLayout_3.addWidget(self.enable_button)
        self.disable_button = QtWidgets.QPushButton(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disable_button.sizePolicy().hasHeightForWidth())
        self.disable_button.setSizePolicy(sizePolicy)
        self.disable_button.setObjectName("disable_button")
        self.verticalLayout_3.addWidget(self.disable_button)
        self.rel_button = QtWidgets.QPushButton(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rel_button.sizePolicy().hasHeightForWidth())
        self.rel_button.setSizePolicy(sizePolicy)
        self.rel_button.setObjectName("rel_button")
        self.verticalLayout_3.addWidget(self.rel_button)
        self.abs_button = QtWidgets.QPushButton(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.abs_button.sizePolicy().hasHeightForWidth())
        self.abs_button.setSizePolicy(sizePolicy)
        self.abs_button.setObjectName("abs_button")
        self.verticalLayout_3.addWidget(self.abs_button)
        self.frame_following = QtWidgets.QFrame(self.frame_general)
        self.frame_following.setGeometry(QtCore.QRect(0, 530, 369, 52))
        self.frame_following.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_following.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_following.setObjectName("frame_following")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_following)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_9 = QtWidgets.QLabel(self.frame_following)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.following_text = QtWidgets.QLineEdit(self.frame_following)
        self.following_text.setAlignment(QtCore.Qt.AlignCenter)
        self.following_text.setObjectName("following_text")
        self.horizontalLayout.addWidget(self.following_text)
        self.following_button = QtWidgets.QPushButton(self.frame_following)
        self.following_button.setObjectName("following_button")
        self.horizontalLayout.addWidget(self.following_button)
        self.frame_speed = QtWidgets.QFrame(self.frame_general)
        self.frame_speed.setGeometry(QtCore.QRect(0, 480, 369, 52))
        self.frame_speed.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_speed.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_speed.setObjectName("frame_speed")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_speed)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.frame_speed)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.speed_text = QtWidgets.QLineEdit(self.frame_speed)
        self.speed_text.setAlignment(QtCore.Qt.AlignCenter)
        self.speed_text.setObjectName("speed_text")
        self.horizontalLayout_3.addWidget(self.speed_text)
        self.speed_button = QtWidgets.QPushButton(self.frame_speed)
        self.speed_button.setObjectName("speed_button")
        self.horizontalLayout_3.addWidget(self.speed_button)
        self.label_volante = QtWidgets.QLabel(self.frame_general)
        self.label_volante.setGeometry(QtCore.QRect(530, 10, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_volante.setFont(font)
        self.label_volante.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_volante.setObjectName("label_volante")
        self.label_volante_2 = QtWidgets.QLabel(self.frame_general)
        self.label_volante_2.setGeometry(QtCore.QRect(610, 10, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_volante_2.setFont(font)
        self.label_volante_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_volante_2.setObjectName("label_volante_2")
        self.reset_encoder_button = QtWidgets.QPushButton(self.frame_general)
        self.reset_encoder_button.setGeometry(QtCore.QRect(650, 20, 93, 28))
        self.reset_encoder_button.setObjectName("reset_encoder_button")
        self.label_volante_3 = QtWidgets.QLabel(self.frame_general)
        self.label_volante_3.setGeometry(QtCore.QRect(740, 170, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_volante_3.setFont(font)
        self.label_volante_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_volante_3.setObjectName("label_volante_3")
        self.widget = QtWidgets.QWidget(self.frame_general)
        self.widget.setGeometry(QtCore.QRect(400, 510, 301, 43))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_position = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_position.sizePolicy().hasHeightForWidth())
        self.label_position.setSizePolicy(sizePolicy)
        self.label_position.setMinimumSize(QtCore.QSize(101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_position.setFont(font)
        self.label_position.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_position.setObjectName("label_position")
        self.horizontalLayout_4.addWidget(self.label_position)
        self.label_volante_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_volante_6.setFont(font)
        self.label_volante_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_volante_6.setObjectName("label_volante_6")
        self.horizontalLayout_4.addWidget(self.label_volante_6)
        self.label_rpm = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rpm.sizePolicy().hasHeightForWidth())
        self.label_rpm.setSizePolicy(sizePolicy)
        self.label_rpm.setMinimumSize(QtCore.QSize(101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_rpm.setFont(font)
        self.label_rpm.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_rpm.setObjectName("label_rpm")
        self.horizontalLayout_4.addWidget(self.label_rpm)
        self.label_volante_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_volante_7.setFont(font)
        self.label_volante_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_volante_7.setObjectName("label_volante_7")
        self.horizontalLayout_4.addWidget(self.label_volante_7)
        self.init_button.raise_()
        self.frame_12.raise_()
        self.label_volante.raise_()
        self.label_volante_2.raise_()
        self.frame_speed.raise_()
        self.frame_following.raise_()
        self.reset_encoder_button.raise_()
        self.label_volante_3.raise_()
        self.label_position.raise_()
        self.label_volante_6.raise_()
        self.label_volante_7.raise_()
        self.label_rpm.raise_()
        self.Conectar = QtWidgets.QPushButton(self.interfaz)
        self.Conectar.setGeometry(QtCore.QRect(400, 30, 93, 22))
        self.Conectar.setObjectName("Conectar")
        self.frame_conexion = QtWidgets.QFrame(self.interfaz)
        self.frame_conexion.setEnabled(True)
        self.frame_conexion.setGeometry(QtCore.QRect(20, 10, 373, 63))
        self.frame_conexion.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_conexion.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_conexion.setObjectName("frame_conexion")
        self.puerto = QtWidgets.QLineEdit(self.frame_conexion)
        self.puerto.setGeometry(QtCore.QRect(230, 20, 111, 22))
        self.puerto.setAlignment(QtCore.Qt.AlignCenter)
        self.puerto.setObjectName("puerto")
        self.ip = QtWidgets.QLineEdit(self.frame_conexion)
        self.ip.setGeometry(QtCore.QRect(57, 20, 110, 22))
        self.ip.setAlignment(QtCore.Qt.AlignCenter)
        self.ip.setObjectName("ip")
        self.label_4 = QtWidgets.QLabel(self.frame_conexion)
        self.label_4.setGeometry(QtCore.QRect(174, 2, 49, 59))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.frame_conexion)
        self.label_3.setGeometry(QtCore.QRect(32, 2, 18, 59))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame_rel = QtWidgets.QFrame(self.interfaz)
        self.frame_rel.setEnabled(True)
        self.frame_rel.setGeometry(QtCore.QRect(210, 80, 571, 411))
        self.frame_rel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_rel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_rel.setObjectName("frame_rel")
        self.frame_5 = QtWidgets.QFrame(self.frame_rel)
        self.frame_5.setEnabled(True)
        self.frame_5.setGeometry(QtCore.QRect(397, 0, 171, 411))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.frame)
        self.slider_giro = QtWidgets.QSlider(self.frame_3)
        self.slider_giro.setMaximum(5)
        self.slider_giro.setOrientation(QtCore.Qt.Vertical)
        self.slider_giro.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.slider_giro.setTickInterval(1)
        self.slider_giro.setObjectName("slider_giro")
        self.horizontalLayout_2.addWidget(self.slider_giro)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.giro_dch = QtWidgets.QPushButton(self.frame_rel)
        self.giro_dch.setGeometry(QtCore.QRect(220, 180, 131, 61))
        self.giro_dch.setObjectName("giro_dch")
        self.giro_izq = QtWidgets.QPushButton(self.frame_rel)
        self.giro_izq.setGeometry(QtCore.QRect(70, 180, 131, 61))
        self.giro_izq.setObjectName("giro_izq")
        self.enderezar = QtWidgets.QPushButton(self.frame_rel)
        self.enderezar.setGeometry(QtCore.QRect(130, 260, 161, 71))
        self.enderezar.setObjectName("enderezar")
        self.reset_rel = QtWidgets.QPushButton(self.frame_rel)
        self.reset_rel.setGeometry(QtCore.QRect(290, 60, 93, 28))
        self.reset_rel.setObjectName("reset_rel")
        self.label_volante_4 = QtWidgets.QLabel(self.frame_rel)
        self.label_volante_4.setGeometry(QtCore.QRect(220, 100, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_volante_4.setFont(font)
        self.label_volante_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_volante_4.setObjectName("label_volante_4")
        self.label_giro_relativo = QtWidgets.QLabel(self.frame_rel)
        self.label_giro_relativo.setGeometry(QtCore.QRect(140, 100, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_giro_relativo.setFont(font)
        self.label_giro_relativo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_giro_relativo.setObjectName("label_giro_relativo")
        self.frame_abs = QtWidgets.QFrame(self.interfaz)
        self.frame_abs.setEnabled(True)
        self.frame_abs.setGeometry(QtCore.QRect(210, 80, 401, 411))
        self.frame_abs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_abs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_abs.setObjectName("frame_abs")
        self.girar_button = QtWidgets.QPushButton(self.frame_abs)
        self.girar_button.setGeometry(QtCore.QRect(120, 200, 161, 71))
        self.girar_button.setObjectName("girar_button")
        self.giro_text = QtWidgets.QLineEdit(self.frame_abs)
        self.giro_text.setGeometry(QtCore.QRect(120, 140, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.giro_text.setFont(font)
        self.giro_text.setAlignment(QtCore.Qt.AlignCenter)
        self.giro_text.setObjectName("giro_text")
        self.press = QtWidgets.QPushButton(self.frame_abs)
        self.press.setGeometry(QtCore.QRect(230, 340, 93, 28))
        self.press.setObjectName("press")
        self.release = QtWidgets.QPushButton(self.frame_abs)
        self.release.setGeometry(QtCore.QRect(80, 340, 93, 28))
        self.release.setObjectName("release")
        self.frame_general.raise_()
        self.frame_rel.raise_()
        self.frame_conexion.raise_()
        self.Conectar.raise_()
        self.frame_abs.raise_()
        InterfazMAXON.setCentralWidget(self.interfaz)

        self.retranslateUi(InterfazMAXON)
        QtCore.QMetaObject.connectSlotsByName(InterfazMAXON)

    def retranslateUi(self, InterfazMAXON):
        _translate = QtCore.QCoreApplication.translate
        InterfazMAXON.setWindowTitle(_translate("InterfazMAXON", "Interfaz de pruebas MAXON"))
        self.init_button.setText(_translate("InterfazMAXON", "Init"))
        self.fault_button.setText(_translate("InterfazMAXON", "Fault/Reset"))
        self.enable_button.setText(_translate("InterfazMAXON", "Activar electroimán"))
        self.disable_button.setText(_translate("InterfazMAXON", "Desactivar electroimán"))
        self.rel_button.setText(_translate("InterfazMAXON", "Giro relativo"))
        self.abs_button.setText(_translate("InterfazMAXON", "Giro absoluto"))
        self.label_9.setText(_translate("InterfazMAXON", "Following error:"))
        self.following_text.setText(_translate("InterfazMAXON", "2000"))
        self.following_button.setText(_translate("InterfazMAXON", "Apply"))
        self.label_11.setText(_translate("InterfazMAXON", "Speed:"))
        self.speed_text.setText(_translate("InterfazMAXON", "5000"))
        self.speed_button.setText(_translate("InterfazMAXON", "Apply"))
        self.label_volante.setText(_translate("InterfazMAXON", "0"))
        self.label_volante_2.setText(_translate("InterfazMAXON", "º"))
        self.reset_encoder_button.setText(_translate("InterfazMAXON", "Rst. Encoder"))
        self.label_volante_3.setText(_translate("InterfazMAXON", "0"))
        self.label_position.setText(_translate("InterfazMAXON", "0"))
        self.label_volante_6.setText(_translate("InterfazMAXON", "pos"))
        self.label_rpm.setText(_translate("InterfazMAXON", "0"))
        self.label_volante_7.setText(_translate("InterfazMAXON", "rpm"))
        self.Conectar.setText(_translate("InterfazMAXON", "Conectar"))
        self.puerto.setText(_translate("InterfazMAXON", "10001"))
        self.ip.setText(_translate("InterfazMAXON", "192.168.0.7"))
        self.label_4.setText(_translate("InterfazMAXON", "Puerto:"))
        self.label_3.setText(_translate("InterfazMAXON", "IP:"))
        self.label_10.setText(_translate("InterfazMAXON", "Giro relativo"))
        self.label_8.setText(_translate("InterfazMAXON", "360"))
        self.label_7.setText(_translate("InterfazMAXON", "50"))
        self.label_6.setText(_translate("InterfazMAXON", "20"))
        self.label_5.setText(_translate("InterfazMAXON", "10"))
        self.label_2.setText(_translate("InterfazMAXON", "5"))
        self.label.setText(_translate("InterfazMAXON", "1"))
        self.giro_dch.setText(_translate("InterfazMAXON", ">>"))
        self.giro_izq.setText(_translate("InterfazMAXON", "<<"))
        self.enderezar.setText(_translate("InterfazMAXON", "Enderezar"))
        self.reset_rel.setText(_translate("InterfazMAXON", "Reset centro"))
        self.label_volante_4.setText(_translate("InterfazMAXON", "º"))
        self.label_giro_relativo.setText(_translate("InterfazMAXON", "0"))
        self.girar_button.setText(_translate("InterfazMAXON", "Girar"))
        self.giro_text.setText(_translate("InterfazMAXON", "0"))
        self.press.setText(_translate("InterfazMAXON", "Press"))
        self.release.setText(_translate("InterfazMAXON", "Release"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InterfazMAXON = QtWidgets.QMainWindow()
    ui = Ui_InterfazMAXON()
    ui.setupUi(InterfazMAXON)
    InterfazMAXON.show()
    sys.exit(app.exec_())
