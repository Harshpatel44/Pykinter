__author__ = 'Harsh'

import tkinter as tk
selected=0
g_root=0
import time
#from PIL import ImageTk,Image
import properties_tab


global gl1,gl2,gr1,gr2,gu,gd




def start_frame(event,taskbar,root,l1,l2,r1,r2,u,d):
    widget=root

    global gl1,gl2,gr1,gr2,gu,gd,selected,g_root
    gl1=l1
    gl2=l2
    gr1=r1
    gr2=r2
    gu=u
    gd=d
    selected=root
    g_root=root
    widget.configure(highlightbackground="#222222")
    widget.drag_start_x=event.x
    widget.drag_start_y=event.y



def stop_frame(event,root):
    widget=root

    # gl1.place(x=widget.winfo_x()-8,y=widget.winfo_y()-8)
    # gl2.place(x=widget.winfo_x()-5 + widget.winfo_width(),y=widget.winfo_y()-7)
    # gr1.place(x=widget.winfo_x()-8,y=widget.winfo_y()-5 +widget.winfo_height())
    # gr2.place(x=widget.winfo_x()-5+widget.winfo_width(),y=widget.winfo_y()-5+widget.winfo_height())
    # gu.place(x=widget.winfo_x()-5+(widget.winfo_width())/2,y=widget.winfo_y()-8)
    # gd.place(x=widget.winfo_x()-5+(widget.winfo_width())/2,y=widget.winfo_y()-3 +widget.winfo_height())



def motion_frame(event,taskbar,root):

    widget=root
    x=widget.winfo_x()-widget.drag_start_x+event.x
    y=widget.winfo_y()-widget.drag_start_y+event.y
    widget.place(x=x,y=y)







def start_btn(event,root,l1,l2,r1,r2,u,d):
    widget=event.widget


    global gl1,gl2,gr1,gr2,gu,gd,selected,g_root
    gl1=l1
    gl2=l2
    gr1=r1
    gr2=r2
    gu=u
    gd=d
    selected=widget
    g_root=root


    l1.configure(height=3,width=3,background="#666666")
    l1.place(x=widget.winfo_x()-3,y=widget.winfo_y()-4)

    u.configure(height=3,width=3,background="#666666")
    u.place(x=widget.winfo_x()-0+(widget.winfo_width())/2,y=widget.winfo_y()-4)

    r1.configure(height=3,width=3,background="#666666")
    r1.place(x=widget.winfo_x()-0 + widget.winfo_width(),y=widget.winfo_y()-4)

    l2.configure(height=3,width=3,background="#666666")
    l2.place(x=widget.winfo_x()-2,y=widget.winfo_y()+widget.winfo_height()-0)

    d.configure(height=3,width=3,background="#666666")
    d.place(x=widget.winfo_x()-0+(widget.winfo_width())/2,y=widget.winfo_y()+widget.winfo_height()+1)

    r2.configure(height=3,width=3,background="#666666")
    r2.place(x=widget.winfo_x()-0+widget.winfo_width(),y=widget.winfo_y()+widget.winfo_height())






    # def l1_bindE(event,arg):
    #    widget=event.widget
    #    widget.configure(background="black")
    #    #widget.bind("<Button-1>",lambda event,arg=widget:start_point(event,widget))
    # def l1_bindL(event,arg):
    #    widget=event.widget
    #    widget.configure(background="#666666")
    #
    l1.bind("<Enter>",lambda event,arg=widget:l1_bindE(event,arg))
    l1.bind("<Leave>",lambda event,arg=widget:l1_bindL(event,arg))
    r1.bind("<Enter>",lambda event,arg=widget:l1_bindE(event,arg))
    r1.bind("<Leave>",lambda event,arg=widget:l1_bindL(event,arg))
    l2.bind("<Enter>",lambda event,arg=widget:l1_bindE(event,arg))
    l2.bind("<Leave>",lambda event,arg=widget:l1_bindL(event,arg))
    r2.bind("<Enter>",lambda event,arg=widget:l1_bindE(event,arg))
    r2.bind("<Leave>",lambda event,arg=widget:l1_bindL(event,arg))
    u.bind("<Enter>",lambda event,arg=widget:l1_bindE(event,arg))
    u.bind("<Leave>",lambda event,arg=widget:l1_bindL(event,arg))
    d.bind("<Enter>",lambda event,arg=widget:l1_bindE(event,arg))
    d.bind("<Leave>",lambda event,arg=widget:l1_bindL(event,arg))

    #print(widget)
    widget.drag_start_x=event.x
    widget.drag_start_y=event.y




def stop_btn(event,root):
    widget=event.widget

    gl1.place(x=widget.winfo_x()-3,y=widget.winfo_y()-4)
    gu.place(x=widget.winfo_x()-0+(widget.winfo_width())/2,y=widget.winfo_y()-4)
    gr1.place(x=widget.winfo_x()-0 + widget.winfo_width(),y=widget.winfo_y()-4)
    gl2.place(x=widget.winfo_x()-2,y=widget.winfo_y() +widget.winfo_height())
    gd.place(x=widget.winfo_x()-0+(widget.winfo_width())/2,y=widget.winfo_y()+widget.winfo_height()+1)
    gr2.place(x=widget.winfo_x()-0+widget.winfo_width(),y=widget.winfo_y()+widget.winfo_height())




def motion(event,root):

    widget=event.widget
    x=widget.winfo_x()-widget.drag_start_x+event.x
    y=widget.winfo_y()-widget.drag_start_y+event.y
    widget.place(x=x,y=y)





def update_h(event,h):

    widget=selected
    widget.configure(height=h)
    widget.update()

    gl1.place(x=widget.winfo_x()-3,y=widget.winfo_y()-4)
    gu.place(x=widget.winfo_x()-0+(widget.winfo_width())/2,y=widget.winfo_y()-4)
    gr1.place(x=widget.winfo_x()-0 + widget.winfo_width(),y=widget.winfo_y()-4)
    gl2.place(x=widget.winfo_x()-2,y=widget.winfo_y() +widget.winfo_height())
    gd.place(x=widget.winfo_x()-0+(widget.winfo_width())/2,y=widget.winfo_y()+widget.winfo_height()+1)
    gr2.place(x=widget.winfo_x()-0+widget.winfo_width(),y=widget.winfo_y()+widget.winfo_height())

def update_w(event,w):

    widget=selected
    widget.configure(width=w)
    widget.update()
    time.sleep(0.1)
    gl1.place(x=widget.winfo_x()-3,y=widget.winfo_y()-4)
    gu.place(x=widget.winfo_x()-0+(widget.winfo_width())/2,y=widget.winfo_y()-4)
    gr1.place(x=widget.winfo_x()-0 + widget.winfo_width(),y=widget.winfo_y()-4)
    gl2.place(x=widget.winfo_x()-2,y=widget.winfo_y() +widget.winfo_height())
    gd.place(x=widget.winfo_x()-0+(widget.winfo_width())/2,y=widget.winfo_y()+widget.winfo_height()+1)
    gr2.place(x=widget.winfo_x()-0+widget.winfo_width(),y=widget.winfo_y()+widget.winfo_height())

