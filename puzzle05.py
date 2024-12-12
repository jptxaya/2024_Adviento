import math
import numpy as np

def validate_rules_not_passed(update):
    i = 0
    while(i < len(update)):
        eval_number = update[i]
        for j in range(i+1,len(update)):    
            if update[j] in rules:
                if eval_number  not in rules[update[j]]:
                    return False
            else:
                print(update)
                return False
        i += 1
    return True

def order_update(update):
    new_order = np.zeros(len(update))
    for elem in update:
        points = 0
        if elem in rules_back:
            for elem_eval in update:
                if elem_eval != elem:
                    if elem_eval in rules_back[elem]:
                        points += 1
        new_order[points] = elem
    return new_order

rules = {}
rules_back = {}
updates = []

with open("data/data05.txt") as file:
    for elem in file.read().splitlines():
        if str(elem).__contains__("|"):
            rule = elem.split("|")
            if rule[1] not in rules:
                rules[rule[1]] = [rule[0]]
            else:
                rules[rule[1]].append(rule[0])
            if rule[0] not in rules_back:
                rules_back[rule[0]] = [rule[1]]
            else:
                rules_back[rule[0]].append(rule[1])
        elif str(elem).__contains__(","):
            updates.append(elem.split(","))
#print(rules)
#print(updates)
sum_valids = 0
sum_no_valids = 0
for update in updates:
    valid = validate_rules_not_passed(update)
    if valid:
        index = math.ceil(len(update) / 2) - 1
        sum_valids += int(update[index])
    else:
        ordered_update = order_update(update)
        index = math.ceil(len(ordered_update) / 2) - 1
        sum_no_valids += ordered_update[index]
print(sum_valids)
print(sum_no_valids)