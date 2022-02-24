from os.path import isdir, isfile
import os


def read_input(path: str):
    if isdir(path):
        files = [
            read_file(os.path.join(path, filename))
            for filename in os.listdir(path)
            if isfile(os.path.join(path, filename))
        ]
    elif isfile(path):
        files = [read_file(path)]
    else:
        raise Exception("Path doesn't exist! Start panicking now")
    return files


def read_file(file_path):
    with open(file_path) as file:
        return file.read()


def get_score() -> int:
    return 0
