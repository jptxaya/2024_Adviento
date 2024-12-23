with open("data/data23.txt") as file:
    computers = set()
    connections = dict()
    for elem in file.read().splitlines():
         connection = elem.split("-")
         for elem in connection:
            computers.add(elem)
            if elem not in connections:
                connections[elem] = set()
         connections[connection[0]].add(connection[1])
         connections[connection[1]].add(connection[0])
#print(connections)

filter_t_computers = list(filter(lambda x: x.startswith("t") > 0, computers))
print(filter_t_computers)
game_sets = set()
for cmp in filter_t_computers:
    i = 0
    clist = list(connections[cmp])
    while( i < len(clist) - 1):
        c2 = clist[i]
        for c3 in clist[i+1:]:
            if c3 in connections[c2]:
              game_set = [cmp,c2,c3]
              game_set = sorted(game_set)
              game_sets.add(tuple(game_set))
        i += 1

for gs in game_sets:
    print(gs)
print(len(game_sets))

