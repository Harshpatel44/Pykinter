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




def name_enter(event):
    widget=event.widget
    global name
    name=widget.get()

    functions.selected.configure(text=widget.get())


def height_enter(event):
    widget=event.widget
    print(widget)
    global height
    height=widget.get()

    #functions.selected.configure(height=widget.get())
    functions.update_h(functions.selected,widget.get())
    #functions.selected.bind("<Return>",lambda a1=functions.selected,a2=functions.g_root,a3=functions.gl1,a4=functions.gl2,a5=functions.gr1,a6=functions.gr2,a7=functions.gu,a8=functions.gd:functions.stop(event,a1,a2,a3,a4,a5,a6,a7,a8))

def width_enter(event):
    widget=event.widget
    global width
    width=widget.get()
    functions.selected.configure(width=widget.get())
    functions.update_w(functions.selected,widget.get())

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
    functions.onfocus_color()    #a special function for on focus color change.