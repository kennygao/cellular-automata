"""
This is a naive implementation of Conway's Game of Life.

The goal is to be pedagogical, not performant.
"""
import random


def display(universe):
    return "\n".join("".join(str(cell) for cell in row) for row in universe)


def flip_cell(cell, cell_neighborhood):
    return 1 - cell


def game_of_life(cell, cell_neighborhood):
    # The neighborhood of a cell contains the cell itself.
    # TODO: This definition can be changed if desired.
    population = sum(cell_neighborhood)

    return {3: 1, 4: cell}.get(population, 0)


def neighborhood(universe, row, column):
    offsets = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    return (
        universe[(row + row_offset) % len(universe)][
            (column + column_offset) % len(universe[row])
        ]
        for row_offset, column_offset in offsets
    )


def tick_universe(universe, tick_cell):
    return [
        [
            tick_cell(universe[row][column], neighborhood(universe, row, column))
            for column in range(len(universe[row]))
        ]
        for row in range(len(universe))
    ]


def main():
    universe = [[random.randrange(2) for _ in range(5)] for _ in range(3)]

    print("universe @ t[0]")
    print(display(universe))

    print("flip_cell")
    print(display(tick_universe(universe, flip_cell)))

    print("game_of_life")
    print(display(tick_universe(universe, game_of_life)))


if __name__ == "__main__":
    main()
