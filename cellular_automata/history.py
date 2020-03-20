class History:
    # TODO: Rewrite.
    """
    ADT to manage Frames.
    Basically a version control system.
    Initially implemented with a stack.
    May want to be a tree or graph in the future.
    Maybe even its own CA simulation.

    Must have a current Frame.
    """

    pass


class StackHistory(History):
    def __init__(self, stack):
        super().__init__()
        # TODO: Throw if stack is empty.
        self.stack = stack

    def current_frame(self):
        # TODO: naming.

        return self.stack[-1]

    def push(self, frame):
        # TODO: naming.

        # DONE: Hoist the mutation up to Application.
        return StackHistory(self.stack + [frame])

    def pop(self):
        # TODO: naming.

        # TODO: In case of failure, return self.
        return StackHistory(self.stack[:-1])
