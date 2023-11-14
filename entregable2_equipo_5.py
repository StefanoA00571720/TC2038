"""
    Primera parte. Plotear los puntos de los electrodos de 8 y 32 -----------------------------------------------------
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



#2 parte. Plotear los puntos de los electrodos de 32 ----------------------------------------------------------------
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

"""
ETAPA 2: - Análisis de caminos en los grafos de conectividad -------------------------------------------------
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
            print("ALERTA no se puede tener autociclos en una grafica no-dirigida")

        elif (v2,e) in self._adjacency_list[v1]:
            #La arista ya existe
            print("ALERTA: la arista de ",v1," a ",v2," con peso :",e," ya existe")

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
            print("ALERTA vertice 123",v," no existe")
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
        print("ALERTA;--- vertex ",v0," no existe")

    if vg not in graph.vertices():
        print("ALERTA -  vertice ",vg," no existe")

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
            adjacent_vertices = graph.adjacent_vertices(node.v)
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
            adjacent_vertices = graph.adjacent_vertices(node.v)
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
            adjacent_vertices = graph.adjacent_vertices(node.v)
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

#Funcion para llenar la grafica
def graficas(matrizTexto, coordenadasTexto,grafica=WeightedGraph):
    matriz = np.loadtxt(matrizTexto, dtype=int)
    coordenadas = np.loadtxt(coordenadasTexto,  dtype=str)

    for i in range(len(coordenadas)):
        grafica.add_vertex(coordenadas[i][0])
    
    for i in range(len(coordenadas)):
        for x in range(len(matriz[i])):
            if (matriz[i][x] == 1 and grafica.is_adjacent(coordenadas[i][0],coordenadas[x][0])== False):
                
                costo = distancia(float(coordenadas[i][1]),float(coordenadas[i][2]),float(coordenadas[i][3]),float(coordenadas[x][1]),float(coordenadas[x][2]),float(coordenadas[x][3]))
                grafica.add_edge(coordenadas[i][0], coordenadas[x][0], costo)
        
    #grafica.print_graph()

#Funcion para llamar a hacer los caminos, BFD, DFS, Uniform cost
def prepCaminos(arregloO_D, grafica = WeightedGraph):
    print("-----BFS-----")

    for x in range(len(arregloO_D)):
        print("Viaje de ",arregloO_D[x][0]," -> ",arregloO_D[x][1])
        res = bfs(grafica, arregloO_D[x][0], arregloO_D[x][1])
        print(res)

    print("-----DFS-----")

    for x in range(len(arregloO_D)):
        print("Viaje de ",arregloO_D[x][0]," -> ",arregloO_D[x][1])
        res = dfs(grafica, arregloO_D[x][0], arregloO_D[x][1])
        print(res)

    print("-----Uniform Cost-----")

    for x in range(len(arregloO_D)):
        print("Viaje de ",arregloO_D[x][0]," -> ",arregloO_D[x][1])
        res = uniform_cost(grafica, arregloO_D[x][0], arregloO_D[x][1])
        print(res)


#Crear la graficas
gr = WeightedGraph(directed = False)

#Enviar a la funcion de graficas, el nombre de la matriz que vas a usar, el mapa de electrodos, y la grafica
#Individuales
#graficas('Lectura_Stef.txt','mapa8electrodos.txt',gr)
#graficas('Lectura_Stef.txt','mapa8electrodos.txt',gr)
#graficas('Lectura_Stef.txt','mapa8electrodos.txt',gr)

graficas('LecturaS0A.txt', 'mapa32electrodos.txt', gr)
#graficas('MemoriasSOA.txt', 'mapa32electrodos.txt', gr)
#graficas('OperacionesSOA.txt', 'mapa32electrodos.txt', gr)


#Arreglo origen destino, tuplas de donde parte a donde va el camino a explorar
#Arreglo para los viajes de 8 electrodos
arregloOD8 = [('Fz','PO8'),('C3','Oz'),('PO7','C4'),('Oz','PO7'),('Cz','Pz')]
arregloOD32 = [('F7','PO4'),('CP5','O2'),('P4','T7'),('AF3','CP6'),('F8','CP2'),('CP1','FC2'),('F3','O1')]

#Para ver los caminos se usa la funcion de prepCaminos, 
#se envia el arregloOD correspondiente y la grafica

#prepCaminos(arregloOD8,gr)
#prepCaminos(arregloOD32,gr)

#--------------------------------FLOYD-----------------------------------

class WeightedGraphFloyd:
    """ 
        Class that is used to represent a weighted graph. Internally, the class uses an adjacency matrix to 
        store the vertices and edges of the graph. This adjacency matrix is defined by a list of lists, whose 
        elements indicate the weights of the edges. A weight of 0 indicates that there is no connection
        between nodes.
        
        The graph can be directed or indirected. In the class constructor, this property is set. The
        behaviour of some operations depends on this property.
        
        This graph class assumes that it is not possible to have multiple links between vertices.
    """
    
    _directed = True            # This flag indicates whether the graph is directed or indirected.

    _vertices = []              # The list of vertices.
    
    _adjacency_matrix = []      # The adjacency matrix.
    
    
    def __init__(self, directed:bool = False):
        """ 
            This constructor initializes an empty graph. 
            
            param directed: A flag that indicates whether the graph is directed (True) or undirected (False).
        """
        
        self._directed = directed
        self._vertices = []
        self._adjacency_matrix = []
        
    def clear(self):
        """ 
            This method clears the graph. 
        """        
        self._vertices = []
        self._adjacency_matrix = []
    
    def number_of_vertices(self):
        """ 
            This method returns the number of vertices of the graph.
        """        
        return len(self._vertices)
    
    def vertices(self):
        """ 
            This method returns the list of vertices.
        """
        return self._vertices
    
    def edges(self):
        """ 
            This method returns the list of edges.
        """
        e = []

        n = len(self._vertices)

        if self._directed: 
            for i in range(n):
                for j in range(n):
                    if (self._adjacency_matrix[i][j] > 0):
                        e.append((self._vertices[i], self._vertices[j], self._adjacency_matrix[i][j]))    
        
        else:
            for i in range(n):
                for j in range(i+1, n):
                    if (self._adjacency_matrix[i][j] > 0):
                        e.append((self._vertices[i], self._vertices[j], self._adjacency_matrix[i][j]))

        return e

        
    def add_vertex(self, v):
        """ 
            Add vertex to the graph.   
            
            param v: The new vertex to be added to the graph.   
        """
        
        if v in self._vertices:
            print("Warning: Vertex ", v, " already exists")
        else:
            
            self._vertices.append(v)
            n = len(self._vertices)
                        
            if n > 1:
                for vertex in self._adjacency_matrix:
                    vertex.append(0)                    
                
            self._adjacency_matrix.append(n*[0])

            
    def remove_vertex(self, v):
        """ 
            Remove vertex from the graph.      
            
            param v: The vertex to be removed from the graph.   
        """
        
        if v not in self._vertices:
            print("Warning: Vertex ", v, " does not exist")
            
        else:
            index = self._vertices.index(v)
            
            self._vertices.pop(index)
            
            for row in self._adjacency_matrix:
                row.pop(index)
            
            self._adjacency_matrix.pop(index)
        

    def add_edge(self, v1, v2, e = 0):
        """ 
            Add edge to the graph. The edge is defined by two vertices v1 and v2, and
            the weigth e of the edge. 
            
            param v1: The start vertex of the new edge.   
            param v2: The end vertex of the new edge.
            param e: The weight of the new edge. 
        """   
        
        if v1 not in self._vertices:
            # The start vertex does not exist.
            print("Warning: Vertex ", v1, " does not exist.")  
            
        elif v2 not in self._vertices:
            # The end vertex does not exist.
            print("Warning: Vertex ", v2, " does not exist.")
            
        elif not self._directed and v1 == v2:
            # The graph is undirected, so it is no allowed to have autocycles.
            print("Warning: An undirected graph cannot have autocycles.")
        
        else:
            index1 = self._vertices.index(v1)
            index2 = self._vertices.index(v2)
            self._adjacency_matrix[index1][index2] = e
            
            if not self._directed:
                self._adjacency_matrix[index2][index1] = e

    def remove_edge(self, v1, v2):
        """ 
            Remove edge from the graph. 
            
            param v1: The start vertex of the edge to be removed.
            param v2: The end vertex of the edge to be removed.
            param e: The weight of the edge to be removed. 
        """     
        
        if v1 not in self._vertices:
            # v1 is not a vertex of the graph
            print("Warning: Vertex ", v1, " does not exist.")   
            
        elif v2 not in self._vertices:
            # v2 is not a vertex of the graph
            print("Warning: Vertex ", v2, " does not exist.")
            
        else:
            index1 = self._vertices.index(v1)
            index2 = self._vertices.index(v2)
            self._adjacency_matrix[index1][index2] = 0
            
            if not self._directed:
                self._adjacency_matrix[index2][index1] = 0

    def adjacent_vertices(self, v):
        """ 
            Adjacent vertices of a vertex.
            
            param v: The vertex whose adjacent vertices are to be returned.
            return: The list of adjacent vertices of v.
        """      
                
        if v not in self._vertices:
            # The vertex is not in the graph.
            print("Warning: Vertex ", v, " does not exist.")
            return []        
        
        else:
            adjacent_list = []
            
            n = len(self._vertices)
            i = self._vertices.index(v)
                       
            for j in range(n):
                if self._adjacency_matrix[i][j] != 0:
                    adjacent_list.append((self._vertices[j], self._adjacency_matrix[i][j]))

            return adjacent_list 
            
    def is_adjacent(self, v1, v2) -> bool:
        """ 
            This method indicates whether vertex v2 is adjacent to vertex v1.
            
            param v1: The start vertex of the relation to test.
            param v2: The end vertex of the relation to test.
            return: True if v2 is adjacent to v1, False otherwise.
        """
        
        if v1 not in self._vertices:
            # v1 is not a vertex of the graph
            print("Warning: Vertex ", v1, " does not exist.") 
            return False
            
        elif v2 not in self._vertices:
            # v2 is not a vertex of the graph
            print("Warning: Vertex ", v2, " does not exist.")
            return False
        
        else:
                      
            i = self._vertices.index(v1)
            j = self._vertices.index(v2)
                       
            return self._adjacency_matrix[i][j] != 0

    def print_graph(self):
        """ 
            This method shows the edges of the graph.
        """
        
        n = len(self._vertices)
        for i in range(n):
            for j in range(n):
                if self._adjacency_matrix[i][j] != 0:
                    print(self._vertices[i], " -> ", self._vertices[j], " edge weight: ", self._adjacency_matrix[i][j])


def floyd_marshall(adjacency_matrix):
    """ 
        This method finds the length of the shortest paths between all the vertices
        of a undirected graph.
            
        param adjacency_matrix: The adjacency matrix of the undirected graph.
        return: A matrix with the length of the shortest paths between vertices of 
        the graph.
    """
    
    BIG_NUMBER = 100000000
    n = len(adjacency_matrix)   

    matrix = np.array(adjacency_matrix)    
    matrix[matrix == 0] = BIG_NUMBER 

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] != BIG_NUMBER and matrix[k][j] != BIG_NUMBER and (matrix[i][k]+matrix[k][j]) < matrix[i][j]:
                    matrix[i][j] = matrix[i][k]+matrix[k][j]
                    
    return matrix

def graficas(matrizTexto, coordenadasTexto,grafica=WeightedGraphFloyd):
    matriz = np.loadtxt(matrizTexto, dtype=int)
    coordenadas = np.loadtxt(coordenadasTexto,  dtype=str)

    for i in range(len(coordenadas)):
        grafica.add_vertex(coordenadas[i][0])
    
    for i in range(len(coordenadas)):
        for x in range(len(matriz[i])):
            if (matriz[i][x] == 1 and grafica.is_adjacent(coordenadas[i][0],coordenadas[x][0])== False):
                
                costo = distancia(float(coordenadas[i][1]),float(coordenadas[i][2]),float(coordenadas[i][3]),float(coordenadas[x][1]),float(coordenadas[x][2]),float(coordenadas[x][3]))
                grafica.add_edge(coordenadas[i][0], coordenadas[x][0], costo)
        
    #grafica.print_graph()
#Crear la grafica
grFloyd = WeightedGraphFloyd(directed = False)


#Matriz de conexion, 0 y 1
graficas('Lectura_Stef.txt', 'mapa8electrodos.txt', grFloyd)
#graficas('Memoria_Stef.txt', 'mapa8electrodos.txt', grFloyd)
#graficas('Operaciones_Stef.txt', 'mapa8electrodos.txt', grFloyd)

#graficas('LecturaS0A.txt', 'mapa32electrodos.txt', grFloyd)
#graficas('MemoriaS0A.txt', 'mapa32electrodos.txt', grFloyd)
#graficas('OperacionesS0A.txt', 'mapa32electrodos.txt', grFloyd)

print("Length of shortest paths Matriz")
print(floyd_marshall(grFloyd._adjacency_matrix))
