from utils import read_input, get_score
from anis import solve, make_output_file
from jaime import input_parser
import os

def main():
    for filename in os.listdir("files"):
        contributors, projects = input_parser(filename)
        assignments = solve(contributors, projects)
        make_output_file(assignments, filename)
        print(filename, assignments)

if __name__ == "__main__":
    main()
