# %%
# Carrera: Ingenieria de Sistemas
# Grupo laboratorio: 1
# Materia: sis420


# Alumnos:
# Menodoza Benito Sergio
# Andrade Flores Carlos Francisco
# Polo Serrano Marco
# Ckuno Torihuano Jhonny Rodrigo



# Crear un software que simule un agente considerando, los diferentes tipos de escenarios y agentes que se revisaron en clases.
# El agente debe corresponder con una entidad que ubique un determinado numero de objetos que
# se estableceran al momento de uniciar el programa, el agente debe recorrer todo el laberinto hasta 
# encontrar todos los objetos a buscar, terminando su trabajo cuando encuentre el ultimo.
# Se debe controlar el tiempo que emplee en realizar este desafio.


# Se implementa un agente que recorre el laberinto aleatoriamente segun los posibles caminos disponibles a su alrededor
# los cuales actuan como sesores y de manera aleatoria se escoge un camino entre los espacios dispobles de manera aleatoria
# el juego termina cuando se encuentra todos los objetivos los cuales se crean de manera aleatoria en el mapa
# implementamos un contador de tiempo para ver cuanto tarda en terminar el juego

# %%
import random
import os
import sys
import time
sys.setrecursionlimit(99999999)

# %%
#funcion que genera un laberinto segun las dimenciones que le mandemos como parametro
def generarLaberinto( filas, columnas ):
    laberintoTemporal = []
    for row in range( 0, filas ):
        fila = []
        for column in range( 0, columnas ): 
            if( row == 0 or column == 0 or row == filas-1 or column == columnas - 1 ):
                fila.append( "#" )
            else:
                fila.append( " " )

        laberintoTemporal.append( fila )

    return laberintoTemporal

#funcion que dibuja el laberinto enviado por consola
def dibujarLaberinto( laberinto ):
    for row in laberinto:
        print( "".join( row ) )
        
#funcion que genera automaticamente las paredes del laberinto segun la cantidad que el usuario escoja
def generarParedes( laberinto, numeroParedes ):
    if( numeroParedes == 0 ):
        return

    x,y = [ random.randint( 1, len( laberinto ) -2 ), random.randint( 1, len( laberinto[ 0 ] ) - 2) ]
    if( laberinto[x][y] == " " ):
        if( laberinto[ x ][ y - 1 ] == " "  or
            laberinto[ x ][ y + 1 ] == " "  or
            laberinto[ x + 1 ][ y ] == " "  or
            laberinto[ x - 1 ][ y ] == " " ):

            laberinto[ x ][ y ] = "#"
            numeroParedes = numeroParedes - 1
    return generarParedes( laberinto, numeroParedes )

#funcion que genera el sujeto que buscara la meta en el laberinto
def generarCoordenadasInicio( laberinto = None, jugador = None):
    x, y = [ random.randint( 1, len( laberinto ) - 2 ), random.randint( 1, len( laberinto[ 0 ] ) - 2)]
    
    if( laberinto[x][y] == " " ):
        laberinto[x][y] = jugador
        return [x,y]
    else:
        return generarCoordenadasInicio( laberinto, jugador )

#funcion que genera la meta en el laberinto
def generarObjetivos( laberinto, numeroObjetivos ):
    if( numeroObjetivos == 0):
        return

    x, y = [ random.randint( 1, len( laberinto ) - 2 ), random.randint( 1, len( laberinto[ 0 ] ) - 2)]

    if( laberinto[x][y] == " "):
        laberinto[x][y] = "o"
        numeroObjetivos = numeroObjetivos - 1     
        return generarObjetivos( laberinto, numeroObjetivos )
    else:
        return generarObjetivos( laberinto, numeroObjetivos )
   
       


#funcion recursiva que resolvera el laberinto
def resolverLaberinto( laberinto, coordJugador, numeroObjetivos, objetivosEncontrados ):

    os.system("cls")
    print("-"*len(laberinto)*2)
    dibujarLaberinto(laberinto)
    print("Objetivosencontrados "+ str(objetivosEncontrados))

    if(numeroObjetivos == objetivosEncontrados):
        print("Fin")
        return

    x, y = coordJugador
    listaCamino = []
    visitado = []
    objetivos = []

    movimientos = [ [x-1,y], [x+1,y], [x,y-1], [x,y+1] ]
   
    for [coordX, coordY] in movimientos:
        if( laberinto[coordX][coordY] == " "):
            listaCamino.append([coordX, coordY])
        if( laberinto[coordX][coordY] == "."):
            visitado.append([coordX, coordY])
        if( laberinto[coordX][coordY] == "o"):
            objetivos.append([coordX, coordY])

    

    if(len(objetivos)>0):
        moverX, moverY = objetivos[ random.randint(0,len(objetivos)-1) ]
        laberinto[moverX][moverY] = laberinto[x][y]
        laberinto[x][y] = "."
        objetivosEncontrados = objetivosEncontrados + 1
        return resolverLaberinto( laberinto,  [moverX, moverY], numeroObjetivos, objetivosEncontrados )

    if( len( listaCamino ) > 0 ):
        moverX, moverY = listaCamino[ random.randint(0,len(listaCamino)-1) ]
        laberinto[moverX][moverY] = laberinto[x][y]
        laberinto[x][y] = "."
        return resolverLaberinto( laberinto,  [moverX, moverY], numeroObjetivos, objetivosEncontrados )

    elif( len( visitado ) > 0 ):
        moverX, moverY = visitado[ random.randint(0,len(visitado)-1) ]
        laberinto[moverX][moverY] = laberinto[x][y]
        laberinto[x][y] = "."
        return resolverLaberinto( laberinto,  [moverX, moverY], numeroObjetivos, objetivosEncontrados )
    else:
        print("sin solucion")
        return


# funcion que inicia el programa
def inicio():
    try:
        filas = int( input("Introduce el numero de filas") )
        columnas = int( input("Introduce el numero de columnas") )
        numParedes = int( input("Introduce el numero de paredes") )
    except:
        print("Solo se permiten numeros enteros.")
        return inicio()
    
    if(filas < 4 or columnas < 4):
        print("Las dimenciones del laberinto debe ser mayor a 4 para que el laberinto funcione")
        return inicio()


    if( numParedes < 1 or numParedes > ( (filas - 2) * (columnas -2) ) - 2 - 9  ):
        print("El numero de paredes no debe superar el limite perimito de : "+ str(( (filas - 2) * (columnas -2) ) - 2 - 9))
        return inicio()

    print( "Dimencion del laberinto: "+str( filas )+" x "+str( columnas ) )
    print( "Numero de paredes: "+str( numParedes ) )

    return [filas, columnas, numParedes]

# %%
filas, columnas, numParedes = inicio()

# %%
laberinto = generarLaberinto( filas, columnas )
generarParedes( laberinto, numParedes )

coordenadasJugador = generarCoordenadasInicio( laberinto, "*" )
numeroObjetivos = 10

generarObjetivos( laberinto, numeroObjetivos)

print("Inicio: *")
print("Objetivos: o")

dibujarLaberinto(laberinto)

objetivosEncontrados = 0

numeroObjetivosTotal = 10

TiempoInicio = time.time()

resolverLaberinto(laberinto, coordenadasJugador, numeroObjetivosTotal, objetivosEncontrados)
TiempoFin = time.time()

print("Tiempo transcurrido: "+ str(TiempoFin - TiempoInicio) + " segundos")

