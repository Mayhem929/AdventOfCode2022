def r():
    with open("inputs/day8.txt") as file:
        lines = [line.strip() for line in file]

    return lines


def is_visible(mat, i, j):
    # debug
    # r1 = mat[i][:j]
    # r2 = mat[i][j+1:]
    # c1 = [row[j] for row in mat][i+1:]
    # c2 = [row[j] for row in mat][:i]

    height = mat[i][j]
    if height > max(mat[i][:j]) or \
            height > max(mat[i][j + 1:]) or \
            height > max([row[j] for row in mat][i + 1:]) or \
            height > max([row[j] for row in mat][:i]):
        return True
    else:
        return False


def scenic_score(mat, i, j):
    height = mat[i][j]
    r1, r2, c1, c2 = 0, 0, 0, 0

    tmp_j = j+1
    while 0 <= tmp_j < len(mat):
        r1 += 1
        if mat[i][tmp_j] >= height: break
        tmp_j+=1

    tmp_j = j-1
    while 0 <= tmp_j < len(mat):
        r2 += 1
        if mat[i][tmp_j] >= height: break
        tmp_j -= 1

    tmp_i = i+1
    while 0 <= tmp_i < len(mat):
        c1 += 1
        if mat[tmp_i][j] >= height: break
        tmp_i += 1

    tmp_i = i-1
    while 0 <= tmp_i < len(mat):
        c2 += 1
        if mat[tmp_i][j] >= height: break
        tmp_i -= 1

    # print(r1,r2,c1,c2)
    return r1*r2*c1*c2


def problem1():
    mat = [[int(i) for i in line] for line in r()]

    count = len(mat) * 4 - 4
    # print(len(mat), len(mat[0]), count)

    for i in range(1, len(mat[0]) - 1):
        for j in range(1, len(mat) - 1):
            if is_visible(mat, i, j):
                count += 1

    return count


def problem2():
    mat = [[int(i) for i in line] for line in r()]

    m = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            score = scenic_score(mat, i, j)
            if score > m:
                m = score

    return m


print(problem1())
print(problem2())
