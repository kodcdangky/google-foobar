from collections import defaultdict
from itertools import product


def solution(g):
    def new_cell_config_table():
        return tuple(product((False, True), repeat=4)), tuple(
            product((False, True), repeat=2)
        )

    def valid_columns(col_index):
        for config0 in cell_config_table[0]:
            if (g[0][col_index] and sum(config0) != 1) or (
                not g[0][col_index] and sum(config0) == 1
            ):
                continue
            col = [config0[:2], config0[2:]]
            col.extend(None for _ in range(len(g) - 1))
            cell_stack = [(1, config) for config in cell_config_table[1]]
            while cell_stack:
                row_index, config = cell_stack.pop()
                if (
                    g[row_index][col_index] and sum(col[row_index]) + sum(config) != 1
                ) or (
                    not g[row_index][col_index]
                    and sum(col[row_index]) + sum(config) == 1
                ):
                    continue
                col[row_index + 1] = config
                if row_index == len(g) - 1:
                    yield tuple(col)
                if row_index < len(g) - 1:
                    cell_stack.extend(
                        (row_index + 1, next_config)
                        for next_config in cell_config_table[1]
                    )

    def column_match(col1, col2):
        for row1, row2 in zip(col1, col2):
            if row1[1] != row2[0]:
                return False
        return True

    def build_by_column(col_index, col):
        for next_col in valid_columns(col_index + 1):
            if column_match(col, next_col):
                config_count[col_index][col] += (
                    1
                    if col_index + 1 == len(g[0]) - 1
                    else config_count[col_index + 1][next_col]
                    if next_col in config_count[col_index + 1]
                    else build_by_column(col_index + 1, next_col)
                )
        return config_count[col_index][col]

    config_count = [defaultdict(int) for _ in range(len(g[0]) - 1)]
    cell_config_table = new_cell_config_table()
    for column in valid_columns(0):
        build_by_column(0, column)
    return sum(config_count[0][config] for config in config_count[0])
