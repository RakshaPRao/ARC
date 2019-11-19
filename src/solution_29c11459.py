#This file has the solution to the task 29c11459.json

from ioOps import read_file, get_file_path, print_grid
import json
import sys

"""
Provides solution for the task 29c11459.json

Args:
    data(list): The data which needs to be processed

Returns:
    Solution for the input data
"""
def solve(data):
    # The number associated with grey color
    grey = 5
    for input in data:
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
    return data

if __name__ == "__main__":
    inputFilePath = get_file_path(sys.argv)
    data = read_file(inputFilePath)
    grid = solve(data)
    print_grid(grid)