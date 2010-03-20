#!/usr/bin/env python

from CShutdown import Shutdown
from dialog import Ui_Dialog as Dlg
from PyQt4 import QtGui, QtCore
import sys


class MeinDialog(QtGui.QDialog, Dlg):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        
        #Slots einrichten
        self.connect(self.pbShutdown, QtCore.SIGNAL("clicked()"), self.startShut)
        self.connect(self.pbStop, QtCore.SIGNAL("clicked()"), self.stopShut)
        self.pbStop.setDisabled(1)
        
        
        
    def startShut(self):
        #print 'Combo: ' + str(self.comboBox.currentText())
        flag= '-P' 
         
        #print 'Shutdown'    
        myShutdown= Shutdown()
        myShutdown.startShutdown(flag, str(self.spinBox.text()))
        self.pbShutdown.setDisabled(1)
        self.pbStop.setEnabled(1)
        
        print 'Ausgefuehrt'
        
    def stopShut(self):
        myShutdown= Shutdown()
        myShutdown.stopShutdown('Shutdown deaktiviert')
        self.pbShutdown.setEnabled(1)
        self.pbStop.setDisabled(1)
        print 'Stop ausgefuehrt'
        
        
app= QtGui.QApplication(sys.argv)
dialog= MeinDialog()
dialog.show()





sys.exit(app.exec_())
