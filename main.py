from email import Email
from ManejadorEmail import Manejador_Email

def test():
    # Prueba punto 1
    usuario = input("Ingrese el id de cuenta: ")
    dominio = input("Ingrese el dominio: ")
    tipo = input("Ingrese el tipo de dominio: ")
    clave=input("Ingresar clave: ")
    e1 = Email(usuario, dominio, tipo, clave)
    nombre = input("Ingrese su nombre: ")
    print("Estimado", nombre, "te enviaremos tus mensajes a la dirección", e1.retornaEmail())

    # Prueba punto 2
    contraseñaActual = input("Ingrese la contraseña actual: ")
    if clave == contraseñaActual:
        nuevaContraseña = input("Ingrese la nueva contraseña: ")
        e1 = Email(usuario, dominio, tipo, nuevaContraseña)
        print("Contraseña modificada exitosamente")
    else:
        print("La contraseña actual no es correcta")

    # Prueba punto 3
    direccionCorreo = input("Ingrese una dirección de correo electrónico: ")
    e2 = Email("", "", "", "")
    c=e2.crearCuenta(direccionCorreo)
    if(c==1):
        print("Dirección de correo creada:", e2.retornaEmail())
    else:
        print("La dirección de correo ingresada es invalida")
    
    #Prueba punto 4
    lista=Manejador_Email()
    lista.cargarDatos()
    lista.dominio()

if __name__ == "__main__":
    test()
