
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@author zhangbohan.dell@gmail.com
@function:
@create 1/10/2020 8:07 PM
"""
import sys

from PyQt5.QtWidgets import QApplication, QDialog

from ui.mainUi import Ui_ncmTransfer

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialog()
    ncmTransfer = Ui_ncmTransfer()
    ncmTransfer.setupUi(window)
    window.show()
    sys.exit(app.exec_())
