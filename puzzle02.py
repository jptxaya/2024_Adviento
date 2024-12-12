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
    direction = False
    credits = True
    #direction = evaluate_direction(lista_numeros)
    if lista_numeros[0] < lista_numeros[1]:
        direction = True
    i=0
    j=1
    text = ""
    while(j <= len(lista_numeros)-1 ):
        difference = abs(lista_numeros[i] - lista_numeros[j])
        if (lista_numeros[i] == lista_numeros[j]):
            if credits:
                text = text + "Equal"
                credits = False
                i = j
                j += 1
            else:
                #print(f"EQ{lista_numeros} {text}")
                return False
        elif difference not in [1,2,3]:
            print(f"{lista_numeros} {i} {j}")
            #We have to choice what is the best option
            if i == 0:
                if abs(lista_numeros[i] - lista_numeros[j+1]) in [1,2,3] or abs(lista_numeros[i+1] - lista_numeros[j+1]) in [1,2,3]:
                    if credits:
                        credits = False
                        i = j+1
                        j = j+2
                    else:
                        return False
                else:
                    return False
            elif j <= len(lista_numeros) - 2:
                if abs(lista_numeros[i] - lista_numeros[j+1]) in [1,2,3]:
                    if credits:
                        credits = False
                        i = j+1
                        j = j+2
                    else:
                        return False
                else:
                    return False
            elif j == len(lista_numeros) - 1:
                if credits:
                    return True
                else:
                    #print(f"hello {lista_numeros}")
                    return False
        else:
            if direction:
                if (lista_numeros[i] > lista_numeros[j]):
                    if not credits:
                        #print(f"EWD{lista_numeros} {text}")
                        return False
                    else:
                        text = text + "WD"
                        credits = False
                        j +=1
                else:
                    i = j
                    j += 1
            else:
                if (lista_numeros[i] < lista_numeros[j]):
                    if not credits:
                        #print(f"EWD{lista_numeros} {text}")
                        return False
                    else:
                        text = text + "WD"
                        credits = False
                        j +=1
                else:
                    i = j
                    j += 1
                        

    print(f"C {lista_numeros}")
    return True

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