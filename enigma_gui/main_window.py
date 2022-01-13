# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'enigma.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(691, 490)
        self.change_config_act = QAction(MainWindow)
        self.change_config_act.setObjectName(u"change_config_act")
        self.settings_act = QAction(MainWindow)
        self.settings_act.setObjectName(u"settings_act")
        self.enc_by_letter_act = QAction(MainWindow)
        self.enc_by_letter_act.setObjectName(u"enc_by_letter_act")
        self.en_from_file_act = QAction(MainWindow)
        self.en_from_file_act.setObjectName(u"en_from_file_act")
        self.a_r_rotor_act = QAction(MainWindow)
        self.a_r_rotor_act.setObjectName(u"a_r_rotor_act")
        self.a_r_reflector_act = QAction(MainWindow)
        self.a_r_reflector_act.setObjectName(u"a_r_reflector_act")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stack = QStackedWidget(self.centralwidget)
        self.stack.setObjectName(u"stack")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stack.sizePolicy().hasHeightForWidth())
        self.stack.setSizePolicy(sizePolicy)
        self.stack.setMinimumSize(QSize(330, 0))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, -1, -1, -1)
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout_4.addWidget(self.label)

        self.cipher_text = QLabel(self.page)
        self.cipher_text.setObjectName(u"cipher_text")
        sizePolicy.setHeightForWidth(self.cipher_text.sizePolicy().hasHeightForWidth())
        self.cipher_text.setSizePolicy(sizePolicy)
        self.cipher_text.setMaximumSize(QSize(16777215, 30))
        self.cipher_text.setMouseTracking(False)
        self.cipher_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.cipher_text.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.cipher_text)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_12 = QLabel(self.page)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setFont(font)

        self.verticalLayout_2.addWidget(self.label_12)

        self.steps_table = QTableView(self.page)
        self.steps_table.setObjectName(u"steps_table")

        self.verticalLayout_2.addWidget(self.steps_table)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 3, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 10)
        self.letter_input = QLineEdit(self.page)
        self.letter_input.setObjectName(u"letter_input")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.letter_input.sizePolicy().hasHeightForWidth())
        self.letter_input.setSizePolicy(sizePolicy2)
        self.letter_input.setCursor(QCursor(Qt.IBeamCursor))

        self.verticalLayout.addWidget(self.letter_input)

        self.encrypt_button = QPushButton(self.page)
        self.encrypt_button.setObjectName(u"encrypt_button")
        sizePolicy2.setHeightForWidth(self.encrypt_button.sizePolicy().hasHeightForWidth())
        self.encrypt_button.setSizePolicy(sizePolicy2)
        self.encrypt_button.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout.addWidget(self.encrypt_button)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_11 = QLabel(self.page)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_3.addWidget(self.label_11)

        self.current_config = QTableView(self.page)
        self.current_config.setObjectName(u"current_config")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.current_config.sizePolicy().hasHeightForWidth())
        self.current_config.setSizePolicy(sizePolicy4)
        self.current_config.setMinimumSize(QSize(315, 0))
        self.current_config.setBaseSize(QSize(0, 0))

        self.verticalLayout_3.addWidget(self.current_config)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_10 = QLabel(self.page)
        self.label_10.setObjectName(u"label_10")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy5)
        self.label_10.setMinimumSize(QSize(70, 0))

        self.horizontalLayout.addWidget(self.label_10)

        self.reflector_name = QLabel(self.page)
        self.reflector_name.setObjectName(u"reflector_name")

        self.horizontalLayout.addWidget(self.reflector_name)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_14 = QLabel(self.page)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_2.addWidget(self.label_14)

        self.plugboard_connections = QLabel(self.page)
        self.plugboard_connections.setObjectName(u"plugboard_connections")

        self.horizontalLayout_2.addWidget(self.plugboard_connections)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 1)

        self.stack.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 191, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_5.setFont(font1)
        self.brow_input_butt = QPushButton(self.page_3)
        self.brow_input_butt.setObjectName(u"brow_input_butt")
        self.brow_input_butt.setGeometry(QRect(240, 100, 80, 23))
        self.input_file_name = QLabel(self.page_3)
        self.input_file_name.setObjectName(u"input_file_name")
        self.input_file_name.setGeometry(QRect(220, 70, 391, 16))
        self.output_file_name = QLabel(self.page_3)
        self.output_file_name.setObjectName(u"output_file_name")
        self.output_file_name.setGeometry(QRect(220, 150, 391, 16))
        self.brow_output_butt = QPushButton(self.page_3)
        self.brow_output_butt.setObjectName(u"brow_output_butt")
        self.brow_output_butt.setGeometry(QRect(240, 180, 80, 23))
        self.brow_config_butt = QPushButton(self.page_3)
        self.brow_config_butt.setObjectName(u"brow_config_butt")
        self.brow_config_butt.setGeometry(QRect(240, 260, 80, 23))
        self.config_file_name = QLabel(self.page_3)
        self.config_file_name.setObjectName(u"config_file_name")
        self.config_file_name.setGeometry(QRect(220, 230, 391, 16))
        self.label_7 = QLabel(self.page_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 70, 131, 41))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_7.setFont(font2)
        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 160, 141, 41))
        self.label_8.setFont(font2)
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 240, 161, 41))
        self.label_9.setFont(font2)
        self.encrypt_file_button = QPushButton(self.page_3)
        self.encrypt_file_button.setObjectName(u"encrypt_file_button")
        self.encrypt_file_button.setGeometry(QRect(150, 340, 171, 41))
        self.stack.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.is_double_step = QCheckBox(self.page_2)
        self.is_double_step.setObjectName(u"is_double_step")
        self.is_double_step.setGeometry(QRect(20, 50, 411, 21))
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 0, 101, 41))
        self.label_3.setFont(font1)
        self.label_13 = QLabel(self.page_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 90, 301, 16))
        self.space_info = QSpinBox(self.page_2)
        self.space_info.setObjectName(u"space_info")
        self.space_info.setGeometry(QRect(190, 90, 47, 24))
        self.space_info.setValue(5)
        self.label_31 = QLabel(self.page_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(20, 120, 301, 16))
        self.stack.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_4 = QLabel(self.page_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 301, 21))
        self.label_4.setFont(font1)
        self.up_button = QToolButton(self.page_4)
        self.up_button.setObjectName(u"up_button")
        self.up_button.setGeometry(QRect(20, 110, 28, 22))
        self.label_18 = QLabel(self.page_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(60, 50, 59, 15))
        self.label_18.setFont(font)
        self.down_button = QToolButton(self.page_4)
        self.down_button.setObjectName(u"down_button")
        self.down_button.setGeometry(QRect(20, 160, 28, 22))
        self.save_init_conf_button = QPushButton(self.page_4)
        self.save_init_conf_button.setObjectName(u"save_init_conf_button")
        self.save_init_conf_button.setGeometry(QRect(190, 380, 121, 31))
        self.label_17 = QLabel(self.page_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(50, 280, 91, 16))
        self.label_17.setFont(font)
        self.label_21 = QLabel(self.page_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(50, 340, 91, 16))
        self.label_21.setFont(font)
        self.add_button = QToolButton(self.page_4)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(260, 50, 28, 22))
        self.remove_button = QToolButton(self.page_4)
        self.remove_button.setObjectName(u"remove_button")
        self.remove_button.setGeometry(QRect(220, 50, 28, 22))
        self.plugboard_line = QLineEdit(self.page_4)
        self.plugboard_line.setObjectName(u"plugboard_line")
        self.plugboard_line.setGeometry(QRect(160, 340, 351, 23))
        self.reflector_comboBox = QComboBox(self.page_4)
        self.reflector_comboBox.setObjectName(u"reflector_comboBox")
        self.reflector_comboBox.setGeometry(QRect(160, 280, 151, 23))
        self.stack2 = QStackedWidget(self.page_4)
        self.stack2.setObjectName(u"stack2")
        self.stack2.setGeometry(QRect(340, 90, 211, 161))
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.stack2.addWidget(self.page_7)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_19 = QLabel(self.page_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 40, 59, 15))
        self.label_19.setFont(font)
        self.pos_comboBox = QComboBox(self.page_6)
        self.pos_comboBox.setObjectName(u"pos_comboBox")
        self.pos_comboBox.setGeometry(QRect(30, 70, 51, 23))
        self.ring_comboBox = QComboBox(self.page_6)
        self.ring_comboBox.setObjectName(u"ring_comboBox")
        self.ring_comboBox.setGeometry(QRect(120, 70, 51, 23))
        self.label_20 = QLabel(self.page_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(120, 40, 59, 15))
        self.label_20.setFont(font)
        self.stack2.addWidget(self.page_6)
        self.rotors_list = QListWidget(self.page_4)
        self.rotors_list.setObjectName(u"rotors_list")
        self.rotors_list.setGeometry(QRect(60, 80, 231, 171))
        self.save_conf_button = QPushButton(self.page_4)
        self.save_conf_button.setObjectName(u"save_conf_button")
        self.save_conf_button.setGeometry(QRect(340, 380, 121, 31))
        self.set_plugboard_button = QPushButton(self.page_4)
        self.set_plugboard_button.setObjectName(u"set_plugboard_button")
        self.set_plugboard_button.setGeometry(QRect(530, 340, 61, 20))
        self.alphabet_label = QLabel(self.page_4)
        self.alphabet_label.setObjectName(u"alphabet_label")
        self.alphabet_label.setGeometry(QRect(160, 320, 351, 16))
        self.stack.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_6 = QLabel(self.page_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 261, 41))
        self.label_6.setFont(font1)
        self.rotors_list_2 = QListWidget(self.page_5)
        self.rotors_list_2.setObjectName(u"rotors_list_2")
        self.rotors_list_2.setGeometry(QRect(20, 110, 221, 311))
        self.add_rotor_mod = QToolButton(self.page_5)
        self.add_rotor_mod.setObjectName(u"add_rotor_mod")
        self.add_rotor_mod.setGeometry(QRect(60, 70, 28, 22))
        self.rem_rotor_mod = QToolButton(self.page_5)
        self.rem_rotor_mod.setObjectName(u"rem_rotor_mod")
        self.rem_rotor_mod.setGeometry(QRect(150, 70, 28, 22))
        self.stack3 = QStackedWidget(self.page_5)
        self.stack3.setObjectName(u"stack3")
        self.stack3.setGeometry(QRect(270, 20, 381, 391))
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.stack3.addWidget(self.page_9)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.mod_rotor_butt = QPushButton(self.page_12)
        self.mod_rotor_butt.setObjectName(u"mod_rotor_butt")
        self.mod_rotor_butt.setGeometry(QRect(120, 360, 80, 23))
        self.label_28 = QLabel(self.page_12)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(140, 30, 91, 16))
        self.label_28.setFont(font)
        self.rotor_indentation_2 = QLineEdit(self.page_12)
        self.rotor_indentation_2.setObjectName(u"rotor_indentation_2")
        self.rotor_indentation_2.setGeometry(QRect(30, 290, 311, 23))
        self.label_25 = QLabel(self.page_12)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(30, 90, 59, 15))
        self.label_26 = QLabel(self.page_12)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(30, 270, 111, 16))
        self.rotor_name_2 = QLineEdit(self.page_12)
        self.rotor_name_2.setObjectName(u"rotor_name_2")
        self.rotor_name_2.setGeometry(QRect(30, 120, 311, 23))
        self.alphabet_label_3 = QLabel(self.page_12)
        self.alphabet_label_3.setObjectName(u"alphabet_label_3")
        self.alphabet_label_3.setGeometry(QRect(10, 200, 351, 16))
        self.label_27 = QLabel(self.page_12)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(30, 170, 59, 15))
        self.rotor_wiring_2 = QLineEdit(self.page_12)
        self.rotor_wiring_2.setObjectName(u"rotor_wiring_2")
        self.rotor_wiring_2.setGeometry(QRect(30, 220, 311, 23))
        self.stack3.addWidget(self.page_12)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.rotor_name = QLineEdit(self.page_11)
        self.rotor_name.setObjectName(u"rotor_name")
        self.rotor_name.setGeometry(QRect(30, 120, 311, 23))
        self.rotor_wiring = QLineEdit(self.page_11)
        self.rotor_wiring.setObjectName(u"rotor_wiring")
        self.rotor_wiring.setGeometry(QRect(30, 220, 311, 23))
        self.rotor_indentation = QLineEdit(self.page_11)
        self.rotor_indentation.setObjectName(u"rotor_indentation")
        self.rotor_indentation.setGeometry(QRect(30, 290, 311, 23))
        self.add_mod_rotor = QPushButton(self.page_11)
        self.add_mod_rotor.setObjectName(u"add_mod_rotor")
        self.add_mod_rotor.setGeometry(QRect(60, 360, 80, 23))
        self.label_16 = QLabel(self.page_11)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 90, 59, 15))
        self.label_22 = QLabel(self.page_11)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(30, 170, 59, 15))
        self.label_23 = QLabel(self.page_11)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(30, 270, 111, 16))
        self.label_24 = QLabel(self.page_11)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(140, 30, 91, 16))
        self.label_24.setFont(font)
        self.cancel_add_rotor = QPushButton(self.page_11)
        self.cancel_add_rotor.setObjectName(u"cancel_add_rotor")
        self.cancel_add_rotor.setGeometry(QRect(180, 360, 80, 23))
        self.alphabet_label_2 = QLabel(self.page_11)
        self.alphabet_label_2.setObjectName(u"alphabet_label_2")
        self.alphabet_label_2.setGeometry(QRect(10, 200, 351, 16))
        self.stack3.addWidget(self.page_11)
        self.stack.addWidget(self.page_5)
        self.stack3.raise_()
        self.label_6.raise_()
        self.rotors_list_2.raise_()
        self.add_rotor_mod.raise_()
        self.rem_rotor_mod.raise_()
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_15 = QLabel(self.page_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 10, 271, 41))
        self.label_15.setFont(font1)
        self.stack4 = QStackedWidget(self.page_8)
        self.stack4.setObjectName(u"stack4")
        self.stack4.setGeometry(QRect(280, 30, 361, 391))
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.stack4.addWidget(self.page_10)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.label_33 = QLabel(self.page_14)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(30, 130, 59, 15))
        self.modify_ref_button = QPushButton(self.page_14)
        self.modify_ref_button.setObjectName(u"modify_ref_button")
        self.modify_ref_button.setGeometry(QRect(130, 320, 80, 23))
        self.reflector_mod_name = QLineEdit(self.page_14)
        self.reflector_mod_name.setObjectName(u"reflector_mod_name")
        self.reflector_mod_name.setGeometry(QRect(30, 150, 321, 23))
        self.reflector_mod_wiring = QLineEdit(self.page_14)
        self.reflector_mod_wiring.setObjectName(u"reflector_mod_wiring")
        self.reflector_mod_wiring.setGeometry(QRect(30, 250, 321, 23))
        self.label_35 = QLabel(self.page_14)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(30, 210, 59, 15))
        self.label_36 = QLabel(self.page_14)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(120, 50, 121, 16))
        self.label_36.setFont(font)
        self.alphabet_label_4 = QLabel(self.page_14)
        self.alphabet_label_4.setObjectName(u"alphabet_label_4")
        self.alphabet_label_4.setGeometry(QRect(10, 230, 351, 16))
        self.stack4.addWidget(self.page_14)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.add_mod_ref = QPushButton(self.page_13)
        self.add_mod_ref.setObjectName(u"add_mod_ref")
        self.add_mod_ref.setGeometry(QRect(60, 310, 80, 23))
        self.label_32 = QLabel(self.page_13)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(130, 40, 101, 20))
        self.label_32.setFont(font)
        self.cancel_add_ref = QPushButton(self.page_13)
        self.cancel_add_ref.setObjectName(u"cancel_add_ref")
        self.cancel_add_ref.setGeometry(QRect(180, 310, 80, 23))
        self.label_37 = QLabel(self.page_13)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(20, 190, 59, 15))
        self.reflector_mod_wiring_2 = QLineEdit(self.page_13)
        self.reflector_mod_wiring_2.setObjectName(u"reflector_mod_wiring_2")
        self.reflector_mod_wiring_2.setGeometry(QRect(20, 230, 321, 23))
        self.label_34 = QLabel(self.page_13)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(20, 110, 59, 15))
        self.alphabet_label_5 = QLabel(self.page_13)
        self.alphabet_label_5.setObjectName(u"alphabet_label_5")
        self.alphabet_label_5.setGeometry(QRect(0, 210, 351, 16))
        self.reflector_mod_name_2 = QLineEdit(self.page_13)
        self.reflector_mod_name_2.setObjectName(u"reflector_mod_name_2")
        self.reflector_mod_name_2.setGeometry(QRect(20, 130, 321, 23))
        self.stack4.addWidget(self.page_13)
        self.add_ref_mod_butt = QToolButton(self.page_8)
        self.add_ref_mod_butt.setObjectName(u"add_ref_mod_butt")
        self.add_ref_mod_butt.setGeometry(QRect(60, 70, 28, 22))
        self.rem_ref_mod_button = QToolButton(self.page_8)
        self.rem_ref_mod_button.setObjectName(u"rem_ref_mod_button")
        self.rem_ref_mod_button.setGeometry(QRect(150, 70, 28, 22))
        self.reflectors_list = QListWidget(self.page_8)
        self.reflectors_list.setObjectName(u"reflectors_list")
        self.reflectors_list.setGeometry(QRect(20, 110, 221, 311))
        self.stack.addWidget(self.page_8)

        self.gridLayout_2.addWidget(self.stack, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 691, 20))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuMenu_2 = QMenu(self.menubar)
        self.menuMenu_2.setObjectName(u"menuMenu_2")
        self.menuAdd_Remove_elements = QMenu(self.menuMenu_2)
        self.menuAdd_Remove_elements.setObjectName(u"menuAdd_Remove_elements")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuMenu_2.menuAction())
        self.menuMenu.addAction(self.enc_by_letter_act)
        self.menuMenu.addAction(self.en_from_file_act)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.change_config_act)
        self.menuMenu_2.addAction(self.settings_act)
        self.menuMenu_2.addAction(self.menuAdd_Remove_elements.menuAction())
        self.menuAdd_Remove_elements.addAction(self.a_r_rotor_act)
        self.menuAdd_Remove_elements.addAction(self.a_r_reflector_act)

        self.retranslateUi(MainWindow)

        self.stack.setCurrentIndex(4)
        self.stack2.setCurrentIndex(1)
        self.stack3.setCurrentIndex(1)
        self.stack4.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Enigma", None))
        self.change_config_act.setText(QCoreApplication.translate("MainWindow", u"Change Machine Configuration", None))
        self.settings_act.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.enc_by_letter_act.setText(QCoreApplication.translate("MainWindow", u"Encrypt letter by letter", None))
        self.en_from_file_act.setText(QCoreApplication.translate("MainWindow", u"Encrypt from file", None))
        self.a_r_rotor_act.setText(QCoreApplication.translate("MainWindow", u"Rotor", None))
        self.a_r_reflector_act.setText(QCoreApplication.translate("MainWindow", u"Reflector", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Your cipher text:", None))
        self.cipher_text.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Encryption steps:", None))
        self.letter_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Letter to encrypt", None))
        self.encrypt_button.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Current Configuration:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Rotors:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Reflector:", None))
        self.reflector_name.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Plugboard:", None))
        self.plugboard_connections.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Encrypt from file", None))
        self.brow_input_butt.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(shortcut)
        self.brow_input_butt.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.input_file_name.setText(QCoreApplication.translate("MainWindow", u"Hasn't selected file yet", None))
        self.output_file_name.setText(QCoreApplication.translate("MainWindow", u"Hasn't selected file yet (by default result.txt)", None))
        self.brow_output_butt.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(shortcut)
        self.brow_output_butt.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.brow_config_butt.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(shortcut)
        self.brow_config_butt.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.config_file_name.setText(QCoreApplication.translate("MainWindow", u"Hasn't selected file yet (by default .../rsc/config.json)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Input file:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Output file:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Configuration file:", None))
        self.encrypt_file_button.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
#if QT_CONFIG(shortcut)
        self.encrypt_file_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.is_double_step.setText(QCoreApplication.translate("MainWindow", u"Double step (only available with three rotors)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Space in encrypt text after                 signs", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"(if 0 encrypt text will be generate without spaces)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Change configuration", None))
        self.up_button.setText(QCoreApplication.translate("MainWindow", u"/\\", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Rotors:", None))
        self.down_button.setText(QCoreApplication.translate("MainWindow", u"\\/", None))
        self.save_init_conf_button.setText(QCoreApplication.translate("MainWindow", u"Save as initial", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Reflector:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Plugboard: ", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.remove_button.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Position:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Ring:", None))
        self.save_conf_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.set_plugboard_button.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.alphabet_label.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Available Custom Rotors", None))
        self.add_rotor_mod.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.rem_rotor_mod.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.mod_rotor_butt.setText(QCoreApplication.translate("MainWindow", u"Modify", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Modify Rotor", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Indentation(s)", None))
        self.alphabet_label_3.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Wiring", None))
        self.add_mod_rotor.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Wiring", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Indentation(s)", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Add Rotor", None))
        self.cancel_add_rotor.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.alphabet_label_2.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Available Custom Reflectors", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.modify_ref_button.setText(QCoreApplication.translate("MainWindow", u"Modify", None))
        self.reflector_mod_name.setPlaceholderText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Wiring", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Modify Reflector", None))
        self.alphabet_label_4.setText("")
        self.add_mod_ref.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Add Reflector", None))
        self.cancel_add_ref.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Wiring", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.alphabet_label_5.setText("")
        self.reflector_mod_name_2.setPlaceholderText("")
        self.add_ref_mod_butt.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.rem_ref_mod_button.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Enigma", None))
        self.menuMenu_2.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuAdd_Remove_elements.setTitle(QCoreApplication.translate("MainWindow", u"Custom Elements Manager", None))
    # retranslateUi

