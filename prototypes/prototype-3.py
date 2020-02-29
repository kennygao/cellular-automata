import tkinter


def main():
    application = Application()
    application.run()


class Application:
    def __init__(self):
        self.root = tkinter.Tk()
        self.visualization = Visualization(self)
        self.simulation = Simulation()

        self.configure_root()

    def configure_root(self):
        self.root.bind("<Left>", lambda e: None)
        self.root.bind("<Right>", lambda e: self.advance_simulation())
        self.root.bind("<Return>", lambda e: self.advance_simulation())

        self.root.bind("<KeyPress>", self.handle_keypress)

    def advance_simulation(self):
        state = self.simulation.update()
        self.visualization.render_state(state)
        # self.root.after(100, self.update)

    def handle_keypress(self, event):
        print(f"{event=}")

    def run(self):
        # TODO: Ask macOS to foreground python.
        #  https://stackoverflow.com/questions/1892339/8775078#8775078

        self.root.mainloop()


class Visualization:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tkinter.Canvas(self.parent.root)

    def render_state(self, state):
        print("visualization.render_state")


class Simulation:
    def __init__(self):
        # self.universe = universe()
        pass

    def update(self):
        pass


if __name__ == "__main__":
    main()
