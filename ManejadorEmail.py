
import csv
from email import Email

class Manejador_Email:
    def __init__(self):
        self.__Cuentas=[]
    
    def cargarDatos(self):
        archivo=open("direcciones.csv", "r")
        direcciones=csv.reader(archivo, delimiter=",")
        for fila in direcciones:
            for elemento in fila:
                print(elemento)
                correo=Email("","","","")
                b=correo.crearCuenta(elemento)
                if b==1:
                    self.__Cuentas.append(correo)
                    print("Cuenta creada: ", correo.retornaEmail())
                else:
                    print("Correo Invalido:", elemento)
        archivo.close()
    
    def dominio(self):
        dominio=input("Ingresar dominio: ")
        cont=0
        for cuenta in self.__Cuentas:
                if cuenta.getDominio() == dominio:
                    cont+=1
        print(f"Hay {cont} objetos de la clase Email que tienen dominio igual al ingresado: {dominio}")