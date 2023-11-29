import osmnx as ox
import networkx as nx
import geopy.distance
import time

# Descargar datos de conectividad urbana alrededor del Parque Metropolitano de León
node_id_parque_leon = 550853775
G = ox.graph_from_point((20.6795, -101.3547), dist=10000, network_type='drive')
ox.plot_graph(G)

# Obtener lista de nodos en el grafo
lista_de_nodos = list(G.nodes)

# Seleccionar algunos nodos para lugares específicos
nodos_seleccionados = lista_de_nodos[:5]  # Puedes ajustar esto según sea necesario

# Crear el diccionario de lugares
places = {f'place{i+1}': (nodo, f'Lugar {i+1}') for i, nodo in enumerate(nodos_seleccionados)}

# Definir funciones para calcular distancias y tiempos de viaje
def calculate_distance(coord_orig, coord_dest):
    return geopy.distance.distance(coord_orig, coord_dest).m

def calculate_travel_time(distance, speed_kph):
    return distance / (speed_kph / 3.6)

# Implementar algoritmos de búsqueda de caminos
def bfs(graph, start_node, end_node):
    return nx.shortest_path(graph, source=start_node, target=end_node)

def dfs(graph, start_node, end_node):
    return nx.dfs_tree(graph, source=start_node, depth_limit=10).to_undirected()

def uniform_cost(graph, start_node, end_node):
    return nx.shortest_path(graph, source=start_node, target=end_node, weight='length')

def a_star(graph, start_node, end_node):
    return nx.astar_path(graph, source=start_node, target=end_node, weight='length')

# Evaluar rendimiento de los algoritmos
for place_key, (node_id, place_name) in places.items():
    print(f"\nRuta para {place_name} (ID del nodo: {node_id}):")

    # Seleccionar otro lugar aleatorio como destino
    other_places = {k: v for k, v in places.items() if k != place_key}
    destination_key, (destination_node, destination_name) = other_places.popitem()

    # Calcular coordenadas de los nodos de origen y destino
    coord_orig = G.nodes[node_id]['y'], G.nodes[node_id]['x']
    coord_dest = G.nodes[destination_node]['y'], G.nodes[destination_node]['x']

    # Calcular distancias y tiempos de viaje
    distance = calculate_distance(coord_orig, coord_dest)

    # Obtener información de la conexión entre los nodos
    edge_data = G.get_edge_data(node_id, destination_node)

    # Verificar si la conexión y la información de velocidad están disponibles
    if edge_data and 'speed_kph' in edge_data:
        speed_kph = edge_data['speed_kph']
        travel_time = calculate_travel_time(distance, speed_kph)
        print(f"Velocidad entre {node_id} y {destination_node}: {speed_kph} kph")
    else:
        # Manejar el caso en el que no hay información de velocidad disponible
        print(f"No hay información de velocidad para la conexión {node_id} -> {destination_node}.")
        speed_kph = None
        travel_time = None

    # Ejecutar y medir el tiempo de ejecución de cada algoritmo
    algorithms = [('BFS', bfs), ('DFS', dfs), ('Costo Uniforme', uniform_cost), ('A*', a_star)]

    for algorithm_name, algorithm_func in algorithms:
        start_time = time.time()
        path = algorithm_func(G, node_id, destination_node)
        end_time = time.time()

        print(f"{algorithm_name}: {path}")
        print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")