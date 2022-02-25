from pathlib import Path

import numpy as np
import pandas as pd
from utils_day11 import (
    NAME,
    convert_to_df_of_int,
    increment_octopuses_level_and_count_flashes,
)

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> np.ndarray:
    df = pd.read_csv(_data_path / filename, names=[NAME], dtype=str)
    return convert_to_df_of_int(df, NAME)


def count_how_many_flashes(data: np.ndarray, steps: int) -> int:
    """
    count how many times octopuses flash by reaching level 9
    """
    # initialise count
    flashes = 0

    # loop through the data
    for _ in range(steps):
        data, count = increment_octopuses_level_and_count_flashes(data)
        flashes += count

    print(f"Q1 flashes: {flashes}")
    return flashes


if __name__ == "__main__":
    energies = read_data("data_day11.csv")
    count_how_many_flashes(energies, 100)
