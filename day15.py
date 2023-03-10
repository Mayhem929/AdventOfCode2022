import re

def r():
    with open("inputs/day15.txt") as file:
        lines = [line.strip() for line in file]

    return lines


def norm1(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


def problem1():

    lines = r()
    no_beacon = set()
    count = 0
    for line in lines:

        s2, s1, b2, b1 = re.findall(r"\d+", line)

        s2, s1, b2, b1 = int(s2), int(s1), int(b2), int(b1)

        sensor = (s1, s2)
        beacon = (b1, b2)

        # print("Norma: ", norm1(sensor, beacon))

        dist = norm1(sensor, beacon) - abs(s1 - 2000000)

        # print("casillas ocupadas en x=10: ", dist)

        if dist >= 0:
            for i in range(s2-dist, s2+dist+1):
                no_beacon.add(i)
                count+=1
                # print("times tried to add:", count)
                # print("times added: ", len(no_beacon))

    print("Total tries to add: ", count)
    return len(no_beacon)


def problem2():
    return


print(problem1())
print(problem2())