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

def move_block(block_pos, new_pos):
    seamap[new_pos[0]][new_pos[1]] = "O"
    seamap[block_pos[0]][block_pos[1]] = "."

def move_all_blocks(mov, block_position):
    b_new_pos = [block_position[0] + mov[0], block_position[1] + mov[1]]
    if seamap[b_new_pos[0]][b_new_pos[1]] != "#":
        if seamap[b_new_pos[0]][b_new_pos[1]] != ".":
             move_all_blocks(mov,b_new_pos)
        if seamap[b_new_pos[0]][b_new_pos[1]] == ".":
            move_block(block_position,b_new_pos)   

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
            if seamap[i][j] == "O":
                result += 100 * i + j
            j += 1
        i += 1
    return result

with open("data/data15.txt") as file:
    seamap = []
    movements = []
    robot_i = 0
    robot_pos = []
    for elem in file.read().splitlines():
        if elem.startswith("#"):
            map_elem = list(elem)
            if "@" in map_elem:
                robot_pos = [robot_i, map_elem.index("@")]
            seamap.append(list(elem))
            robot_i += 1
        elif elem.startswith("<") or elem.startswith(">") or elem.startswith("^") or elem.startswith("v"):
            movements.extend(list(elem))

for mov in movements:
    robot_pos = do_movements(mov, robot_pos)
#print(seamap)
print(calculate_sum_coordinates(seamap))
