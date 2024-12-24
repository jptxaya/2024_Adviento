def do_operation(operation,gates):
    if isinstance(gates[operation[0]],int) and isinstance(gates[operation[2]],int):
        #We can solve operation
        match(operation[1]):
            case "XOR":
                return gates[operation[0]] ^ gates[operation[2]]
            case "OR":
                return gates[operation[0]] or gates[operation[2]]
            case "AND":
                return gates[operation[0]] and gates[operation[2]]
    return -1


with open("data/data24.txt") as file:
    gates = dict()
    for elem in file.read().splitlines():
        if elem.count(":") == 1:
            x_aux = elem.split(":")
            gates[x_aux[0]] = int(x_aux[1])
        elif elem.count(">"):
            x_aux = elem.split(" -> ")
            gates[x_aux[1]] = x_aux[0].split(" ")

gates_count = len(gates)
i = 0
while( i != len(gates)):
    i = 0
    for key,value in gates.items():
        if isinstance(value,int):
            i += 1
        else:
            result = do_operation(value,gates)
            if result != -1:
                gates[key] = result
                i += 1
#print(gates)
z_gates = dict((k,v) for k,v in gates.items() if k.startswith("z"))
lz_gates = sorted(z_gates,reverse=True)
print(z_gates)
print(lz_gates)
result = ""
for elem in lz_gates:
    result += str(z_gates[elem])
print(int(result,2))




