import tkinter

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Define UI structure.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# root
root = tkinter.Tk()
root.wm_title("cellular-automata")

# canvas
canvas = tkinter.Canvas(root, height=300, width=300)
canvas.pack()
photo = tkinter.PhotoImage(file="feep.ppm")
zoom = photo.zoom(2)
image = canvas.create_image((150, 150), image=photo)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Define UI behavior.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# When canvas receives "next", it updates itself.
def update_canvas(event):
    # canvas.delete(tkinter.ALL)
    print(f'{canvas.itemcget(image, "image")=}')
    canvas.itemconfigure(image, image=zoom)
    print(f"{event=}")


canvas.bind("<Return>", update_canvas)

# When button receives "click", it sends "next" to the canvas.

# When root receives "return", it sends "next" to the canvas.


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Send "mainloop" to root.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

root.mainloop()
