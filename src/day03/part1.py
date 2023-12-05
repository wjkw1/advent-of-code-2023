"""Day 3"""

import pandas as pd
import numpy as np
from src import utils


def is_number(value):
    return value.isdigit()


def is_symbol(value):
    return value != "." and not value.isalnum()


if __name__ == "__main__":
    # inputs = utils.read_file("src/day03/input-part1-mini.txt")
    inputs = utils.read_file("src/day03/input.txt")
    # 0. Setup dataframe
    matrix = [list(row) for row in inputs if row]
    df = pd.DataFrame(matrix)
    print(df)

    # 1 & 2. symbol mask & number mask
    df_symbol_mask = df.applymap(is_symbol)
    print(df_symbol_mask)

    # 3. get a validation mask in a 3x3 around each symbol
    df_validation_mask = pd.DataFrame(False, index=df.index, columns=df.columns)
    # get iloc of all symbols using the mask
    symbol_indices = np.where(df_symbol_mask)
    print(symbol_indices)
    for row, col in zip(*symbol_indices):
        # Iterate over the rows and columns of the 3x3 area around the location
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = row + dx, col + dy
                # Check if the indices are within the bounds of the DataFrame
                if 0 <= nx < df.shape[0] and 0 <= ny < df.shape[1]:
                    df_validation_mask.iloc[nx, ny] = True

    output = 0
    tmp_num = ""
    tmp_valid = False
    num_rows, num_cols = df.shape
    # i = row, j = column
    for i in range(num_rows):
        for j in range(num_cols):
            if is_number(df.iloc[i, j]):
                tmp_num = tmp_num + df.iloc[i, j]
                tmp_valid = df_validation_mask.iloc[i, j] or tmp_valid
            else:
                if tmp_num != "" and tmp_valid:
                    output = output + int(tmp_num)
                tmp_num = ""
                tmp_valid = False
        if tmp_num != "" and tmp_valid:
            output = output + int(tmp_num)
        tmp_num = ""
        tmp_valid = False

    print(output)
