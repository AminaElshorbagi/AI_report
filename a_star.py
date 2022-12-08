graph={
    'A':[('B',6),('F',3)],
    'B':[('D',2),('C',3)],
    'C':[('D',1),('E',8)],
    'D':[('C',1),('E',5)],
    'E':[('I',5),('J',5)],
    'F':[('G',1),('H',7)],
    'G':[('I',3)],
    'H':[('I',2)],
    'I':[('E',5),('J',3)]
}
H_table={
    'A':10,
    'B':8,
    'C':5,
    'D':7,
    'E':3,
    'F':6,
    'G':5,
    'H':3,
    'I':1,
    'J':0
}
def path_f_cost(path):
    g_cost=0
    for(node,cost)in path:
        g_cost+=cost
        last_node=path[-1][0]
        h_cost=H_table[last_node]
        f_cost=g_cost+h_cost
    return f_cost,last_node
def a_star_search(graph,start,goal):
    visited=[]
    queue=[[(start,0)]]
    while queue:
        queue.sort(key=path_f_cost)
        path=queue.pop(0)
        node=path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes=graph.get(node,[])
            for (node2,cost) in adjacent_nodes:
                new_path=path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)

solution=a_star_search(graph,'A','J')
print('solution is ',solution)
print('cost of solution is ',path_f_cost(solution)[0])

