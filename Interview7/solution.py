def place_queens(n: int) -> list[list[int]]:
    def is_safe(row, col):
        return not (cols[col] or diag1[row + col] or diag2[row - col])

    def place_queen(row, col):
        queens[row] = col
        cols[col] = diag1[row + col] = diag2[row - col] = True

    def remove_queen(row, col):
        cols[col] = diag1[row + col] = diag2[row - col] = False

    def backtrack(row):
        if row == n:
            result.append(queens[:])
            return
        for col in range(n):
            if is_safe(row, col):
                place_queen(row, col)
                backtrack(row + 1)
                remove_queen(row, col)

    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)
    queens = [-1] * n
    result = []
    backtrack(0)
    return result