# This file has the solution to the task aabf363d.json
from ioOps import read_file, get_file_path, print_grid
from itertools import groupby
import numpy as np
import sys

def solve(data):
    for input in data:
        colour = input[-1][0]
        input[-1][0] = 0
        input[input != 0] = colour
    return data

if __name__ == "__main__":
    inputFilePath = get_file_path(sys.argv)
    data = read_file(inputFilePath)
    grid = solve(data)
    print_grid(grid)