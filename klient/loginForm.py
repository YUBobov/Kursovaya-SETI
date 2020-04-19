# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogDialog(object):
    def setupUi(self, LogDialog):
        LogDialog.setObjectName("LogDialog")
        LogDialog.resize(292, 182)
        self.lineEdit_log = QtWidgets.QLineEdit(LogDialog)
        self.lineEdit_log.setGeometry(QtCore.QRect(100, 60, 113, 20))
        self.lineEdit_log.setObjectName("lineEdit")
        self.lineEdit_pass = QtWidgets.QLineEdit(LogDialog)
        self.lineEdit_pass.setGeometry(QtCore.QRect(100, 90, 113, 20))
        self.lineEdit_pass.setObjectName("lineEdit_2")
        self.label_log = QtWidgets.QLabel(LogDialog)
        self.label_log.setGeometry(QtCore.QRect(40, 60, 47, 13))
        self.label_log.setObjectName("label")
        self.label_pass = QtWidgets.QLabel(LogDialog)
        self.label_pass.setGeometry(QtCore.QRect(40, 90, 47, 13))
        self.label_pass.setObjectName("label_2")
        self.loginButton = QtWidgets.QPushButton(LogDialog)
        self.loginButton.setGeometry(QtCore.QRect(120, 130, 75, 23))
        self.loginButton.setObjectName("pushButton")

        self.retranslateUi(LogDialog)
        QtCore.QMetaObject.connectSlotsByName(LogDialog)

    def retranslateUi(self, LogDialog):
        _translate = QtCore.QCoreApplication.translate
        LogDialog.setWindowTitle(_translate("LogDialog", "Login"))
        self.label_log.setText(_translate("LogDialog", "Name"))
        self.label_pass.setText(_translate("LogDialog", "Password"))
        self.loginButton.setText(_translate("LogDialog", "Login"))
