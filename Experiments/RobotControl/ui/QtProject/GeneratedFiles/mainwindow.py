# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created: Mon Mar  9 16:20:04 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(383, 621)
        MainWindow.setIconSize(QtCore.QSize(64, 64))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 15, 321, 191))
        self.groupBox.setObjectName("groupBox")
        self.ip_line_edit = QtGui.QLineEdit(self.groupBox)
        self.ip_line_edit.setGeometry(QtCore.QRect(160, 40, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ip_line_edit.setFont(font)
        self.ip_line_edit.setObjectName("ip_line_edit")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(28, 61, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.port_line_edit = QtGui.QLineEdit(self.groupBox)
        self.port_line_edit.setGeometry(QtCore.QRect(160, 68, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.port_line_edit.setFont(font)
        self.port_line_edit.setObjectName("port_line_edit")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(56, 33, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(56, 104, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.connection_status = QtGui.QLineEdit(self.groupBox)
        self.connection_status.setGeometry(QtCore.QRect(140, 110, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.connection_status.setFont(font)
        self.connection_status.setReadOnly(True)
        self.connection_status.setObjectName("connection_status")
        self.connect_button = QtGui.QPushButton(self.groupBox)
        self.connect_button.setGeometry(QtCore.QRect(110, 146, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.connect_button.setFont(font)
        self.connect_button.setObjectName("connect_button")
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 240, 321, 321))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.rotate_right_button = QtGui.QPushButton(self.tab)
        self.rotate_right_button.setGeometry(QtCore.QRect(30, 20, 60, 60))
        self.rotate_right_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/resources/rorate_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rotate_right_button.setIcon(icon)
        self.rotate_right_button.setIconSize(QtCore.QSize(45, 45))
        self.rotate_right_button.setObjectName("rotate_right_button")
        self.up_button = QtGui.QPushButton(self.tab)
        self.up_button.setGeometry(QtCore.QRect(128, 93, 60, 60))
        self.up_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/resources/arrow_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.up_button.setIcon(icon1)
        self.up_button.setIconSize(QtCore.QSize(32, 32))
        self.up_button.setObjectName("up_button")
        self.right_button = QtGui.QPushButton(self.tab)
        self.right_button.setGeometry(QtCore.QRect(186, 153, 60, 60))
        self.right_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            ":/resources/arrow_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.right_button.setIcon(icon2)
        self.right_button.setIconSize(QtCore.QSize(32, 32))
        self.right_button.setObjectName("right_button")
        self.down_button = QtGui.QPushButton(self.tab)
        self.down_button.setGeometry(QtCore.QRect(128, 210, 60, 60))
        self.down_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(
            ":/resources/arrow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.down_button.setIcon(icon3)
        self.down_button.setIconSize(QtCore.QSize(32, 32))
        self.down_button.setObjectName("down_button")
        self.left_button = QtGui.QPushButton(self.tab)
        self.left_button.setGeometry(QtCore.QRect(69, 153, 60, 60))
        self.left_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(
            ":/resources/arrow_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left_button.setIcon(icon4)
        self.left_button.setIconSize(QtCore.QSize(32, 32))
        self.left_button.setObjectName("left_button")
        self.rotate_left_button = QtGui.QPushButton(self.tab)
        self.rotate_left_button.setGeometry(QtCore.QRect(228, 20, 60, 60))
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
        self.question_request_button.setGeometry(QtCore.QRect(70, 30, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.question_request_button.setFont(font)
        self.question_request_button.setObjectName("question_request_button")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 383, 21))
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
        self.question_request_button.setText(QtGui.QApplication.translate(
            "MainWindow", "Requête de question", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate(
            "MainWindow", "Question", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate(
            "MainWindow", "Préhenseur", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate(
            "MainWindow", "Caméra", None, QtGui.QApplication.UnicodeUTF8))

import Experiments.RobotControl.ui.QtProject.GeneratedFiles.resource_rc
