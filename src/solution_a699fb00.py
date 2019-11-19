# This file will have the solution for the task a699fb00
from ioOps import read_file, print_grid, get_file_path
import json
import sys

"""
Method to find solution for the task a699fb00.json

Args:
    data(list): The data which needs to be processed

Returns:
    Solution for the task
"""
def solve(data):
    # For every input grid
    for input in data:
        for row in input:
            for index in range(len(row) - 2):
                # Fill 2 for wvery cell which has cell numbered 1 to its left and right
                if row[index] == 1 and row[index + 2] == 1:
                    row[index + 1] = 2
    return data

if __name__ == "__main__":
    inputFilePath = get_file_path(sys.argv)
    data = read_file(inputFilePath)
    grid = solve(data)
    print_grid(grid)
