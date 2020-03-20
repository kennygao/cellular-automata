from __future__ import annotations


class Simulation:
    # TODO: Rewrite.
    """
    The state of the world.
    """

    def __init__(self, history, ruleset):
        self.history = history
        self.ruleset = ruleset

    def tick(self) -> Simulation:
        # Potential data race.
        previous_frame = self.history.current_frame()
        next_frame = self.ruleset.apply(previous_frame)
        next_history = self.history.push(next_frame)
        return Simulation(next_history, self.ruleset)

    def undo(self) -> Simulation:
        next_history = self.history.pop()
        return Simulation(next_history, self.ruleset)
