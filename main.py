from utils import read_input, get_score
from anis import solve, make_output_file
from jaime import input_parser
import os
import time

def main():
    start = time.time()
    for filename in os.listdir("files"):
        contributors, projects = input_parser(filename)
        assignments = solve(contributors, projects)
        make_output_file(assignments, filename)
        print(filename, assignments)
    final_time = time.time() - start
    print(f"Time elpased {final_time // 60} min and {int(final_time % 60)} sec")

if __name__ == "__main__":
    main()
