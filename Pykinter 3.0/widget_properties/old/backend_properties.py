
import tkinter as tk
from widgets.old import functions
from old.program_editor import update

global fontsize
global name
global height
global width
global fontcolor
global fontstyle
global bg_color
global bd_size
global bd_color
global onfocus_bdcolor
global onfocus_textclor
global counter_bold

counter_bold=0

fontsize=10


def check_configure(name_enter,height_enter,fontstyle_enter):

    if(functions.selected.winfo_class()== "Entry"):

        name_enter.configure(state=tk.DISABLED)
        height_enter.configure(state=tk.DISABLED)
        fontstyle_enter.configure(state=tk.DISABLED)



        functions.selected.update()

    elif(functions.selected.winfo_class() == "TProgressbar"):

        name_enter.configure(state=tk.DISABLED)
        height_enter.configure(state=tk.DISABLED)

   # elif(functions.selected.winfo_class()=="")
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
    #update.save_widget_props(selected,he,ne,we,fce,fse,fsie,bdn,bcn,bce)

def height_enter(event):
    widget=event.widget

    global height
    height=widget.get()
    functions.update_h(widget.get())
    update.save_widget_props(selected, he, ne, we, fce, fse, fsie, bdn, bcn, bce)

def width_enter(event):
    widget=event.widget
    global width
    width=widget.get()

    if(functions.selected.winfo_class()== "TProgressbar"):
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


    functions.selected.configure(font=(widget.get(), fontsize))




def fontsize_enter(event):
    widget=event.widget
    global fontsize
    fontsize=widget.get()

    functions.selected.configure(font=(widget.cget("font"), fontsize))

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

def onfocus_bgcolor__enter(event,number):   #number 1 for bgcolor and number 2 for textcolor
    widget=event.widget
    onfocus_bdcolor=''
    onfocus_textcolor=''     #onfocus textcolor

    if(number==0):
        onfocus_bdcolor=widget.get()
    if(number==1):
        onfocus_textcolor=widget.get()

    functions.widget_focus(onfocus_bdcolor, onfocus_textcolor, number)    #a special function for on focus color change.

def cursor_change(value):
    print(value)


def window_naming(event,name):
    #widgets_tab.wid_tab().title_label.configure(text=name)
    print(name)





def window_icon(value):
    print(value)

def taskbar_icon(value):
    print(value)

def taskbar_colorchange(event):
    print(event)

def taskbar_borderchange(event):
    print(event)

def taskbar_heightchange(event):
    print(event)

def taskbar_widthchange(event):
    print(event)



def enter_X(event):
    print(event)

def enter_Y(event):
    print(event)

def cursor_sizechange(event):
    print(event)

def Font_styling(event,number):
    print("Reached fontstyling")
    global counter_bold


    widget=event.widget
    # print(widget.cget("font"))
    #
    # Font_style_bold=widget.cget("font")
    # Font_style_italic=widget.cget("font")
    # Font_style_underline=widget.cget("font")



    if number==0:

       functions.selected.configure(font=(widget.cget("font"), fontsize, "bold"))
    if number==1:
       functions.selected.configure(font=(widget.cget("font"), fontsize, "italic"))
    if number==2:
       functions.selected.configure(font=(widget.cget("font"), fontsize, "underline"))

    #functions.font_styling_change(Font_style_bold,Font_style_italic,Font_style_underline,number)


