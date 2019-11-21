#This file has the solution to the task 746b3537.json
from ioOps import read_file, get_file_path, print_grid
from itertools import groupby
import numpy as np
import sys

"""

"""

def solve(data):
    # For each input grid
    output_list = []
    for input in data:
        input_list = input.tolist()
        row = input_list[0]
        column = [a[0] for a in input_list]
        row = [k for k, g in groupby(row) if k != 0]
        column = [k for k, g in groupby(column) if k != 0]
        if len(row) == 1:
            column_list = []
            for i in column:
                column_list.append([i])
            output_list.append(column_list)
        else:
            output_list.append([row])
    return output_list

if __name__ == "__main__":
    inputFilePath = get_file_path(sys.argv)
    data = read_file(inputFilePath)
    grid = solve(data)
    print_grid(grid)