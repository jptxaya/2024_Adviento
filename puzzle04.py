def xmas_horizontal(matrix,i,j):
    if ("".join(matrix[i][j:j+4]) == "XMAS" ):
        return True
    return False

def xmas_horizontal_reversed(matrix,i,j):
    if ("".join(matrix[i][j-3:j+1]) == "SAMX" ):
        return True
    return False

def xmas_vertical(matrix,i,j):
    if ("".join([matrix[i][j],matrix[i+1][j],matrix[i+2][j],matrix[i+3][j]]) == "XMAS" ):
        return True
    return False

def xmas_vertical_reversed(matrix,i,j):
    if ("".join([matrix[i][j],matrix[i-1][j],matrix[i-2][j],matrix[i-3][j]]) == "XMAS" ):
        return True
    return False

def diag_11(matrix,i,j):
    if ("".join([matrix[i][j],matrix[i-1][j-1],matrix[i-2][j-2],matrix[i-3][j-3]]) == "XMAS" ):
        return True
    return False

def diag_12(matrix,i,j):
    if ("".join([matrix[i][j],matrix[i-1][j+1],matrix[i-2][j+2],matrix[i-3][j+3]]) == "XMAS" ):
        return True
    return False

def diag_21(matrix,i,j):
    if ("".join([matrix[i][j],matrix[i+1][j-1],matrix[i+2][j-2],matrix[i+3][j-3]]) == "XMAS" ):
        return True
    return False

def diag_22(matrix,i,j):
    if ("".join([matrix[i][j],matrix[i+1][j+1],matrix[i+2][j+2],matrix[i+3][j+3]]) == "XMAS" ):
        return True
    return False

def find_max(matrix,i,j):
    if (i + 2 <= len(matrix)) and (i - 2 >= -1) and (j - 2 >= -1) and (j + 2 <= len(matrix[i])):
        dig_1 = "".join([matrix[i-1][j-1],matrix[i][j],matrix[i+1][j+1]])
        dig_2 = "".join([matrix[i-1][j+1],matrix[i][j],matrix[i+1][j-1]])
        if ((dig_1 == "MAS" ) or (dig_1 == "SAM" )) and ((dig_2 == "MAS") or (dig_2 == "SAM")):
            return True
    return False


with open("data/data04.txt","r") as file:
    lista = file.read().splitlines()
matrix = []
for i in range(len(lista)):
    matrix.append(list(lista[i]))

count_xmas = 0
count_mas = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'X':
            if (j + 4 <= len(matrix[i])) and (xmas_horizontal(matrix=matrix,i=i,j=j)):
                count_xmas +=1
            if (j - 4 >= -1) and (xmas_horizontal_reversed(matrix=matrix,i=i,j=j)):
                count_xmas += 1
            if (i + 4 <= len(matrix)) and (xmas_vertical(matrix=matrix,i=i,j=j)):
                count_xmas +=1
            if (i - 4 >= -1) and (xmas_vertical_reversed(matrix=matrix,i=i,j=j)):
                count_xmas += 1
            
            if (i - 4 >= -1) and (j - 4 >= -1) and (diag_11(matrix=matrix,i=i,j=j)):
                count_xmas += 1
            if (i - 4 >= -1) and (j + 4 <= len(matrix[i])) and (diag_12(matrix=matrix,i=i,j=j)):
                count_xmas += 1
            if (i + 4 <= len(matrix)) and (j - 4 >= -1) and (diag_21(matrix=matrix,i=i,j=j)):
                count_xmas += 1
            if (i + 4 <= len(matrix)) and (j + 4 <= len(matrix[i])) and (diag_22(matrix=matrix,i=i,j=j)):
                count_xmas += 1

        elif matrix[i][j] == "A":
            if find_max(matrix,i,j):
                count_mas += 1

print(count_xmas)
print(count_mas)