"""Day 3"""

import pandas as pd
import numpy as np
from src import utils


def is_number(value):
    return value.isdigit()


def is_gear(value):
    return value == "*"


if __name__ == "__main__":
    inputs = utils.read_file("src/day03/input.txt")
    # inputs = utils.read_file("src/day03/input-part1-mini.txt")

    matrix = [list(row) for row in inputs if row]
    df = pd.DataFrame(matrix)
    df_gear_mask = df.applymap(is_gear)

    tmp_valid = False
    tmp_num = ""
    tmp_num_list = []
    gear_ratio_list = []
    gear_indices = np.where(df_gear_mask)
    for row, col in zip(*gear_indices):
        # check rows above, on, and below
        for dy in [-1, 0, 1]:
            # Check around our gear knowing that digits are 3 length max
            # valid numbers should have a digit in the [-1, 0, 1] location
            for dx in [-3, -2, -1, 0, 1, 2, 3]:
                tmp_row, tmp_col = row + dy, col + dx
                if 0 <= tmp_row < df.shape[0] and 0 <= tmp_col < df.shape[1]:
                    if is_number(df.iloc[tmp_row, tmp_col]):
                        tmp_num = tmp_num + df.iloc[tmp_row, tmp_col]
                        valid_col_digit_pos = [(col + -1), (col + 0), (col + 1)]
                        if tmp_col in valid_col_digit_pos:
                            tmp_valid = True

                        # we should reset if last item we are checking is a number too
                        if tmp_col == (col + 3):
                            if tmp_num != "" and tmp_valid:
                                tmp_num_list.append(tmp_num)
                            tmp_valid = False
                            tmp_num = ""

                    else:
                        # time to reset
                        if tmp_num != "" and tmp_valid:
                            tmp_num_list.append(tmp_num)
                        tmp_valid = False
                        tmp_num = ""

        if len(tmp_num_list) == 2:
            # We have a game on our hands
            gear_ratio = int(tmp_num_list[0]) * int(tmp_num_list[1])
            gear_ratio_list.append(gear_ratio)
            print(
                f"Gear Ratio: {int(tmp_num_list[0])} * {int(tmp_num_list[1])} = {gear_ratio}"
            )
        else:
            print(f"Failed Gear Ratio: at loc {(row,col)}")
        tmp_num_list = []


    print(gear_ratio_list)
    print(len(gear_ratio_list))
    output = sum(gear_ratio_list)
    print(output)
