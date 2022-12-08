graph_file=open("graph","r")
graph=graph_file.read()
graph=eval(graph)
visited = []
queue = []

def bfs(visited, graph, node):  # function for BFS
       visited.append(node)
       queue.append(node)
       while queue:  # Creating loop to visit each node
           m = queue.pop(0)
           print(m, end=" ")
           for neighbour in graph[m]:
               if neighbour not in visited:
                   visited.append(neighbour)
                   queue.append(neighbour)
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')  # function calling