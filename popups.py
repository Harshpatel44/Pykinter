__author__ = 'harsh'
import tkinter as tk
# this file is just for practise and implementation of concepts
popup=tk.Tk()
popup.geometry("200x80+%d+%d"%(300,300))
popup.overrideredirect(True)


x_1=0
y_1=0
def StartMove(event):
    global x_1,y_1
    x_1 = event.x
    y_1 = event.y

def StopMove(event):
    event.widget.move.x = None
    event.widget.move.y = None

def OnMotion(event):
    global x_1,y_1
    deltax = event.x - x_1
    deltay = event.y - y_1
    x = popup.winfo_x() + deltax
    y = popup.winfo_y() + deltay
    popup.geometry("+%s+%s" % (x, y))

title_bar=tk.Frame(popup,width=200,height=22,background="#6D7993",highlightbackground="#6d7993",highlightthickness=1)
title_lbl=tk.Label(title_bar,text="Change Button id",background="#6D7993",fg="white")
title_lbl.place(x=0,y=0)
title_bar.bind("<Button-1>",StartMove)
title_bar.bind("<B1-Motion>",OnMotion)
#title_bar.bind("<B1-Release>",StopMove)

def entering(event):
        widget=event.widget
        widget.configure(background='#CC1166')
def leaving(event):
        widget=event.widget
        widget.configure(background="#333333")
def close(event):
    popup.destroy()
closeButton=tk.Canvas(title_bar,height=10,width=10,background="#333333",relief='flat')
closeButton.place(x=180,y=3)
closeButton.bind('<Enter>',entering)
closeButton.bind("<Button-1>",close)
closeButton.bind('<Leave>',leaving)

title_bar.pack()

popup.title('Change Button id')
lbl=tk.Label(popup,text="Button id",width=200)
lbl.pack()
Entry=tk.Entry(popup)
Entry.pack()
Entry.focus()
popup.mainloop()