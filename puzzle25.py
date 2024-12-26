import numpy as np

with open("data/data25.txt") as file:
    locks = []
    keys = []
    lines = file.read().splitlines()
    k = 0
    while(k < len(lines)):
        elem = lines[k]
        if elem.startswith("#"):
            lock = np.array([0,0,0,0,0])
            k += 1
            for i in range(5):
                row = list(lines[k])
                for j, cell in enumerate(row):
                    if cell == "#":
                        lock[j] += 1
                k += 1
            locks.append(lock) 
        elif elem.startswith("."):
            key = np.array([0,0,0,0,0])
            k += 1
            for i in range(5):
                row = list(lines[k])
                for j, cell in enumerate(row):
                    if cell == "#":
                        key[j] += 1
                k += 1
            keys.append(key)
        k += 1

good_pairs = 0
for lock in locks:
    for key in keys:
        fix = lock + key
        if np.amax(fix) <= 5:
            good_pairs += 1

#print(locks)
#print(keys)
print(f"Good pairs:{good_pairs}")



