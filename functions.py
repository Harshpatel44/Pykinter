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
    widget_main=event.widget


    global gl1,gl2,gr1,gr2,gu,gd,selected,g_root
    gl1=l1
    gl2=l2
    gr1=r1
    gr2=r2
    gu=u
    gd=d
    selected=widget_main
    g_root=root


    l1.configure(height=3,width=3,background="#666666",cursor="plus")
    l1.place(x=widget_main.winfo_x()-3,y=widget_main.winfo_y()-4)

    u.configure(height=3,width=3,background="#666666",cursor="plus")
    u.place(x=widget_main.winfo_x()-0+(widget_main.winfo_width())/2,y=widget_main.winfo_y()-4)

    r1.configure(height=3,width=3,background="#666666",cursor="plus")
    r1.place(x=widget_main.winfo_x()-0 + widget_main.winfo_width(),y=widget_main.winfo_y()-4)

    l2.configure(height=3,width=3,background="#666666",cursor="plus")
    l2.place(x=widget_main.winfo_x()-2,y=widget_main.winfo_y()+widget_main.winfo_height()-0)

    d.configure(height=3,width=3,background="#666666",cursor="plus")
    d.place(x=widget_main.winfo_x()-0+(widget_main.winfo_width())/2,y=widget_main.winfo_y()+widget_main.winfo_height()+1)

    r2.configure(height=3,width=3,background="#666666",cursor="plus")
    r2.place(x=widget_main.winfo_x()-0+widget_main.winfo_width(),y=widget_main.winfo_y()+widget_main.winfo_height())






    def l1_bindE(event,arg):
       widget=event.widget

       widget.drag_start_x=event.x
       widget.drag_start_y=event.y
       #widget.bind("<Button-1>",lambda event,arg=widget:start_point(event,widget))
    def l1_bindL(event,arg):
       widget=event.widget
       h_init=arg.cget('height')
       w_init=arg.cget('width')

       # if(event.x<0 or event.y<0):
       #     print('-')
       #     w=arg.cget('width')-(event.x)
       #     h=arg.cget('height')-(event.y)
       #
       #     print('current',arg.cget('width'))
       #     print('width',w)
       # if(event.x>=0 or event.y>0):
       #     print('+')
       #       w=arg.cget('width')+(event.x)
       #       h=arg.cget('height')+(event.y)
       if(event.x<100 and event.x>0):
           event.x=0
       else:
           event.x=1
       if(event.y<100 and event.y>0):event.y=0
       else:
           event.y=1
       w=round(w_init+(event.x))
       h=round(h_init+(event.y))

       #print(w,h)
       arg.configure(width=w,height=h)

    l1.bind("<Button-1>",lambda event,arg=widget_main:l1_bindE(event,arg))
    l1.bind("<B1-Motion>",lambda event,arg=widget_main:l1_bindL(event,arg))
    r1.bind("<Button-1>",lambda event,arg=widget_main:l1_bindE(event,arg))
    r1.bind("<B1-Motion>",lambda event,arg=widget_main:l1_bindL(event,arg))
    l2.bind("<Button-1>",lambda event,arg=widget_main:l1_bindE(event,arg))
    l2.bind("<B1-Motion>",lambda event,arg=widget_main:l1_bindL(event,arg))
    r2.bind("<Button-1>",lambda event,arg=widget_main:l1_bindE(event,arg))
    r2.bind("<B1-Motion>",lambda event,arg=widget_main:l1_bindL(event,arg))
    u.bind("<Button-1>",lambda event,arg=widget_main:l1_bindE(event,arg))
    u.bind("<B1-Motion>",lambda event,arg=widget_main:l1_bindL(event,arg))
    d.bind("<Button-1>",lambda event,arg=widget_main:l1_bindE(event,arg))
    d.bind("<B1-Motion>",lambda event,arg=widget_main:l1_bindL(event,arg))

    #print(widget)
    widget_main.drag_start_x=event.x
    widget_main.drag_start_y=event.y




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

