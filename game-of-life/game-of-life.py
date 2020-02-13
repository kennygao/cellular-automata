"""
This is a naive implementation of Conway's Game of Life.

The goal is to be pedagogical, not performant.
"""


def display(universe):
    return '\n'.join(''.join(str(cell) for cell in row) for row in universe)


def main():
    universe = [[0 for columns in range(5)] for rows in range(3)]
    print(f'{universe=}')
    print(display(universe))


if __name__ == '__main__':
    main()
