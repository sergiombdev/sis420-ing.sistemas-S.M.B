# %%
# Carrera: Ingenieria de Sistemas
# Grupo laboratorio: 1
# Materia: sis420
# gihub : https://github.com/sergiombdev/sis420-ing.sistemas-S.M.B.git

# Alumno: Menodoza Benito Sergio




# A partir del codigo fuente del aarchivo bpa (Busqueda promero en anchura), modificar el mismo para encontrar la sulucion, 
# pero utilizando una lista_frontera ordenada de mayo a menor valor que cada nodo pueda tener en su campo costo
# ese valor debe llenarselo de manera aleatoria en el momento de creacion del nodo. Una vez implementado se debe describir que sucede 
# y que capacidad de resolver rompecabezas lineales de 4, 6, 7, 8, 9, 10, .... se puede resolver con el mismo. Alguna menora o criterio que usted
# considere es importante realizar para mejorar la capacidad de resolucion. toda la explicación se debe incluir en el codigo fuente.

# El trabajo es de caracter individual, se debe subir el codigo y compartir el enlace del repositorio.

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
import random

# %%
# funcion para ordenar el nodo frontera por el costo
def comparar(nodo):
    return nodo.get_costo()

# %%
def bpa(estadoInicio, estadoSolucion):
    resuelto = False

    nodosVisitados = []
    nodosFrontera = []
    
    nodoRaiz = Nodo(estadoInicio)

    # se asigna un costo de 0 al nodo raiz
    nodoRaiz.set_costo(0)

    nodosFrontera.append(nodoRaiz)

    while not resuelto and len(nodosFrontera) > 0:
        #ordenamos la lista nodo frontera
        nodosFrontera = sorted(nodosFrontera, key=comparar)

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

                #asignamos un costo aleatorio a los nodos hijos
                nodoHijo.set_costo( nodoActual.get_costo() + random.randint( 1, 10 ) )

                if not nodoHijo.en_lista(nodosVisitados):
                    
                    if( not nodoHijo.en_lista(nodosFrontera)):
                        nodosFrontera.append(nodoHijo)
                    else:
                        for nodoF in nodosFrontera:
                            if nodoF.equal(nodoHijo) and  nodoHijo.get_costo() < nodoF.get_costo():
                                #si el nodo es igual pero el costo es menor se remplaza por el que tiene el costo menor
                                nodosFrontera.remove(nodoF)
                                nodosFrontera.append(nodoHijo)
                    #añadimos el nodo hijo al nodo actual
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


# Al ser el costo aleatorio en algunos casos es capaz de resolverlo en 3s y en otros casos mas de 1min,
# para mejorar el tiempo de resolucion tendriamos que tener costos fijos en cada nodo, pero es claro que los costos 
# mejoran en gran medida el proceso que realiza el algoritmo al no recorrer nodos innecesarios al conciderar el costo como un
# valor para tomar deciciones.



