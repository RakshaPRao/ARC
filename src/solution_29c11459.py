# This file has the solution to the task 29c11459.json
from ioOps import read_file, get_file_path, print_grid
import json
import sys

"""
Method to find solution for the task 29c11459.json

Args:
    data(input): The data grid to be processed

Returns:
    Output grid with a line of the colour reaching out from left and right cells and the middle cell as grey
"""
def solve(input):
    # The number associated with grey colour
    grey = 5
    for row in input:
        if row[0] != 0:
            length = len(row)
            # Finding mid cell of the row to color it grey
            midPoint = length // 2
            # getting the start color number
            startCode = row[0]
            # Getting the end color number
            endCode = row[length - 1]
            row[midPoint] = grey
            # Filling start number from beginning of row to mid of row
            row[1: midPoint] = startCode
            # Filling end color number from mid to end of row
            row[midPoint + 1: ] = endCode
    return input

if __name__ == "__main__":
    inputFilePath = get_file_path(sys.argv)
    data = read_file(inputFilePath)
    grid = []
    for input in data:
        grid.append(solve(input))
    print_grid(grid)