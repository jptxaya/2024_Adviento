def change_position(buffer, i, j, changes, changed_number):
    for k in range(i,i + changes):
        buffer[k] = changed_number
    for k in range(j, j + changes):
        buffer[k] = "."


with open("data/data09.txt") as file:
    disk = list(file.readline())
disk_c = []
disk_f = []
i = 0
while(i<len(disk)):
    if (i % 2 == 0):
        disk_c.append(disk[i])
    else:
        disk_f.append(disk[i])
    i += 1

#built the String
i = 0
index = 0
buffer = []
while(i < len(disk_c)):
    for j in range(int(disk_c[i])):
        buffer.append(index)
    try:
        for j in range(int(disk_f[i])):
            buffer.append(".")
    except IndexError:
        pass
    
    index += 1
    i += 1
print(buffer)

j = len(buffer) - 1
while(j >= 0):
 conj_number = buffer[j]
 conj_number_j = j
 if conj_number != ".":
    while (conj_number == buffer[conj_number_j]):
        conj_number_j -= 1 
    necessary_j = j - conj_number_j
    i = 0
    while (i < len(buffer)) and (i < j - necessary_j):
        if ( buffer[i] == "."):
            vacio_pos = i
            while ( buffer[vacio_pos] == "."):
                vacio_pos += 1
            if vacio_pos - i >= necessary_j:
                change_position(buffer, i, conj_number_j + 1, necessary_j, conj_number)
                break
        i += 1
    j -= necessary_j
 else:
     j -= 1

print(f"R:{buffer}")


checksum = 0
for i, elem in enumerate(buffer):
    if elem != ".":
        checksum += i * elem
print(checksum)

