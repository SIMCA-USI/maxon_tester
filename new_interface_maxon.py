# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_maxonZyPABj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_InterfazMAXON(object):
    def setupUi(self, InterfazMAXON):
        if not InterfazMAXON.objectName():
            InterfazMAXON.setObjectName(u"InterfazMAXON")
        InterfazMAXON.resize(965, 607)
        InterfazMAXON.setMaximumSize(QSize(965, 607))
        self.interfaz = QWidget(InterfazMAXON)
        self.interfaz.setObjectName(u"interfaz")
        self.frame_general = QFrame(self.interfaz)
        self.frame_general.setObjectName(u"frame_general")
        self.frame_general.setEnabled(True)
        self.frame_general.setGeometry(QRect(20, 60, 761, 531))
        self.frame_general.setFrameShape(QFrame.StyledPanel)
        self.frame_general.setFrameShadow(QFrame.Raised)
        self.frame_12 = QFrame(self.frame_general)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(0, 0, 191, 421))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_12)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.init_button = QPushButton(self.frame_12)
        self.init_button.setObjectName(u"init_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.init_button.sizePolicy().hasHeightForWidth())
        self.init_button.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.init_button)

        self.fault_button = QPushButton(self.frame_12)
        self.fault_button.setObjectName(u"fault_button")
        sizePolicy.setHeightForWidth(self.fault_button.sizePolicy().hasHeightForWidth())
        self.fault_button.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.fault_button)

        self.enable_button = QPushButton(self.frame_12)
        self.enable_button.setObjectName(u"enable_button")
        sizePolicy.setHeightForWidth(self.enable_button.sizePolicy().hasHeightForWidth())
        self.enable_button.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.enable_button)

        self.disable_button = QPushButton(self.frame_12)
        self.disable_button.setObjectName(u"disable_button")
        sizePolicy.setHeightForWidth(self.disable_button.sizePolicy().hasHeightForWidth())
        self.disable_button.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.disable_button)

        self.rel_button = QPushButton(self.frame_12)
        self.rel_button.setObjectName(u"rel_button")
        sizePolicy.setHeightForWidth(self.rel_button.sizePolicy().hasHeightForWidth())
        self.rel_button.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.rel_button)

        self.abs_button = QPushButton(self.frame_12)
        self.abs_button.setObjectName(u"abs_button")
        sizePolicy.setHeightForWidth(self.abs_button.sizePolicy().hasHeightForWidth())
        self.abs_button.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.abs_button)

        self.verticalLayout_5.setStretch(0, 2)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 1)
        self.verticalLayout_5.setStretch(3, 1)
        self.verticalLayout_5.setStretch(4, 1)
        self.verticalLayout_5.setStretch(5, 1)
        self.frame_following = QFrame(self.frame_general)
        self.frame_following.setObjectName(u"frame_following")
        self.frame_following.setGeometry(QRect(0, 480, 369, 52))
        self.frame_following.setFrameShape(QFrame.StyledPanel)
        self.frame_following.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_following)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_9 = QLabel(self.frame_following)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_9)

        self.following_text = QLineEdit(self.frame_following)
        self.following_text.setObjectName(u"following_text")
        self.following_text.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.following_text)

        self.following_button = QPushButton(self.frame_following)
        self.following_button.setObjectName(u"following_button")

        self.horizontalLayout.addWidget(self.following_button)

        self.frame_speed = QFrame(self.frame_general)
        self.frame_speed.setObjectName(u"frame_speed")
        self.frame_speed.setGeometry(QRect(0, 430, 369, 52))
        self.frame_speed.setFrameShape(QFrame.StyledPanel)
        self.frame_speed.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_speed)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_11 = QLabel(self.frame_speed)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.speed_text = QLineEdit(self.frame_speed)
        self.speed_text.setObjectName(u"speed_text")
        self.speed_text.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.speed_text)

        self.speed_button = QPushButton(self.frame_speed)
        self.speed_button.setObjectName(u"speed_button")

        self.horizontalLayout_3.addWidget(self.speed_button)

        self.label_volante = QLabel(self.frame_general)
        self.label_volante.setObjectName(u"label_volante")
        self.label_volante.setGeometry(QRect(600, 10, 71, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_volante.setFont(font1)
        self.label_volante.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_volante_2 = QLabel(self.frame_general)
        self.label_volante_2.setObjectName(u"label_volante_2")
        self.label_volante_2.setGeometry(QRect(680, 10, 71, 41))
        self.label_volante_2.setFont(font1)
        self.label_volante_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_rel = QFrame(self.frame_general)
        self.frame_rel.setObjectName(u"frame_rel")
        self.frame_rel.setEnabled(True)
        self.frame_rel.setGeometry(QRect(190, 0, 571, 421))
        self.frame_rel.setFrameShape(QFrame.StyledPanel)
        self.frame_rel.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.frame_rel)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setEnabled(True)
        self.frame_5.setGeometry(QRect(430, 62, 141, 361))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_10)

        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame)

        self.slider_giro = QSlider(self.frame_3)
        self.slider_giro.setObjectName(u"slider_giro")
        self.slider_giro.setMaximum(5)
        self.slider_giro.setOrientation(Qt.Vertical)
        self.slider_giro.setTickPosition(QSlider.TicksAbove)
        self.slider_giro.setTickInterval(1)

        self.horizontalLayout_2.addWidget(self.slider_giro)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.giro_dch = QPushButton(self.frame_rel)
        self.giro_dch.setObjectName(u"giro_dch")
        self.giro_dch.setGeometry(QRect(220, 180, 131, 61))
        self.giro_izq = QPushButton(self.frame_rel)
        self.giro_izq.setObjectName(u"giro_izq")
        self.giro_izq.setGeometry(QRect(70, 180, 131, 61))
        self.enderezar = QPushButton(self.frame_rel)
        self.enderezar.setObjectName(u"enderezar")
        self.enderezar.setGeometry(QRect(130, 260, 161, 71))
        self.reset_rel = QPushButton(self.frame_rel)
        self.reset_rel.setObjectName(u"reset_rel")
        self.reset_rel.setGeometry(QRect(290, 60, 93, 28))
        self.label_volante_4 = QLabel(self.frame_rel)
        self.label_volante_4.setObjectName(u"label_volante_4")
        self.label_volante_4.setGeometry(QRect(220, 100, 71, 41))
        self.label_volante_4.setFont(font1)
        self.label_volante_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_giro_relativo = QLabel(self.frame_rel)
        self.label_giro_relativo.setObjectName(u"label_giro_relativo")
        self.label_giro_relativo.setGeometry(QRect(140, 100, 71, 41))
        self.label_giro_relativo.setFont(font1)
        self.label_giro_relativo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_abs = QFrame(self.frame_general)
        self.frame_abs.setObjectName(u"frame_abs")
        self.frame_abs.setEnabled(True)
        self.frame_abs.setGeometry(QRect(190, 0, 571, 421))
        self.frame_abs.setFrameShape(QFrame.StyledPanel)
        self.frame_abs.setFrameShadow(QFrame.Raised)
        self.girar_button = QPushButton(self.frame_abs)
        self.girar_button.setObjectName(u"girar_button")
        self.girar_button.setGeometry(QRect(220, 230, 161, 71))
        self.giro_text = QLineEdit(self.frame_abs)
        self.giro_text.setObjectName(u"giro_text")
        self.giro_text.setGeometry(QRect(220, 170, 161, 41))
        font2 = QFont()
        font2.setPointSize(15)
        self.giro_text.setFont(font2)
        self.giro_text.setAlignment(Qt.AlignCenter)
        self.frame_control = QFrame(self.interfaz)
        self.frame_control.setObjectName(u"frame_control")
        self.frame_control.setGeometry(QRect(790, 60, 151, 531))
        self.frame_control.setMinimumSize(QSize(0, 0))
        self.frame_control.setFrameShape(QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_control)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_12 = QLabel(self.frame_control)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_12)

        self.frame_swondis = QFrame(self.frame_control)
        self.frame_swondis.setObjectName(u"frame_swondis")
        self.frame_swondis.setFrameShape(QFrame.WinPanel)
        self.frame_swondis.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_swondis)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.pushButton_swondis = QPushButton(self.frame_swondis)
        self.pushButton_swondis.setObjectName(u"pushButton_swondis")
        sizePolicy.setHeightForWidth(self.pushButton_swondis.sizePolicy().hasHeightForWidth())
        self.pushButton_swondis.setSizePolicy(sizePolicy)
        self.pushButton_swondis.setStyleSheet(u"background-color: rgb(244, 244, 244);")

        self.verticalLayout_6.addWidget(self.pushButton_swondis)


        self.verticalLayout_3.addWidget(self.frame_swondis)

        self.frame_ready = QFrame(self.frame_control)
        self.frame_ready.setObjectName(u"frame_ready")
        self.frame_ready.setFrameShape(QFrame.WinPanel)
        self.frame_ready.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_ready)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.pushButton_ready = QPushButton(self.frame_ready)
        self.pushButton_ready.setObjectName(u"pushButton_ready")
        sizePolicy.setHeightForWidth(self.pushButton_ready.sizePolicy().hasHeightForWidth())
        self.pushButton_ready.setSizePolicy(sizePolicy)
        self.pushButton_ready.setStyleSheet(u"background-color: rgb(244, 244, 244);")

        self.verticalLayout_4.addWidget(self.pushButton_ready)


        self.verticalLayout_3.addWidget(self.frame_ready)

        self.frame_swon = QFrame(self.frame_control)
        self.frame_swon.setObjectName(u"frame_swon")
        self.frame_swon.setFrameShape(QFrame.WinPanel)
        self.frame_swon.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_swon)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.pushButton_swon = QPushButton(self.frame_swon)
        self.pushButton_swon.setObjectName(u"pushButton_swon")
        sizePolicy.setHeightForWidth(self.pushButton_swon.sizePolicy().hasHeightForWidth())
        self.pushButton_swon.setSizePolicy(sizePolicy)
        self.pushButton_swon.setStyleSheet(u"background-color: rgb(244, 244, 244);")

        self.verticalLayout_7.addWidget(self.pushButton_swon)


        self.verticalLayout_3.addWidget(self.frame_swon)

        self.frame_openabled = QFrame(self.frame_control)
        self.frame_openabled.setObjectName(u"frame_openabled")
        self.frame_openabled.setFrameShape(QFrame.WinPanel)
        self.frame_openabled.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_openabled)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.pushButton_openabled = QPushButton(self.frame_openabled)
        self.pushButton_openabled.setObjectName(u"pushButton_openabled")
        sizePolicy.setHeightForWidth(self.pushButton_openabled.sizePolicy().hasHeightForWidth())
        self.pushButton_openabled.setSizePolicy(sizePolicy)
        self.pushButton_openabled.setStyleSheet(u"background-color: rgb(244, 244, 244);")

        self.verticalLayout_8.addWidget(self.pushButton_openabled)


        self.verticalLayout_3.addWidget(self.frame_openabled)

        self.frame_fault = QFrame(self.frame_control)
        self.frame_fault.setObjectName(u"frame_fault")
        self.frame_fault.setStyleSheet(u"")
        self.frame_fault.setFrameShape(QFrame.NoFrame)
        self.frame_fault.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_fault)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(25, 2, 25, 2)
        self.label_fault = QLabel(self.frame_fault)
        self.label_fault.setObjectName(u"label_fault")
        self.label_fault.setFont(font)
        self.label_fault.setStyleSheet(u"border-radius: 38px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(244, 244, 244);\n"
"border: 2px solid black;")
        self.label_fault.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_fault)


        self.verticalLayout_3.addWidget(self.frame_fault)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 2)
        self.verticalLayout_3.setStretch(3, 2)
        self.verticalLayout_3.setStretch(4, 2)
        self.verticalLayout_3.setStretch(5, 2)
        self.frame_conexion = QFrame(self.interfaz)
        self.frame_conexion.setObjectName(u"frame_conexion")
        self.frame_conexion.setEnabled(True)
        self.frame_conexion.setGeometry(QRect(20, 10, 921, 51))
        self.frame_conexion.setFrameShape(QFrame.NoFrame)
        self.frame_conexion.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_conexion)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_15 = QLabel(self.frame_conexion)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_15)

        self.comboBox_2 = QComboBox(self.frame_conexion)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_4.addWidget(self.comboBox_2)

        self.label_3 = QLabel(self.frame_conexion)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.ip = QLineEdit(self.frame_conexion)
        self.ip.setObjectName(u"ip")
        self.ip.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.ip)

        self.label_4 = QLabel(self.frame_conexion)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.puerto = QLineEdit(self.frame_conexion)
        self.puerto.setObjectName(u"puerto")
        self.puerto.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.puerto)

        self.label_14 = QLabel(self.frame_conexion)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_14)

        self.comboBox = QComboBox(self.frame_conexion)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(False)
        self.comboBox.setModelColumn(0)

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.Conectar = QPushButton(self.frame_conexion)
        self.Conectar.setObjectName(u"Conectar")

        self.horizontalLayout_4.addWidget(self.Conectar)

        InterfazMAXON.setCentralWidget(self.interfaz)

        self.retranslateUi(InterfazMAXON)

        QMetaObject.connectSlotsByName(InterfazMAXON)
    # setupUi

    def retranslateUi(self, InterfazMAXON):
        InterfazMAXON.setWindowTitle(QCoreApplication.translate("InterfazMAXON", u"Interfaz de pruebas MAXON", None))
        self.init_button.setText(QCoreApplication.translate("InterfazMAXON", u"Init", None))
        self.fault_button.setText(QCoreApplication.translate("InterfazMAXON", u"Fault/Reset", None))
        self.enable_button.setText(QCoreApplication.translate("InterfazMAXON", u"Activar electroim\u00e1n", None))
        self.disable_button.setText(QCoreApplication.translate("InterfazMAXON", u"Desactivar electroim\u00e1n", None))
        self.rel_button.setText(QCoreApplication.translate("InterfazMAXON", u"Giro relativo", None))
        self.abs_button.setText(QCoreApplication.translate("InterfazMAXON", u"Giro absoluto", None))
        self.label_9.setText(QCoreApplication.translate("InterfazMAXON", u"Following error:", None))
        self.following_text.setText(QCoreApplication.translate("InterfazMAXON", u"2000", None))
        self.following_button.setText(QCoreApplication.translate("InterfazMAXON", u"Apply", None))
        self.label_11.setText(QCoreApplication.translate("InterfazMAXON", u"Speed:", None))
        self.speed_text.setText(QCoreApplication.translate("InterfazMAXON", u"5000", None))
        self.speed_button.setText(QCoreApplication.translate("InterfazMAXON", u"Apply", None))
        self.label_volante.setText(QCoreApplication.translate("InterfazMAXON", u"0", None))
        self.label_volante_2.setText(QCoreApplication.translate("InterfazMAXON", u"\u00ba", None))
        self.label_10.setText(QCoreApplication.translate("InterfazMAXON", u"Giro relativo", None))
        self.label_8.setText(QCoreApplication.translate("InterfazMAXON", u"360", None))
        self.label_7.setText(QCoreApplication.translate("InterfazMAXON", u"50", None))
        self.label_6.setText(QCoreApplication.translate("InterfazMAXON", u"20", None))
        self.label_5.setText(QCoreApplication.translate("InterfazMAXON", u"10", None))
        self.label_2.setText(QCoreApplication.translate("InterfazMAXON", u"5", None))
        self.label.setText(QCoreApplication.translate("InterfazMAXON", u"1", None))
        self.giro_dch.setText(QCoreApplication.translate("InterfazMAXON", u">>", None))
        self.giro_izq.setText(QCoreApplication.translate("InterfazMAXON", u"<<", None))
        self.enderezar.setText(QCoreApplication.translate("InterfazMAXON", u"Enderezar", None))
        self.reset_rel.setText(QCoreApplication.translate("InterfazMAXON", u"Reset centro", None))
        self.label_volante_4.setText(QCoreApplication.translate("InterfazMAXON", u"\u00ba", None))
        self.label_giro_relativo.setText(QCoreApplication.translate("InterfazMAXON", u"0", None))
        self.girar_button.setText(QCoreApplication.translate("InterfazMAXON", u"Girar", None))
        self.giro_text.setText(QCoreApplication.translate("InterfazMAXON", u"0", None))
        self.label_12.setText(QCoreApplication.translate("InterfazMAXON", u"DEVICE CONTROL", None))
        self.pushButton_swondis.setText(QCoreApplication.translate("InterfazMAXON", u"SWITCH ON\n"
" DISABLED", None))
        self.pushButton_ready.setText(QCoreApplication.translate("InterfazMAXON", u"READY TO \n"
"SWITCH ON", None))
        self.pushButton_swon.setText(QCoreApplication.translate("InterfazMAXON", u"SWITCHED ON", None))
        self.pushButton_openabled.setText(QCoreApplication.translate("InterfazMAXON", u"OPERATION\n"
" ENABLED", None))
        self.label_fault.setText(QCoreApplication.translate("InterfazMAXON", u"FAULT", None))
        self.label_15.setText(QCoreApplication.translate("InterfazMAXON", u"Device", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("InterfazMAXON", u"EPOS 4", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("InterfazMAXON", u"Maxon", None))

        self.label_3.setText(QCoreApplication.translate("InterfazMAXON", u"IP:", None))
        self.ip.setText(QCoreApplication.translate("InterfazMAXON", u"192.168.0.8", None))
        self.label_4.setText(QCoreApplication.translate("InterfazMAXON", u"Puerto:", None))
        self.puerto.setText(QCoreApplication.translate("InterfazMAXON", u"10001", None))
        self.label_14.setText(QCoreApplication.translate("InterfazMAXON", u"COBID", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("InterfazMAXON", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("InterfazMAXON", u"2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("InterfazMAXON", u"3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("InterfazMAXON", u"4", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("InterfazMAXON", u"5", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("InterfazMAXON", u"6", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("InterfazMAXON", u"7", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("InterfazMAXON", u"8", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("InterfazMAXON", u"9", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("InterfazMAXON", u"10", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("InterfazMAXON", u"1", None))
        self.Conectar.setText(QCoreApplication.translate("InterfazMAXON", u"Conectar", None))
    # retranslateUi

