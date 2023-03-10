import re
import time


def r():
    with open("inputs/day14.txt") as file:
        lines = [line.strip() for line in file]

    return lines


# version lenta usando listas
def next_sand1(rocks, start, sand):

    curr_pos = start

    lowest_rock = max([i[0] for i in rocks])

    while curr_pos[0] < lowest_rock:

        if (curr_pos[0]+1, curr_pos[1]) not in (rocks + sand):
            curr_pos = (curr_pos[0]+1, curr_pos[1])
        elif (curr_pos[0]+1, curr_pos[1]-1) not in (rocks + sand):
            curr_pos = (curr_pos[0]+1, curr_pos[1]-1)
        elif (curr_pos[0]+1, curr_pos[1]+1) not in (rocks + sand):
            curr_pos = (curr_pos[0]+1, curr_pos[1]+1)
        else:
            return curr_pos, True


    return curr_pos, False


# version rapida usando un diccionario como grid
def next_sand2(grid, start):

    curr_pos = start

    while curr_pos[0] < 169:

        if grid[(curr_pos[0] + 1, curr_pos[1])] == '.':
            curr_pos = (curr_pos[0]+1, curr_pos[1])
        elif grid[curr_pos[0] + 1, curr_pos[1] - 1] == '.':
            curr_pos = (curr_pos[0]+1, curr_pos[1]-1)
        elif grid[curr_pos[0] + 1, curr_pos[1] + 1] == '.':
            curr_pos = (curr_pos[0]+1, curr_pos[1]+1)
        else:
            return curr_pos

    return curr_pos


def print_grid(grid):

    out = ""
    for i in range(0,150):
        for j in range(480, 650):
            out += grid[(i, j)]

        out+= "\n"

    print(out)


def problem1():
    lines = r()

    rock_lines = []
    index = 0
    for line in lines:
        rock_lines.append([])
        for pair in re.findall(r"\d+,\d+", line):
            new_pair = [int(i) for i in pair.split(",")]
            new_pair.reverse()
            rock_lines[index].append(new_pair)
        index += 1

    rocks = []
    index = 0

    for rock_line in rock_lines:
        for i in range(len(rock_line)-1):
            if rock_line[i][0] == rock_line[i+1][0]:
                for j in range(min(rock_line[i][1], rock_line[i+1][1]), max(rock_line[i][1], rock_line[i+1][1])+1):
                    rocks.append((rock_line[i][0], j))

            if rock_line[i][1] == rock_line[i+1][1]:
                for j in range(min(rock_line[i][0], rock_line[i+1][0]), max(rock_line[i][0], rock_line[i+1][0])+1):
                    rocks.append((j, rock_line[i][1]))

    rocks = set(rocks)
    rocks = list(rocks)
    print("Total rocks: ", len(rocks))

    source = (0, 500)
    sand = []

    go_on = True
    count = 0
    while go_on:
        count+=1
        next, go_on = next_sand1(rocks, source, sand)
        sand.append(next)

        if count%500 == 0:
            mat = [["#" if (i, j) in rocks else "o" if (i, j) in sand else "." for j in range(480, 650)] for i in
                   range(0, 200)]
            for i in mat:
                print("".join(i))
            print(count)

    mat = [["#" if (i,j) in rocks else "o" if (i,j) in sand else "." for j in range(480, 650)] for i in range(0, 200)]
    for i in mat:
        print("".join(i))

    return count


def problem2():

    lines = r()

    rock_lines = []
    index = 0
    for line in lines:
        rock_lines.append([])
        for pair in re.findall(r"\d+,\d+", line):
            new_pair = [int(i) for i in pair.split(",")]
            new_pair.reverse()
            rock_lines[index].append(new_pair)
        index += 1


    grid = {}
    for i in range(500):
        for j in range(0, 1000):
            grid[(i, j)] = '.'

    grid[(0, 500)] = "S"

    # print_grid(grid)

    index = 0

    for rock_line in rock_lines:
        for i in range(len(rock_line)-1):
            if rock_line[i][0] == rock_line[i+1][0]:
                for j in range(min(rock_line[i][1], rock_line[i+1][1]), max(rock_line[i][1], rock_line[i+1][1])+1):
                    grid[(rock_line[i][0], j)] = "#"

            if rock_line[i][1] == rock_line[i+1][1]:
                for j in range(min(rock_line[i][0], rock_line[i+1][0]), max(rock_line[i][0], rock_line[i+1][0])+1):
                    grid[(j, rock_line[i][1])] = "#"



    source = (0, 500)

    go_on = True
    count = 0
    while go_on:
        count+=1
        next = next_sand2(grid, source)

        if next == source:
            go_on = False

        grid[next] = 'o'
        if count%2000 == 0:
            print_grid(grid)
            print(count)

    print_grid(grid)
    return count


print(problem1())
time.sleep(3)
print("\n")
print("problem2: ")
print(problem2())