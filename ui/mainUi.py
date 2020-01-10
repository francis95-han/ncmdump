# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '网易云音乐.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import os
import re
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QApplication, QDialog, QMessageBox, QSizePolicy

from config.logger import Logger
from ncmdump import dump
from ui.popout import Ui_Message


class Ui_ncmTransfer(object):
    def __init__(self):
        self.logger = Logger().getFroName("ncmTransfer")

    def setupUi(self, ncmTransfer):
        ncmTransfer.setObjectName("ncmTransfer")
        ncmTransfer.resize(384, 338)
        self.ncmTransfer = ncmTransfer
        self.chosenButton = QtWidgets.QDialogButtonBox(ncmTransfer)
        self.chosenButton.setGeometry(QtCore.QRect(30, 300, 341, 32))
        self.chosenButton.setOrientation(QtCore.Qt.Horizontal)
        self.chosenButton.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.chosenButton.setObjectName("chosenButton")
        self.message = QtWidgets.QTextBrowser(ncmTransfer)
        self.message.setGeometry(QtCore.QRect(20, 120, 351, 181))
        self.message.setObjectName("message")
        self.sourceButton = QtWidgets.QPushButton(ncmTransfer)
        self.sourceButton.setGeometry(QtCore.QRect(290, 6, 75, 21))
        self.sourceButton.setObjectName("sourceButton")
        self.sourceButton.clicked.connect(self.chosenSourcePath)
        self.label = QtWidgets.QLabel(ncmTransfer)
        self.label.setGeometry(QtCore.QRect(20, 10, 201, 16))
        self.label.setObjectName("label")
        self.sourcePathLabel = QtWidgets.QLineEdit(ncmTransfer)
        self.sourcePathLabel.setGeometry(QtCore.QRect(20, 30, 351, 20))
        self.sourcePathLabel.setObjectName("sourcePath")
        self.sourcePathLabel.setReadOnly(True)
        self.savePathLabel = QtWidgets.QLineEdit(ncmTransfer)
        self.savePathLabel.setGeometry(QtCore.QRect(20, 80, 351, 20))
        self.savePathLabel.setObjectName("savePath")
        self.savePathLabel.setReadOnly(True)

        self.label_2 = QtWidgets.QLabel(ncmTransfer)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 261, 16))
        self.label_2.setObjectName("label_2")
        self.saveButton = QtWidgets.QPushButton(ncmTransfer)
        self.saveButton.setGeometry(QtCore.QRect(290, 54, 75, 23))
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.chosenSavePath)

        self.retranslateUi(ncmTransfer)
        self.chosenButton.accepted.connect(self.ok)
        self.chosenButton.rejected.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(ncmTransfer)

        self.sourcePath = None
        self.sourceFiles = []
        self.savePath = None

    def validate_name(self, name):
        pattern = {u'\\': u'＼', u'/': u'／', u':': u'：', u'*': u'＊', u'?': u'？', u'"': u'＂', u'<': u'＜', u'>': u'＞', u'|': u'｜'}
        for character in pattern:
            name = name.replace(character, pattern[character])
        return name

    def validate_collision(self, path):
        index = 1
        origin = path
        while os.path.exists(path):
            path = '({})'.format(index).join(os.path.splitext(origin))
            index += 1
        return path

    def name_format(self, path, meta, format=""):
        information = {
            'artist': ','.join([artist[0] for artist in meta.get('artist')]) if 'artist' in meta else None,
            'title': meta.get('musicName'),
            'album': meta.get('album')
        }

        def substitute(matched):
            key = matched.group(1)
            if key in information:
                return information[key]
            else:
                return key

        name = re.sub(r'%(.+?)%', substitute, format)
        name = os.path.splitext(os.path.split(path)[1])[0] if not name else name
        name = self.validate_name(name)
        name += '.' + meta['format']
        folder = self.savePath if self.savePath else os.path.dirname(path)
        save = os.path.join(folder, name)
        return save

    def ok(self):
        if not self.sourcePathLabel.text():
            messageWindow = QDialog()
            message = Ui_Message()
            message.setupUi(messageWindow, "未选择ncm文件所在位置，请先选择ncm所在文件夹！！！")
            messageWindow.setWindowModality(Qt.ApplicationModal )
            messageWindow.setFixedSize(messageWindow.width(),messageWindow.height())
            messageWindow.show()
            messageWindow.exec_()
        elif len(self.sourceFiles) == 0 :
            messageWindow = QDialog()
            message = Ui_Message()
            message.setupUi(messageWindow, "您选择的文件夹中不包含ncm文件，请重新选择！！！")
            messageWindow.setWindowModality(Qt.ApplicationModal )
            messageWindow.show()
            messageWindow.exec_()
        else:
            self.showMessage("(*￣︶￣)~~选中的文件正在转码中~~(*￣︶￣)")
            for i in range(0, len(self.sourceFiles)):
                self.showMessage("转化中 --- {}%".format(str((i + 1) * 100 / len(self.sourceFiles))))
                self.showMessage("正在转化 --- " + self.sourceFiles[i])
                try:
                    self.logger.info("转化中 ---> {}".format(self.sourcePath + "/" + self.sourceFiles[i]))
                    mp3file = dump(self.sourcePath + "/" + self.sourceFiles[i],self.name_format)
                    self.showMessage("已生成 --- " + mp3file)
                    self.logger.info("生成文件 --- " + mp3file)
                except Exception as e:
                    self.logger.error(e)
            self.showMessage("转化完成")
            complateMessage = QMessageBox()
            complateMessage.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            complateMessage.setWindowModality(Qt.ApplicationModal )
            reply = complateMessage.question(self.ncmTransfer,"完成选择","确认退出吗？",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.ncmTransfer.accept()  # 接受关闭事件
            self.clearAll()
            self.message.clear()

    def clearAll(self):
        self.sourcePath = None
        self.sourcePathLabel.clear()
        self.savePathLabel.clear()
        self.sourceFiles = []
        self.savePath = None

    def close(self):
        sys.exit(QApplication.exec_())

    def showMessage(self, msg):
        self.message.append(msg)
        QApplication.processEvents()

    def chosenSourcePath(self):
        self.sourcePath = QFileDialog.getExistingDirectory(self.ncmTransfer)
        if self.sourcePath:
            self.sourcePathLabel.setText(self.sourcePath)
            self.savePathLabel.setText(self.sourcePath)
            self.savePath = self.sourcePath
        for (root, dirs, files) in os.walk(self.sourcePath):
            for file in files:
                if re.match(".*\.ncm$", str(file)) is not None:
                    self.sourceFiles.append(file)
                    self.logger.info("添加文件 ---> {}".format(file))
                    self.showMessage("已添加文件 --- " + file)

    def chosenSavePath(self):
        self.savePath = QFileDialog.getExistingDirectory(self.ncmTransfer)
        if self.savePath:
            self.savePathLabel.setText(self.savePath)

    def retranslateUi(self, ncmTransfer):
        _translate = QtCore.QCoreApplication.translate
        ncmTransfer.setWindowTitle(_translate("ncmTransfer", "ncm转换工具"))
        self.sourceButton.setText(_translate("ncmTransfer", "选择文件夹"))
        self.label.setText(_translate("ncmTransfer", "请选择ncm文件所在文件夹"))
        self.label_2.setText(_translate("ncmTransfer", "修改MP3文件所在文件夹（默认同ncm文件目录）"))
        self.saveButton.setText(_translate("ncmTransfer", "选择文件夹"))
