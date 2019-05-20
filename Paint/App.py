from tkinter import *

canvas_width = 700
canvas_height = 600
brush_size = 3
color = "black"


def paint(event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    w.create_oval(x1, y1, x2, y2,
                  fill=color, outline=color)


def brush_size_change(new_size):
    global brush_size
    brush_size = new_size


def color_change(new_color):
    global color
    color = new_color


root = Tk()
root.title("Paint")
root.geometry("730x700")

w = Canvas(root,
           width=canvas_width,
           height=canvas_height,
           bg="white")

w.bind("<B1-Motion>", paint)

red_btn = Button(text="Red", width=10, bg="red",
                 command=lambda: color_change("red"))

blue_btn = Button(text="Blue", width=10, bg="blue",
                  command=lambda: color_change("blue"))

yellow_btn = Button(text="Yellow", width=10, bg="yellow",
                    command=lambda: color_change("yellow"))

orange_btn = Button(text="Orange", width=10, bg="orange",
                    command=lambda: color_change("orange"))

clear_btn = Button(text="Delete", width=10,
                   command=lambda: color_change("white"))

clear_all_btn = Button(text="Clear all", width=10,
                       command=lambda: w.delete("all"))

five_btn = Button(text="5", width=10,
                  command=lambda: brush_size_change(5))

ten_btn = Button(text="10", width=10,
                 command=lambda: brush_size_change(10))

twelve_btn = Button(text="12", width=10,
                    command=lambda: brush_size_change(12))

fifteen_btn = Button(text="15", width=10,
                     command=lambda: brush_size_change(15))

label_size = Label(text="Brush size:", width=10)
w.grid(row=2, column=0,
       columnspan=6, padx=5,
       pady=5, sticky=E+W+S+N)

w.columnconfigure(6, weight=2)
w.rowconfigure(2, weight=2)
red_btn.grid(row=0, column=0)
blue_btn.grid(row=0, column=1)
yellow_btn.grid(row=0, column=2)
orange_btn.grid(row=0, column=3)
clear_btn.grid(row=0, column=4)
clear_all_btn.grid(row=0, column=5)

five_btn.grid(row=3, column=1)
ten_btn.grid(row=3, column=2)
twelve_btn.grid(row=3, column=3)
fifteen_btn.grid(row=3, column=4)
label_size.grid(row=3, column=0)
root.mainloop()
