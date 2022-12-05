import re


def read_input():
    lines = open("inputs/day5.txt").readlines()
    return lines


def problem1():

    lines = read_input()

    data = lines[:8]
    data.reverse()
    instruct = lines[10:]

    index = 0
    piles = []
    for i in range(9):
        piles.append([])

    for line in data:
        for j in range(1, 34, 4):
            if line[j] != " ":
                piles[index].append(line[j])
            index+=1
        index=0

    instruct = lines[10:]
    for i in instruct:
        n = re.findall(r"[0-9]+", i)
        n = [int(i) for i in n]
        # move 3 from 9 to 7
        #    n[0]   n[1] n[2]

        index1 = n[1]-1
        index2 = n[2]-1

        for j in range(n[0]):
            piles[index2].append(piles[index1][-1])
            piles[index1].pop()

    out=""
    for pile in piles:
        out += str(pile[-1])
    return out


def problem2():
    lines = open("inputs/day5.txt").readlines()

    data = lines[:8]
    data.reverse()
    index = 0
    piles = []
    for i in range(9):
        piles.append([])

    for line in data:

        for j in range(1, 34, 4):
            if line[j] != " ":
                piles[index].append(line[j])
            index+=1
        index=0


    instruct = lines[10:]
    for i in instruct:
        n = re.findall(r"[0-9]+", i)
        n = [int(i) for i in n]
        # move 3 from 9 to 7
        #    n[0]   n[1] n[2]

        index1 = n[1]-1
        index2 = n[2]-1
        piles[index2] += piles[index1][-n[0]:]

        for j in range(n[0]):
            piles[index1].pop()

    out=""
    for pile in piles:
        out += str(pile[-1])

    return out


print(problem1())
print(problem2())