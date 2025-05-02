import heapq

def prim_mst(graph):
    vertices = list(graph.keys())
    visited = {vertex: False for vertex in vertices}
    mst = []
    total_cost = 0

    start_vertex = vertices[0]
    heap = [(0, start_vertex)]

    while heap:
        cost, current_vertex = heapq.heappop(heap)

        if visited[current_vertex]:
            continue

        visited[current_vertex] = True
        total_cost += cost

        if cost > 0:
            mst.append((current_vertex, cost))

        for neighbor, edge_cost in graph[current_vertex]:
            if not visited[neighbor]:
                heapq.heappush(heap, (edge_cost, neighbor))

    return mst, total_cost

# Function to get dynamic input for graph
def get_input_graph():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        edge_info = input("Enter edge info (source, destination, cost): ").split()
        source, dest, cost = edge_info[0], edge_info[1], int(edge_info[2])

        if source not in graph:
            graph[source] = []
        if dest not in graph:
            graph[dest] = []

        graph[source].append((dest, cost))
        graph[dest].append((source, cost))

    return graph

# Get dynamic input for the graph
graph = get_input_graph()

# Find Minimum Spanning Tree using Prim's algorithm
mst, total_cost = prim_mst(graph)

# Print the Minimum Spanning Tree and total cost
print("Minimum Spanning Tree:", mst)
print("Total Cost:", total_cost)

