# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settingsWidget(object):
    def setupUi(self, settingsWidget):
        settingsWidget.setObjectName("settingsWidget")
        settingsWidget.resize(800, 600)
        self.backButton = QtWidgets.QPushButton(settingsWidget)
        self.backButton.setGeometry(QtCore.QRect(10, 10, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")

        self.retranslateUi(settingsWidget)
        QtCore.QMetaObject.connectSlotsByName(settingsWidget)

    def retranslateUi(self, settingsWidget):
        _translate = QtCore.QCoreApplication.translate
        settingsWidget.setWindowTitle(_translate("settingsWidget", "Form"))
        self.backButton.setText(_translate("settingsWidget", "Go back"))