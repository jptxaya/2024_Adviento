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
                   #Contruct all antindodes lu
                   rep = 1
                   while( (pos_y - (dif_y * rep) >= 0) and (pos_x - (dif_x * rep) >= 0) ):
                       set_antenna.add((pos_y - (dif_y * rep) , pos_x - (dif_x * rep)))
                       rep += 1
                   #Contruct all antindodes rd
                   rep = 1
                   while( (y + (dif_y * rep) < len(mapa)) and (x + (dif_x * rep) < len(mapa[0])) ):
                       set_antenna.add((y + (dif_y * rep) , x + (dif_x * rep)))
                       rep += 1
               else:
                   #Contruct all antindodes ru
                   rep = 1
                   while( (pos_y - (dif_y * rep) >= 0) and (pos_x + abs(dif_x * rep) < len(mapa[0])) ):
                       set_antenna.add((pos_y - (dif_y * rep) , pos_x + abs(dif_x * rep)))
                       rep += 1
                   #Contruct all antindodes ld
                   rep = 1
                   while( (y + (dif_y * rep) < len(mapa)) and (x + (dif_x * rep) >= 0) ):
                       set_antenna.add((y + (dif_y * rep) , x + (dif_x * rep)))
                       rep += 1
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
            #Part 2
            set_antenna.add((i,j))
            #End Part 2 
            set_aninodes(find_character,i,j,set_antenna)
        j  += 1
    i += 1
print(len(set_antenna))


