

graph = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

visited = []
def dfs(graph, node):
    if node not in visited:
        visited.append(node)
        for i in graph[node]:
            dfs(graph, i)
    return visited
             
if __name__ == '__main__':
    visited = dfs(graph, 'E')
    print( visited )