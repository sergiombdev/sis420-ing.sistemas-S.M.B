# %%
# Carrera: Ingenieria de Sistemas
# Grupo laboratorio: 1
# Materia: sis420
# gihub : https://github.com/sergiombdev/sis420-ing.sistemas-S.M.B.git

# Alumnos:
# Menodoza Benito Sergio
# Andrade Flores Carlos Francisco


# A partir del codigo proporcionado para resolver un rompecabezas de con cuatro digitos de tipo lineal, 
# que solo permite un movimiento simultane entre dos numeros contiguos solamente, desarrollar lo siguiente:
# Implementar una funcion que permita expandir nodos hijos para n caracteres, los cuales deben ser establecidos al momento de iniciar el programa.
# Describir cual es el nivel maximo de numero de digitos que el rompecabezas se puede 
# resolver en su maquina, explicando a que se deberia este limite y como se lo podria superara.
# hacer correr el mismo programa, pero utilizando una lista LIFO para la lista frontera.


# Solucion
# El numero maximo de digitos que podria correr mi maquina es el mismo limite del tamaño permitido por el array en python
# aunque por obvias razones el proceso de encontrar la solucion demoraria mas de lo esperado
# el numero de digitos que podria calcular en tiempo aceptable oscila entre 10 y 15 digitos con un tiempo de 30 seg 
# dicho proceso se podria mejorar aumentando la capacidad de los componentes fisicos como la memoria ram y el cpu el proceso seria mucho mas rapido.

# Existe otro factor que podria mejorar el tiempo que tarda al encontrar el resultado y este es el algoritom de busqueda que implementamos,
# este podria cambiarse por otro que sea mas optimo al momneto de procesar la informacion
# al ser este un algortmo de busqueda en anchura si los digitos son muy grandes tendremos arbol binario demaciado extenso e cual tendriamos que recorrer 
# para encontrar la solucion.



# %%
class Nodo:
    def __init__(self, datos, hijo=None):
        self.datos = datos
        self.hijos = []
        self.padre = None
        self.costo = None
        self.set_hijo(hijo)
        
    def set_hijo(self, hijo):
        if (hijo is not None):
            self.hijos.append(hijo)
            if self.hijos is not None:
                for h in self.hijos:
                    h.padre = self
                
    def get_hijos(self):
        return self.hijos
    
    def set_padre(self, padre):
        self.padre = padre
        
    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos
    
    def get_datos(self):
        return self.datos
    
    def set_costo(self, costo):
        self.costo = costo
        
    def get_costo(self):
        return self.costo
    
    def equal(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False
    
    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado
    
    def __str__(self):
        return str(self.get_datos())

# %%
def bpa(estadoInicio, estadoSolucion):
    resuelto = False

    nodosVisitados = []
    nodosFrontera = []
    
    nodoRaiz = Nodo(estadoInicio)
    nodosFrontera.append(nodoRaiz)

    while not resuelto and len(nodosFrontera) > 0:
        
        nodoActual = nodosFrontera.pop(0)
        nodosVisitados.append(nodoActual)

        if nodoActual.get_datos() == estadoSolucion:
            resuelto = True
            return nodoActual
        else:

            for i in range(0, len(nodoActual.get_datos()) - 1 ):
                datoHijo = nodoActual.get_datos().copy()
                
                valorActual = datoHijo[i]
                datoHijo[i] = datoHijo[i+1]
                datoHijo[i+1] = valorActual

                nodoHijo = Nodo(datoHijo)
                
                if not nodoHijo.en_lista(nodosVisitados) and not nodoHijo.en_lista(nodosFrontera):
                    nodosFrontera.append(nodoHijo)
                    nodoActual.set_hijo(nodoHijo)

def caminoSolucion(nodoSolucion, camino=[]):
    if not nodoSolucion.get_padre():
        camino.append(nodoSolucion.get_datos())
        camino.reverse()
        return camino
    
    camino.append(nodoSolucion.get_datos())    
    return caminoSolucion(nodoSolucion.get_padre(), camino)


    

# %%
estadoInicio = [3,1,2,5,7,6,4,8,9,10]
estadoSolucion = [1,2,3,4,5,6,7,8,9,10]

nodoSolucion = bpa(estadoInicio, estadoSolucion)

print(estadoInicio)
print("camino solucion")

listaCamino = caminoSolucion(nodoSolucion)

for val in listaCamino:
    print(val)


# %%
#hacer correr el mismo programa, pero utilizando una lista LIFO para la lista frontera.
#en este caso solo nesesitamos cambiar la forma de extraer valores de la lista nodoFrontera
# el cual antes se escogia el primero siendo este la pocicion 0,
# para el ejercicio lo cambiaresmos por nodoFrontera.pop(-1) siendo-1 el ultimo valor de la lista 

# Algo que pudimos notar es que el proceso de busqueda tarda mas que en el metodo Fifo y haciendo un analisis 
# esto tiene sentido ya que esta vez comienza a recorrer el nodo hacia abajo y ya no en anchura este proceso hace que el proceso se alargue un poco
# al momento de ejecutar el programa.

def bpaLIFO(estadoInicio, estadoSolucion):
    resuelto = False

    nodosVisitados = []
    nodosFrontera = []
    
    nodoRaiz = Nodo(estadoInicio)
    nodosFrontera.append(nodoRaiz)

    while not resuelto and len(nodosFrontera) > 0:
        
        # Fifo
        # nodoActual = nodosFrontera.pop(0)
        
        
        # Lifo
        nodoActual = nodosFrontera.pop(-1) # linea modificada
        
        
        
        nodosVisitados.append(nodoActual)

        if nodoActual.get_datos() == estadoSolucion:
            resuelto = True
            return nodoActual
        else:

            for i in range(0, len(nodoActual.get_datos()) - 1 ):
                datoHijo = nodoActual.get_datos().copy()
                
                valorActual = datoHijo[i]
                datoHijo[i] = datoHijo[i+1]
                datoHijo[i+1] = valorActual

                nodoHijo = Nodo(datoHijo)
                
                if not nodoHijo.en_lista(nodosVisitados) and not nodoHijo.en_lista(nodosFrontera):
                    nodosFrontera.append(nodoHijo)
                    nodoActual.set_hijo(nodoHijo)

def caminoSolucion(nodoSolucion, camino=[]):
    if not nodoSolucion.get_padre():
        camino.append(nodoSolucion.get_datos())
        camino.reverse()
        return camino
    
    camino.append(nodoSolucion.get_datos())    
    return caminoSolucion(nodoSolucion.get_padre(), camino)


# %%
estadoInicio = [3,1,2,5,4]
estadoSolucion = [1,2,3,4,5]

nodoSolucion = bpaLIFO(estadoInicio, estadoSolucion)

print(estadoInicio)
print("camino solucion")

listaCamino = caminoSolucion(nodoSolucion)

for val in listaCamino:
    print(val)


