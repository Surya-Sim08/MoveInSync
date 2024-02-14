class Driver:
    def __init__(self, name, rating, location):
        self.name = name
        self.rating = rating
        self.location = location

class Path:
    def __init__(self, start, end, distance, waiting_time, traffic):
        self.start = start
        self.end = end
        self.distance = distance
        self.waiting_time = waiting_time
        self.traffic = traffic

def allocate_driver(drivers, paths, start, destination):
    # Initialize distances and visited nodes
    distances = {node: float('inf') for node in drivers + [start]}
    visited = set()

    # Set distance to start node as 0
    distances[start] = 0

    while drivers:
        # Find the driver with the highest rating
        current_driver = max(drivers, key=lambda d: d.rating)
        drivers.remove(current_driver)

        # Update distances for adjacent nodes
        for path in paths:
            if path.start == current_driver.location:
                total_cost = path.distance * 10 + path.waiting_time * 2
                if total_cost + distances[current_driver.location] < distances[path.end]:
                    distances[path.end] = total_cost + distances[current_driver.location]

    # Find the shortest path from start to destination
    path = []
    current_node = destination
    while current_node != start:
        path.append(current_node)
        for p in paths:
            if p.end == current_node and distances[current_node] - p.distance * 10 - p.waiting_time * 2 == distances[p.start]:
                current_node = p.start
                break
    path.append(start)
    path.reverse()

    return path


drivers = [
    Driver("Driver1", 4.2, "A"),
    Driver("Driver2", 4.8, "B"),
    Driver("Driver3", 4.5, "C"),
    Driver("Driver4", 4.0, "D"),
    Driver("Driver5", 4.7, "E"),
    Driver("Driver6", 4.3, "F"),
    Driver("Driver7", 4.6, "G"),
    Driver("Driver8", 4.9, "H"),
    Driver("Driver9", 4.4, "I"),
    Driver("Driver10", 4.1, "J"),
    Driver("Driver11", 4.7, "K"),
    Driver("Driver12", 4.2, "L"),
    Driver("Driver13", 4.8, "M"),
    Driver("Driver14", 4.5, "N"),
    Driver("Driver15", 4.3, "O")
    
]

paths = [
    Path("A", "B", 5, 10, 1),
    Path("B", "C", 3, 5, 0),
    Path("C", "D", 4, 8, 1),
    Path("D", "E", 6, 12, 2),
    Path("E", "F", 2, 4, 0),
    Path("F", "G", 7, 14, 1),
    Path("G", "H", 5, 10, 0),
    Path("H", "I", 3, 6, 1),
    Path("I", "J", 4, 8, 0),
    Path("J", "K", 6, 12, 2),
    Path("K", "L", 2, 4, 0),
    Path("L", "M", 7, 14, 1),
    Path("M", "N", 5, 10, 0),
    Path("N", "O", 3, 6, 1),
    Path("O", "A", 4, 8, 0)
]

start_location = "A"
destination_location = "M"

allocated_path = allocate_driver(drivers, paths, start_location, destination_location)
print("Allocated path:", allocated_path)

