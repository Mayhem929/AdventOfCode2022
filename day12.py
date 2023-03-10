import sys
import os
import time

def r():
    with open("inputs/day12.txt") as file:
        lines = [line.strip() for line in file]

    return lines


class Node:
    def __init__(self, pos, parent, g, h):
        self.pos = pos
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g+h

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))


# this function returns all correct positions to go to from curr_pos
# curr_pos = tuple with current i j position
def adjacent1(mat, height, curr_pos, closed):
    closed = [(node.pos[0], node.pos[1]) for node in closed]
    result = []

    i = curr_pos[0] - 1
    j = curr_pos[1]
    if i >= 0:
        result.append((i, j))

    i = curr_pos[0] + 1
    j = curr_pos[1]
    if i < len(mat):
        result.append((i, j))

    i = curr_pos[0]
    j = curr_pos[1] - 1
    if j >= 0:
        result.append((i, j))

    i = curr_pos[0]
    j = curr_pos[1] + 1
    if j < len(mat[0]):
        result.append((i, j))

    for tp in result.copy():
        if tp in closed or mat[tp[0]][tp[1]] - height > 1:
            result.remove(tp)

    return result


path = []


def g1(parent):
    return parent.g + 1


def h1(mat, start, end):
    return mat[end[0]][end[1]] - mat[start[0]][start[1]]


count = 0
def print_path(path):

    global count
    count+=1
    mat = [['.' for _ in range(172)] for _ in range(41)]
    for node in path:
        mat[node.pos[0]][node.pos[1]] = "#"

    out = ""
    for i in mat:
        out += ("".join(i)) + "\n"

    out += "\tNum caminos explorados: " + str(count)
    out += "\n\n\n\n\n\n\n\n\n\n\n\n"

    # os.system("cls")
    print(out, end="")


def aStar1(mat, start, end):
    open, closed = [], []

    curr_node = Node(start, None, 0, h1(mat, start, end))
    open.append(curr_node)

    while end not in [node.pos for node in open] and open:

        # Calculamos el nodo de menor peso
        min_f = open[0].f
        for node in open:
            if node.f <= min_f:
                min_f = node.f
                curr_node = node

        closed.append(curr_node)
        open.remove(curr_node)

        for pos in adjacent1(mat, mat[curr_node.pos[0]][curr_node.pos[1]], curr_node.pos, closed):
            new_node = Node(pos, curr_node, g1(curr_node), h1(mat, pos, end))

            if pos not in [node.pos for node in open]:
                open.append(new_node)
                print_path(new_node.path())
            else:
                for node in open:
                    if node.pos == pos and node.g > new_node.g:
                        open.remove(node)
                        open.append(new_node)

    return len(open[-1].path()) -1


# this function returns all correct positions to go to from curr_pos
# curr_pos = tuple with current i j position
def adjacent2(mat, height, curr_pos, closed):
    closed = [(node.pos[0], node.pos[1]) for node in closed]
    result = []

    i = curr_pos[0] - 1
    j = curr_pos[1]
    if i >= 0:
        result.append((i, j))

    i = curr_pos[0] + 1
    j = curr_pos[1]
    if i < len(mat):
        result.append((i, j))

    i = curr_pos[0]
    j = curr_pos[1] - 1
    if j >= 0:
        result.append((i, j))

    i = curr_pos[0]
    j = curr_pos[1] + 1
    if j < len(mat[0]):
        result.append((i, j))

    for tp in result.copy():
        if tp in closed or height - mat[tp[0]][tp[1]] > 1:
            result.remove(tp)

    return result


def g2(parent):
    return parent.g + 1


def h2(mat, start, height):
    i = mat[start[0]][start[1]] - height
    return i


def aStar2(mat, start, height):

    open, closed = [], []

    curr_node = Node(start, None, 0, h2(mat, start, height))
    open.append(curr_node)

    while mat[curr_node.pos[0]][curr_node.pos[1]] > height and open:

        # Calculamos el nodo de menor peso
        min_f = open[0].f
        for node in open:
            if node.f <= min_f:
                min_f = node.f
                curr_node = node

        closed.append(curr_node)
        open.remove(curr_node)

        for pos in adjacent2(mat, mat[curr_node.pos[0]][curr_node.pos[1]], curr_node.pos, closed):
            new_node = Node(pos, curr_node, g2(curr_node), h2(mat, pos, height))

            if pos not in [node.pos for node in open]:
                open.append(new_node)
                print_path(new_node.path())
            else:
                for node in open:
                    if node.pos == pos and node.g > new_node.g:
                        open.remove(node)
                        open.append(new_node)

    return len(open[-1].path()) -1


def problem1():

    lines = r()

    height = 0
    start = tuple()
    end = tuple()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'S': start = (i, j)
            if lines[i][j] == 'E': end = (i, j)

    mat = [[ord(c) - 96 if c != 'S' and c != 'E' else 0 if c == 'S' else 27 for c in j] for j in lines]

    [print(i) for i in mat]
    print()

    return aStar1(mat, start, end)


def problem2():
    lines = r()

    height = 0
    start = tuple()
    end = tuple()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'S': start = (i, j)
            if lines[i][j] == 'E': end = (i, j)

    mat = [[ord(c) - 96 if c != 'S' and c != 'E' else 0 if c == 'S' else 27 for c in j] for j in lines]

    [print(i) for i in mat]
    print()

    return aStar2(mat, end, 2)


if __name__=="__main__":
    print("Problema 1:\n\n\n\n\n\n")

    time.sleep(2)

    print("\t Longitud camino mas corto:",problem1())

    print("\n")
    print("Problema 2:\n\n\n\n\n\n")
    count = 0

    time.sleep(3)

    print("\t Longitud camino mas corto:",problem2())
