from collections import defaultdict
from itertools import product


def solution(g):
    def new_cell_config_table():
        return tuple(
            tuple(product((False, True), repeat=repeat)) for repeat in (4, 2, 1)
        )

    def new_kernel_sum_table():
        return {kernel: sum(kernel) == 1 for kernel in product((False, True), repeat=4)}

    def valid_base_column():
        for config0 in cell_config_table[0]:
            if g[0][0] != kernel_sum_table[config0]:
                continue
            col = [config0[:2], config0[2:]]
            col.extend(() for _ in range(len(g) - 1))
            cell_stack = [(1, config) for config in cell_config_table[1]]
            while cell_stack:
                row_index, config = cell_stack.pop()
                if g[row_index][0] != kernel_sum_table[col[row_index] + config]:
                    continue
                col[row_index + 1] = config
                if row_index == len(g) - 1:
                    yield tuple(col)
                if row_index < len(g) - 1:
                    cell_stack.extend(
                        (row_index + 1, next_config)
                        for next_config in cell_config_table[1]
                    )

    def valid_columns(previous_col_half, col_index):
        for config0 in cell_config_table[1]:
            if (
                g[0][col_index]
                != kernel_sum_table[
                    config0 + previous_col_half[0] + previous_col_half[1]
                ]
            ):
                continue
            col = [
                previous_col_half[0] + config0[:1],
                previous_col_half[1] + config0[1:],
            ]
            col.extend(half for half in previous_col_half[2:])
            cell_stack = [(1, config) for config in cell_config_table[2]]
            while cell_stack:
                row_index, config = cell_stack.pop()
                if (
                    g[row_index][col_index]
                    != kernel_sum_table[
                        col[row_index] + col[row_index + 1][:1] + config
                    ]
                ):
                    continue
                col[row_index + 1] = col[row_index + 1][:1] + config
                if row_index == len(g) - 1:
                    yield tuple(col)
                if row_index < len(g) - 1:
                    cell_stack.extend(
                        (row_index + 1, next_config)
                        for next_config in cell_config_table[2]
                    )

    def column_match(col1, col2):
        for row1, row2 in zip(col1, col2):
            if row1[1] != row2[0]:
                return False
        return True

    def build_by_col(col_index, col):
        previous_col_half = tuple(row[1:] for row in col)
        for next_col in valid_columns(previous_col_half, col_index + 1):
            if column_match(col, next_col):
                config_count[col_index][col] += (
                    1
                    if col_index + 1 == len(g[0]) - 1
                    else config_count[col_index + 1][next_col]
                    if next_col in config_count[col_index + 1]
                    else build_by_col(col_index + 1, next_col)
                )
        return config_count[col_index][col]

    config_count = [defaultdict(int) for _ in range(len(g[0]) - 1)]
    cell_config_table = new_cell_config_table()
    kernel_sum_table = new_kernel_sum_table()
    for column in valid_base_column():
        build_by_col(0, column)
    return sum(config_count[0][config] for config in config_count[0])
