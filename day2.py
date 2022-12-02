def r():
    with open("inputs/day2.txt") as fin:
        lines = [line.strip() for line in fin]

    return lines


def problem1():
    guide = r()
    total = 0
    for i in guide:
        if 'A Y' in i or 'B Z' in i or 'C X' in i:
            total += 6
        if 'A X' in i or 'B Y' in i or 'C Z' in i:
            total += 3
        if 'X' in i: total += 1
        if 'Y' in i: total += 2
        if 'Z' in i: total += 3

    return total


def problem2():
    guide = r()

    dct = {'A Z': 8, 'A Y': 4, 'A X': 3,
           'B Z': 9, 'B Y': 5, 'B X': 1,
           'C Z': 7, 'C Y': 6, 'C X': 2}

    total = 0
    for i in guide:
        total += dct[i]
    return total


def version_corta_p1():
    d={'A Z':3,'A Y':8,'A X':4,'B Z':9,'B Y':5,'B X':1,'C Z':6,'C Y':2,'C X':7};return sum(list(map(lambda i:d[i],r())))


def version_corta_p2():
    d={'A Z':8,'A Y':4,'A X':3,'B Z':9,'B Y':5,'B X':1,'C Z':7,'C Y':6,'C X':2};return sum(list(map(lambda i:d[i],r())))


print(problem1())
print(version_corta_p1())
print(problem2())
print(version_corta_p2())
