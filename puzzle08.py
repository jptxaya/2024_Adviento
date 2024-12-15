def set_aninodes(antenna,pos_y, pos_x,set_antenna):
    count_antenna = 0
    y = pos_y 
    while y < len(mapa):
        if y == pos_y:
            x = x = pos_x + 1
        else:
            x = 0
        while x < len(mapa[0]):
            if antenna == mapa[y][x]:
               dif_x = x - pos_x
               dif_y = y - pos_y
               if dif_x >= 0:
                   antinode1 = [pos_y - dif_y,pos_x - dif_x]
                   antinode2 = [y + dif_y, x + dif_x]
               else:
                   antinode1 = [pos_y - dif_y,pos_x + abs(dif_x)]
                   antinode2 = [y + dif_y, x + dif_x]
               if (antinode1[0] >= 0)  and (antinode1[0] < len(mapa)) and (antinode1[1] >= 0) and antinode1[1] < len(mapa[0]): #and mapa[antinode1[0]][antinode1[1]] == ".":
                   count_antenna += 1
                   set_antenna.add((antinode1[0],antinode1[1]))
               if (antinode2[0] >= 0)  and (antinode2[0] < len(mapa)) and (antinode2[1] >= 0) and antinode2[1] < len(mapa[0]): #and mapa[antinode2[0]][antinode2[1]] == ".":
                   count_antenna += 1
                   set_antenna.add((antinode2[0],antinode2[1]))
            x += 1
        y += 1
    return count_antenna


with open("data/data08.txt") as file:
    mapa = []
    for elem in file.read().splitlines():
        mapa.append(list(elem))

i = 0
set_antenna = set()
while(i < len(mapa)):
    j = 0
    while( j < len(mapa[0])):
        if mapa[i][j] != ".":
            find_character = mapa[i][j]
            set_aninodes(find_character,i,j,set_antenna)
        j  += 1
    i += 1
print(len(set_antenna))


