#Stefano Herrejon A00571720

from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue

#import numpy as np

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
    
def prim(v0, graph=WeightedGraph, newGraph = WeightedGraph):
    
    cost = 0
    selected = [v0]
    newGraph.add_vertex(v0)
    remain = []
    vnext = None
    padre = None

    

    for i in graph.vertices():
        if i != v0 and len(graph.adjacent_vertices(i)) > 0:
            remain.append(i)
        
    while len(remain) > 0:
        minCost = float('inf')
        padre = None
        vnext = None

        for vector in selected:
            vecinos = graph._adjacency_list[vector]
            
            for vecino in vecinos:
                cn = vecino[1]

                if(cn < minCost and vecino[0] not in selected):
                    padre = vector
                    minCost = cn
                    vnext = vecino[0]
        
        if (vnext == None):
            print("No hay solucion")
            return None
        
        
        newGraph.add_vertex(vnext)
        newGraph.add_edge(padre,vnext,minCost)

        selected.append(vnext)
        remain.remove(vnext)

        cost = cost + minCost



    print(selected, cost)
    graph.print_graph()
    newGraph.print_graph()
    return(selected, cost)
    



gr = WeightedGraph(directed = False)

grNew = WeightedGraph(directed = False)

gr.add_vertex('Ylane')
gr.add_vertex('Goding')
gr.add_vertex('Ontdale')
gr.add_vertex('Togend')
gr.add_vertex('Strento')
gr.add_vertex('Oriaron')
gr.add_vertex('Blebus')
gr.add_vertex('Zrusall')
gr.add_vertex('Adaset')
gr.add_vertex('Ertonwell')
gr.add_vertex('Duron')
gr.add_vertex('Lagos')
gr.add_vertex('Goxmont')
gr.add_vertex('Niaphia')

gr.add_edge('Ylane', 'Goding',88)
gr.add_edge('Ylane', 'Strento',99)
gr.add_edge('Ylane', 'Oriaron',117)

gr.add_edge('Goding', 'Ontdale',98)

gr.add_edge('Ontdale', 'Togend',210)
gr.add_edge('Ontdale', 'Oriaron',219)
gr.add_edge('Ontdale', 'Blebus',165)

gr.add_edge('Togend', 'Blebus',121)

gr.add_edge('Strento', 'Oriaron',221)
gr.add_edge('Strento', 'Zrusall',112)

gr.add_edge('Oriaron', 'Blebus',291)

gr.add_edge('Blebus', 'Duron',160)

gr.add_edge('Zrusall', 'Adaset', 15)
gr.add_edge('Zrusall', 'Goxmont',112)

gr.add_edge('Adaset', 'Ertonwell',130)
gr.add_edge('Adaset', 'Goxmont',103)

gr.add_edge('Ertonwell', 'Duron',121)
gr.add_edge('Ertonwell', 'Niaphia',56)

gr.add_edge('Duron', 'Lagos',119)

gr.add_edge('Lagos', 'Niaphia',300)

gr.add_edge('Goxmont', 'Niaphia',212)


prim('Oriaron',gr,grNew)
