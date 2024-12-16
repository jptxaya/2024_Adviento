def blink(list_numbers)->list:
    new_list = []
    for elem in list_numbers:
        if elem == 0:
            new_list.append(1)
        elif len(str(elem)) % 2 == 0:
            new_list.append(int(str(elem)[:len(str(elem)) // 2]))
            new_list.append(int(str(elem)[(len(str(elem)) // 2):])) 
        else:
            new_list.append(elem * 2024)
    return new_list


with open("data/data11.txt") as file:
    numbers = [int(x) for x in file.read().splitlines()[0].split(" ")]
for i in range(75):
    numbers = blink(numbers)
print(len(numbers))