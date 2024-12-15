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
#rearrange buffer
rearrange_buffer = []
i  = 0
j = len(buffer) - 1
while (i <= j):
    if buffer[i] == ".":
        rearrange_buffer.append(buffer[j])
        j -= 1
        while(buffer[j] == "."):
            j -= 1
    else:
        rearrange_buffer.append(buffer[i])
    i += 1
print(rearrange_buffer)
#Calculate checksum
checksum = 0
for i, elem in enumerate(rearrange_buffer):
    checksum += i * elem
print(checksum)

