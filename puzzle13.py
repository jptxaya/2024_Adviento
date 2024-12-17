import numpy as np

def using_numpy(a,b,r):
    e1 = np.array([[int(a[0]), int(b[0])],[int(a[1]), int(b[1])]])
    s = np.array([int(r[0]), int(r[1])]) + 10000000000000
    result = np.linalg.solve(e1,s).round()
    if (int(a[0]) * int(result[0]) + int(b[0]) * int(result[1]) == int(s[0])) and (int(a[1]) * int(result[0]) + int(b[1]) * int(result[1]) == int(s[1])):
        #Problem with decimals
        return result[0] * 3 + result[1]
    return 0

def using_loops(a,b,r):
    result_a = 0
    result_b = 0
    for i in range(101):
        for j in range(101):
            if (int(a[0]) * i + int(b[0]) * j == int(r[0])) and (int(a[1]) * i + int(b[1]) * j == int(r[1])):
                result_a = i
                result_b = j
                break
    return result_a, result_b

with open("data/data13.txt") as file:
    operations = []
    for elem in file.read().splitlines():
        operations.append(elem)
k = 0
sum_tokens = 0
correct_equations = 0
while (k < len(operations)):
    line1 = operations[k]
    line2 = operations[k+1]
    line3 = operations[k+2]
    a = line1.replace("Button A: X+","").replace(", Y+"," ").split(" ")
    b = line2.replace("Button B: X+","").replace(", Y+"," ").split(" ")
    r = line3.replace("Prize: X=","").replace(", Y="," ").split(" ")
    result_a, result_b = using_loops(a,b,r)
    #sum_tokens += 3 * result_a + result_b 
    sum_tokens += using_numpy(a,b,r)
    k += 4
print(sum_tokens)
