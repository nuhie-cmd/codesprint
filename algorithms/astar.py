import heapq
import math

from dijikstra import build_graph
from room_lookup import get_node


coordinates = {
    1:(0,0),
    2:(2,1),
    3:(1,3),
    4:(3,4),
    5:(5,3),
    6:(4,6)
}


def heuristic(node, goal, coordinates):

    x1, y1 = coordinates[node]
    x2, y2 = coordinates[goal]

    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def astar(graph, coordinates, start, goal):

    open_set = []

    heapq.heappush(open_set, (0, start))

    g_score = {node: float("inf") for node in graph}
    f_score = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}

    g_score[start] = 0
    f_score[start] = heuristic(start, goal, coordinates)

    while open_set:

        _, current = heapq.heappop(open_set)

        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = previous[current]

            path.reverse()

            return path, g_score[goal]

        for neighbour, weight in graph[current]:

            tentative = g_score[current] + weight

            if tentative < g_score[neighbour]:

                previous[neighbour] = current

                g_score[neighbour] = tentative

                f_score[neighbour] = tentative + heuristic(
                    neighbour,
                    goal,
                    coordinates
                )

                heapq.heappush(
                    open_set,
                    (f_score[neighbour], neighbour)
                )

    return [], float("inf")


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

    start = get_node("Entrance")
    end = get_node("AI Lab")

    path, distance = astar(graph, coordinates, start, end)

    print("Path:", path)
    print("Distance:", distance)