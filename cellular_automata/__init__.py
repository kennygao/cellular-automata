from __future__ import annotations

import tkinter

from application import Application
from frame import Frame
from history import StackHistory
from ruleset import TrivialRuleSet
from simulation import Simulation
from visualization import Visualization


def main():
    Application(
        root=tkinter.Tk(),
        visualization=Visualization(),
        simulation=Simulation(StackHistory([Frame(0, [])]), TrivialRuleSet()),
    ).start()


if __name__ == "__main__":
    main()
