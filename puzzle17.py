
def get_literal_operand(operand)->int:
    match (operand):
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return reg_a
        case 5:
            return reg_b
        case 6:
            return reg_c
        case 7:
            raise Exception("No valid operand")


def step(opcode, combo_operand, index, reg_a, reg_b, reg_c, output):
    index += 2
    match (opcode):
        case 0:
            reg_a = reg_a // (2 ** combo_operand)
        case 1:
            reg_b = reg_b ^ combo_operand
        case 2:
            reg_b = get_literal_operand(combo_operand) % 8
        case 3:
            if reg_a != 0:
                index = combo_operand
        case 4:
            reg_b = reg_b ^ reg_c
        case 5:
             val = str(get_literal_operand(combo_operand) % 8)
             if len(output) == 0:
                output = str(val)
             else:
                output += f',{val}'
        case 6:
            reg_b = reg_a // (2 ** get_literal_operand(combo_operand))
        case 7:
            reg_c = reg_a // (2 ** get_literal_operand(combo_operand))
    return reg_a, reg_b, reg_c, index, output   



reg_a, reg_b, reg_c = 0,0,0
programs = []
with open("data/data17.txt") as file:
    for elem in file.read().splitlines():
        if "A" in elem:
            reg_a = int(elem.split(": ")[1])
        if "B" in elem:
            reg_b = int(elem.split(": ")[1])
        if "C" in elem:
            reg_c = int(elem.split(": ")[1])
        if "Program:" in elem:
            programs = list(map(int, elem.split(": ")[1].split(",")))

print(reg_a,reg_b,reg_c)
print(programs)

index = 0
output = ""

while(index < len(programs)):
   reg_a, reg_b, reg_c, index, output = step(programs[index], programs[index + 1], index=index,reg_a=reg_a, reg_b=reg_b,reg_c=reg_c,output=output)

print(f"Reg_a:{reg_a}")
print(f"Reg_b:{reg_b}")
print(f"Reg_c:{reg_c}")
print(f"output:{output}")

