import heapq

direction = { #[y,x]
    0: [-1,0],
    1: [0,1],
    2: [1,0],
    3: [0,-1]
}

def get_posible_directions(dir):
    if dir % 2 == 0:
        return [dir,3,1]
    return [dir,0,2]

def dijkstra(grid,start,end,dir):

    pq = [] # To create priarity quee we need a list
    #Inserting the first value in priority quee
    heapq.heappush(pq,(0,start,dir))
    #Visited - To stoarage the distance when visiting the node
    visited = dict()

    distances = []
    #Starting the process
    while pq:
        #Recover the min item from pq
        current_distance, node, dir = heapq.heappop(pq)
        #Verify is final node
        if node == end:
            distances.append(current_distance)
            continue      
        #If we pass for this node and his value is better, we dont do anything,
        #otherwise we assing this value
        if (node,dir) in visited and visited[(node,dir)] < current_distance:
            continue         
        visited[(node,dir)] = current_distance

        next_nodes = []
        for new_direction in get_posible_directions(dir):
            y, x = direction.get(new_direction)
            if new_direction == dir:
                neighboor = (1, (node[0] + y, node[1] + x), new_direction) 
            else:
                neighboor = (1001, (node[0] + y, node[1] + x), new_direction)
            if (neighboor[1]) in grid:
                next_nodes.append(neighboor)
        for sum_distance, nnode, ndir in next_nodes:
            heapq.heappush(pq,(current_distance + sum_distance,nnode, ndir))
    return distances


with open("data/data16.txt") as file:
    i = 0
    free = []
    for elem in file.read().splitlines():
        celds = list(elem)
        j = 0
        while ( j < len(celds)):
            if celds[j] == ".":
                free.append((i,j))
            elif celds[j] == "E":
                end = (i,j)
                free.append(end)
            elif celds[j] == "S":
                start = (i,j)
            j += 1
        i += 1

distances = dijkstra(free,start,end,1)
print(min(distances))