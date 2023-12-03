import re


def read_file(filename: str):
    with open(filename, "r") as file:
        data = file.readlines()
    return data


def concatenate_first_and_last_digits(line: str) -> str:
    matches = re.findall(r"\d", line)
    if len(matches) > 1:
        return str(matches[0]) + str(matches[-1])
    else:
        return matches[0] + matches[0]


if __name__ == "__main__":
    inputs = read_file("src/day01/input.txt")

    total = 0
    for line in inputs:
        digit = concatenate_first_and_last_digits(line)
        total = int(digit) + total
        print(f"{line} -> {digit}")
    
    print(f"Total: {total}")

