''' Klasse zur Ausfuehrung des Shutdownbefehls '''
import os

class Shutdown(object):
    
    __option= ''
    __minuten= ''
    __mitteilung=''
    
    def __init__(self, option='-P', minuten='1', mitteilung='Nothing'):
        self.__option= option
        self.__minuten= minuten
        self.__mitteilung= mitteilung
        
        
        
    def startShutdown(self, option, minuten):
        self.__option= option
        self.__minuten= minuten
        command= 'shutdown'

        os.system(command + ' ' + self.__option + ' ' + self.__minuten + '&')
    
    
    def stopShutdown(self, mitteilung):
        self.__mitteilung= mitteilung
        command= 'shutdown'
        option= '-c'
        
        os.system(command + ' ' + option + ' ' + self.__mitteilung + '&')
        
        
        