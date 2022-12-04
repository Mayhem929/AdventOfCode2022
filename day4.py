def r():
    with open("inputs/day4.txt") as file:
        lines = [line.strip() for line in file]

    return lines


def contained(a, b):
    if a[0] <= b[0] and a[1] >= b[1] or a[0] >= b[0] and a[1] <= b[1]:
        return True


def problem1():
    lines = [i.split(',') for i in r()]

    count=0
    for i in lines:
        line= [[int(j) for j in k.split('-')] for k in i]
        if contained(line[0], line[1]):
            count += 1

    return count


def overlap(a, b):
    if not (a[1] < b[0] or a[0] > b[1]):
        return True


def problem2():
    lines = [i.split(',') for i in r()]

    count = 0
    for i in lines:
        line = [[int(j) for j in k.split('-')] for k in i]
        if overlap(line[0], line[1]):
            count += 1

    return count


print(problem1())
print(problem2())
