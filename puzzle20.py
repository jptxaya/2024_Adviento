from collections import deque
import copy

directions={
    0:[0,-1],
    1:[1,0],
    2:[0,1],
    3:[-1,0]
}


def bfs(cheated_tree, start, end):
    visited = []
    queue = deque([(start,0)])
    while queue:
        node  = queue.popleft()
        if node[0] == end:
            return node[1]
        if node[0] not in visited:
            visited.append(node[0])
            for neighboor in cheated_tree[node[0]]:
                queue.append([neighboor, node[1] + 1])




def set_neighbourg_obstacle(elem, free, xtree):
    for direction in [0,1,2,3]:
        pos_node = (elem[0]+ directions[direction][0],elem[1]+ directions[direction][1])
        if pos_node in free:
            if elem in xtree:
                list_aux = xtree.get(elem)
                list_aux.append(pos_node)
                xtree[elem] = list_aux
            else:
                xtree[elem] = [(pos_node)]
    for cell in xtree[elem]:
        #Update new nodes
        list_aux = xtree.get(cell)
        list_aux.append(elem)
        xtree[cell] = list_aux
    return xtree


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
        cheats.add((elem[0]+1,elem[1]))
    if ((elem[0], elem[1]+1) not in free) and ((elem[0], elem[1]+2) in free):
         cheats.add((elem[0],elem[1]+1))
#print(cheats)

#Testing
# cheats = set()
# cheats.add((12,4))
# cheats.add((2,2))

distance_without_cheating = bfs(tree,start,end)
print(distance_without_cheating)

new_cheating_distances = []
#original_tree = tree.copy()
for cheat in cheats:
    original_tree = copy.deepcopy(tree)
    cheated_tree = set_neighbourg_obstacle(cheat, free, original_tree)
    new_cheating_distances.append(bfs(cheated_tree,start,end))
difference_distances = list(map(lambda x: distance_without_cheating - x, new_cheating_distances))
#print(sorted(difference_distances))
#print(len(new_cheating_distances))
least_100 = list(filter(lambda x: x >= 100,difference_distances ))
print(least_100)
print(len(least_100))
