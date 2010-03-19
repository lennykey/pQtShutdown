# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Fri Mar 19 19:16:28 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(507, 148)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 40, 471, 61))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setEditable(False)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem('Shutdown')
        self.comboBox.addItem('Stop')
        self.horizontalLayout.addWidget(self.comboBox)
        self.spinBox = QtGui.QSpinBox(self.widget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.password = QtGui.QLineEdit(self.widget)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName("password")
        self.horizontalLayout.addWidget(self.password)
        self.pbShutdown = QtGui.QPushButton(self.widget)
        self.pbShutdown.setObjectName("pbShutdown")
        self.horizontalLayout.addWidget(self.pbShutdown)
        self.pbStop = QtGui.QPushButton(self.widget)
        self.pbStop.setDefault(False)
        self.pbStop.setObjectName("pbStop")
        self.horizontalLayout.addWidget(self.pbStop)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pbShutdown.setText(QtGui.QApplication.translate("Dialog", "Shutdown", None, QtGui.QApplication.UnicodeUTF8))
        self.pbShutdown.setShortcut(QtGui.QApplication.translate("Dialog", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.pbStop.setText(QtGui.QApplication.translate("Dialog", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.pbStop.setShortcut(QtGui.QApplication.translate("Dialog", "Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))

