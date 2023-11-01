#------------------------------------------------------------------------------------------------------------------
#   Example of implementation of the Floyd-Warshall Algorithm.
#------------------------------------------------------------------------------------------------------------------

import numpy as np

#------------------------------------------------------------------------------------------------------------------
#   WeightedGraph class
#------------------------------------------------------------------------------------------------------------------
class WeightedGraph:
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


#------------------------------------------------------------------------------------------------------------------
#   Floyd-Marshall algorithm
#------------------------------------------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------------------------------------------
#   Test algorithm
#------------------------------------------------------------------------------------------------------------------

# Create graph
gr = WeightedGraph(directed = False)

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

print("Length of shortest paths")
print(floyd_marshall(gr._adjacency_matrix))

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------