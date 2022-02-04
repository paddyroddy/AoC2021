import pandas as pd

DISPLAY = pd.DataFrame(
    data=[
        [True, True, True, False, True, True, True],
        [False, False, True, False, False, True, False],
        [True, False, True, True, True, False, True],
        [True, False, True, True, False, True, True],
        [False, True, True, True, False, True, False],
        [True, True, False, True, False, True, True],
        [True, True, False, True, True, True, True],
        [True, False, True, False, False, True, False],
        [True, True, True, True, True, True, True],
        [True, True, True, True, False, True, True],
    ],
    columns=["a", "b", "c", "d", "e", "f", "g"],
)


def create_columns(content: list[str]) -> list[str]:
    """
    create columns for the initial dataframe the format is of
    <a> ... <b> | <c> ... <d>
    """
    first_line = content[0]
    split_at_pipe = first_line.split("|")
    n_input = split_at_pipe[0].count(" ")
    n_output = split_at_pipe[1].count(" ")
    input_columns = [f"input{i}" for i in range(n_input)]
    output_columns = [f"output{o}" for o in range(n_output)]
    return input_columns + output_columns


def find_all_string_lengths(df: pd.DataFrame) -> pd.DataFrame:
    """
    helper method to find length of all strings in a dataframe
    """
    return df.applymap(lambda x: len(x))
