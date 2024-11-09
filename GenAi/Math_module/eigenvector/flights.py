import csv
import sys
from collections import defaultdict, deque

def parse_csv(file_path):
    flights = defaultdict(dict)
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            origin = row['Origin'].strip().lower()
            destination = row['Destination'].strip().lower()
            airline = row['Airline']
            flight_number = row['Flight Number']
            flights[origin][destination] = (airline, flight_number)
    return flights

def bfs_shortest_path_with_stops(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()
    min_path = None

    while queue:
        (node, path) = queue.popleft()
        if node not in visited:
            visited.add(node)

            if node == end and len(path) > 2:  # Ensure at least one stop
                if min_path is None or len(path) < len(min_path):
                    min_path = path
                continue  # Continue searching for potentially shorter paths

            for next_node in graph[node]:
                if next_node not in visited:
                    new_path = path + [next_node]
                    if next_node == end and len(new_path) > 2:
                        if min_path is None or len(new_path) < len(min_path):
                            min_path = new_path
                    elif next_node != end:
                        queue.append((next_node, new_path))
    
    return min_path

def main():
    if len(sys.argv) != 2:
        print("Usage: python flights.py <path_to_csv_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    flights = parse_csv(file_path)

    start = input("Enter the starting point: ").strip().lower()
    end = input("Enter the destination: ").strip().lower()

    if start not in flights or end not in flights:
        print("Error: Start or destination city not found in the flight data.")
        sys.exit(1)

    path = bfs_shortest_path_with_stops(flights, start, end)

    if path:
        print(f"\nShortest path from {start.title()} to {end.title()} (excluding direct flights):")
        for i in range(len(path) - 1):
            origin = path[i]
            destination = path[i + 1]
            airline, flight_number = flights[origin][destination]
            print(f"{i+1}. {origin.title()} to {destination.title()} - {airline} {flight_number}")
        print(f"\nTotal number of stops: {len(path) - 2}")
    else:
        print(f"No path found between {start.title()} and {end.title()} with at least one stop")

if __name__ == "__main__":
    main()