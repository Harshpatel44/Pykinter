__author__ = 'Harsh'
from tkinter import  ttk
import tkinter as tk
import functions
import properties_tab
import update

bg_color="#fef1e8"

def allTime(root):
    global l1,l2,r1,r2,u,d,rect
    l1=tk.Canvas(root,bd=0,highlightthickness=0)   #creation of 6 dots which makes the selected part of the widget
    l1.place_forget()
    l2=tk.Canvas(root,bd=0,highlightthickness=0)
    l2.place_forget()    # to hide the widget
    r1=tk.Canvas(root,bd=0,highlightthickness=0)
    r1.place_forget()
    r2=tk.Canvas(root,bd=0,highlightthickness=0)
    r2.place_forget()
    u=tk.Canvas(root,bd=0,highlightthickness=0)
    u.place_forget()
    d=tk.Canvas(root,bd=0,highlightthickness=0)
    d.place_forget()
    #rect=root.create_rectangle(0,0,200,200,fill="red")



def moveIn_MF(event,arg):     #when pressed in middle frame , to hide the selection
    widget=event.widget
    widget.bind("<Button-1>",lambda event:forget_all(arg))

def forget_all(root):          # to hide the selection dots
     l1.place_forget()
     l2.place_forget()
     r1.place_forget()
     r2.place_forget()
     u.place_forget()
     d.place_forget()
     root.configure(highlightbackground="#555555")


def startMultiSelect(event):
    l1.place_forget()
    l2.place_forget()
    r1.place_forget()
    r2.place_forget()
    u.place_forget()
    d.place_forget()

def moveIn_Frame(event_main,centre_frame,taskbar,working_window):              #bindings when we enter in centre frame

    working_window.bind("<Button-1>",lambda event,arg=working_window:startMultiSelect(centre_frame))    #to hide the selection_lines when clicked on the frame
    #provide motion and drag the main_frame when taskbar is dragged
    taskbar.bind("<Button-1>",lambda event,arg=taskbar,arg2=centre_frame,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d: functions.start_frame(event,arg,arg2,a1,a2,a3,a4,a5,a6))
    taskbar.bind("<B1-Motion>",lambda event,arg=taskbar,arg2=centre_frame: functions.motion_frame(event,arg,arg2))
    taskbar.bind("<ButtonRelease-1>",lambda event,arg2=centre_frame: functions.stop_frame(event,arg2))

def button(root):           #bindings for buttons

    B1=tk.Button(root,text="Button",height=1,bd=0,highlightthickness=5,highlightbackground="black",width=10,background=bg_color,relief=tk.RAISED)
    B1.bind("<Button-1>",lambda event,arg2=root,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d: functions.start_btn(event,arg2,a1,a2,a3,a4,a5,a6))
    B1.bind("<ButtonRelease-1>",lambda event,arg2=root: functions.stop_btn(event,arg2))
    B1.bind("<B1-Motion>", lambda event,arg=B1,arg2=root: functions.motion(event,arg2))
    update.get_data(B1)
    B1.place(x=10,y=10)


def check_button(root):         #bindings for check buttons
    check=tk.Checkbutton(root,text="Button",height=1,bd=1,width=10,background=bg_color)
    check.bind("<Button-1>",lambda event,arg2=root,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d: functions.start_btn(event,arg2,a1,a2,a3,a4,a5,a6))
    check.bind("<ButtonRelease-1>",lambda event,arg2=root: functions.stop_btn(event,arg2))
    check.bind("<B1-Motion>", lambda event,arg2=root: functions.motion(event,arg2))
    update.get_data(check)
    check.place(x=10,y=10)

def radio_button(root):         #bindings for radio button
    radio=tk.Radiobutton(root,text="Button",height=1,bd=1,width=10,background=bg_color)
    radio.bind("<Button-1>",lambda event,arg2=root,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d: functions.start_btn(event,arg2,a1,a2,a3,a4,a5,a6))
    radio.bind("<ButtonRelease-1>",lambda event,arg2=root: functions.stop_btn(event,arg2))
    radio.bind("<B1-Motion>",lambda event , arg2=root: functions.motion(event,arg2))
    update.get_data(radio)
    radio.place(x=10,y=10)

def entry_button(root):         # bindings for entry button
    entry=tk.Entry(root,background=bg_color)
    entry.bind("<Button-1>",lambda event,arg2=root,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d: functions.start_btn(event,arg2,a1,a2,a3,a4,a5,a6))
    entry.bind("<ButtonRelease-1>",lambda event,arg2=root: functions.stop_btn(event,arg2))
    entry.bind("<B1-Motion>",lambda event , arg2=root: functions.motion(event,arg2))
    update.get_data(entry)
    entry.place(x=10,y=10)

def label_click(root):          #bindings for label click
    label=tk.Label(root,text="Label",background=bg_color)
    label.bind("<Button-1>", lambda event,arg2=root,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d: functions.start_btn(event,arg2,a1,a2,a3,a4,a5,a6))
    label.bind("<ButtonRelease-1>",lambda event,arg2=root: functions.stop_btn(event,arg2))
    label.bind("<B1-Motion>", lambda event , arg2=root: functions.motion(event,arg2))
    update.get_data(label)
    label.place(x=10,y=10)


def scroll_click(root):         #bindings for scroll click
    scrollbar=tk.Scrollbar(root)
    scrollbar.bind("<Button-1>",lambda event,arg2=root,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d: functions.start_btn(event,arg2,a1,a2,a3,a4,a5,a6))
    scrollbar.bind("<ButtonRelease-1>",lambda event,arg2=root: functions.stop_btn(event,arg2))
    scrollbar.bind("<B1-Motion>", lambda event , arg2=root: functions.motion(event,arg2))
    scrollbar.place(x=10,y=10)


def dropmenu_click(root):         #bindings for option menu
    scrollbar=tk.OptionMenu(root)
    scrollbar.bind("<Button-1>",lambda event,arg2=root,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d: functions.start_btn(event,arg2,a1,a2,a3,a4,a5,a6))
    scrollbar.bind("<ButtonRelease-1>",lambda event,arg2=root: functions.stop_btn(event,arg2))
    scrollbar.bind("<B1-Motion>", lambda event , arg2=root: functions.motion(event,arg2))
    scrollbar.place(x=10,y=10)

def combobox_click(root):
    combobox=ttk.Combobox(root)
    combobox.bind("<Button-1>",lambda event,arg2=root,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d: functions.start_btn(event,arg2,a1,a2,a3,a4,a5,a6))
    combobox.bind("<ButtonRelease-1>",lambda event,arg2=root: functions.stop_btn(event,arg2))
    combobox.bind("<B1-Motion>", lambda event , arg2=root: functions.motion(event,arg2))
    combobox.place(x=10,y=10)


def progressbar_click(root):
    progressbar=ttk.Progressbar(root)
    progressbar.bind("<Button-1>",lambda event,arg2=root,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d: functions.start_btn(event,arg2,a1,a2,a3,a4,a5,a6))
    progressbar.bind("<ButtonRelease-1>",lambda event,arg2=root: functions.stop_btn(event,arg2))
    progressbar.bind("<B1-Motion>", lambda event , arg2=root: functions.motion(event,arg2))
    progressbar.place(x=10,y=10)



def listbox_click(root):
    listbox=tk.Listbox(root)
    listbox.bind("<Button-1>",lambda event,arg2=root,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d: functions.start_btn(event,arg2,a1,a2,a3,a4,a5,a6))
    listbox.bind("<ButtonRelease-1>",lambda event,arg2=root: functions.stop_btn(event,arg2))
    listbox.bind("<B1-Motion>", lambda event , arg2=root: functions.motion(event,arg2))
    listbox.place(x=10,y=10)


def image_click(root):
    imagecanvas=tk.Button(root)
    imagecanvas.configure(height="10",width="40",relief="flat",bd=0,text="CLICK HERE",fg="black")

    imagecanvas.bind("<Button-1>",lambda event,arg2=root,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d: functions.start_btn(event,arg2,a1,a2,a3,a4,a5,a6))
    imagecanvas.bind("<ButtonRelease-1>",lambda event,arg2=root: functions.stop_btn(event,arg2))
    imagecanvas.bind("<B1-Motion>", lambda event , arg2=root: functions.motion(event,arg2))
    imagecanvas.place(x=10,y=10)




def spinbox_click(root):
    spinbox=tk.Spinbox(root)
    spinbox.bind("<Button-1>",lambda event,arg2=root,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d: functions.start_btn(event,arg2,a1,a2,a3,a4,a5,a6))
    spinbox.bind("<ButtonRelease-1>",lambda event,arg2=root: functions.stop_btn(event,arg2))
    spinbox.bind("<B1-Motion>", lambda event , arg2=root: functions.motion(event,arg2))
    spinbox.place(x=10,y=10)


