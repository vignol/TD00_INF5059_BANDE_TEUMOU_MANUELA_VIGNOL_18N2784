from collections import deque
def bfs(graph, first):
    queue=deque([first])
    visited=set()
    while queue:
        location=queue.popleft()
        if location not in visited:
            print(location, end=' ')
            visited.add(location)
            queue.extend(graph[location]-visited)

def dfs(graph, first, visited=None):
    if visited is None:
        visited=set()
    if first not in visited:
        print(first, end=' ')
        visited.add(first)
        for neighbor in graph[first]:
            dfs(graph, neighbor, visited)

def check_connect(graph, loc1, loc2):
    queue= deque([loc1])
    visited=set()
    while queue:
        location=queue.popleft()
        if location==loc2:
            return True
        if location not in visited:
            visited.add(location)
            queue.extend(graph[location]-visited)
    return False
graph = {
    'X': {'Y', 'Z'},
    'Y': {'X', 'W', 'V'},
    'Z': {'X', 'U'},
    'W': {'Y'},
    'V': {'Y', 'U'},
    'U': {'Z', 'V'},
    'A': {'B'},
    'B': {'A'}
}
print("\n Check connection W and U:", check_connect(graph, 'W', 'U'))
print("\n Check connection X and W:", check_connect(graph, 'A', 'U'))

print("***BFS***")
bfs(graph,'X')
print("\n ***DFS***")
dfs(graph,'X')
