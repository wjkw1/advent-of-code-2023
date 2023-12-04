from src import utils


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


def get_max_required_colours(game_string: str):
    # find the required number of values for each colour for our game
    required_red = 0
    required_green = 0
    required_blue = 0
    grab_strings = game_string.split("; ")

    for grab in grab_strings:
        grab_dict = grab_cubes(grab)

        if grab_dict.get("red") and grab_dict.get("red") > required_red:
            required_red = grab_dict.get("red")

        if grab_dict.get("green") and grab_dict.get("green") > required_green:
            required_green = grab_dict.get("green")

        if grab_dict.get("blue") and grab_dict.get("blue") > required_blue:
            required_blue = grab_dict.get("blue")

    return required_red, required_green, required_blue


if __name__ == "__main__":
    # inputs = utils.read_file("src/day02/input-part1-mini.txt")
    inputs = utils.read_file("src/day02/input.txt")

    color_dict = grab_cubes("3 blue, 4 red")
    print(color_dict)

    r, g, b = get_max_required_colours("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    print(f"(r,g,b), ({r},{g},{b})")

    total_powers = []
    for line in inputs:
        game_id, game_string = line.split(": ")
        r, g, b = get_max_required_colours(game_string)
        power = r * g * b
        total_powers.append(power)
    
    print(total_powers)
    print(sum(total_powers))
