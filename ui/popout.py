# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QSizePolicy


class Ui_Message(object):
    def setupUi(self, Message, msg):
        Message.setObjectName("Message")
        Message.resize(350, 60)
        Message.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.Message = Message
        self.message = QtWidgets.QLabel(Message)
        self.message.setGeometry(QtCore.QRect(10, 5, 361, 21))
        self.message.setObjectName("message")
        self.messageOk = QtWidgets.QPushButton(Message)
        self.messageOk.setGeometry(QtCore.QRect(140, 30, 60, 20))
        self.messageOk.setObjectName("pushButton")
        self.messageOk.clicked.connect(Message.accept)

        self.retranslateUi(Message, msg)
        QtCore.QMetaObject.connectSlotsByName(Message)

    def retranslateUi(self, Form, msg):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "提示信息"))
        self.message.setText(_translate("Form", msg))
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.messageOk.setText(_translate("Form", "确认"))
