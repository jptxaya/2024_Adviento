import numpy as np

def get_number_direction(p_character):
    if p_character ==  "^":
        return 2
    elif p_character == ">":
        return 3
    elif p_character == "v":
        return 4
    elif p_character == "<":
       return 5
    return p_character

def change_direction(p_character):
    if p_character != 5:
        return p_character + 1
    return 2
    

def get_direction(p_character):
    calc_movement = np.zeros(2)
    if p_character ==  2:
        calc_movement = np.array([-1,0])
    elif p_character == 3:
        calc_movement = np.array([0,1])
    elif p_character == 4:
        calc_movement = np.array([1,0])
    elif p_character == 5:
        calc_movement = np.array([0,-1])
    return calc_movement

def inside_limits(position_array,guard_map):
    if (position_array[0] >= 0 and position_array[0] < len(guard_map) and position_array[1] >= 0 and position_array[1] < len(guard_map[0])):
        return True
    return False

def verify_obstacle_posibilities( p_array, n_direction):
        find_direction = change_direction(n_direction)
        m_mov = get_direction(n_direction)
        n_mov_find = get_direction(find_direction)
        while(inside_limits(p_array,guard_map)) and (guard_map[p_array[0]][p_array[1]] != 1):    
            new_array_pos = p_array
            while(inside_limits(new_array_pos,guard_map)) and (guard_map[new_array_pos[0]][new_array_pos[1]] != 1):
                if n_direction == 5 and guard_map[new_array_pos[0]][new_array_pos[1]] == find_direction:
                    result = np.sum([ p_array, m_mov], axis=0)
                    return (result[0],result[1])
                if guard_map[new_array_pos[0]][new_array_pos[1]] == find_direction:
                    result = np.sum([ p_array, m_mov], axis=0)
                    return (result[0],result[1])
                new_array_pos = np.sum([ new_array_pos, n_mov_find], axis=0)
            p_array = np.sum([ p_array, m_mov], axis=0)
        return None


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
number_direction = get_number_direction(pos_character)
#define direction
calc_movement = get_direction(number_direction)
position_array = np.array(position)

obstacles_posibilities = set()
while( inside_limits(position_array,guard_map)):
    if guard_map[position_array[0]][position_array[1]] == 1:
        position_array = np.sum([ position_array, -1 * calc_movement], axis=0)
        guard_map[position_array[0]][position_array[1]] = number_direction
        number_direction = change_direction(number_direction)
        calc_movement = get_direction(number_direction)
    elif guard_map[position_array[0]][position_array[1]] == 0:
        verify_obstacle = verify_obstacle_posibilities(position_array,number_direction)
        if verify_obstacle:
            obstacles_posibilities.add(verify_obstacle)
        guard_map[position_array[0]][position_array[1]] = number_direction
        position_array = np.sum([ position_array, calc_movement], axis=0)
        movements += 1
    else:
        verify_obstacle = verify_obstacle_posibilities(position_array,number_direction)
        if verify_obstacle:
            obstacles_posibilities.add(verify_obstacle)
        position_array = np.sum([ position_array, calc_movement], axis=0)
print(movements)
print(len(obstacles_posibilities))
print(obstacles_posibilities)

