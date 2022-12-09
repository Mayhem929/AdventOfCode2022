import os
import time


def read_input():
    with open("inputs/day9.txt") as file:
        lines = [line.strip() for line in file]

    return lines


# def print_mat(passed):
#     mat = ["".join(['T' if (j, i) in passed else '.' for i in range(-200, 0)]) for j in range(100,-101, -1)]
#
#     s=""
#     for i in mat:
#         s += i + "\n"
#
#     print(s)
#
#
# def print_rope(dct):
#
#     mat = [ " ".join([str(dct[(i,j)]) if (i, j) in dct.keys() else '.' for i in range(22)]) for j in range(22)]

def update_next(ihead, jhead, itail, jtail):
    rows_appart = ihead - itail
    cols_appart = jhead - jtail

    if abs(rows_appart) > 1:
        itail += int(abs(rows_appart) / rows_appart)  # truquito matematico le sumo 1 o -1 segun el signo de rows_appart
        jtail += cols_appart

    elif abs(cols_appart) > 1:
        jtail += int(abs(cols_appart) / cols_appart)
        itail += rows_appart

    return itail, jtail


def problem1():
    lines = read_input()

    passed = set()

    ihead, itail, jhead, jtail = 0, 0, 0, 0

    for line in lines:
        direction = line.split(" ")[0]
        steps = int(line.split(" ")[1])
        for i in range(steps):
            jhead += 1 if direction == 'R' else -1 if direction == 'L' else 0
            ihead += 1 if direction == 'U' else -1 if direction == 'D' else 0

            itail, jtail = update_next(ihead, jhead, itail, jtail)
            passed.add((itail, jtail))

    return len(passed)


def problem2():

    lines = read_input()
    rope = [[0,0] for i in range(10)]
    passed = set()

    for line in lines:
        direction = line.split(" ")[0]
        steps = int(line.split(" ")[1])
        for i in range(steps):
            rope[0][0] += 1 if direction == 'U' else -1 if direction == 'D' else 0
            rope[0][1] += 1 if direction == 'R' else -1 if direction == 'L' else 0

            for j in range(9):
                rope[j+1][0], rope[j+1][1] = update_next(rope[j][0], rope[j][1], rope[j + 1][0], rope[j + 1][1])

            passed.add((rope[9][0], rope[9][1]))

    print(rope)

    return len(passed)


print(problem1())
print(problem2())
