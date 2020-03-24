import functions


class Visualization:
    # TODO: Rewrite.
    """
    Renders Frames.
    """

    def render_time(self, simulation):
        # TODO: This is a placeholder.
        return simulation.history.current_frame().time

    def render_space(self, simulation):
        def render_cell(cell):
            return {0: (0, 0, 0), 1: (1, 1, 1)}[cell]

        space = simulation.history.current_frame().space

        height = len(space)
        width = max(map(len, space))

        preamble = bytes(f"P6 {width} {height} 1" + "\n", "ascii")

        # The following expressions should all evaluate to the same result.
        #
        # TODO: After we have a better idea of what our data will look like, choose which to use.
        raster = bytes(
            # sample for row in space for cell in row for sample in render_cell(cell)
            # functions.flatten(map(render_cell, functions.flatten(space)))
            functions.compose(
                functions.flatten,
                lambda cells: map(render_cell, cells),
                functions.flatten,
            )(space)
        )

        return preamble + raster
