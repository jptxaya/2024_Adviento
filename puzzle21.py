
import heapq

keypad = {
    "A": {"3": "^","0": "<"},
    "0": {"A": ">","2": "^"},
    "1": {"2": ">","4": "^"},
    "2": {"3": ">","5": "^","1":"<","0":"v"},
    "3": {"6": "^","2":"<","A":"v"},
    "4": {"5": ">","7": "^","1":"v"},
    "5": {"6": ">","8": "^","4":"<","2":"v"},
    "6": {"9": "^","5":"<","3":"v"},
    "7": {"8": ">","4":"v"},
    "8": {"9": ">","5":"v","7":"<"},
    "9": {"8":"<","6":"v"}
}

remote_pad = {
    "A":{"^":"<",">":"v"},
    ">":{"A":"^","v":"<"},
    "^":{"A":">","v":"v"},
    "v":{">":">","^":"^","<":"<"},
    "<":{"v":">"}
}
def get_shorted(elements):
    result = []
    minimun_length= min([len(x) for x in elements])
    result = list(filter(lambda x: len(x) == minimun_length,elements))
    return result

def djistra(pad,start,end):
    pq = []
    visited = dict()
    path = []
    heapq.heappush(pq,(0,start,path))
    routes = []
    while (len(pq) > 0):
        dist, node, path = heapq.heappop(pq)
        if node == end:
            final_route = "".join(path) + "A"
            routes.append(final_route)
            continue
        if node in visited and dist > visited[node]:
            continue
        visited[node] = dist
        for elem in pad[node]:
            next_path = []
            next_path.extend(path)
            next_path += pad[node][elem]
            heapq.heappush(pq,(len(next_path),elem,next_path))
    return routes

remote_pad_dict = dict()
keys =["A","<",">","v","^"]
for index in keys:
    remote_pad_dict[index] = dict()
    for end in list(filter(lambda x: x != index,keys)):
        routes = []
        routes = djistra(remote_pad,index,end)
        routes = get_shorted(routes)
        remote_pad_dict[index][end] = routes
    remote_pad_dict[index][index] = ["A"]


def convert_number(sequence):
    return int(sequence.replace("A", ""))

def get_sum_code(sequence):
    code = list(sequence)
    first_robot = []
    start = "A"
    first_robot = [""]
    for elem in code:
        rts = djistra(keypad,start,elem)
        rts = get_shorted(rts)
        first_robot = [ x+y for x in first_robot for y in rts]
        start = elem
#    print(first_robot)
    second_robot = []
    for elem in first_robot:
        aux = [""]
        for l_elem in list(elem):
            rts = djistra(remote_pad,start,l_elem)
            rts = get_shorted(rts)
            aux = [ x+y for x in aux for y in rts]
            start = l_elem
        second_robot.extend(aux)
    second_robot = get_shorted(second_robot)
    #print(second_robot)
    third_robot = []
    for elem in second_robot:
        aux = [""]
        for l_elem in list(elem):
            print(start,l_elem)
            rts = djistra(remote_pad,start,l_elem)
            rts = get_shorted(rts)
            aux = [ x+y for x in aux for y in rts]
            start = l_elem
        third_robot.extend(aux)
    third_robot = get_shorted(third_robot)
    length_code = len(third_robot[0])
    print(f"Sequence {sequence}:{length_code}")
    converted_number = convert_number(sequence)
    return length_code * converted_number

def get_sum_code2(sequence):
    code = list(sequence)
    first_robot = []
    start = "A"
    first_robot = [""]
    for elem in code:
        rts = djistra(keypad,start,elem)
        rts = get_shorted(rts)
        first_robot = [ x+y for x in first_robot for y in rts]
        start = elem
    num_robots = 2
    robot = first_robot
    result_robot = []
    for num_robot in range(num_robots):
        print(f"Robot:{num_robot}")
        aux_robot = []
        for elem in robot:
            aux = [""]
            start = "A"
            for l_elem in list(elem):
                rts = remote_pad_dict[start][l_elem]
                aux = [ x+y for x in aux for y in rts]
                start = l_elem
            aux_robot.extend(aux)
            aux_robot = get_shorted(aux_robot)
        robot = aux_robot
        robot = get_shorted(aux_robot)
        robot = robot
    result_robot.extend(robot)
    result_robot = get_shorted(result_robot)
    length_code = len(result_robot[0])
    print(f"Sequence {sequence}:{length_code}")
    converted_number = convert_number(sequence)
    return length_code * converted_number


#Testing
#test = get_sum_code2("980A")


with open("data/data21_test.txt") as file:
    sum_codes = 0
    for elem in file.read().splitlines():
        sum_codes += get_sum_code2(elem)

print(f"Result:{sum_codes}")

