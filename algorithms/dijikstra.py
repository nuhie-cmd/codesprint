
import heapq
from database import get_nodes, get_edges


def build_graph(node_ids, edges):

    graph = {node: [] for node in node_ids}

    for edge in edges:
        src = edge["from_node"]
        dest = edge["to_node"]
        dist = edge["weight"]

        graph[src].append((dest, dist))
        graph[dest].append((src, dist))

    return graph


def shortest_path(graph, start, end):

    pq = [(0, start)]

    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0

    while pq:

        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        if current_node == end:
            break

        for neighbour, weight in graph[current_node]:

            new_distance = current_distance + weight

            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                previous[neighbour] = current_node

                heapq.heappush(
                    pq,
                    (new_distance, neighbour)
                )

    if distances[end] == float("inf"):
        return [], float("inf")

    path = []

    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path, distances[end]


#if __name__ == "__main__":

 #   nodes = get_nodes()
  #  edges = get_edges()

   # node_ids = [node["id"] for node in nodes]

    #graph = build_graph(node_ids, edges)

    #path, distance = shortest_path(graph, 1, 6)

    #print("Path:", path)
