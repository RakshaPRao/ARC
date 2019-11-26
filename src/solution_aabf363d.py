# This file has the solution to the task aabf363d.json
from ioOps import read_file, get_file_path, print_grid
from itertools import groupby
import numpy as np
import sys

"""
Method to find solution for the task aabf363d.json

Args:
    data(input): The input grid to be processed

Returns:
    Output grid with all the non black cells filled with the colour on the lower-most left cell and re-colouring the lower-most left cell to black
"""
def solve(input):
    input[input != 0] = input[-1][0]
    input[-1][0] = 0
    return input

if __name__ == "__main__":
    inputFilePath = get_file_path(sys.argv)
    data = read_file(inputFilePath)
    grid = []
    for input in data:
        grid.append(solve(input))
    print_grid(grid)