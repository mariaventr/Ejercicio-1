class Email:
    __idCuenta= ""
    __dominio= ""
    __tipoDominio=""
    __contraseña= ""
    def __init__(self, idCuenta, dominio, tipoDominio, contraseña):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contraseña = contraseña
    
    def retornaEmail(self):
        return self.__idCuenta + "@" + self.__dominio + "." + self.__tipoDominio 
    
    def getDominio(self):
        return self.__dominio
    
    def crearCuenta(self, xcorreo):
        if xcorreo.find('@')!=-1:
            auxcorreo=xcorreo.split('@')
            user=auxcorreo[0]
            if not user:
                print("Error:El correo no contiene ID Cuenta")
            elif auxcorreo[1].find('.')!= -1:
                domCompleto=auxcorreo[1].split('.')
                auxdominio=domCompleto[0]
                if not auxdominio:
                    print("Error:El correo no contiene Dominio")
                else:
                    auxtipodominio=domCompleto[1]
                    if not auxtipodominio:
                        print("Error:El correo no contiene Tipo de Dominio")
                    else:
                        self.__idCuenta = user
                        self.__dominio = auxdominio
                        self.__tipoDominio = auxtipodominio
                        return(1)
            else: print('Error: El correo ingresado no contiene "."')
        else: print('Error: El correo ingresado no contiene @')

   
            
            
