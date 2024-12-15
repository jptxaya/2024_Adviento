def all_operations(result, partial_result,numbers, list_result):
    if (len(numbers) >= 1):
        all_operations(result, partial_result + numbers[0], numbers[1:],list_result )
        all_operations(result, partial_result * numbers[0], numbers[1:],list_result )
        all_operations(result, int(str(partial_result)+str(numbers[0])), numbers[1:],list_result )
    if partial_result == result and len(numbers) == 0:
        list_result.append(True)
    return list_result





with open("data/data07.txt","r") as file:
    equations_list = []
    for elem in file.read().splitlines():
        equations_list.append(elem.split(":"))
correct_equations = 0
for equation in equations_list:
    result = int(equation[0])
    numbers = [ int(x) for x in equation[1].lstrip().split(" ")]
    result_list = []
    all_operations(result, numbers[0], numbers[1:],result_list)
    if len(result_list) >= 1:
        correct_equations += result
print(correct_equations)
