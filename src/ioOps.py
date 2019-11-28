import numpy as np
import json
import itertools
from sys import exit

"""
This method gets the file path from the arguments passed
Args:
    args(str): The list of arguments passed
Returns:
    Path to the input file
"""
def get_file_path(args):
    if len(args) <= 1:
        print("Please provide path to the input file")
        exit(-1)
    return args[1]


"""
This method reads the file from the path provided and returns numpy array of 2D grids
Args:
    pathToFile(str): The path to the input file to be read for processing
Returns:
    The numpy array of 2D grids which contain the training and testing cases
"""
def read_file(pathToFile):
    lists = []
    with open(pathToFile, "r+") as jsonFile:
        data = json.load(jsonFile)
        train = data["train"]
        test = data["test"]

        # Taking inputs from train and test of the json
        for i in itertools.chain(train, test):
            lists.append(np.asarray(i["input"]))
        return np.asarray(lists)


"""
This method prints the output grid for all the training and testing cases
Args:
    data(list): The output that needs to be printed
"""
def print_grid(data):
    for input in data:
        counter = 0
        dimension = len(input[0])
        arr = np.asarray(input).flatten()
        for i in arr:
            print(i, end=" ")
            counter += 1
            # This is the condition check for end of one row as it 2D grid is flattened to 1D
            # to reduce the time complexity of the method
            if (counter % dimension == 0):
                print()
        print()