from utils import read_input, get_score
from anis import solve
from jaime import input_parser

def main():
    contributors, projects = input_parser("a_an_example.in.txt")
    assignments = solve(contributors, projects)
    print(assignments)

if __name__ == "__main__":
    main()
