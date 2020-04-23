# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ayieko/Projects And  Research/PycharmProjects/HttpServer/GUI/startupDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(321, 230)
        self.SDTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.SDTextEdit.setGeometry(QtCore.QRect(0, 0, 321, 44))
        self.SDTextEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.SDTextEdit.setReadOnly(True)
        self.SDTextEdit.setObjectName("SDTextEdit")
        self.SDHostEntry = QtWidgets.QLineEdit(Form)
        self.SDHostEntry.setGeometry(QtCore.QRect(70, 60, 161, 20))
        self.SDHostEntry.setObjectName("SDHostEntry")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 60, 51, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 51, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.SDPortEntry = QtWidgets.QLineEdit(Form)
        self.SDPortEntry.setGeometry(QtCore.QRect(80, 100, 91, 20))
        self.SDPortEntry.setObjectName("SDPortEntry")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 51, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.SDPasswordEntry = QtWidgets.QLineEdit(Form)
        self.SDPasswordEntry.setGeometry(QtCore.QRect(80, 140, 201, 20))
        self.SDPasswordEntry.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.SDPasswordEntry.setObjectName("SDPasswordEntry")
        self.SDStartButton = QtWidgets.QPushButton(Form)
        self.SDStartButton.setGeometry(QtCore.QRect(60, 182, 75, 31))
        self.SDStartButton.setObjectName("SDStartButton")
        self.SDCancelButton = QtWidgets.QPushButton(Form)
        self.SDCancelButton.setGeometry(QtCore.QRect(180, 182, 75, 31))
        self.SDCancelButton.setObjectName("SDCancelButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Start Up Connection SetUp"))
        self.SDTextEdit.setPlainText(_translate("Form", "Please Enter The Administrative Details Of The Server You Want To Start."))
        self.SDHostEntry.setWhatsThis(_translate("Form", "Hostname or IP address. To refer to this computer, enter localhost(Default)"))
        self.SDHostEntry.setText(_translate("Form", "localhost"))
        self.label.setText(_translate("Form", "Host"))
        self.label_2.setText(_translate("Form", "Port"))
        self.SDPortEntry.setWhatsThis(_translate("Form", "Enter the administration port (8000 by default)"))
        self.SDPortEntry.setText(_translate("Form", "8000"))
        self.label_3.setText(_translate("Form", "Password"))
        self.SDPasswordEntry.setWhatsThis(_translate("Form", "Adding a password wont allow browser requests"))
        self.SDPasswordEntry.setPlaceholderText(_translate("Form", "Server Password"))
        self.SDStartButton.setWhatsThis(_translate("Form", "Start the server with the above settings"))
        self.SDStartButton.setText(_translate("Form", "START!"))
        self.SDCancelButton.setText(_translate("Form", "Cancel"))


