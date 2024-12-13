import numpy as np

def change_direction(p_character):
    if p_character ==  "^":
        p_character = ">"
    elif p_character == ">":
        p_character = "v"
    elif p_character == "v":
        p_character = "<"
    elif p_character == "<":
        p_character = "^"
    return p_character

def get_direction(p_character):
    calc_movement = np.zeros(2)
    if p_character ==  "^":
        calc_movement = np.array([-1,0])
    elif p_character == ">":
        calc_movement = np.array([0,1])
    elif p_character == "v":
        calc_movement = np.array([1,0])
    elif p_character == "<":
        calc_movement = np.array([0,-1])
    return calc_movement


with open("data/data06_test.txt","r") as file:
    file_map = file.read().splitlines()

position = []
guard_map = []
pos_character = ""
#Construct map
for i,elem in enumerate(file_map):
    find_it =  elem.find("^") or elem.find(">") or elem.find("v") or elem.find("<")
    if find_it != -1:
        position = [i,find_it]
        pos_character = elem[position[1]]   
    lista = list(elem)
    new_list = list(map(lambda x:0 if x == "."  or x == pos_character else 1,lista))
    guard_map.append(new_list)

movements = 0
#define direction
calc_movement = get_direction(pos_character)
position_array = np.array(position)
print(len(guard_map))
while(position_array[0] >= 0 and position_array[0] < len(guard_map) and position_array[1] >= 0 and position_array[1] < len(guard_map[0])):
    if guard_map[position_array[0]][position_array[1]] == 1:
        position_array = np.sum([ position_array, -1 * calc_movement], axis=0)
        guard_map[position_array[0]][position_array[1]] = pos_character
        pos_character = change_direction(pos_character)
        calc_movement = get_direction(pos_character)
        print("Change direction")

    elif guard_map[position_array[0]][position_array[1]] == 0:
        guard_map[position_array[0]][position_array[1]] = pos_character
        position_array = np.sum([ position_array, calc_movement], axis=0)
        movements += 1
    else: #guard_map[position_array[0]][position_array[1]] == "X":
        position_array = np.sum([ position_array, calc_movement], axis=0)
print(movements)

