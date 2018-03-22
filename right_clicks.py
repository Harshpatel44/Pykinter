__author__ = 'harsh'
import tkinter as tk

def button_id(event,rc):
    rc.place_forget()
    popup=tk.Tk()
    popup.geometry("100x50+%d+%d"%(300,300))
    title_bar=tk.Frame(popup,width="50",height=10,bd=1,background="#444444")
    title_lbl=tk.Label(title_bar,text="Change Button id",foreground="#ffffff")
    title_lbl.pack()
    title_bar.pack()
    popup.title('Change Button id')
    lbl=tk.Label(popup,text="Button id")
    lbl.pack()
    Entry=tk.Entry(popup)
    Entry.pack()
    popup.mainloop()