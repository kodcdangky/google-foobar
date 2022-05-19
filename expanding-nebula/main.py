from itertools import product


def solution(g):
    def build_count_valid_parents(next_cell):
        global valid
        row, col = next_cell
        adjacents = adjacency_table[row][col]
        for config in config_table[len(adjacents)]:
            for (adj_row, adj_col), value in zip(adjacents, config):
                parent[adj_row][adj_col] = value

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

    def new_adjacency_cell_table():
        table = []
        for row_index in range(len(g)):
            table.append([])
            for col_index in range(len(g[row_index])):
                table[-1].append([(row_index + 1, col_index + 1)])
                if row_index == 0:
                    table[-1][-1].append((row_index, col_index + 1))
                if col_index == 0:
                    table[-1][-1].append((row_index + 1, col_index))
                if row_index == col_index == 0:
                    table[-1][-1].append((row_index, col_index))
        return table

    def new_config_table():
        table = [()]
        for length in range(1, 5):
            table.append(tuple(product((False, True), repeat=length)))
        return table

    global valid
    valid = 0

    adjacency_table = new_adjacency_cell_table()
    config_table = new_config_table()
    parent = [[None for _ in range(len(g[0]) + 1)] for _ in range(len(g) + 1)]
    build_count_valid_parents((0, 0))
    return valid
