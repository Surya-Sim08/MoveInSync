import heapq

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node] = []

    def add_edge(self, node1, node2, distance, waiting_time):
        self.nodes[node1].append((node2, distance, waiting_time))
        self.nodes[node2].append((node1, distance, waiting_time))

def dtra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    predecessors = {node: None for node in graph.nodes}
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, distance, waiting_time in graph.nodes[current_node]:
            # Below we are calculating cost per km and waiting cost while travelling through a particular way.
            
            distance_cost = distance * 10 
            waiting_cost = waiting_time * 2  
            total_cost = current_distance + distance_cost + waiting_cost

            if total_cost < distances[neighbor]:
                distances[neighbor] = total_cost
                predecessors[neighbor] = current_node
                heapq.heappush(queue, (total_cost, neighbor))

    return distances, predecessors

def allocate_driver(graph, start, destination, min_rating):
    
    # I am filtering drivers with rating >= min_rating
    
    eligible_drivers = [node for node in graph.nodes if graph.nodes[node][0][2] >= min_rating]

    # Calculate shortest paths from start for eligible drivers
    short_paths = {}
    for driver in eligible_drivers:
        short_paths[driver], _ = dtra(graph, driver)

    # Now we are finding the nearest driver with the shortest path to the destination
    min_cost = float('inf')
    allocated_driver = None
    for driver, distances in short_paths.items():
        if distances[destination] < min_cost:
            min_cost = distances[destination]
            allocated_driver = driver

    return allocated_driver, min_cost

def get_live_path(graph, start, destination, user):
    _, predecessors = dtra(graph, start)
    path = []
    current_node = destination
    while current_node:
        path.append(current_node)
        current_node = predecessors[current_node]
    path.reverse()
    return path

# Function to find driver based on user conditions
def find_driver(graph, start, destination, min_rating):
    allocated_driver, min_cost = allocate_driver(graph, start, destination, min_rating)
    if allocated_driver:
        live_path = get_live_path(graph, start, destination, "user1")
        driver_location = allocated_driver if live_path else None
        return allocated_driver, driver_location, min_cost
    else:
        return None, None, None

# Now taking Example with sample inputs
if __name__ == "__main__":
    
    # Creating the graph
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")
    graph.add_node("F")
    graph.add_node("G")
    graph.add_node("H")
    graph.add_node("I")
    graph.add_node("J")
    graph.add_node("K")
    graph.add_node("L")
    graph.add_node("M")
    graph.add_node("N")
    graph.add_node("O")
    
    # Add edges with 4 parameters: 2 of nodes from starting to ending point, distance between starting and ending point and waiting time between them.(nodes, distance, waiting time)
    graph.add_edge("A", "B", 5, 3)
    graph.add_edge("B", "C", 7, 2)
    graph.add_edge("C", "D", 3, 1)
    graph.add_edge("D", "E", 4, 2)
    graph.add_edge("E", "F", 6, 3)
    graph.add_edge("F", "G", 5, 1)
    graph.add_edge("G", "H", 3, 2)
    graph.add_edge("H", "I", 2, 1)
    graph.add_edge("I", "J", 4, 3)
    graph.add_edge("J", "K", 5, 2)
    graph.add_edge("K", "L", 6, 1)
    graph.add_edge("L", "M", 7, 2)
    graph.add_edge("M", "N", 3, 1)
    graph.add_edge("N", "O", 2, 3)

    # Now taking data of driver ratings which we can take as huge dataset if needed.
    graph.nodes["A"].append(("B", 0, 3.7))  
    graph.nodes["B"].append(("A", 0, 4.0))  
    graph.nodes["C"].append(("D", 0, 3.5))  
    graph.nodes["D"].append(("E", 0, 4.2)) 
    graph.nodes["G"].append(("H", 0, 3.8))  
    graph.nodes["J"].append(("I", 0, 3.9))  
    graph.nodes["L"].append(("K", 0, 4.5))  
    graph.nodes["N"].append(("M", 0, 3.6)) 

    # Atkast calling functions to find driver for user with specific conditions
    allocated_driver, driver_location, min_cost = find_driver(graph, "A", "O", 3.5)
    if allocated_driver:
        print("Driver allocated:", allocated_driver)
        print("Driver location:", driver_location)
        print("Minimum cost:", min_cost)
    else:
        print("No eligible driver found.")
