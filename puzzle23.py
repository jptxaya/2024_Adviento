from collections import deque
with open("data/data23_test.txt") as file:
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

filter_t_computers = sorted(list(filter(lambda x: x.startswith("t"), computers)))
max_length = 0
result = set()
results = set()

for cmp in filter_t_computers:
    pps = set([cmp])
    for elem in connections.get(cmp, []):
         if all(elem in connections.get(base, []) for base in pps):
            pps.add(elem)
    if len(pps) >= max_length:
        max_length = len(pps)
        aux = sorted(list(pps))
        result.add(tuple(aux))
for elem in result:
    results.add(",".join(elem))

max_length = max(len(s) for s in results)
results = list(filter(lambda x: len(x) == max_length,results))
print(sorted(results))