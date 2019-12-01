# Hand coded solutions for tasks in Abstraction and Reasoning Corpus (ARC)

This repository contains hand coded solutions in the ARC for the tasks 29c11459, 746b3537, aabf363d and a699fb00.

Solving these tasks is easy for a human but the same tasks are very hard for an AI system. Finding patterns without any human intervention for all these tasks is beyond the current state of the art.

A complete description of the dataset, its goals, and its underlying logic, can be found in: [The Measure of Intelligence](https://arxiv.org/abs/1911.01547).

## Task file format

There is a `src` directory that has the following files

- `solution_task.py`: These files provide the solutions for the tasks which is described by it. Eg: solution_29c11459.py solves the task described in 29c11459.json which is in `data/training` directory.
- `ioOps.py`: This file has the operations that are common for solving all the tasks like reading, training file and printing the output grid on console.
- `19230887and19233027Report.pdf`: This contains the comprehensive report.

Each of the solution file has a the following features

- `main` method which takes the path of the training data JSON as its input from command line. Eg. solution_29c11459.py need to be run as `python solution_29c11459.py path/to/training/data/json/file`
- `solve` method which contains the hand coded solution for the particular task.
- `output` of the task is the solution printing the output grid on the console

The sample output for a task looks like the one shown below

![output](https://i.ibb.co/Sfhnt28/Annotation-2019-12-01-184607.png)
