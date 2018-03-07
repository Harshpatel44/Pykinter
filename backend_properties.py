__author__ = 'Harsh'

import tkinter as tk
import functions


global fontsize
global name
global height
global width
global fontcolor
global fontstyle
global bg_color
global bd_size
global bd_color


fontsize=10


def check_configure(name_enter,height_enter,width_enter):

    if(functions.selected.winfo_class()=="Entry"):

        name_enter.configure(state=tk.DISABLED)
        height_enter.configure(state=tk.DISABLED)

    if(functions.selected.winfo_class()=="TProgressbar"):

        name_enter.configure(state=tk.DISABLED)
        height_enter.configure(state=tk.DISABLED)

    else:
         name_enter.configure(state=tk.NORMAL)
         height_enter.configure(state=tk.NORMAL)
    #     functions.update_h(widget.get())

def name_enter(event):
    widget=event.widget
    global name
    name=widget.get()
    functions.update_w(functions.selected.cget('width'))
    functions.selected.configure(text=widget.get())

    functions.update_w(functions.selected.cget('width'))


def height_enter(event):
    widget=event.widget
    print(widget)
    global height
    height=widget.get()
    functions.update_h(widget.get())


def width_enter(event):
    widget=event.widget
    global width
    width=widget.get()

    if(functions.selected.winfo_class()=="TProgressbar"):
        functions.selected.configure(length=widget.get())      #condition to change length(width in tk)
        functions.update_w_progressbar(widget.get())     #diffrent function for Progressbar
    else:
        functions.selected.configure(width=widget.get())
        functions.update_w(widget.get())


def fontcolor_enter(event):
    widget=event.widget
    global fontcolor
    fontcolor=widget.get()
    functions.selected.configure(fg=widget.get())


def fontstyle_enter(event):
    widget=event.widget
    global fontsize,fontstyle
    fontstyle=widget.get()
    functions.selected.configure(font=(widget.get(),fontsize))



# def font_enter(event):
#     widget=event.widget
#     widget_change=functions.selected
#     widget_change.configure(font=(widget.get()))






def fontsize_enter(event):
    widget=event.widget
    global fontsize
    fontsize=widget.get()
    functions.selected.configure(font=(widget.cget("font"),fontsize))

def bg_enter(event):
    widget=event.widget

    global bg_color
    bg_color=widget.get()


    functions.selected.configure(background=widget.get())

def bd_enter(event):
    widget=event.widget
    global bd_size
    bd_size=widget.get()
    functions.selected.configure(bd=widget.get())

def bdcolor_enter(event):
    widget=event.widget
    global bd_color
    bd_color=widget.get()
    functions.selected.configure(highlightbackground=widget.get())

def onfocus_bgcolor__enter(event):
    widget=event.widget
    global onfocus_bgcolor
    onfocus_bdcolor=widget.get()
    functions.onfocus_color(onfocus_bdcolor)    #a special function for on focus color change.