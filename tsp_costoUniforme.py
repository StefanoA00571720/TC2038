
from queue import PriorityQueue
import copy 

#Clase WeightedGraph para representar la grafica

class WeightedGraph:
    """
    Clase que representa la weighted graph.
    Se usa una lista de adjacencia para los vertices y sus respectivos caminos/aristas.
    Por cada vertice hay una dupla que contine su vecino y su costo

    """
    _directed = True #Indica si es dirigida o no dirigida

    _adjacency_list = {} #Lista de adjacencia de la grafica

    def __init__(self, directed:bool = False):
        """
        Inicialisa la grafica vacia.
        directed: bandera que indica si la grafica es dirigida. True = Dirigida
        """
        self._adjacency_list = {}
        self._directed = directed
    
    def clear(self):
        """
        EL metodo reinicia la lista de adjacencia
        """
        self._adjacency_list = {}
    
    def number_of_vertices(self):
        """
        Regresa el numero de vertices de la grafica
        """
        return len(self._adjacency_list)
    
    def vertices(self):
        """
        Regresa todos los vertices que se encuentran en la lista/grafica
        """
        v = []
        for vertice in self._adjacency_list:
            v.append(vertice)
        return v
    
    def edges(self):
        """
        Regresa las aristas
        """
        e = []

        if self._directed: #Si es una grafica dirigida
            for vertice in self._adjacency_list:
                for arista in self._adjacency_list[vertice]:
                    e.append((vertice, arista[0], arista[1])) # 0 : destino, 1: costo
        
        else: 
            for vertice in self._adjacency_list:
                for arista in self._adjacency_list[vertice]:
                    if (arista[0], vertice, arista[1]) not in e: #Checar que no este esa arista en la lista del lado contrario B->A
                        e.append((vertice, arista[0], arista[1]))  # origen, 0 : destino, 1 : costo

        return e

    def add_vertex(self, v):
        """
        Añadir un vertice
        v : vertice a añadir
        """

        if v in self._adjacency_list:
            print("El vertice ",v," ya existe")
        
        else:
            self._adjacency_list[v] = [] #Crear su registro e iniciar su lista de vecinos/aristas


    def remove_vertex(self, v):
        """
        Quitar un vertice de la grafica, sus aristas
        v : vertice a remover
        """ 

        if v not in self._adjacency_list:
            print("Vertice ",v," no existe")
        else:
            #Remover el vertice de la lista de vertices
            self._adjacency_list.remove(v)

            #Remover sus aristas de origen/destino

            for vertice in self._adjacency_list:
                for arista in self._adjacency_list[vertice]:
                    if arista[0] == v: #Si el vertice que queremos eliminar es el destino se elimina
                        self._adjacency_list[vertice].remove(arista)
    
    def add_edge(self, v1, v2, e = 0):
        """
        Añadir arista a la grafica
        v1 : origen
        v2 : destino
        e : costo
        """

        if v1 not in self._adjacency_list:
            print("No existe el vertice de origen ",v1)

        elif v2 not in self._adjacency_list:
            print("No existe el vertice de destino ",v2)
        
        elif not self._directed and v1 == v2:
            print("No debe de haber autociclos en una grafica no-dirigida")
        
        elif (v2,e) in self._adjacency_list[v1]:
            print("Ya existe el camino de : ",v1," a ",v2," con costo ",e)
        
        else:
            self._adjacency_list[v1].append((v2,e))
            if not self._directed: 
                #Si no es una grafica dirigida se crea el mismo camino de regreso
                self._adjacency_list[v2].append((v1,e))

    def remove_edge(self, v1, v2, e):
        """
        Remover arista
        v1 : origen
        v2 : destino
        e = costo
        """

        if v1 not in self._adjacency_list:
            print("No existe el vertice de origen ",v1)
        
        elif v2 not in self._adjacency_list:
            print("No existe el vertice de destino ",v2)
        
        else:
            for arista in self._adjacency_list[v1]:
                if arista == (v2, e):
                    self._adjacency_list[v1].remove(arista)
            
            if not self._directed:
                for arista in self._adjacency_list[v2]:
                    if arista == (v1, e):
                        self._adjacency_list[v2].remove(arista)
    
    def adjacent_vertices(self, v):
        """
        Devuelve una lista de vertices vecinos de v
        """

        if v not in self._adjacency_list:
            print("NO existe el vertice ",v)

        else:
            return self._adjacency_list[v]
    
    def is_adjacent(self, v1, v2 )-> bool:
        """
        Devuelve si v1 y v2 estan unidos por una arista
        """

        if v1 not in self._adjacency_list:
            print("Vertice de origen ",v1," no existe")
            return False

        elif v2 not in self._adjacency_list:
            print("Vertice de destino ",v2," no existe")
            return False

        else:
            for arista in self._adjacency_list[v1]:
                if arista[0] == v2:
                    return True
            return False
        
    def print(self):
        """
        Imprime la grafica con sus vertices y sus respectivos caminos/aristas
        """

        for vertice in self._adjacency_list:
            for arista in self._adjacency_list[vertice]:
                print(vertice," -> ", arista[0]," costo:", arista[1])

#Clase nodo para TSP con uniform cost
class TspUcsNode:
    """
    Clase usada para representar un nodo en el caso de busqueda uniforme para el TSP
    Cada nodo tiene :
        *referencia a su padre
        *el vertice al cual representa de la grafica
        *el costo de la raiz hasta si mismo
        *la lista de nodos explorados
    """

    def __init__(self, parent, v, c, explored):
        """
            se inicializa el nodo
            parent : el padre
            v : el grafo que representa de la tabla
            c : el costo de la raiz hasta si mismo
            explored : el camino de vertices de la raiz a si mismo
        """
        self.parent = parent
        self.v = v
        self.c = c
        self.explored = explored

    def __lt__(self, node):
        """ 
            Operator <. This definition is requiered by the PriorityQueue class.
        """
        return False;

#Funcion para encontrar si hay camino
def tsp_ucs(graph:WeightedGraph, v0):
    """
    Se busca/encuentra el camino de costo minimo partiendo del v0, 
    pasando un total de 1 vez por cada nodo y rgresando a v0

    Regresa una tupla del camino o null si no hay camino posible
    Logica : se hace una cola de prioridad con el v0 como el primer nodo a explorar.
    while True:
        Mientras que la frontera no este vacia (No hay respuesta) o 
        no se llegue al nodo de inicio sin antes pasar por todos los vertices (respuesta)
        se agarran una lista de los vecinos del nodo a explorar, ver si ya han sido visitados, 
        en caso que no se agregan a la lista de prioridad con el costo como el costo del nodo
        + el camino al vecino, se agregan a visitados, y con eso se crea el nuevo nodo de la 
        priority queue
    """
    vertices = graph.vertices()
    n = len(vertices)

    if v0 not in vertices:
        print("Vertice de origen ",v0," no existe")

    frontier = PriorityQueue()
    #Parametros, priodidad, nodo(sin padre, vector que representa, costo, lista de nodos visitados)
    frontier.put((0, TspUcsNode(None, v0, 0, [(v0,0)])))

    while True:
        #si la frontera se vacia significa que no se encontro un camino
        if frontier.empty():
            print("No hay un camino posible")
            return None

        #Agarrar un nodo de la frontera, 0 = prioridad, 1 = nodo
        node = frontier.get()[1]

        if len(node.explored) == (n+1) and node.v == v0: 
            #Si se han explorado todos los nodos y se llego de vuelta
            return {"Path": node.explored, "Cost":node.c}
        
        #Expandir nodos
        adjacent_vertices = gr.adjacent_vertices(node.v)
        for vertice in adjacent_vertices:
            already_included = False

            #Checar si un vecino es el vertice del pricipio
            #El vertice inicial solo puede ser añadido al final del ciclo

            if vertice[0] == v0 and len(node.explored) < n:
                #Si el vertice 0 (destino) es el del principio y explorados le falta nodos
                #Se pretende que ya se visito
                already_included = True
            
            #Checar si el vertice ya esta dentro del ciclo/camino recorrido
            for i in range(1, len(node.explored)):
                if vertice[0] == node.explored[i][0]:
                    already_included = True
                    break
            
            if not already_included:
                #si no esta en el ciclo se agrega, el costo es el del nodo + el nuevo camino
                cost = vertice[1] + node.c
                #Se agega a la frontera con la prioridad del costo
                #se crea un tspnode con el padre sienod el nodo, el vertice, el costo total, la lista de explorados + el vertice actual
                frontier.put((cost, TspUcsNode(node, vertice[0], cost, node.explored + [vertice])))

#Clase nodo para TSP con ramificación y poda

class TspBBNode:
    """ 
        Clase para representar un nodo por medio de ramificación y poda
        *Referencia a su padre
        *Vertice al cual representa
        *Costo total de la raiz al nodo
        *lista de nodos explorados
        *matrix de reduccion
    """   
    
    def __init__(self, parent, v, c, cpos, explored, m):
        """ 
           Constructor
            
            parent: padre
            v: nodo al cual representa
            c: costo total
            cpos: la heuristica, el posible costo
            explored: el camino de la raiz al nodo actual
           m: la matriz de reduccion
        """
        self.parent = parent
        self.v = v
        self.c = c
        self.cpos = cpos
        self.explored = explored
        self.m = m
        
    def __lt__(self, node):
        """ 
            Operator <. This definition is requiered by the PriorityQueue class.
        """
        return False;


#--------------------------------------------------
        
def tsp_bb(graph:WeightedGraph, v0):
    """ 
        This method finds the Hamiltonian cycle of minimum cost of a directed graph starting from 
        the given vertex.The estimated cost of each node of the tree is calcualted using the 
        reduction matrix technique.
            
        param graph: The graph to traverse.
        param v0: The initial vertex.
        return: A tuple with the Hamiltonian of minimum cost, or null if there is no a path.
    """

    vertices = graph.vertices()
    n = len(vertices)

    # Check graph and initial vertex
    if v0 not in vertices:
        print("Warning: Vertex", v0, "is not in Graph")        
       
    ################ Reduction matrix ################
    vindices = {}
    for i, v in enumerate(vertices, 0):
        vindices[v] = i

    # Adyacency matrix    
    inf_val = 100000000
    m = [[inf_val]*n for i in range(n)]

    for edge in gr.edges():
        i = vindices[edge[0]]
        j = vindices[edge[1]]
        c = edge[2]
        m[i][j] = c
        m[j][i] = c
    
    # Reduce rows
    rrows = [0]*n
    for i in range(n):    
        rrows[i] = min(m[i])
        if rrows[i] == inf_val:
            rrows[i] = 0        
    
        for j in range(n): 
            if m[i][j] != inf_val:
                m[i][j] -= rrows[i]
    
    # Reduce columns
    rcols = [0]*n
    for j in range(n):  
        col = [m[i][j] for i in range(n)]    
        rcols[j] = min(col)
        if rcols[j] == inf_val:
            rcols[j] = 0
        
        for i in range(n): 
            if m[i][j] != inf_val:
                m[i][j] -= rcols[j]
    
    # Reduction cost
    reduced_cost = sum(rrows) + sum(rcols)    
    
    #################################################

    # Initialize frontier     
    frontier = PriorityQueue()
    frontier.put((0, TspBBNode(None, v0, 0, reduced_cost, [(v0, 0)], m)))   
    
    # Initialize best solution
    best = None
    best_val = inf_val
    
    # Find cycle
    while not frontier.empty():
        
        # Get node from frontier
        node = frontier.get()[1]
        
        # Update best solution
        if len(node.explored) == (n+1) and node.v == v0:            
            if node.c < best_val:
                best = node
                best_val = node.c                
            continue
        
        # Check if the possible value is better than the current best value
        if node.cpos <= best_val:
            
            # Expand node        
            adjacent_vertices = gr.adjacent_vertices(node.v)
            for vertex in adjacent_vertices:
                already_included = False
                
                # Check if the adjacent vertex is the initial vertex. The initial
                # vertex can be included only at the end of the cycle.
                if vertex[0] == v0 and len(node.explored) < n:
                    already_included = True

                # Check if the vertex has been already included in the cycle.
                for i in range(1, len(node.explored)):
                    if vertex[0] == node.explored[i][0]:
                        already_included = True
                        break

                # Add the vertex if it is not already included in the cycle.
                if not already_included:
                    cost = vertex[1] + node.c
                    new_explored = node.explored + [vertex]
                
                    ################ Reduction matrix ################
                    m = copy.deepcopy(node.m)

                    row = vindices[node.v]
                    col = vindices[vertex[0]]

                    # Fill with inf_val rows and columns of vertices in the path
                    for k in range(n): 
                        m[row][k] = inf_val
                    
                    for k in range(n): 
                        m[k][col] = inf_val
                
                    for i in range(len(new_explored)):
                        for j in range(i+1, len(new_explored)):
                            v1 = vindices[new_explored[i][0]]
                            v2 = vindices[new_explored[j][0]]
                            m[v1][v2] = inf_val
                            m[v2][v1] = inf_val

                    # Reduce rows
                    rrows = [0]*n
                    for i in range(n):    
                        rrows[i] = min(m[i])
                        if rrows[i] == inf_val:
                            rrows[i] = 0        
    
                        for j in range(n): 
                            if m[i][j] != inf_val:
                                m[i][j] -= rrows[i]
    
                    # Reduce columns
                    rcols = [0]*n
                    for j in range(n):  
                        col = [m[i][j] for i in range(n)]    
                        rcols[j] = min(col)
                        if rcols[j] == inf_val:
                            rcols[j] = 0
        
                        for i in range(n): 
                            if m[i][j] != inf_val:
                                m[i][j] -= rcols[j]
    
                    reduced_cost = sum(rrows) + sum(rcols)

                    cpos = vertex[1] + node.cpos + reduced_cost
                
                    #################################################
                
                    frontier.put((cpos, TspBBNode(node, vertex[0], cost, cpos, new_explored, m)))       
                
    return {"Path": best.explored, "Cost": best.c}
 
 #Clase nodo para TSP con ramificación y poda

            

# Create graph
gr = WeightedGraph(directed = False)


gr.add_vertex('Cadiz')
gr.add_vertex('Sevilla')
gr.add_vertex('Granada')
gr.add_vertex('Leon')
gr.add_vertex('Jaen')
gr.add_vertex('Murcia')
gr.add_vertex('Albacete')
gr.add_vertex('Valencia')
gr.add_vertex('Madrid')
gr.add_vertex('Badajoz')
gr.add_vertex('Salamanca')
gr.add_vertex('Vigo')
gr.add_vertex('Valladolid')
gr.add_vertex('Zaragoza')
gr.add_vertex('Barcelona')
gr.add_vertex('Coruña')
gr.add_vertex('Oviedo')
gr.add_vertex('Bilbao')
gr.add_vertex('Mancha')
gr.add_vertex('Gerona')

gr.add_edge('Cadiz', 'Sevilla',125)
gr.add_edge('Cadiz', 'Leon',150)

gr.add_edge('Sevilla', 'Granada',256)
gr.add_edge('Sevilla', 'Jaen',242)

gr.add_edge('Leon', 'Granada',70)

gr.add_edge('Granada', 'Jaen',99)
gr.add_edge('Granada', 'Murcia',278)

gr.add_edge('Jaen', 'Madrid',335)

gr.add_edge('Murcia', 'Albacete',150)
gr.add_edge('Murcia', 'Valencia',241)

gr.add_edge('Albacete', 'Valencia',191)
gr.add_edge('Albacete', 'Madrid',251)

gr.add_edge('Valencia', 'Barcelona',349)

gr.add_edge('Madrid', 'Badajoz',403)
gr.add_edge('Madrid', 'Valladolid',193)
gr.add_edge('Madrid', 'Bilbao',305)
gr.add_edge('Madrid', 'Zaragoza',325)

gr.add_edge('Badajoz', 'Salamanca',100)

gr.add_edge('Salamanca', 'Vigo',101)

gr.add_edge('Vigo', 'Valladolid',356)
gr.add_edge('Vigo', 'Coruña',171)

gr.add_edge('Valladolid', 'Coruña',455)
gr.add_edge('Valladolid', 'Oviedo',260)
gr.add_edge('Valladolid', 'Bilbao',280)

gr.add_edge('Zaragoza', 'Bilbao',324)
gr.add_edge('Zaragoza', 'Mancha',200)
gr.add_edge('Zaragoza', 'Barcelona',296)

gr.add_edge('Barcelona', 'Gerona',100)

gr.add_edge('Oviedo', 'Bilbao',304)

gr.add_edge('Mancha', 'Gerona',100)


print("-----Uniform cost search-----")
res = tsp_ucs(gr, 'Cadiz')
print(res)


print("-----Branch and bound-----")
res = tsp_bb(gr, 'Cadiz')
print(res)