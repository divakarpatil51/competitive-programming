# Given
# a
# boolean
# 2
# D
# matrix, find
# the
# number
# of
# islands.A
# group
# of
# connected
# 1
# s
# forms
# an
# island.For
# example, the
# below
# matrix
# contains
# 5
# islands
# Example:
#
# Input: mat[][] =
#                   {{1, 1, 0, 0, 0},
#                   {0, 1, 0, 0, 1},
#                   {1, 0, 0, 1, 1},
#                   {0, 0, 0, 0, 0},
#                   {1, 0, 1, 0, 1}}
# Output: 5
#
# r * c
#
# r + 1
# r - 1
# c + 1
# c - 1
#
# # Can we use graph?
# 1.
# adjacency
# list - nope
# 2.
# recursive - dfs
#
# 1.
# keep
# list
# of
# visited
# items
#
# Algorithm:
#

def find_island(island_matrix) -> int:
    island_count = 0
    visited_island = []
    for row in range(0, len(island_matrix)):
        for column in range(0, len(island_matrix[0])):

            island_count += get_island(row, column, island_matrix, visited_island)
    return island_count


def get_island(row, column, island_matrix, visited_island) -> int:

    if 0 <= row < len(island_matrix) and 0 <= column < len(island_matrix[0]):

        if island_matrix[row][column] == 0:
            return 0

        visited = f"{row},{column}"
        if visited in visited_island:
            return 0
        visited_island.append(visited)

        # We are moving columns
        get_island(row, column + 1, island_matrix, visited_island)
        get_island(row, column - 1, island_matrix, visited_island)

        # We are moving rows
        get_island(row + 1, column, island_matrix, visited_island)
        get_island(row - 1, column, island_matrix, visited_island)

        # We are moving diagonally back
        get_island(row - 1, column - 1, island_matrix, visited_island)
        get_island(row - 1, column + 1, island_matrix, visited_island)

        # We are moving diagonally forward
        get_island(row + 1, column - 1, island_matrix, visited_island)
        get_island(row + 1, column + 1, island_matrix, visited_island)

        return 1
    return 0


island_c = find_island(
    [[1, 1, 0, 0, 0],
     [0, 0, 0, 0, 1],
     [1, 0, 0, 1, 1],
     [0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1]]
)

print(f"Island count: {island_c}")
