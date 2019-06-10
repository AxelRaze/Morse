"""
>>> Morse = Morse(957)
>>> Morse.Encriptar()
>>> Morse.getElCodigoMorse()
'----......--...'
"""
class Morse:
    __numero = int(0)
    __tranformacion = int(0)
    __premorse = ''
    __morse = ''
#En este programa que hice se convierten los numero enteros a codigo morse
    def __init__(self, numero):
        self.__numero = numero
#Decidí llamar al metodo principal como encriptar, ya que se le aplicara al codigo normal una codificacion para que sea mas dificil descubrir el mensaje, en este caso una cifra
    def Encriptar(self):
        if(self.__numero >= 0):
            if((self.__numero - int(self.__numero))== 0):
                if(self.__numero == 0):
                    self.__morse = '-----'
                else:
                    while(self.__numero != 0):
                        self.__tranformacion = (self.__numero%10)
                        if(self.__tranformacion == 1):
                            self.__premorse = '.----'
                        elif(self.__tranformacion == 2):
                            self.__premorse = '..---'
                        elif (self.__tranformacion == 3):
                            self.__premorse = '...--'
                        elif (self.__tranformacion == 4):
                            self.__premorse = '....-'
                        elif (self.__tranformacion == 5):
                            self.__premorse = '.....'
                        elif (self.__tranformacion == 6):
                            self.__premorse = '-....'
                        elif (self.__tranformacion == 7):
                            self.__premorse = '--...'
                        elif (self.__tranformacion == 8):
                            self.__premorse = '---..'
                        elif (self.__tranformacion == 9):
                            self.__premorse = '----.'
                        else:
                            self.__premorse = '-----'
                        self.__morse = self.__premorse+self.__morse
                        self.__numero = int(self.__numero/10)
            else:
                self.__morse = 'Error'
        else:
            self.__morse = 'Error'

    def getElCodigoMorse(self):
        return self.__morse

if __name__=='__main__':
    import doctest
    doctest.testmod()

"""
Esto lo hizo AxelRaze

Y aqui estuvo "El Tocayo" :v
"""