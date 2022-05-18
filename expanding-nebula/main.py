def solution(g):
    def build_count_valid_parents(next_cell):
        def get_unfilled_adjacents(cell):
            row, col = cell
            return ((row + next_row, col + next_col) for next_row, next_col in ((0, 0), (0, 1), (1, 0), (1, 1)) if parent[row + next_row][col + next_col] is None)

        unfilled_adjacents = get_unfilled_adjacents(next_cell)
        

        parent = [[None for _ in range(len(g[0]) + 1)] for _ in range(len(g) + 1)]

