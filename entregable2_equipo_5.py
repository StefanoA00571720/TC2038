"""
    Primera parte. Plotear los puntos de los electrodos de 8
"""

import numpy as np
import matplotlib.pyplot as plt

""" 

channels = ['Fz', 'C3', 'Cz', 'C4', 'Pz', 'PO7', 'Oz', 'PO8']

points3D = [[0,0.71934,0.694658], [-0.71934,0,0.694658], [0,0,1], [0.71934,0,0.694658], [0,-0.71934,0.694658], [-0.587427,-0.808524,-0.0348995], [0,-0.999391,-0.0348995], [0.587427,-0.808524,-0.0348995]]
points3D = np.array(points3D)

r = np.sqrt(points3D[:,0]**2 + points3D[:,1]**2 + points3D[:,2]**2)
t = r/(r + points3D[:,2])
x = r*points3D[:,0]
y = r*points3D[:,1]
points2D = np.column_stack((x,y))

circle = plt.Circle((0,0),1, color = 'r', alpha = 0.25, fill = False)
plt.scatter(points2D[:,0], points2D[:,1])
plt.gca().add_patch(circle)

for i in range(len(points2D)):
    plt.text(points2D[i,0]-0.02, points2D[i,1]+0.025, channels[i])
    
plt.axis('equal')
plt.show()

"""
    
"""
2 parte. Plotear los puntos de los electrodos de 32
channels = ['Fp1','Fp2', 'AF3', 'AF4', 'F7', 'F3', 'Fz', 'F4', 'F8', 'FC5', 'FC1', 'FC2', 'FC6', 'T7', 'C3', 'Cz', 'C4', 'T8', 'CP5', 'CP1', 'CP2', 'CP6', 'P7', 'P3', 'Pz', 'P4', 'P8', 'PO3', 'PO4', 'O1', 'Oz', 'O2']

points3D = [[-0.308829,0.950477,-0.0348995], [0.308829,0.950477,-0.0348995], [-0.406247,0.871199,0.275637], [0.406247,0.871199,0.275637], [-0.808524,0.587427,-0.0348995], [-0.545007,0.673028,0.5], [0,0.71934,0.694658], [0.545007,0.673028,0.5], [0.808524,0.587427,-0.0348995], [-0.887888,0.340828,0.309017], [-0.37471,0.37471,0.848048], [0.37471,0.37471,0.848048], [0.887888,0.340828,0.309017], [-0.999391,0,-0.0348995], [-0.71934,0,0.694658], [0,0,1], [0.71934,0,0.694658], [0.999391,0,-0.0348995], [-0.887888,-0.340828,0.309017], [-0.37471,-0.37471,0.848048], [0.37471,-0.37471, 0.848048], [0.887888,-0.340828,0.309017], [-0.808524,-0.587427,-0.0348995], [-0.545007,-0.673028,0.5], [0,-0.71934,0.694658], [0.545007,-0.673028,0.5], [0.808524,-0.587427,-0.0348995], [-0.406247,-0.871199,0.275637], [0.406247,-0.871199,0.275637], [-0.308829,-0.950477,-0.0348995], [0,-0.999391,-0.0348995], [0.308829,-0.950477,-0.0348995]]
points3D = np.array(points3D)

r = np.sqrt(points3D[:,0]**2 + points3D[:,1]**2 + points3D[:,2]**2)
t = r/(r + points3D[:,2])
x = r*points3D[:,0]
y = r*points3D[:,1]
points2D = np.column_stack((x,y))

circle = plt.Circle((0,0),1, color = 'r', alpha = 0.25, fill = False)
plt.scatter(points2D[:,0], points2D[:,1])
plt.gca().add_patch(circle)

for i in range(len(points2D)):
    plt.text(points2D[i,0]-0.02, points2D[i,1]+0.025, channels[i])

plt.axis('equal')
plt.show()

"""
from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue

class WeightedGraph:
    #Representacion de la grafica con peso. 
    #Lista de adjacencia para guardar vertices y aristas. La lista es un diccionario cuyas llaves representar los vertices.
    #Para cada vertice dentro del diccionario hay una lista de tuples, que tienen el vertice vecino y su peso
    #La grafica puede ser dirigida o no dirigida

    _directed = True 
    _adjacency_list = {} #Lista de adjacencia

    def __init__(self, directed:bool = False):
        """ 
            This constructor initializes an empty graph. 

            param directed: A flag that indicates whether the graph is directed (True) or undirected (False).
        """

        self._directed = directed
        self._adjacency_list = {}

    def clear(self):
        #Limpia la lista de adyacencia
        self._adjacency_list = {}

    def numer_of_vertices(self):
        #Regresa el numero de vertices de la grafica
        return len(self._adjacency_list)

    def vertices(self):
        #Regresa una lista de vertices
        v = []
        for vi in self._adjacency_list:
            v.append(vi)
        return v

    def edges(self):
        #Regresa lisa de aristas
        e = []
        if self._directed:
            for v in self._adjacency_list:
                for edge in self._adjacency_list[v]:
                    e.append((v, edge[0], edge[1]))
        else:
            for v in self._adjacency_list:
                for edge in self._adjacency_list[v]:
                    if(edge[0], v, edge[1]) not in e:
                        e.append((v, edge[0], edge[1]))
        return e

    def add_vertex(self, v):
        #Añade vertices a la grafica
        #Necesita el nuevo vertice

        if v in self._adjacency_list:
            print("ALERTA : vertice ",v, " ya existe")
        else:
            self._adjacency_list[v] = []


    def remove_vertex(self, v):
        #Elimina un vertice
        if v not in self._adjacency_list:
            print("ALERTA vertice ",v," no existe")
        else:
            #Remover vertice de la lista de adjacencia
            self._adjacency_list.remove(v)

            #Remover aristar donde el vertice es destino
            for vertex in self._adjacency_list:
                for edge in self._adjacency_list[vertex]:
                    if edge[0] == v:
                        self._adjacency_list[vertex].remove(edge)

    def add_edge(self, v1, v2, e = 0):
        #Añade una arista, vertice origen, vectice destino, peso del camino si no se incluye el valor el peso es 0

        if v1 not in self._adjacency_list:
            #El vertice de inicio no exite
            print("ALERTA vertice ",v1," de origen no existe")

        elif v2 not in self._adjacency_list:
            #El vertice de destino no existe
            print("ALERTE vertice ",v2," de destino no existe")

        elif not self._directed and v1 == v2:
            #La grafica no es dirigida y hay un autociclo
            x = 0
            print("ALERTA no se puede tener autociclos en una grafica no-dirigida")

        elif (v2,e) in self._adjacency_list[v1]:
            #La arista ya existe
            x = 0
            #print("ALERTA: la arista de ",v1," a ",v2," con peso :",e," ya existe")

        else:
            self._adjacency_list[v1].append((v2,e))
            if not self._directed:
                self._adjacency_list[v2].append((v1,e))

    def remove_edge(self, v1, v2, e):
        #Quitar una arista, vertice de origen, vertice destino, costo del camino
        if v1 not in self._adjacency_list:
            print("ALERTA vertice ",v1," no existe")

        elif v2 not in self._adjacency_list:
            print("ALERTA vertice ",v2," no existe" )

        else:
            for edge in self._adjacency_list[v1]:
                if edge == (v2,e):
                    self._adjacency_list[v1].remove(edge)

            if not self._directed:
                for edge in self._adjacency_list[v2]:
                    if edge == (v1,e):
                        self._adjacency_list[v2].remove(edge)

    def adjacent_vertices(self,v):
        #Lista de adyacencia del vertice

        if v not in self._adjacency_list:
            #El vertice no existe
            print("ALERTA vertice ",v," no existe")
            return []
        else:
            return self._adjacency_list[v]


    def is_adjacent(self, v1, v2) -> bool:
        #Comprueba si v2 es vecino de v1
        #Regresa true si son vecinos y false si no hay camino directo

        if v1 not in self._adjacency_list:
            #No existe v1
            print("ALERTA vertice ",v1," no existe")
            return False
        elif v2 not in self._adjacency_list:
            #No existe v2
            print("ALERTA vertice",v2," no exsite")
            return False

        else:
            for edge in self._adjacency_list[v1]:
                if edge[0] == v2:
                    return True
            return False

    def print_graph(self):
        #Muestra las aristas de la grafica

        for vertex in self._adjacency_list:
            for edges in self._adjacency_list[vertex]:
                print(vertex," -> ",edges[0], " peso ",edges[1])

class TreeNode:
    def __init__(self, parent, v, c):
        """ 
            This constructor initializes a node. 

            param parent: The node parent.
            param v: The graph vertex that is represented by the node.
            param c: The path cost to the node from the root.
        """
        self.parent = parent
        self.v = v
        self.c = c

    def __lt__(self, node):
        """ 
            Operator <. This definition is requiered by the PriorityQueue class.
        """
        return False; 

    def path(self):
        #Crea la lista de vertices de la raiz al nodo
        node = self
        path = []
        while node != None:
            path.insert(0,node.v) #--------------que es el 0 ?
            node = node.parent 
        return path

def bfs(graph:WeightedGraph, v0,  vg):
    #Recorrido en anchura (Breadth-first), de v0 a vg
    #Regresa una tupla con el camino de vi a vg y el costo, en caso de no existir regresa null

    #Checar si los vrtices no existen
    if v0 not in graph.vertices():
        print("ALERTA; vertex ",v0," no existe")

    if vg not in graph.vertices():
        print("ALERTA vertice ",vg," no existe")

    #Inicializar frontera
    frontier = Queue()
    frontier.put(TreeNode(None, v0,0))

    #Inicialilzar set de exploracion
    explored_set = {}

    while True:
        if frontier.empty():
            return None

        node = frontier.get()

        #Checar si el nodo es el destino
        if node.v == vg:
            return{"Path ":node.path(), "Cost":node.c}

        #Expandir nodo
        if node.v not in explored_set:
            adjacent_vertices = gr.adjacent_vertices(node.v)
            for vertex in adjacent_vertices:
                frontier.put(TreeNode(node, vertex[0], vertex[1]+ node.c))

        explored_set[node.v] = 0

def dfs(graph:WeightedGraph, v0, vg):
    #Busqueda de profundidad, del v0 a vg
    #Regresa una tupla con el camino de vi a vg

    #checar si existen los nodos
    if v0 not in graph.vertices():
        print("ALERTA vertice", v0," no existe")

    if vg not in graph.vertices():
        print("ALERTA vertice ",vg," no existe")

    #Inicializar frontera
    frontier = LifoQueue()
    frontier.put(TreeNode(None,v0,0))

    explored_set = {}

    while True:
        if frontier.empty():
            return None

        node = frontier.get()

        #Checar node
        if node.v == vg:
            return {"Path": node.path(), "Cost":node.c}

        if node.v not in explored_set:
            adjacent_vertices = gr.adjacent_vertices(node.v)
            for vertex in adjacent_vertices:
                frontier.put(TreeNode(node, vertex[0], vertex[1]+node.c))

        explored_set[node.v] = 0

def uniform_cost(graph:WeightedGraph, v0,vg):
    #Costo uniforme de v0 a vg
    #Regresa  una tupla del camino entre v0 a vg con su costo

    #Checar si existen
    if v0 not in graph.vertices():
        print("ALERTA vertice", v0," no existe")

    if vg not in graph.vertices():
        print("ALETA vertice ",vg," no existe")

    #Inicializar frontera
    frontier = PriorityQueue()
    frontier.put((0, TreeNode(None, v0, 0)))

    explored_set = {}

    while True:
        if frontier.empty():
            return None

        node = frontier.get()[1]

        #Checar si el node es el que se busca
        if node.v == vg:
            #Regresa el camino y costo como diccionario
            return {"Path":node.path(),"Cost":node.c}

        #Expandir nodo
        if node.v not in explored_set:
            adjacent_vertices = gr.adjacent_vertices(node.v)
            for vertex in adjacent_vertices:
                cost = vertex[1]+ node.c
                frontier.put((cost, TreeNode(node, vertex[0], vertex[1]+node.c)))


        explored_set[node.v] = 0

#Funcion para medir la distancia 3d entre 2 puntos para obtener el peso
def distancia(xA, yA, zA, xB, yB, zB):
    punto1 = np.array([xA, yA, zA])
    punto2 = np.array([xB, yB, zB])
    distancia = np.linalg.norm(punto2 - punto1)
    return distancia

#Crear la grafica
gr = WeightedGraph(directed = False)

#Datos = lectura de matriz de un txt
datos = np.loadtxt('Lectura_Stef.txt', dtype=int)
#datos = np.loadtxt('Memoria_Stef.txt', dtype=int)
#datos = np.loadtxt('Operaciones_Stef.txt', dtype=int)

#DatosE8 = mapa con los nombres y coordenadas de los electrodos
datosE8 = np.loadtxt('mapa8electrodos.txt',  dtype=str)

#Añadir los vertices
for i in range(len(datosE8)):
    gr.add_vertex(datosE8[i][0])

#Añador las aristas entre los vertices
for i in range(len(datosE8)):
    for x in range(len(datos[i])):
        if (datos[i][x] == 1 and gr.is_adjacent(datosE8[i][0],datosE8[x][0])== False):
            
            costo = distancia(float(datosE8[i][1]),float(datosE8[i][2]),float(datosE8[i][3]),float(datosE8[x][1]),float(datosE8[x][1]),float(datosE8[x][1]))
            gr.add_edge(datosE8[i][0], datosE8[x][0], costo)


#gr.print_graph()

#BFS
print("-----BFS-----")
print("Viaje de Fz a PO8")
res = bfs(gr, 'Fz', 'PO8')
print(res)

print("Viaje de C3 a Oz")
res = bfs(gr, 'C3', 'Oz')
print(res)

print("Viaje de PO7 a C4")
res = bfs(gr, 'PO7', 'C4')
print(res)

print("Viaje de Oz a PO7")
res = bfs(gr, 'Oz', 'PO7')
print(res)

print("Viaje de Cz a Pz")
res = bfs(gr, 'Cz', 'Pz')
print(res)

#DFS
print("-----DFS-----")
print("Viaje de Fz a PO8")
res = dfs(gr, 'Fz', 'PO8')
print(res)

print("Viaje de C3 a Oz")
res = dfs(gr, 'C3', 'Oz')
print(res)

print("Viaje de PO7 a C4")
res = dfs(gr, 'PO7', 'C4')
print(res)

print("Viaje de Oz a PO7")
res = dfs(gr, 'Oz', 'PO7')
print(res)

print("Viaje de Cz a Pz")
res = dfs(gr, 'Cz', 'Pz')
print(res)

print("-----Uniforn cost-----")
print("Viaje de Fz a PO8")
res = uniform_cost(gr, 'Fz', 'PO8')
print(res)

print("Viaje de C3 a Oz")
res = uniform_cost(gr, 'C3', 'Oz')
print(res)

print("Viaje de PO7 a C4")
res = uniform_cost(gr, 'PO7', 'C4')
print(res)

print("Viaje de Oz a PO7")
res = uniform_cost(gr, 'Oz', 'PO7')
print(res)

print("Viaje de Cz a Pz")
res = uniform_cost(gr, 'Cz', 'Pz')
print(res)