import heapq
from collections import deque

def create_tree(obs,x,y):
    tree = dict()
    for i in range(x):
        for j in range(y):
            for direct in [0,1,2,3]:
                next_node = (i + directions[direct][0],  j+ directions[direct][1])
                if next_node not in obs and next_node[0] >= 0 and next_node[0] < x and next_node[1] >= 0 and next_node[1] < y:
                    if (i,j) not in tree:
                        tree[(i,j)] = [next_node]
                    else:
                        list_aux = tree.get((i,j))
                        list_aux.append(next_node)
                        tree[(i,j)] = list_aux
    return tree
                

def bfs(tree, start, end):
    visited = []
    queue = deque([(start,0)])
    while queue:
        node  = queue.popleft()
        if node[0] == end:
            return node[1]
        if node[0] not in visited:
            visited.append(node[0])
            for neighboor in tree[node[0]]:
                queue.append([neighboor, node[1] + 1])



obstacles = []
with open("data/data18.txt") as file:
    bytes_selected = 0
    for elem in file.read().splitlines():
        if (bytes_selected < 1024):
            obs = list(map(int,elem.split(",")))
            obstacles.append((obs[0],obs[1]))
            bytes_selected += 1
print(len(obstacles))

directions={
    0:[0,-1],
    1:[1,0],
    2:[0,1],
    3:[-1,0]
}

tree = create_tree(obstacles,71,71)
dista = bfs(tree,(0,0),(70,70))
print(dista)
