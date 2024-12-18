def get_movement_values(movement):
    match movement:
        #movements in [y=i,x]
        case "^":
            return [-1,0]
        case "v":
            return [1,0]
        case "<":
            return [0,-1]
        case ">":
            return [0,1]

def move_block_right(block_pos, new_pos):
    seamap[new_pos[0]][new_pos[1]] = seamap[new_pos[0]][new_pos[1] - 1]
    seamap[new_pos[0]][new_pos[1] - 1] = seamap[new_pos[0]][new_pos[1] - 2]
    seamap[new_pos[0]][new_pos[1] - 2] = "."

def move_block_left(block_pos, new_pos):
    seamap[new_pos[0]][new_pos[1]] = seamap[new_pos[0]][new_pos[1] + 1]
    seamap[new_pos[0]][new_pos[1] + 1] = seamap[new_pos[0]][new_pos[1] + 2]
    seamap[new_pos[0]][new_pos[1] + 2] = "."

def move_blocks(b1,b2,b1_new,b2_new):
    seamap[b1_new[0]][b1_new[1]] = seamap[b1[0]][b1[1]]
    seamap[b2_new[0]][b2_new[1]] = seamap[b2[0]][b2[1]]
    seamap[b1[0]][b1[1]] = "."
    seamap[b2[0]][b2[1]] = "."


def move_all_blocks(mov, block_position):
    movi = [mov[0] * 2, mov[1] * 2]
    if mov == [0,-1] or mov == [0,1]:    
        b_new_pos = [block_position[0] + movi[0], block_position[1] + movi[1]]
        if seamap[b_new_pos[0]][b_new_pos[1]] != "#":
            if seamap[b_new_pos[0]][b_new_pos[1]] != ".":
                move_all_blocks(mov,b_new_pos)
            if seamap[b_new_pos[0]][b_new_pos[1]] == ".":
                if (mov[1] > 0):
                    move_block_right(block_position,b_new_pos)
                else:
                    move_block_left(block_position,b_new_pos)
    else:
        #Up down
        #Identify block
        b1 = [block_position[0], block_position[1]]
        if seamap[block_position[0]][block_position[1]] == "]":
            b2 = [block_position[0], block_position[1] - 1]
        if seamap[block_position[0]][block_position[1]] == "[":
            b2 = [block_position[0], block_position[1] + 1]
        
        b_new_pos1 = [b1[0] + mov[0], b1[1] + mov[1]]
        b_new_pos2 = [b2[0] + mov[0], b2[1] + mov[1]]

        elem_b1 = seamap[b_new_pos1[0]][b_new_pos1[1]]
        elem_b2 = seamap[b_new_pos2[0]][b_new_pos2[1]]

        if  elem_b1 != "#" and  elem_b2 != "#":
            if elem_b1 != "." or elem_b2 != ".":
                if elem_b1 != ".":
                    move_all_blocks(mov,b_new_pos1)
                if seamap[b_new_pos2[0]][b_new_pos2[1]] != "." and seamap[b_new_pos1[0]][b_new_pos1[1]] == ".":
                    move_all_blocks(mov,b_new_pos2)
            if seamap[b_new_pos1[0]][b_new_pos1[1]] == "." and seamap[b_new_pos2[0]][b_new_pos2[1]] == ".":
                move_blocks(b1,b2, b_new_pos1, b_new_pos2)


def move_robot(robot_pos, new_pos):
    seamap[new_pos[0]][new_pos[1]] = "@"
    seamap[robot_pos[0]][robot_pos[1]] = "."

def do_movements(movement, robot_pos):
    #Verify is can we do the movement
    mov = get_movement_values(movement)
    r_new_pos = [robot_pos[0] + mov[0], robot_pos[1] + mov[1]]
    if seamap[r_new_pos[0]][r_new_pos[1]] != "#":
        if seamap[r_new_pos[0]][r_new_pos[1]] != ".":
            move_all_blocks(mov, r_new_pos)
        if seamap[r_new_pos[0]][r_new_pos[1]] == ".":
            move_robot(robot_pos,r_new_pos)
            robot_pos = r_new_pos
    return robot_pos

def calculate_sum_coordinates(seamap):
    result = 0
    i = 0
    while(i<len(seamap)):
        j = 0
        while (j < len(seamap[0])):
            if seamap[i][j] == "[":
                result += 100 * i + j
            j += 1
        i += 1
    return result

def convert_map_p2( val ):
    if val == "#":
        return ["#","#"]
    elif val == ".":
        return [".","."]
    elif val == "@":
        return ["@","."]
    else:
        return ["[","]"]
    

with open("data/data15_test2.txt") as file:
    seamap = []
    movements = []
    robot_i = 0
    robot_pos = []
    for elem in file.read().splitlines():
        if elem.startswith("#"):
            map_elem = list(elem)
            #Part2
            list_elem = []
            for elem in map_elem:
                list_elem.extend(convert_map_p2(elem))
            if "@" in list_elem:
                robot_pos = [robot_i, list_elem.index("@")]
            seamap.append(list_elem)
            robot_i += 1
        elif elem.startswith("<") or elem.startswith(">") or elem.startswith("^") or elem.startswith("v"):
            movements.extend(list(elem))

for mov in movements:
    robot_pos = do_movements(mov, robot_pos)
#print(seamap)
print(calculate_sum_coordinates(seamap))
