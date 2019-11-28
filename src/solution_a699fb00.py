# This file has the solution for the task a699fb00.json
from ioOps import read_file, print_grid, get_file_path
import json
import sys

"""
Method to find solution for the task a699fb00.json

Args:
    data(input): The input grid to be processed

Returns:
    Output grid with cell filled with red colour where the adjacent cells are blue
"""
def solve(input):
    for row in input:
        for index in range(len(row) - 2):
            # Fill 2 for very cell which has cell numbered 1 to its left and right
            if row[index] == 1 and row[index + 2] == 1:
                row[index + 1] = 2
    return input


if __name__ == "__main__":
    inputFilePath = get_file_path(sys.argv)
    data = read_file(inputFilePath)
    grid = []
    for input in data:
        grid.append(solve(input))
    print_grid(grid)
