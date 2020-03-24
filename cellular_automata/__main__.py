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
    Application(
        root=tkinter.Tk(),
        visualization=Visualization(),
        simulation=Simulation(
            history=StackHistory(
                stack=[
                    Frame(
                        time=0,
                        space=[
                            [random.randrange(2) for _ in range(100)]
                            for _ in range(100)
                        ],
                    )
                ]
            ),
            ruleset=TrivialRuleSet(),
        ),
    ).start()


if __name__ == "__main__":
    main()
