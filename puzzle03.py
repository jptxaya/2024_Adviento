import re
with open("data/data03.txt","r") as file:
    lista = []
    for line in file:
        lista.extend(re.findall("(?:mul\(\d{1,3},\d{1,3}\))",line))
    #lista = file.readlines()#re.findall("(?:mul\(\d{1,3},\d{1,3}\))",file.readlines())
sum_mul = 0
for elem in lista:
    list_elem= elem.split(",")
    sum_mul += int(list_elem[0].replace("mul(","")) * int(list_elem[1].replace(")",""))
print(f"Solution1:{sum_mul}")


#Part 2
with open("data/data03.txt","r") as file:
    lista = []
    for line in file:
        lista.extend(re.findall("(?:mul\(\d{1,3},\d{1,3}\))|(?:do\(\))|(?:don\'t\(\))",line))
activated = True
sum_mul = 0
for elem in lista:
    if elem.startswith("mul(") and activated:
        list_elem= elem.split(",")
        sum_mul += int(list_elem[0].replace("mul(","")) * int(list_elem[1].replace(")",""))
    elif elem == "do()":
        activated = True
    else:
        activated = False
print(f"Solution_2:{sum_mul}")
    