import numpy as np

def read_input():
    with open("inputs/day1.txt") as fin:
        lines = [line.strip() for line in fin]

    return lines


def problem1():
    input = read_input()

    index = 0
    elfs = [0]
    for value in input:
        if value:
            elfs[index] += int(value)
        else:
            index += 1
            elfs.append(0)

    return max(elfs)


def problem2():
    input = read_input()

    index = 0
    elfs = [0]
    for value in input:
        if value == "":
            index += 1
            elfs.append(0)
        else:
            elfs[index] += int(value)

    sum = 0
    for value in range(3):
        max_kal = max(elfs)
        sum += max_kal
        elf = elfs.index(max_kal)
        # print(max, elf+1)
        elfs.pop(elf)

    return sum


print(problem1())
print(problem2())
