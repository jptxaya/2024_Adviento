import re

with open("data/data19.txt") as file:
    first = True
    count_designs = 0
    for elem in file.read().splitlines():
        #contruct regex
        if first:
            num_patterns = len(elem.split(","))
            regex = "^(" + elem.replace(", ","|") +")+$"
            print(regex)
            first = False

        if re.search(regex, elem) and not first:
            count_designs += 1
print(count_designs)
        