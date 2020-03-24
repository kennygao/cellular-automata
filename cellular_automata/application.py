import os
import sys
import tkinter


class Application:
    """
    Imperative scaffolding/shell.  Manager and orchestrator of functional components/core.
    """

    def __init__(self, root, visualization, simulation):
        self.root = root
        self.visualization = visualization
        self.simulation = simulation

        self.ui = {}

        self.configure_ui()
        self.configure_bind()

        self.display(self.simulation)

    def configure_ui(self):
        self.ui["time"] = tkinter.Label(self.root)
        self.ui["space"] = tkinter.Label(self.root)

        self.ui["time"].pack()
        self.ui["space"].pack()

    def configure_bind(self):
        self.root.bind("<Right>", lambda e: self.display(self.tick()))
        self.root.bind("<Left>", lambda e: self.display(self.undo()))

    def tick(self):
        # TODO: naming.

        self.simulation = self.simulation.tick()
        return self.simulation

    def undo(self):
        # TODO: naming.

        self.simulation = self.simulation.undo()
        return self.simulation

    def display(self, simulation):
        self.ui["time"].text = self.visualization.render_time(simulation)
        self.ui["space"].image = tkinter.PhotoImage(
            data=self.visualization.render_space(simulation), format="ppm"
        )

        self.ui["time"]["text"] = self.ui["time"].text
        self.ui["space"]["image"] = self.ui["space"].image

    def start(self):
        if sys.platform == "darwin":
            self.macos_foreground_ui()

        self.root.mainloop()

    def macos_foreground_ui(self):
        # On macOS, the Python `tkinter` UI lives in a separate "application", which spawns at
        # the bottom of the z-order instead of the top.
        #
        # To correct for this unexpected behavior, we'll shell out to an AppleScript command to
        # ask macOS to hoist the UI to the foreground.
        #
        # NB: This command may fail for many reasons, and that's okay.
        #
        # NB: `os.system` seems to be headed towards deprecation, but we're choosing to use it
        # because it's concise, lightweight, and fits our fire-and-forget use case.
        os.system(
            'osascript -e \'tell application "System Events" to set frontmost of process "Python" to true\''
        )
