import numpy as np

def calculate_plot(type,i,j):
    area_perimeter = np.array([0,0])
    if type == garden[i][j]:
        area_perimeter += np.array([1,0])
        garden[i][j] = "-" + garden[i][j]
        if ( i - 1 >= 0 ) and (garden[i-1][j] == type):
            area_perimeter += calculate_plot(type, i-1,j)
        elif ( i - 1 < 0) or (type not in garden[i-1][j]):
            area_perimeter += np.array([0,1])
        
        if ( j + 1 < len(garden[0]) ) and (garden[i][j + 1] == type):
            area_perimeter += calculate_plot(type, i,j + 1)
        elif (j + 1 >= len(garden[0])) or (type not in garden[i][j + 1]):
            area_perimeter += np.array([0,1])
        
        if ( i + 1 < len(garden) ) and (garden[i+1][j] == type):
            area_perimeter += calculate_plot(type, i+1,j)
        elif (i + 1 >= len(garden)) or (type not in garden[i+1][j]):
            area_perimeter += np.array([0,1])
        
        if ( j - 1 >= 0 ) and (garden[i][j - 1] == type):
            area_perimeter += calculate_plot(type, i,j - 1)
        elif ( j - 1 < 0 ) or (type not in garden[i][j - 1]):
            area_perimeter += np.array([0,1])
    return area_perimeter


with open("data/data12.txt") as file:
    garden = []
    for elem in file.read().splitlines():
        garden.append(list(elem))
i = 0
price_cost = 0
while(i < len(garden)):
    j = 0
    while (j < len(garden[0])):
        if "-" not in garden[i][j]:
            plot_cost = calculate_plot(garden[i][j],i, j)
            price_cost += (plot_cost[0] * plot_cost[1])
        j += 1
    i += 1
print(price_cost)