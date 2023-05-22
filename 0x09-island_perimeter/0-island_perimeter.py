#!/usr/bin/python3
"""Island perimeter computing module.
"""

def island_perimeter(grid):
  """Computes the perimeter of an island with no lakes.
  """
  # Initialize perimeter
  perimeter = 0
  # Get number of rows and columns
  rows = len(grid)
  cols = len(grid[0])
  # Loop through each cell
  for i in range(rows):
    for j in range(cols):
      # If cell is land
      if grid[i][j] == 1:
        # Add 4 to perimeter for each side
        perimeter += 4
        # Subtract 2 for each adjacent land cell on the same row
        if i > 0 and grid[i-1][j] == 1:
          perimeter -= 2
        # Subtract 2 for each adjacent land cell on the same column
        if j > 0 and grid[i][j-1] == 1:
          perimeter -= 2
  # Return final perimeter        
  return perimeter
