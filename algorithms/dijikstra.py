import heapq


def build_graph(nodes, edges):

    graph = {node: [] for node in nodes}

    for edge in edges:
        src = edge["from"]
        dest = edge["to"]
        dist = edge["distance"]

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


if __name__ == "__main__":

    nodes = [1,2,3,4,5,6]

    edges = [
        {"from":1,"to":2,"distance":5},
        {"from":1,"to":3,"distance":3},
        {"from":2,"to":4,"distance":4},
        {"from":3,"to":4,"distance":2},
        {"from":3,"to":5,"distance":6},
        {"from":4,"to":6,"distance":1},
        {"from":5,"to":6,"distance":2},
    ]

    graph = build_graph(nodes, edges)

    path, distance = shortest_path(graph, 1, 6)

    print("Path:", path)
    print("Distance:", distance)