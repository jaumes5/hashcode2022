from utils import read_input, get_score
from anis import solve, make_output_file
from jaime import input_parser

def main():
    contributors, projects = input_parser("a_an_example.in.txt")
    assignments = solve(contributors, projects)
    make_output_file(assignments)
    print(assignments)

if __name__ == "__main__":
    main()
