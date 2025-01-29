import os
import time

WIDTH = 10
HEIGHT = 10
SLEEP = 0.5

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def empty_grid():
    return [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]

def print_grid(grid):
    print("   " + " ".join(str(x) for x in range(WIDTH)))
    print("  ╭" + "─" * (2 * WIDTH) + "╮")
    for y in range(HEIGHT):
        row = f"{y:2}│"
        for x in range(WIDTH):
            row += "* " if grid[y][x] else "  "
        row += "│"
        print(row)
    print("  ╰" + "─" * (2 * WIDTH) + "╯")

def count_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1),          ( 0, 1),
                  ( 1, -1), ( 1, 0), ( 1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
            count += grid[ny][nx]
    return count

def next_generation(grid):
    return [
        [apply_rules(grid[y][x], count_neighbors(grid, x, y)) for x in range(WIDTH)]
        for y in range(HEIGHT)
    ]

def apply_rules(alive, neighbors):
    return (neighbors == 3) or (alive and neighbors == 2)

def input_cells(grid):
    print("\nEnter live cell coordinates. Type 'done' when finished.")
    while True:
        entry = input("Cell (x y): ").strip()
        if entry.lower() == "done":
            break
        try:
            x_str, y_str = entry.split()
            x, y = int(x_str), int(y_str)
            if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                grid[y][x] = not grid[y][x]
                clear()
                print_grid(grid)
            else:
                print("Out of bounds.")
        except ValueError:
            print("Enter two numbers: x y")

def main():
    grid = empty_grid()
    clear()
    print_grid(grid)
    input_cells(grid)

    while True:
        mode = input("\nMode? [s]tep / [r]un / [q]uit: ").strip().lower()
        if mode == "q":
            break
        elif mode == "s":
            grid = next_generation(grid)
            clear()
            print_grid(grid)
        elif mode == "r":
            try:
                while True:
                    grid = next_generation(grid)
                    clear()
                    print_grid(grid)
                    time.sleep(SLEEP)
            except KeyboardInterrupt:
                print("\nPaused. Returning to menu.")
        else:
            print("Invalid input. Choose [s], [r], or [q].")

if __name__ == "__main__":
    main()
