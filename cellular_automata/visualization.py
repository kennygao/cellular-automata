class Visualization:
    # TODO: Rewrite.
    """
    Renders Frames.
    """

    def render_time(self, simulation):
        # TODO: This is a placeholder.
        return simulation.history.current_frame().time

    def render_space(self, simulation):
        space = simulation.history.current_frame().space

        height = len(space)
        width = max(map(len, space))

        preamble = bytes(f"P6 {width} {height} 1" + "\n", "ascii")
        raster = bytes(
            sample for row in space for cell in row for sample in self.render_cell(cell)
        )

        return preamble + raster

    def render_cell(self, cell):
        return {0: (0, 0, 0), 1: (1, 1, 1)}[cell]
