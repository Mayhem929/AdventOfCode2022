def r():
    with open("inputs/day7.txt") as file:
        lines = [line.strip() for line in file]

    return lines


def get_file_system():
    lines = r()
    system = {}
    current_path = "/"
    paths = []
    for line in lines:
        if "$ cd .." == line:
            current_path = current_path[:current_path[:-1].rindex("/") + 1]
        elif "$ cd" in line:
            if "$ cd /" != line:
                current_path += line.split(" ")[2] + "/"
            paths.append(current_path)
            system[current_path] = 0
        # en vez de guiarme por las lineas de dir con los cd es suficiente
        elif "dir" in line or "$ ls" in line:
            pass
        # cada vez que añade el tamaño de un archivo lo añade a todos sus
        # antecesores
        else:
            to_add = int(line.split(" ")[0])
            for path in paths:
                if path in current_path:
                    system[path] += to_add

    return system


def problem1():
    system = get_file_system()
    sum = 0
    for path, size in system.items():
        if size < 100000:
            sum += size

    return sum


def problem2():
    system = get_file_system()
    needed = 30000000 - 70000000 + system["/"]

    candidates = {}
    for path, size in system.items():
        if size >= needed:
            candidates[path] = size

    return min(candidates.values())


print(problem1())
print(problem2())
