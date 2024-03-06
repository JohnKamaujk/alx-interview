#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    """
    Computes the perimeter of an island with no lakes.

    Args:
    - grid: A list of lists representing the island where:
            0 represents water
            1 represents land

    Returns:
    - perimeter: The perimeter of the island
    """

    perimeter = 0

    # Check if grid is a list
    if not isinstance(grid, list):
        return 0

    # Get the number of rows and columns in the grid
    num_rows = len(grid)
    num_cols = len(grid[0]) if num_rows > 0 else 0

    # Iterate through each cell in the grid
    for i in range(num_rows):
        for j in range(num_cols):
            # Check if the cell is land
            if grid[i][j] == 1:
                # Check neighboring cells to determine edges
                edges = [
                    (i == 0 or grid[i - 1][j] == 0),  # top
                    (j == num_cols - 1 or grid[i][j + 1] == 0),  # right
                    (i == num_rows - 1 or grid[i + 1][j] == 0),  # bottom
                    (j == 0 or grid[i][j - 1] == 0)  # left
                ]
                # Add the number of edges to the perimeter
                perimeter += sum(edges)

    return perimeter
