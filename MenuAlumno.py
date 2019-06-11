
global lista
lista = list()

#Defino los atributos del alumno
class Alumno:
    rut =""
    nombre = ""
    edad=0

def registrarAlumno():
    print ("Registro de Alummnos")
    a = Alumno()

    a.rut = str(input("Ingrese rut: "))
    a.nombre = str(input("Ingrese nombre: ")
    a.edad = input("Ingrese edad: ")


    lista.append(a)

def listarAlumno():
    print ("Lista de Alummnos")

    for a in lista:
        print (a.rut, "-", a.nombre, "-", a.edad, "-")


def buscarAlumno():
    print ("Buscar Alumnos")

def salir():
    print ("Gracias por utilizar la aplicación")

def menu():
    op = 0

    while op!= 4:
        #Mostrar el menu
        print ("Menu")
        print ("1.- Registrar Alumno")
        print ("2.- Listar Alumnos")
        print ("3.- Buscar Alumno")
        print ("4.- Salir")
        op =int(input("Digite opción: "))

        if (op == 1):
            registrarAlumno()
        elif op == 2:
            listarAlumno()
        elif op == 3:
            buscarAlumno()
        elif op == 4:
            salir()
            #exit //key para salir
            #exit() //key para salir



menu()
