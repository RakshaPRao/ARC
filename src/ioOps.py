import numpy as np
import json
import itertools
from sys import exit

"""
This method gets the input file path from the arguments its been passed

Args:
    args (str): The list of arguments passed
Returns:
    Path to the input file
"""
def get_file_path(args):
    if len(args) <= 1:
        print("Please provide path to the input file")
        exit(-1)
    return args[1]


"""
This methofd reads the file from the path provided and processes it

Args:
    pathToFile (str): The path to the input file which has to be read
Returns:
    The numpy array of 2D grids which contain the test cases
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
This method prints the output grid

Args:
    data(list): The output that needs to be printed
"""
def print_grid(data):
    for input in data:
        counter = 0
        dimention = len(input[0])
        arr = np.asarray(input).flatten()
        for i in arr:
            print(i, end=" ")
            counter += 1
            # This is the condition check for end of one row as it 2D grid is flattened to 1D
            # to reduce the time complexity of the method
            if (counter % dimention == 0):
                print()
        print()