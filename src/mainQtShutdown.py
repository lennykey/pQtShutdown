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
        
        
    def startShut(self):
        #print 'Combo: ' + str(self.comboBox.currentText())
        if str(self.comboBox.currentText())== 'Shutdown':
            flag= '-P' 
            #print flag
        else:
            flag= '-c'
            #print flag
         
        #print 'Shutdown'    
        myShutdown= Shutdown()
        myShutdown.startShutdown(flag, str(self.spinBox.text()) , str(self.password.text()))
        
        print 'Ausgefuehrt'
        
    def stopShut(self):
        myShutdown= Shutdown()
        myShutdown.stopShutdown('Shutdown deaktiviert', str(self.password.text()))
        print 'Stop ausgefuehrt'
        
        
app= QtGui.QApplication(sys.argv)
dialog= MeinDialog()
dialog.show()





sys.exit(app.exec_())