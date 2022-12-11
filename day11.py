import re
import math


def r():
    with open("inputs/day11.txt") as file:
        lines = [line.strip() for line in file]

    return lines


def problem1():
    lines = "".join(open("inputs/day11.txt").readlines()).split("\n\n")

    # get starting items
    items = []
    for line in r():
        if "Starting items" in line:
            arr = re.findall(r"\d+", line)
            items.append([int(i) for i in arr])

    monkeys = [monkey.split("\n") for monkey in lines]

    total_thrown = [0 for _ in monkeys]

    for _ in range(20):
        for i in range(len(monkeys)):
            # Parsing monkey
            add = 0
            mult = 1
            old = False
            test = 0
            true = 0
            false = 0
            for line in monkeys[i]:
                line = str(line)
                if "Operation" in line:
                    n = line.split()[-1]
                    if "*" in line and n.isdigit():
                        mult = int(n)
                    elif "+" in line:
                        add = int(n)
                    else:
                        old = True

                if "Test" in line: test = int(line.split()[-1])
                if "true" in line: true = int(line.split()[-1])
                if "false" in line: false = int(line.split()[-1])

            # Apply data to each item
            j=0
            while j < len(items[i]):
                total_thrown[i] += 1

                new = 0
                if old:
                    new = items[i][j] * items[i][j]
                else:
                    new = items[i][j] * mult + add
                new = int(new / 3)

                if new % test == 0:
                    items[true].append(new)
                else:
                    items[false].append(new)

                items[i].pop(j)


    m1 = max(total_thrown)
    total_thrown.remove(m1)
    m2 = max(total_thrown)

    return m1*m2


def problem2():
    lines = "".join(open("inputs/day11.txt").readlines()).split("\n\n")

    # get starting items
    items = []
    for line in r():
        if "Starting items" in line:
            arr = re.findall(r"\d+", line)
            items.append([int(i) for i in arr])

    monkeys = [monkey.split("\n") for monkey in lines]

    total_thrown = [0 for _ in monkeys]

    for _ in range(10000):
        total_thrown_aux = [0 for _ in monkeys]
        for i in range(len(monkeys)):
            # Parsing monkey
            add = 0
            mult = 1
            old = False
            test = 0
            true = 0
            false = 0
            for line in monkeys[i]:
                line = str(line)
                if "Operation" in line:
                    n = line.split()[-1]
                    if "*" in line and n.isdigit():
                        mult = int(n)
                    elif "+" in line:
                        add = int(n)
                    else:
                        old = True

                if "Test" in line: test = int(line.split()[-1])
                if "true" in line: true = int(line.split()[-1])
                if "false" in line: false = int(line.split()[-1])

            # Apply data to each item
            j = 0
            while j < len(items[i]):
                total_thrown[i] += 1
                total_thrown_aux[i] += 1
                new = 0
                if old:
                    new = items[i][j] * items[i][j]
                else:
                    new = items[i][j] * mult + add

                # mcm del test
                # if new > 96577:
                #     new = new%96577

                if new > 9699690:
                    new = new % 9699690

                if new % test == 0:
                    items[true].append(new)
                else:
                    items[false].append(new)

                items[i].pop(j)

    m1 = max(total_thrown)
    total_thrown.remove(m1)
    m2 = max(total_thrown)

    return m1 * m2


print(problem1())
print(problem2())
