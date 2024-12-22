from collections import deque

directions={
    0:[0,-1],
    1:[1,0],
    2:[0,1],
    3:[-1,0]
}

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

with open("data/data20.txt") as file:
    y = 0
    free = []
    for elem in file.read().splitlines():
        x = 0
        for cell in list(elem):
            #Detect free
            if cell == ".":
                free.append((x,y))
            #Detect Start points
            elif cell == "S":
                start = (x,y)
                free.append(start)
            #Detect End points
            elif cell == "E":
                end = (x,y)
                free.append(end)
            x += 1
        y += 1

#Generate tree
tree = dict()
for elem in free:
    #get posible nodes
    for direction in [0,1,2,3]:
        pos_node = (elem[0]+ directions[direction][0],elem[1]+ directions[direction][1])
        if pos_node in free:
            if elem in tree:
                list_aux = tree.get(elem)
                list_aux.append(pos_node)
                tree[elem] = list_aux
            else:
                tree[elem] = [(pos_node)]
#print(tree)

#Find posible cheats
cheats = set()
for elem in free:
    if ((elem[0]+1, elem[1]) not in free) and ((elem[0]+2, elem[1]) in free):
        cheats.add((elem,(elem[0]+1,elem[1]),(elem[0]+2, elem[1])))
    if ((elem[0], elem[1]+1) not in free) and ((elem[0], elem[1]+2) in free):
         cheats.add((elem,(elem[0],elem[1]+1),(elem[0], elem[1]+2)))
#print(cheats)

#Testing
#cheats = set()
#cheats.add(((12, 7), (12,8), (12, 9)))
# cheats.add((2,2))

distance_without_cheating = bfs(tree,start,end)
print(distance_without_cheating)

new_cheating_distances = []
for cheat in cheats:
    distance = bfs(tree,cheat[0],cheat[2]) -2
    new_cheating_distances.append(distance)
print(sorted(new_cheating_distances))
least_100 = list(filter(lambda x: x >= 100,new_cheating_distances ))
print(len(least_100))

