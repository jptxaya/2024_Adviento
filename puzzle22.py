def mix(secret_number, given_value):
    return given_value ^ secret_number

def prune(secret_number):
    if secret_number == 100000000:
        return 16113920
    aux = secret_number % 16777216
    return aux

def sequences(secret_number, sequence):
    value = 0
    match(sequence):
        case 0:
            value = secret_number * 64
        case 1:
            value = secret_number // 32
        case 2:
            value = secret_number * 2048
    return (prune(mix(secret_number=secret_number,given_value=value)))
#Testing
#print(mix(42,15))
#buyers = [1,10,100,2024]

buyers = []
with open("data/data22.txt") as file:
    for elem in file.read().splitlines():
        buyers.append(int(elem))


sum = 0
for val in buyers:
    for i in range(2000):
        for sequence in range(3):
            val = sequences(val,sequence)
    #print(val)
    sum += val
print(sum)
