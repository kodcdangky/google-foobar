from itertools import product


def solution(g):
    def build_count_valid_parents(next_cell):
        global valid
        row, col = next_cell
        offset = offset_table[bool(row) * 2 + bool(col)]
        for config in config_table[len(offset)]:
            for (row_offset, col_offset), value in zip(offset, config):
                parent[row + row_offset][col + col_offset] = value

            if (
                g[row][col]
                and sum(
                    (
                        parent[row][col],
                        parent[row][col + 1],
                        parent[row + 1][col],
                        parent[row + 1][col + 1],
                    )
                )
                != 1
            ) or (
                not g[row][col]
                and sum(
                    (
                        parent[row][col],
                        parent[row][col + 1],
                        parent[row + 1][col],
                        parent[row + 1][col + 1],
                    )
                )
                == 1
            ):
                continue

            if (row, col) == (len(g) - 1, len(g[-1]) - 1):
                valid += 1
                continue

            build_count_valid_parents(
                (row, col + 1) if col < len(g[0]) - 1 else (row + 1, 0)
            )

    def new_offset_table():
        return (
            ((0, 0), (0, 1), (1, 0), (1, 1)),
            ((0, 1), (1, 1)),
            ((1, 0), (1, 1)),
            ((1, 1),),
        )

    def new_config_table():
        table = [()]
        for length in range(1, 5):
            table.append(tuple(product((False, True), repeat=length)))
        return table

    global valid
    valid = 0
    offset_table = new_offset_table()
    config_table = new_config_table()
    parent = [[None for _ in range(len(g[0]) + 1)] for _ in range(len(g) + 1)]
    build_count_valid_parents((0, 0))
    return valid
