def find_trails(pos_i, pos_j, next_number, finded_finished):
    if (pos_i >= 0) and (pos_i < len(topo)) and (pos_j >= 0) and (pos_j < len(topo[0])):
        if next_number == 9 and int(topo[pos_i][pos_j]) == 9:
            finded_finished.add((pos_i,pos_j))
        else: 
            if int(topo[pos_i][pos_j]) == next_number:
                #Find in al direction the next number
                #UP
                find_trails(pos_i - 1,pos_j, next_number + 1, finded_finished)
                #DOWN
                find_trails(pos_i + 1,pos_j, next_number + 1, finded_finished)
                #LEFT
                find_trails(pos_i,pos_j - 1, next_number + 1, finded_finished)
                #RIGHT
                find_trails(pos_i,pos_j + 1, next_number + 1, finded_finished)

with open("data/data10.txt") as file:
    topo = []
    for elem in file.read().splitlines():
        topo.append(list(elem))
print(topo)

trails = 0
i = 0
while (i < len(topo)):
    j = 0
    while( j < len(topo[0])):
        if topo[i][j] == "0":
            finded_finished = set()
            find_trails( i , j, 0, finded_finished)
            trails += len(finded_finished)
        j += 1
    i += 1
print(f"Result Trails:{trails}")

