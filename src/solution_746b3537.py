# This file has the solution to the task 746b3537.json
from ioOps import read_file, get_file_path, print_grid
from itertools import groupby
import numpy as np
import sys

"""
Method to find solution for the task 746b3537.json

Args:
    data(input): The input grid to be processed
    
Returns:
    The unique colour in the form of row-array or column-array based on how they appear in the input grid 
"""
def solve(input):
    input_list = input.tolist()
    # Getting the first row and the column array for easy processing
    row = input_list[0]
    column = [a[0] for a in input_list]

    # Finding the unique colours in row and the column to reduce one of the two to a single cell
    row = [k for k, g in groupby(row) if k != 0]
    column = [k for k, g in groupby(column) if k != 0]

    # Returning the array with unique colours for the input
    if len(row) == 1:
        column_list = []    # Creating a column array if the unique colours are in the column of the grid
        for i in column:
            column_list.append([i])
        return column_list
    else:
        return [row]

if __name__ == "__main__":
    inputFilePath = get_file_path(sys.argv)
    data = read_file(inputFilePath)
    grid = []
    for input in data:
        grid.append(solve(input))
    print_grid(grid)