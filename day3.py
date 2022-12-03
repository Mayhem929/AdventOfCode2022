def r():
    with open("inputs/day3.txt") as file:
        lines = [line.strip() for line in file]

    return lines


def problem1():
    lines = r()
    prio=0

    for line in lines:
        part1= line[:int(len(line)/2)]
        part2= line[int(len(line)/2):]

        repeated = ''
        for i in part1:
            if i in part2:
                repeated = i

        prio += (ord(repeated)-ord('a')+1 if repeated.lower()==repeated else ord(repeated)-ord('A')+27)

    return prio


def problem2():
    lines = r()
    lines = [[lines[i],lines[i+1],lines[i+2]] for i in range(0, len(lines), 3)]

    print(lines)
    prio = 0

    for trio in lines:

        repeated = ''
        for i in trio[0]:
            if i in trio[1] and i in trio[2]:
                repeated = i

        prio += (ord(repeated) - ord('a') + 1 if repeated.lower() == repeated else ord(repeated) - ord('A') + 27)

    return prio


print(problem1())
print(problem2())