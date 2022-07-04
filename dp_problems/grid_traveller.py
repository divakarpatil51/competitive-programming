# A traveller can move only down or right in the grid. We have to find the number of ways that he can reach from top
# left corner to botton right corner.

memo = {}


def grid_traveller(row, col):
    if row == 0 or col == 0:
        return 0
    if row == 1 and col == 1:
        return 1
    if f"{row},{col}" in memo:
        return memo[f"{row},{col}"]
    row_count = grid_traveller(row - 1, col)
    col_count = grid_traveller(row, col - 1)
    memo[f"{row},{col}"] = row_count + col_count
    return memo[f"{row},{col}"]


print(grid_traveller(1, 1))
print(grid_traveller(2, 3))
print(grid_traveller(3, 2))
print(grid_traveller(3, 3))
print(grid_traveller(18, 18))
