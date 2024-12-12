import os
import pandas as pd
import collections

lista0 = []
lista1 = []
with open("data/data01.txt") as file:
    for line in file:
        line_object = line.split("   ")
        lista0.append(int(line_object[0]))
        lista1.append(int(line_object[1]))
lista0.sort()
lista1.sort()
sum = 0
for i in range(len(lista0)):
    sum += abs(lista0[i] - lista1[i])
print(f"Solution1:{sum}")
#Part 2
set_lista0 = set(lista0)
c0 = collections.Counter(lista0)
c1 = collections.Counter(lista1)
sum_similarity = 0
for elem in set_lista0:
    sum_similarity += elem * c1.get(elem,0)
print(f"Solution2:{sum_similarity}")