def problem1():
    with open("inputs/day6.txt") as f:
        line = list(f.readline())
        code_len = 4
        count = 0
        while len(line[count:count+code_len]) != len(set(line[count:count+code_len])):
            count+=1

        return count+code_len


def problem2():
    with open("inputs/day6.txt") as f:
        line = list(f.readline())
        code_len = 14
        count = 0
        while len(line[count:count+code_len]) != len(set(line[count:count+code_len])):
            count+=1

        return count+code_len


print(problem1())
print(problem2())
