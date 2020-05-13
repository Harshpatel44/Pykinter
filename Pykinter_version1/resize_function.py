import tkinter as tk

global circle
circle = 0

def motion(event):
    x, y = event.x + 3, event.y + 7  
    #the addition is just to center the oval around the center of the mouse
    #remove the the +3 and +7 if you want to center it around the point of the mouse

    global circle
    global canvas

    canvas.delete(circle)  #to refresh the circle each motion

    radius = 4  #change this for the size of your circle

    x_max = x + radius
    x_min = x - radius
    y_max = y + radius
    y_min = y - radius

    circle = canvas.create_oval(x_max, y_max, x_min, y_min, outline="black")

root = tk.Tk()
root.bind("<Motion>", motion)

global canvas

canvas = tk.Canvas(root)
canvas.pack()

root.mainloop()