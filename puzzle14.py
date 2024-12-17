import numpy as np

with open("data/data14.txt") as file:
    list_robots = []
    for elem in file.read().splitlines():
        robot = elem.split(" ")
        robot_position = [int(x.replace("p=","")) for x in robot[0].split(",")]
        robot_movement = [int(x.replace("v=","")) for x in robot[1].split(",")]
        num_movements = 100
        robot_new_position = np.array([robot_position[0],robot_position[1]],dtype=int) + num_movements * np.array([robot_movement[0],robot_movement[1]],dtype=int)
        list_robots.append([(robot_new_position[0] % 101),(robot_new_position[1] % 103)])
print(list_robots)
lista_robots = list(filter(lambda x: (x[0] != 50) and (x[1] != 51),list_robots))
print(lista_robots)
sub_div1 = list(filter(lambda x: (x[0] < 50) and (x[1] < 51),list_robots))
sub_div2 = list(filter(lambda x: (x[0] > 50) and (x[1] < 51),list_robots))
sub_div3 = list(filter(lambda x: (x[0] < 50) and (x[1] > 51),list_robots))
sub_div4 = list(filter(lambda x: (x[0] > 50) and (x[1] > 51),list_robots))
result= len(sub_div1) * len(sub_div2) * len(sub_div3) * len(sub_div4)
print(result)