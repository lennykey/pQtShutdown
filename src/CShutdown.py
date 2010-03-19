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
        
        
        
    def startShutdown(self, option, minuten, passwort):
        self.__option= option
        self.__minuten= minuten
        
        passwortUebergabe= 'echo ' + passwort + ' | '
        superuserDo= 'sudo -S'
        command= 'shutdown'
        
        
        os.system(passwortUebergabe + superuserDo+ ' ' + command + ' ' + self.__option + ' ' + self.__minuten+'&')
        #print passwortUebergabe + superuserDo+ ' ' + command + ' ' + self.__option + ' ' + self.__minuten
    
    def stopShutdown(self, mitteilung, passwort):
        self.__mitteilung= mitteilung
        
        os.system('echo ' + passwort + ' |'+ 'sudo -S shutdown -c' + ' ' + self.__mitteilung)
        
        
        