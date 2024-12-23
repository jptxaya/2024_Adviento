import copy

def evaluate_1(lista_numeros)-> bool:
    direction = False
    if lista_numeros[0] < lista_numeros[1]:
        direction = True
    for i in range(len(lista_numeros)-1):
        difference = abs(lista_numeros[i] - lista_numeros[i+1])
        if direction:
            if (lista_numeros[i] >= lista_numeros[i+1]) or difference not in [1,2,3]:
                return False
        else:
            if (lista_numeros[i] <= lista_numeros[i+1]) or difference not in [1,2,3]:
                return False
    return True

def evaluate_direction(lista_numeros)-> bool:
    #Ascending value True
    count_incr = 0
    count_decr = 0
    for i in range(len(lista_numeros)-1):
        if lista_numeros[i] < lista_numeros[i+1]:
            count_incr += 1
        elif lista_numeros[i] > lista_numeros[i+1]:
            count_decr += 1
    if count_decr > count_incr:
        return False
    return True

def evaluate_2(lista_numeros)-> bool:
    i = 0
    while i < len(lista_numeros):
        aux_lista = copy.deepcopy(lista_numeros)
        aux_lista.pop(i)
        if evaluate_1(aux_lista):
            return True
        i += 1
    return False

safe_reports_1 = 0
safe_reports_2 = 0
errors = 0
with open("data/data02.txt","r") as file:
    for line in file:
        lista = list(map(int,line.split(" ")))
        if evaluate_1(lista):
            safe_reports_1 += 1
            safe_reports_2 += 1
        elif evaluate_2(lista):
            #print(f"A {lista}")
            safe_reports_2 += 1
        else:
            #print(f"E {lista}")
            errors += 1
print(f"Solution1:{safe_reports_1}")
print(f"Solution2:{safe_reports_2}")
print(f"Solution2:{errors}")