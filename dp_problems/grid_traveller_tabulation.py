# A traveller can move only down or right in the grid. We have to find the number of ways that he can reach from top
# left corner to botton right corner.

# Time Complexity: O(row * col)
# Space Complexity: O(row * col)


def grid_traveller(row, col):
    grid = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
    grid[1][1] = 1
    for curr_row in range(row + 1):
        for curr_col in range(col + 1):
            if curr_row + 1 <= row:
                grid[curr_row+1][curr_col] += grid[curr_row][curr_col]
            if curr_col + 1 <= col:
                grid[curr_row][curr_col+1] += grid[curr_row][curr_col]

    return grid[row][col]


# print(grid_traveller(1, 1))
print(grid_traveller(2, 3))
# print(grid_traveller(3, 2))
# print(grid_traveller(3, 3))
# print(grid_traveller(18, 18))
