import string
from typing import Union

import numpy as np
import pandas as pd


class Plate:
    def __init__(
        self,
        df: pd.DataFrame,
        n_rows: int = 8,
        n_cols: int = 12,
        well_column: str = "well",
        value_column: str = "value",
    ) -> None:
        self.n_rows = n_rows
        self.n_cols = n_cols

        self.rows = {
            letter: row_num
            for row_num, letter in enumerate(string.ascii_uppercase[:n_rows])
        }
        self.n_col_digits = int(np.ceil(np.log10(n_cols)))
        self.cols = {
            f"{colname:0{self.n_col_digits}}": col_num
            for col_num, colname in enumerate(list(range(1, n_cols + 1))[:n_cols])
        }
        self.cells = {
            f"{row_letter}{col_char}": (row_num, col_num)
            for row_letter, row_num in self.rows.items()
            for col_char, col_num in self.cols.items()
        }
        vals = np.full((self.n_rows, self.n_cols), None)
        for cell_name, idx in self.cells.items():
            value = df[df[well_column] == cell_name][value_column].values
            if len(value) != 0:
                ValueError(f"Received {len(value)} values for {cell_name}: {value}")
            vals[idx] = value[0]
        self.vals = np.float64(vals)

    def get_cell(self, cell_name: str) -> np.array:
        return self.vals[self.cells[cell_name]]

    def get_row(self, letter: str) -> np.array:
        return self.vals[self.rows[letter], :]

    def get_column(self, colname: Union[str, int]) -> np.array:
        if isinstance(colname, int):
            return self.vals[:, self.cols[f"{colname:0{self.n_col_digits}}"]]
        else:
            return self.vals[:, self.cols[colname]]
