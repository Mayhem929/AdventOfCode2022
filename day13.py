import ast
import json


def r():
    with open("inputs/day13.txt") as file:
        lines = [line.strip() for line in file]

    return lines


def compare(list1, list2):

    if not list1:
        return 1
    if not list2:
        return -1
    if list1 == list2:
        return 0

    if type(list1) is int and type(list2) is int:
        if list1 < list2:
            return 1
        elif list1 > list2:
            return -1
        else:
            return 0

    if type(list1) is int and type(list2) is list:
        res = compare([list1], list2)
        return res

    if type(list1) is list and type(list2) is int:
        res = compare(list1, [list2])
        return res

    i = 0
    while i < min(len(list1), len(list2)):
        res = compare(list1[i], list2[i])
        if res != 0:
            return res
        i+=1

    if len(list1) < len(list2):
        return 1
    elif len(list1) > len(list2):
        return -1
    else:
        return 0



def problem1():

    lines = r()
    data = []
    for line in lines:
        if line != "":
            dct = json.loads(line)
            data.append(dct)

    correct = []
    for i in range(0, len(data), 2):
        if 0 < compare(data[i], data[i+1]) <= 1:
            correct.append(int(i/2 +1))

    print(correct)
    return sum(correct)



print(problem1())

