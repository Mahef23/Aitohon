graph={
    'A':['B'],
    'B':['C','D'],
    'C':['D'],
    'D':[]
}
visited = []
queue = []

def befs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Following Breadth-First-Search")
befs(visited,graph,'A')