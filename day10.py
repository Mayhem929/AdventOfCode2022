def r():
    with open("inputs/day10.txt") as file:
        lines = [line.strip() for line in file]

    return lines


def problem1():
    lines = r()

    cycles = 0
    x = 1
    strengths = list()

    for line in lines:
        if "addx" in line:
            cycles += 2
            if (cycles - 20) % 40 == 0:
                strengths.append(cycles * x)
            if (cycles - 20) % 40 == 1:
                strengths.append((cycles-1) * x)

            x += int(line.split(" ")[1])
        else:
            cycles += 1
            if (cycles - 20) % 40 == 0:
                print(cycles)
                strengths.append(cycles * x)

    return sum(strengths)


def problem2():
    lines = r()

    cycles = 0
    x = 1

    crt = ""
    length=0

    for line in lines:
        if "addx" in line:

            for _ in range(2):
                if x-1 <= length <= x+1:
                    crt += "#"
                else:
                    crt += "."
                length += 1
                if length >= 40:
                    length = length%40
                    crt += "\n"

            cycles += 2

            x += int(line.split(" ")[1])
        else:
            cycles += 1
            if x - 1 <= length <= x + 1:
                crt += "#"
            else:
                crt += "."
            length += 1
            if length >= 40:
                length = length % 40
                crt += "\n"

    return crt


print(problem1())
print(problem2())
PGHFGLUG