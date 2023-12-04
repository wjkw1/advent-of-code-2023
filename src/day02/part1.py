from src import utils

NUMBER_OF_RED_CUBES = 12
NUMBER_OF_GREEN_CUBES = 13
NUMBER_OF_BLUE_CUBES = 14


def grab_cubes(grab_string: str):
    # returns a dict for each colour with the numbers

    color_pairs = grab_string.split(", ")
    colour_dict = {}
    for pair in color_pairs:
        number, color = pair.split()
        number = int(number)
        if color in colour_dict:
            colour_dict[color] += number
        else:
            colour_dict[color] = number
    return colour_dict


def is_valid_grab(colour_dict: dict):
    errors = []
    default_number: int = 0
    if colour_dict.get("red") and colour_dict.get("red") > NUMBER_OF_RED_CUBES:
        errors.append(
            f"Too many red cubes: {colour_dict.get('red')} out of {NUMBER_OF_RED_CUBES}"
        )
    if (
        colour_dict.get("green")
        and colour_dict.get("green", default_number) > NUMBER_OF_GREEN_CUBES
    ):
        errors.append(
            f"Too many green cubes: {colour_dict.get('green')} out of {NUMBER_OF_GREEN_CUBES}"
        )
    if (
        colour_dict.get("blue")
        and colour_dict.get("blue", default_number) > NUMBER_OF_BLUE_CUBES
    ):
        errors.append(
            f"Too many blue cubes: {colour_dict.get('blue')} out of {NUMBER_OF_BLUE_CUBES}"
        )

    if len(errors) != 0:
        print(errors)
        return False
    # Successful grab
    return True


def is_valid_game(game_string: str):
    # gets a game and loops through the string

    grab_strings = game_string.split("; ")
    for grab in grab_strings:
        grab_dict = grab_cubes(grab)
        is_valid = is_valid_grab(grab_dict)
        if not is_valid:
            return False

    return True


if __name__ == "__main__":
    # inputs = utils.read_file("src/day02/input-part1-mini.txt")
    inputs = utils.read_file("src/day02/input.txt")
    valid_game_id_numbers = []
    for line in inputs:
        game_id, game_string = line.split(": ")
        game_status = is_valid_game(game_string)
        print(f"{game_id} -> Is it Valid? {game_status}")

        if game_status:
            _, game_id_number = game_id.split(" ")
            valid_game_id_numbers.append(int(game_id_number))

    print(valid_game_id_numbers)
    print(sum(valid_game_id_numbers))
