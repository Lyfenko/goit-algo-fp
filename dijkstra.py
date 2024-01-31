import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(set)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].add(to_node)
        self.edges[to_node].add(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance


def dijkstra(graph, start):
    visited = set()
    hq = [(0, start)]
    distances = {n: float('inf') for n in graph.nodes}
    distances[start] = 0
    previous_nodes = {n: None for n in graph.nodes}

    while hq:
        current_distance, current_node = heapq.heappop(hq)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor in graph.edges[current_node]:
            new_distance = current_distance + graph.distances[(current_node, neighbor)]

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(hq, (new_distance, neighbor))

    return distances, previous_nodes


def print_shortest_paths(start, dist, prev_nodes):
    for n in dist:
        path = []
        current_node = n
        while current_node is not None:
            path.insert(0, current_node)
            current_node = prev_nodes[current_node]
        print(f"Найкоротший шлях з {start} до {n}: {path}, Відстань: {dist[n]}", end='\n\n')


def draw_graph(graph):
    G = nx.Graph()
    G.add_nodes_from(graph.nodes)

    for (from_node, to_node), weight in graph.distances.items():
        G.add_edge(from_node, to_node, weight=weight)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black')
    edge_labels = {(from_node, to_node): weight for (from_node, to_node), weight in graph.distances.items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()


if __name__ == "__main__":
    # Example usage
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')

    g.add_edge('A', 'B', 1)
    g.add_edge('B', 'C', 2)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'D', 7)
    g.add_edge('C', 'D', 1)

    start_node = 'A'
    shortest_distances, previous_nodes = dijkstra(g, start_node)

    print("Найкоротші відстані:")
    for n, d in shortest_distances.items():
        print(f"{start_node} до {n}: {d}")

    print("\nНайкоротші шляхи:")
    print_shortest_paths(start_node, shortest_distances, previous_nodes)

    # Draw the graph
    draw_graph(g)
