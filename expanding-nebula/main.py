from itertools import product


def solution(g):
    def build_count_valid_parents(next_cell):
        def get_unfilled_adjacents(cell):
            row, col = cell
            return tuple(
                (row + next_row, col + next_col)
                for next_row, next_col in ((0, 0), (0, 1), (1, 0), (1, 1))
                if parent[row + next_row][col + next_col] is None
            )

        unfilled_adjacents = get_unfilled_adjacents(next_cell)
        row, col = next_cell
        for config in product((False, True), repeat=len(unfilled_adjacents)):
            for (adj_row, adj_col), value in zip(unfilled_adjacents, config):
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

    valid = 0
    parent = [[None for _ in range(len(g[0]) + 1)] for _ in range(len(g) + 1)]
    build_count_valid_parents((0, 0))
    return valid
