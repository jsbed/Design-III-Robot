# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created: Sun Mar 22 21:05:14 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 609)
        MainWindow.setIconSize(QtCore.QSize(64, 64))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 15, 361, 191))
        self.groupBox.setObjectName("groupBox")
        self.ip_line_edit = QtGui.QLineEdit(self.groupBox)
        self.ip_line_edit.setGeometry(QtCore.QRect(181, 40, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ip_line_edit.setFont(font)
        self.ip_line_edit.setObjectName("ip_line_edit")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(49, 61, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.port_line_edit = QtGui.QLineEdit(self.groupBox)
        self.port_line_edit.setGeometry(QtCore.QRect(181, 68, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.port_line_edit.setFont(font)
        self.port_line_edit.setObjectName("port_line_edit")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(77, 33, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(77, 104, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.connection_status = QtGui.QLineEdit(self.groupBox)
        self.connection_status.setGeometry(QtCore.QRect(161, 110, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.connection_status.setFont(font)
        self.connection_status.setReadOnly(True)
        self.connection_status.setObjectName("connection_status")
        self.connect_button = QtGui.QPushButton(self.groupBox)
        self.connect_button.setGeometry(QtCore.QRect(131, 146, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.connect_button.setFont(font)
        self.connect_button.setObjectName("connect_button")
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 240, 361, 321))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.rotate_right_button = QtGui.QPushButton(self.tab)
        self.rotate_right_button.setGeometry(QtCore.QRect(51, 20, 60, 60))
        self.rotate_right_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/resources/rorate_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rotate_right_button.setIcon(icon)
        self.rotate_right_button.setIconSize(QtCore.QSize(45, 45))
        self.rotate_right_button.setObjectName("rotate_right_button")
        self.up_button = QtGui.QPushButton(self.tab)
        self.up_button.setGeometry(QtCore.QRect(149, 93, 60, 60))
        self.up_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/resources/arrow_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.up_button.setIcon(icon1)
        self.up_button.setIconSize(QtCore.QSize(32, 32))
        self.up_button.setObjectName("up_button")
        self.right_button = QtGui.QPushButton(self.tab)
        self.right_button.setGeometry(QtCore.QRect(207, 153, 60, 60))
        self.right_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            ":/resources/arrow_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.right_button.setIcon(icon2)
        self.right_button.setIconSize(QtCore.QSize(32, 32))
        self.right_button.setObjectName("right_button")
        self.down_button = QtGui.QPushButton(self.tab)
        self.down_button.setGeometry(QtCore.QRect(149, 210, 60, 60))
        self.down_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(
            ":/resources/arrow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.down_button.setIcon(icon3)
        self.down_button.setIconSize(QtCore.QSize(32, 32))
        self.down_button.setObjectName("down_button")
        self.left_button = QtGui.QPushButton(self.tab)
        self.left_button.setGeometry(QtCore.QRect(90, 153, 60, 60))
        self.left_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(
            ":/resources/arrow_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left_button.setIcon(icon4)
        self.left_button.setIconSize(QtCore.QSize(32, 32))
        self.left_button.setObjectName("left_button")
        self.rotate_left_button = QtGui.QPushButton(self.tab)
        self.rotate_left_button.setGeometry(QtCore.QRect(249, 20, 60, 60))
        self.rotate_left_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(
            ":/resources/rotate_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rotate_left_button.setIcon(icon5)
        self.rotate_left_button.setIconSize(QtCore.QSize(45, 45))
        self.rotate_left_button.setObjectName("rotate_left_button")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.question_request_button = QtGui.QPushButton(self.tab_2)
        self.question_request_button.setGeometry(QtCore.QRect(90, 30, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.question_request_button.setFont(font)
        self.question_request_button.setObjectName("question_request_button")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.display_country_button = QtGui.QPushButton(self.tab_5)
        self.display_country_button.setGeometry(QtCore.QRect(120, 42, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.display_country_button.setFont(font)
        self.display_country_button.setObjectName("display_country_button")
        self.led_country_line_edit = QtGui.QLineEdit(self.tab_5)
        self.led_country_line_edit.setGeometry(QtCore.QRect(159, 14, 113, 20))
        self.led_country_line_edit.setObjectName("led_country_line_edit")
        self.label_3 = QtGui.QLabel(self.tab_5)
        self.label_3.setGeometry(QtCore.QRect(70, 11, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.square_color_combo_box = QtGui.QComboBox(self.tab_5)
        self.square_color_combo_box.setGeometry(QtCore.QRect(190, 100, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.square_color_combo_box.setFont(font)
        self.square_color_combo_box.setObjectName("square_color_combo_box")
        self.square_color_combo_box.addItem("")
        self.square_color_combo_box.addItem("")
        self.square_color_combo_box.addItem("")
        self.square_color_combo_box.addItem("")
        self.square_color_combo_box.addItem("")
        self.square_color_combo_box.addItem("")
        self.square_color_combo_box.addItem("")
        self.label_5 = QtGui.QLabel(self.tab_5)
        self.label_5.setGeometry(QtCore.QRect(57, 100, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.tab_5)
        self.label_6.setGeometry(QtCore.QRect(85, 130, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.square_number_combo_box = QtGui.QComboBox(self.tab_5)
        self.square_number_combo_box.setGeometry(
            QtCore.QRect(190, 130, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.square_number_combo_box.setFont(font)
        self.square_number_combo_box.setObjectName("square_number_combo_box")
        self.square_number_combo_box.addItem("")
        self.square_number_combo_box.addItem("")
        self.square_number_combo_box.addItem("")
        self.square_number_combo_box.addItem("")
        self.square_number_combo_box.addItem("")
        self.square_number_combo_box.addItem("")
        self.square_number_combo_box.addItem("")
        self.square_number_combo_box.addItem("")
        self.square_number_combo_box.addItem("")
        self.update_square_button = QtGui.QPushButton(self.tab_5)
        self.update_square_button.setGeometry(QtCore.QRect(140, 162, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.update_square_button.setFont(font)
        self.update_square_button.setObjectName("update_square_button")
        self.line = QtGui.QFrame(self.tab_5)
        self.line.setGeometry(QtCore.QRect(0, 80, 361, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtGui.QFrame(self.tab_5)
        self.line_2.setGeometry(QtCore.QRect(0, 198, 361, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.open_red_led_button = QtGui.QPushButton(self.tab_5)
        self.open_red_led_button.setGeometry(QtCore.QRect(70, 222, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.open_red_led_button.setFont(font)
        self.open_red_led_button.setObjectName("open_red_led_button")
        self.close_red_led_button = QtGui.QPushButton(self.tab_5)
        self.close_red_led_button.setGeometry(QtCore.QRect(180, 221, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.close_red_led_button.setFont(font)
        self.close_red_led_button.setObjectName("close_red_led_button")
        self.close_all_leds_button = QtGui.QPushButton(self.tab_5)
        self.close_all_leds_button.setGeometry(QtCore.QRect(123, 258, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.close_all_leds_button.setFont(font)
        self.close_all_leds_button.setObjectName("close_all_leds_button")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.take_cube_button = QtGui.QPushButton(self.tab_3)
        self.take_cube_button.setGeometry(QtCore.QRect(105, 30, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.take_cube_button.setFont(font)
        self.take_cube_button.setObjectName("take_cube_button")
        self.drop_cube_button = QtGui.QPushButton(self.tab_3)
        self.drop_cube_button.setGeometry(QtCore.QRect(105, 76, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.drop_cube_button.setFont(font)
        self.drop_cube_button.setObjectName("drop_cube_button")
        self.lift_gripper_button = QtGui.QPushButton(self.tab_3)
        self.lift_gripper_button.setGeometry(QtCore.QRect(105, 174, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lift_gripper_button.setFont(font)
        self.lift_gripper_button.setObjectName("lift_gripper_button")
        self.lower_gripper_button = QtGui.QPushButton(self.tab_3)
        self.lower_gripper_button.setGeometry(QtCore.QRect(105, 220, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lower_gripper_button.setFont(font)
        self.lower_gripper_button.setObjectName("lower_gripper_button")
        self.open_gripper_max_button = QtGui.QPushButton(self.tab_3)
        self.open_gripper_max_button.setGeometry(
            QtCore.QRect(105, 126, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.open_gripper_max_button.setFont(font)
        self.open_gripper_max_button.setObjectName("open_gripper_max_button")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 420, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate(
            "MainWindow", "Robot Controler", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate(
            "MainWindow", "Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.ip_line_edit.setText(QtGui.QApplication.translate(
            "MainWindow", "127.0.0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate(
            "MainWindow", "Server PORT :", None, QtGui.QApplication.UnicodeUTF8))
        self.port_line_edit.setText(QtGui.QApplication.translate(
            "MainWindow", "5000", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate(
            "MainWindow", "Server IP :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate(
            "MainWindow", "Status -", None, QtGui.QApplication.UnicodeUTF8))
        self.connection_status.setText(QtGui.QApplication.translate(
            "MainWindow", "No connection", None, QtGui.QApplication.UnicodeUTF8))
        self.connect_button.setText(QtGui.QApplication.translate(
            "MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate(
            "MainWindow", "Déplacement", None, QtGui.QApplication.UnicodeUTF8))
        self.question_request_button.setText(QtGui.QApplication.translate("MainWindow", "Requête + analyse \n"
                                                                          "de question", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate(
            "MainWindow", "Question", None, QtGui.QApplication.UnicodeUTF8))
        self.display_country_button.setText(QtGui.QApplication.translate(
            "MainWindow", "Display Country", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate(
            "MainWindow", "Country :", None, QtGui.QApplication.UnicodeUTF8))
        self.square_color_combo_box.setItemText(0, QtGui.QApplication.translate(
            "MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.square_color_combo_box.setItemText(1, QtGui.QApplication.translate(
            "MainWindow", "Red", None, QtGui.QApplication.UnicodeUTF8))
        self.square_color_combo_box.setItemText(2, QtGui.QApplication.translate(
            "MainWindow", "Green", None, QtGui.QApplication.UnicodeUTF8))
        self.square_color_combo_box.setItemText(3, QtGui.QApplication.translate(
            "MainWindow", "Blue", None, QtGui.QApplication.UnicodeUTF8))
        self.square_color_combo_box.setItemText(4, QtGui.QApplication.translate(
            "MainWindow", "Yellow", None, QtGui.QApplication.UnicodeUTF8))
        self.square_color_combo_box.setItemText(5, QtGui.QApplication.translate(
            "MainWindow", "White", None, QtGui.QApplication.UnicodeUTF8))
        self.square_color_combo_box.setItemText(6, QtGui.QApplication.translate(
            "MainWindow", "Black", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate(
            "MainWindow", "Square Color :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate(
            "MainWindow", "Square # :", None, QtGui.QApplication.UnicodeUTF8))
        self.square_number_combo_box.setItemText(0, QtGui.QApplication.translate(
            "MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.square_number_combo_box.setItemText(1, QtGui.QApplication.translate(
            "MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.square_number_combo_box.setItemText(2, QtGui.QApplication.translate(
            "MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.square_number_combo_box.setItemText(3, QtGui.QApplication.translate(
            "MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.square_number_combo_box.setItemText(4, QtGui.QApplication.translate(
            "MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.square_number_combo_box.setItemText(5, QtGui.QApplication.translate(
            "MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.square_number_combo_box.setItemText(6, QtGui.QApplication.translate(
            "MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.square_number_combo_box.setItemText(7, QtGui.QApplication.translate(
            "MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.square_number_combo_box.setItemText(8, QtGui.QApplication.translate(
            "MainWindow", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.update_square_button.setText(QtGui.QApplication.translate(
            "MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.open_red_led_button.setText(QtGui.QApplication.translate(
            "MainWindow", "Open Red LED", None, QtGui.QApplication.UnicodeUTF8))
        self.close_red_led_button.setText(QtGui.QApplication.translate(
            "MainWindow", "Close Red LED", None, QtGui.QApplication.UnicodeUTF8))
        self.close_all_leds_button.setText(QtGui.QApplication.translate(
            "MainWindow", "Close All LEDs", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate(
            "MainWindow", "LEDs", None, QtGui.QApplication.UnicodeUTF8))
        self.take_cube_button.setText(QtGui.QApplication.translate(
            "MainWindow", "Prendre cube", None, QtGui.QApplication.UnicodeUTF8))
        self.drop_cube_button.setText(QtGui.QApplication.translate(
            "MainWindow", "Laisser cube", None, QtGui.QApplication.UnicodeUTF8))
        self.lift_gripper_button.setText(QtGui.QApplication.translate(
            "MainWindow", "Lever", None, QtGui.QApplication.UnicodeUTF8))
        self.lower_gripper_button.setText(QtGui.QApplication.translate(
            "MainWindow", "Baisser", None, QtGui.QApplication.UnicodeUTF8))
        self.open_gripper_max_button.setText(QtGui.QApplication.translate(
            "MainWindow", "Ouvrir pince max", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate(
            "MainWindow", "Préhenseur", None, QtGui.QApplication.UnicodeUTF8))

import Experiments.RobotControl.ui.QtProject.GeneratedFiles.resource_rc