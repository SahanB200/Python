#Author: Sahan Baddegama
#Date: 23rd Mar 2025

# Create a 5x5 grid filled with zeros
grid = [[0 for _ in range(5)] for _ in range(5)]

# Starting position: middle of the top row
x, y = 0, 2
grid[x][y] = 1

# Loop from 2 to 25
for num in range(2, 26):
    # Calculate the next position (diagonally up and to the right)
    new_x, new_y = (x - 1) % 5, (y + 1) % 5

    # Check if the calculated position is already filled
    if grid[new_x][new_y] != 0:
        # Move vertically down one position instead
        new_x, new_y = (x + 1) % 5, y

    # Place the number in the calculated position
    grid[new_x][new_y] = num

    # Update current position
    x, y = new_x, new_y

# Print the grid
for row in grid:
    print(row)