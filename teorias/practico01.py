# Alumno: Menodoza Benito Sergio
# Carrera: Ingenieria de Sistemas
# Grupo: 1

biografia = """
    Hola mi nombre es Sergio Mendoza Benito, naci el 6 de marzo de 1995.
    Soy una persona a la que le apaciona todo lo relacionado a tecnologia
    siendo esta la razon por la cual decidi estudiar Ingenieria de Sistemas.

    Me gusta mucho programar y espero poder aprender las bases de la inteligencia
    artificial en este semestre para luego poder aplicarlo a futuros proyectos.    
"""
nombre = "Sergio Mendoza Benito"
carrera = "Ingenieria de sistemas"
grupoTeorico = 1
grupoPractico = 1
numeroDeContacto = "+591 65263449"

githubPersonal = "https://github.com/sergiombdev"


def menu():
    
    print("""
        --------------------------------------------
        MENU
        --------------------------------------------

        1) Biografia
        2) Ver nombre
        3) Mi github
        4) Contactos
        5) Ver grupo de la materia programados
        6) Salir
        
        --------------------------------------------
    """)

    return input("Escoge una opcion: ")


def iniciar():
    try:
        opcion  = int( menu() )
    except:
        print()
        print("No es una opcion valida!!")
        print()
        return iniciar()

    if( opcion == 6 ):
        return
    print()
    print("*"*30)

    if( opcion == 1 ):
        print("Biografia:")
        print(biografia)
    elif(opcion == 2):
        print("Nombre Completo:")
        print(nombre)
    elif(opcion == 3):
        print("Github:")
        print(githubPersonal)
    elif(opcion == 4):
        print("Contactos:")
        print(numeroDeContacto)
    elif(opcion == 5):
        print("Ver grupo de la materia programados:")
        print(nombre)
        print(carrera)
        print("Grupo Teorico: "+ str(grupoTeorico))
        print("Grupo Laboratorio: "+ str(grupoPractico))
    else:
        print("Opcion incorrecta!!")

    print("*"*30)
    print()
    return iniciar()

iniciar()