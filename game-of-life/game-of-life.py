"""
This is a naive implementation of Conway's Game of Life.

The goal is to be pedagogical, not performant.
"""
import random


def display(universe):
    return "\n".join("".join(str(cell) for cell in row) for row in universe)


def tick(universe):
    return [[1 - cell for cell in row] for row in universe]


def main():
    universe = [[random.randrange(2) for columns in range(5)] for rows in range(3)]

    print("universe @ t[0]")
    print(display(universe))

    print("universe @ t[1]")
    print(display(tick(universe)))


if __name__ == "__main__":
    main()
