import random
import tkinter

toplevel = tkinter.Tk()
toplevel.wm_title("cellular-automata")

canvas = tkinter.Canvas(
    toplevel,
    background="gray",
    height=200,
    width=200,
    scrollregion=(-100, -100, 100, 100),
)
canvas.pack()


def render():
    canvas.create_line(
        random.randrange(-100, 100),
        random.randrange(-100, 100),
        random.randrange(-100, 100),
        random.randrange(-100, 100),
        fill="black",
    )

    canvas.after(100, render)


render()

toplevel.mainloop()
