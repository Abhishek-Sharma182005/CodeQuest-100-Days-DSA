from collections import deque 
graph = {}
graph_input = input("Graph: ")
edges = graph_input.split(",")

for edge in edges:
    parts = edge.split(":")
    node = parts[0].strip()  
    neighbors = parts[1].strip().split()
    graph[node] = neighbors
start_node = input("Start at: ").strip()

visited = set() 
queue = deque() 
queue.append(start_node)
visited.add(start_node)

print("BFS Traversal:", end=" ")
while queue:
    current_node = queue.popleft()
    print(current_node, end=" ")
    for neighbor in graph.get(current_node, []):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)