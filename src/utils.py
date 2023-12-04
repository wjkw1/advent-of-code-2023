# Utility files common across the days


def read_file(filename: str):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    return lines
