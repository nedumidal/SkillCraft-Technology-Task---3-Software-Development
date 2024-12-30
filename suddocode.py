def print_grid(grid):
    """Prints the Sudoku grid in a readable format."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))


def is_valid(grid, row, col, num):
    """Checks if placing a number in a specific position is valid."""
    if num in grid[row]:
        return False

    for r in range(9):
        if grid[r][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(grid):
    """Uses backtracking to solve the Sudoku puzzle."""

    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True  # Puzzle is solved

    row, col = empty_cell


    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num  

            if solve_sudoku(grid): 
                return True

            grid[row][col] = 0  

    return False 


def find_empty_cell(grid):
    """Finds an empty cell in the Sudoku grid."""
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:  
                return r, c
    return None

sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

print("Sudoku Puzzle:")
print_grid(sudoku_grid)

if solve_sudoku(sudoku_grid):
    print("\nSolved Sudoku:")
    print_grid(sudoku_grid)
else:
    print("\nNo solution exists for the given Sudoku puzzle.")
