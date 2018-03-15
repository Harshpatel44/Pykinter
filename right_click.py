import tkinter as tk


def menu(event,root):
    widget=event.widget
    def first_time():
        canvas=tk.Canvas(root,height=150,width=120,background="#dddddd",bd=0)
        canvas.place(x=widget.winfo_x()+event.x,y=widget.winfo_y()+event.y)

    first_time()
