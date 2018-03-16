import tkinter as tk

rc=''
def menu_start(event,root):
    widget=event.widget
    def first_time():
        global rc
        rc=tk.Canvas(root,height=150,width=120,background="#dddddd",bd=0)
        rc.place(x=widget.winfo_x()+event.x,y=widget.winfo_y()+event.y)
        copy_text=tk.Label(rc,text="Copy")
        copy_text.pack()
        copy_last=tk.Label(rc,text="Properties of Last Widget")
        copy_last.pack()
    first_time()
def menu_close(event,root):
    widget=event.widget
    global rc
    rc.place_forget()
