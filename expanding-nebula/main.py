from itertools import product


def solution(g):
    def build_by_column(next_col):
        def build_valid_column(col):
            pass

    def new_cell_config_table():
        return tuple(product((False, True), repeat=2)), tuple(product((False, True), repeat=4))

    def new_cell_offset_table():
        return ((1, 0), (1, 1)), tuple(product((0, 1), repeat=2))


    config_count = [{} for _ in g[0]]
    cell_config_table = new_cell_config_table()
    cell_offset_table = new_cell_offset_table()
    parent = [[None for _ in range(len(g[0]) + 1)] for _ in range(len(g) + 1)]
    build_by_column(0)
    return sum(config_count[0])