import numpy as np

def read_input():
    with open("inputs/day1.txt") as fin:
        lines = [line.strip() for line in fin]

    return lines