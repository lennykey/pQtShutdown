# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Sat Mar 20 16:39:52 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(382, 149)
        Dialog.setMinimumSize(QtCore.QSize(382, 149))
        Dialog.setMaximumSize(QtCore.QSize(382, 149))
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 20, 271, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.pbShutdown = QtGui.QPushButton(self.layoutWidget)
        self.pbShutdown.setObjectName("pbShutdown")
        self.horizontalLayout.addWidget(self.pbShutdown)
        self.pbStop = QtGui.QPushButton(self.layoutWidget)
        self.pbStop.setDefault(False)
        self.pbStop.setObjectName("pbStop")
        self.horizontalLayout.addWidget(self.pbStop)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "pQtShutdown", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBox.setToolTip(QtGui.QApplication.translate("Dialog", "Minuten eingeben", None, QtGui.QApplication.UnicodeUTF8))
        self.pbShutdown.setToolTip(QtGui.QApplication.translate("Dialog", "Shutdown starten", None, QtGui.QApplication.UnicodeUTF8))
        self.pbShutdown.setText(QtGui.QApplication.translate("Dialog", "Shutdown", None, QtGui.QApplication.UnicodeUTF8))
        self.pbShutdown.setShortcut(QtGui.QApplication.translate("Dialog", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.pbStop.setToolTip(QtGui.QApplication.translate("Dialog", "Shutdown stoppen", None, QtGui.QApplication.UnicodeUTF8))
        self.pbStop.setText(QtGui.QApplication.translate("Dialog", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.pbStop.setShortcut(QtGui.QApplication.translate("Dialog", "Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))

