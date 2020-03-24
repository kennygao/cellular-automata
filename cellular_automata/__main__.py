from __future__ import annotations

import random
import tkinter

from .application import Application
from .frame import Frame
from .history import StackHistory
from .ruleset import TrivialRuleSet
from .simulation import Simulation
from .visualization import Visualization


def main():
    initial_space = [[random.randrange(2) for _ in range(100)] for _ in range(100)]
    initial_frame = Frame(0, initial_space)
    initial_history = StackHistory([initial_frame])

    Application(
        root=tkinter.Tk(),
        visualization=Visualization(),
        simulation=Simulation(initial_history, TrivialRuleSet()),
    ).start()


if __name__ == "__main__":
    main()
