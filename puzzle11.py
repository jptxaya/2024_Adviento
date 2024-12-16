def blink_process(list_numbers):
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


def blink(lnumbers, times,executed_times):
    sum = 0
    if executed_times == times:
        return len(lnumbers)
    else:
        new_list = blink_process(lnumbers)
        for elem in new_list:
            sum += blink([elem],times,executed_times + 1)
    return sum

with open("data/data11.txt") as file:
    numbers = [int(x) for x in file.read().splitlines()[0].split(" ")]
#for i in range(5):
count = 0
count = blink(numbers,75,0)
print(count)