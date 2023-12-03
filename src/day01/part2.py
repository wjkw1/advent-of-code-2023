import re


def read_file(filename: str):
    with open(filename, "r") as file:
        data = file.readlines()
    return data


def broken_concatenate_first_and_last_digits(line: str) -> str:
    # This failed on oneight case grr.., kept for the meme
    pattern = r"(?:[1-9]|one|two|three|four|five|six|seven|eight|nine)"
    matches = re.findall(pattern, line)

    first_digit = convert_word_number_to_digit(matches[0])
    if len(matches) == 1:
        return first_digit + first_digit

    elif len(matches) > 1:
        last_digit = convert_word_number_to_digit(matches[-1])
        return first_digit + last_digit
    else:
        raise KeyError("No matches found for string.")


def concatenate_first_and_last_digits(line: str) -> str:
    valid_words = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    valid_digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    valids = valid_words + valid_digits

    # Find the valid digits in the string
    first_indices = []
    last_indices = []
    for valid_value in valids:
        # searching from left
        first_index = line.find(valid_value)
        if first_index != -1:
            first_indices.append((first_index, valid_value))
        # searching from right
        last_index = line.rfind(valid_value)
        if last_index != -1:
            last_indices.append((last_index, valid_value))

    _, first_index = min(first_indices)
    first_digit = convert_word_number_to_digit(first_index)
    
    _, last_index = min(last_indices)
    last_digit = convert_word_number_to_digit(max(last_indices)[1])

    return first_digit + last_digit


def convert_word_number_to_digit(number_as_word: str) -> str:
    NUMBERS_AS_WORDS = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    number = NUMBERS_AS_WORDS.get(number_as_word, None)
    if number is None:
        return number_as_word
    return number


if __name__ == "__main__":
    # inputs = read_file("src/day01/input-part2-mini.txt")
    inputs = read_file("src/day01/input.txt")
    total = 0
    for line in inputs:
        digit = concatenate_first_and_last_digits(line)
        total = int(digit) + total
        print(f"{digit} -> {line}")

    print(f"Total: {total}")
