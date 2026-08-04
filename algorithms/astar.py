import heapq
import math

from dijikstra import build_graph
from room_lookup import get_node
from database import get_nodes, get_edges


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


#if __name__ == "__main__":

 #   nodes = get_nodes()
  #  edges = get_edges()

   # coordinates = {
    #node["id"]: (node["x"], node["y"])
    #for node in nodes
    #}

    #node_ids = [node["id"] for node in nodes]

    #graph = build_graph(node_ids, edges)


    #start = get_node("Main Block")
    #end = get_node("AI ML Lab 1")
    
    #if start is None or end is None:
     #   print("Invalid room name.")
    #else:
     #   path, distance = astar(graph, coordinates, start, end)
      #  print("Path:", path)
       # print("Distance:", distance)
