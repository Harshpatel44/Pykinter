__author__ = 'Harsh'

import tkinter as tk

selected=0
g_root=0
import time
#from PIL import ImageTk,Image
import properties_tab
import backend_properties

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
    selected=root      #selected becomes the clicked element (globally)

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
    properties_tab.sync_widget()
    g_root=root

    print(widget_main.winfo_class())

    l1.configure(height=5,width=5,background="#666666",cursor="plus")
    l1.place(x=widget_main.winfo_x()-4,y=widget_main.winfo_y()-6)

    u.configure(height=5,width=5,background="#666666",cursor="plus")
    u.place(x=widget_main.winfo_x()-1+(widget_main.winfo_width())/2,y=widget_main.winfo_y()-6)

    r1.configure(height=5,width=5,background="#666666",cursor="plus")
    r1.place(x=widget_main.winfo_x()-0 + widget_main.winfo_width(),y=widget_main.winfo_y()-6)

    l2.configure(height=5,width=5,background="#666666",cursor="plus")
    l2.place(x=widget_main.winfo_x()-4,y=widget_main.winfo_y()+widget_main.winfo_height()+2)

    d.configure(height=5,width=5,background="#666666",cursor="plus")
    d.place(x=widget_main.winfo_x()-1+(widget_main.winfo_width())/2,y=widget_main.winfo_y()+widget_main.winfo_height()+2)

    r2.configure(height=5,width=5,background="#666666",cursor="plus")
    r2.place(x=widget_main.winfo_x()+0+widget_main.winfo_width(),y=widget_main.winfo_y()+widget_main.winfo_height()+2)


    global current_x,current_y
    current_x=0
    current_y=0

    def r1_bindE(event,arg):
        widget=event.widget

        widget.drag_start_x=event.x
        widget.drag_start_y=event.y

    def r1_bindM(event,arg):
       global current_x,current_y
       widget=event.widget

       l1.place_forget()   #hiding the selection dots
       l2.place_forget()
       r1.place_forget()
       r2.place_forget()
       u.place_forget()
       d.place_forget()

       if(arg.winfo_class()=='TProgressbar'):


           #print(w_init)
            if(widget.drag_start_x!=event.x):
               if(event.x>current_x):
                   if(event.x%1==0):
                        w=(arg.configure()['length'][4])+3              #arg.configure() contains dictionary of attributes hance length is taken from there
                        arg.configure(length=w)
                        current_x=event.x
               if(event.x<current_x):
                   if(event.x%1==0):
                        w=(arg.configure()['length'][4])-3
                        arg.configure(length=w)
                        current_x=event.x

       elif(arg.winfo_class()=="Entry"):
           #w_init=arg.cget('width')
           if(widget.drag_start_x!=event.x):

               if(event.x>current_x):
                   if(event.x%1==0):
                        w=arg.cget('width')+1
                        arg.configure(width=w)
                        current_x=event.x
               if(event.x<current_x):
                   if(event.x%1==0):
                        w=arg.cget('width')-1
                        arg.configure(width=w)
                        current_x=event.x
       else:

           h_init=arg.cget('height')
           w_init=arg.cget('width')
           if(widget.drag_start_x!=event.x):

               if(event.x>current_x):
                   if(event.x%2==0):
                        w=arg.cget('width')+1
                        arg.configure(width=w)
                        current_x=event.x
               if(event.x<current_x):
                   if(event.x%2==0):
                        w=arg.cget('width')-1
                        arg.configure(width=w)
                        current_x=event.x

           if(widget.drag_start_y!=event.y):

               if(event.y<current_y):
                   if(event.y%5==0):
                        h=arg.cget('height')+1
                        arg.configure(height=h)
                        current_y=event.y

                        arg.place(x=arg.winfo_x(),y=(arg.winfo_y())-15)
                        arg.update()

               if(event.y>current_y):
                   if(event.y%5==0):
                       h=arg.cget('height')-1
                       arg.configure(height=h)
                       current_y=event.y
                       arg.place(x=arg.winfo_x(),y=(arg.winfo_y())+15)


    def r1_bindL(event,arg):
        print()



    def r2_bindE(event,arg):
       widget=event.widget

       widget.drag_start_x=event.x
       widget.drag_start_y=event.y

       #widget.bind("<Button-1>",lambda event,arg=widget:start_point(event,widget))

    def r2_bindM(event,arg):
       global current_x,current_y
       widget=event.widget

       l1.place_forget()   #hiding the selection dots
       l2.place_forget()
       r1.place_forget()
       r2.place_forget()
       u.place_forget()
       d.place_forget()

       if(arg.winfo_class()=='TProgressbar'):


           #print(w_init)
           if(widget.drag_start_x!=event.x):
               if(event.x>current_x):
                   if(event.x%1==0):
                        w=(arg.configure()['length'][4])+3              #arg.configure() contains dictionary of attributes hance length is taken from there
                        arg.configure(length=w)
                        current_x=event.x
               if(event.x<current_x):
                   if(event.x%1==0):
                        w=(arg.configure()['length'][4])-3
                        arg.configure(length=w)
                        current_x=event.x

       elif(arg.winfo_class()=="Entry"):
           #w_init=arg.cget('width')
           if(widget.drag_start_x!=event.x):

               if(event.x>current_x):
                   if(event.x%1==0):
                        w=arg.cget('width')+1
                        arg.configure(width=w)
                        current_x=event.x
               if(event.x<current_x):
                   if(event.x%1==0):
                        w=arg.cget('width')-1
                        arg.configure(width=w)
                        current_x=event.x
       else:

           h_init=arg.cget('height')
           w_init=arg.cget('width')
           if(widget.drag_start_x!=event.x):

               if(event.x>current_x):
                   if(event.x%2==0):
                        w=arg.cget('width')+1
                        arg.configure(width=w)
                        current_x=event.x
               if(event.x<current_x):
                   if(event.x%2==0):
                        w=arg.cget('width')-1
                        arg.configure(width=w)
                        current_x=event.x

           if(widget.drag_start_y!=event.y):

               if(event.y>current_y):
                   if(event.y%3==0):
                        h=arg.cget('height')+1
                        arg.configure(height=h)
                        current_y=event.y

               if(event.y<current_y):
                   if(event.y%3==0):
                       if(arg.cget('height')==1):
                           pass
                       else:
                           h=arg.cget('height')-1
                           arg.configure(height=h)
                           current_y=event.y

    def r2_bindL(event,arg):
        #arg.configure(width=10,height=1)
        if(arg.winfo_class()=='Entry'):
            update_w(arg.cget('width'))
        elif(arg.winfo_class()=='TProgressbar'):
            update_w_progressbar(arg.cget('length'))
        else:
            update_h(arg.cget('height'))
            update_w(arg.cget('width'))


    l1.bind("<Button-1>",lambda event,arg=widget_main:l1_bindE(event,arg))
    l1.bind("<B1-Motion>",lambda event,arg=widget_main:l1_bindL(event,arg))
    l1.bind("<ButtonRelease-1>",lambda event,arg=widget_main:l1_bindR(event,arg))
    r1.bind("<Button-1>",lambda event,arg=widget_main:r1_bindE(event,arg))
    r1.bind("<B1-Motion>",lambda event,arg=widget_main:r1_bindM(event,arg))
    r1.bind("<ButtonRelease-1>",lambda event,arg=widget_main:r1_bindL(event,arg))
    l2.bind("<Button-1>",lambda event,arg=widget_main:l1_bindE(event,arg))
    l2.bind("<B1-Motion>",lambda event,arg=widget_main:l1_bindL(event,arg))
    l2.bind("<ButtonRelease-1>",lambda event,arg=widget_main:l1_bindR(event,arg))
    r2.bind("<Button-1>",lambda event,arg=widget_main:r2_bindE(event,arg))
    r2.bind("<B1-Motion>",lambda event,arg=widget_main:r2_bindM(event,arg))
    r2.bind("<ButtonRelease-1>",lambda event,arg=widget_main:r2_bindL(event,arg))
    u.bind("<Button-1>",lambda event,arg=widget_main:l1_bindE(event,arg))
    u.bind("<B1-Motion>",lambda event,arg=widget_main:l1_bindL(event,arg))
    u.bind("<ButtonRelease-1>",lambda event,arg=widget_main:l1_bindR(event,arg))
    d.bind("<Button-1>",lambda event,arg=widget_main:l1_bindE(event,arg))
    d.bind("<B1-Motion>",lambda event,arg=widget_main:l1_bindL(event,arg))
    d.bind("<ButtonRelease-1>",lambda event,arg=widget_main:l1_bindR(event,arg))
    #print(widget)
    widget_main.drag_start_x=event.x
    widget_main.drag_start_y=event.y




def stop_btn(event,root):    #invokes when drag is stopped.
    widget=event.widget

    gl1.place(x=widget.winfo_x()-4,y=widget.winfo_y()-6)
    gu.place(x=widget.winfo_x()-1+(widget.winfo_width())/2,y=widget.winfo_y()-6)
    gr1.place(x=widget.winfo_x()-0 + widget.winfo_width(),y=widget.winfo_y()-6)
    gl2.place(x=widget.winfo_x()-4,y=widget.winfo_y()+widget.winfo_height()+2)
    gd.place(x=widget.winfo_x()-1+(widget.winfo_width())/2,y=widget.winfo_y()+widget.winfo_height()+2)
    gr2.place(x=widget.winfo_x()+0+widget.winfo_width(),y=widget.winfo_y()+widget.winfo_height()+2)




def motion(event,root,l1,l2,r1,r2,u,d):    #motion of widget

    widget=event.widget
    x=widget.winfo_x()-widget.drag_start_x+event.x
    y=widget.winfo_y()-widget.drag_start_y+event.y
    l1.place_forget()
    l2.place_forget()
    r1.place_forget()
    r2.place_forget()
    u.place_forget()
    d.place_forget()
    widget.place(x=x,y=y)






def update_h(h):   #changing height dynamically

    widget=selected
    widget.invoke()
    widget.configure(height=h)
    widget.update()

    gl1.place(x=widget.winfo_x()-4,y=widget.winfo_y()-6)
    gu.place(x=widget.winfo_x()-1+(widget.winfo_width())/2,y=widget.winfo_y()-6)
    gr1.place(x=widget.winfo_x()-0 + widget.winfo_width(),y=widget.winfo_y()-6)
    gl2.place(x=widget.winfo_x()-4,y=widget.winfo_y()+widget.winfo_height()+2)
    gd.place(x=widget.winfo_x()-1+(widget.winfo_width())/2,y=widget.winfo_y()+widget.winfo_height()+2)
    gr2.place(x=widget.winfo_x()+0+widget.winfo_width(),y=widget.winfo_y()+widget.winfo_height()+2)

def update_w(w):    #changing width dyanmically

    widget=selected

    widget.configure(width=w)
    widget.update()
    time.sleep(0.1)
    gl1.place(x=widget.winfo_x()-4,y=widget.winfo_y()-6)
    gu.place(x=widget.winfo_x()-1+(widget.winfo_width())/2,y=widget.winfo_y()-6)
    gr1.place(x=widget.winfo_x()-0 + widget.winfo_width(),y=widget.winfo_y()-6)
    gl2.place(x=widget.winfo_x()-4,y=widget.winfo_y()+widget.winfo_height()+2)
    gd.place(x=widget.winfo_x()-1+(widget.winfo_width())/2,y=widget.winfo_y()+widget.winfo_height()+2)
    gr2.place(x=widget.winfo_x()+0+widget.winfo_width(),y=widget.winfo_y()+widget.winfo_height()+2)

def update_w_progressbar(w):    #changing width dyanmically

    widget=selected

    widget.configure(length=w)
    widget.update()
    time.sleep(0.1)
    gl1.place(x=widget.winfo_x()-3,y=widget.winfo_y()-4)
    gu.place(x=widget.winfo_x()-1+(widget.winfo_width())/2,y=widget.winfo_y()-4)
    gr1.place(x=widget.winfo_x()-0 + widget.winfo_width(),y=widget.winfo_y()-4)
    gl2.place(x=widget.winfo_x()-4,y=widget.winfo_y()+widget.winfo_height()+2)
    gd.place(x=widget.winfo_x()-1+(widget.winfo_width())/2,y=widget.winfo_y()+widget.winfo_height()+2)
    gr2.place(x=widget.winfo_x()+0+widget.winfo_width(),y=widget.winfo_y()+widget.winfo_height()+2)

def widget_focus(color_bg,color_text,flag):

    #only one of the 2 things will work at the same time hence , if we fill one ..other entry should be disabled showing this error

        current_color_bg=''
        current_color_text=''
        if(flag==0):

            print(flag)
            current_color_bg=selected.cget('background')
        if(flag==1):
            print(flag)
            current_color_text=selected.cget('fg')
            print('current text:',current_color_text)

        def focus_change(event,new_bg,new_text,number):

            if(number==0):
                event.widget.configure(background=str(new_bg),fg=event.widget.cget('fg'))
                event.widget.update()



            if(number==1):
                event.widget.configure(fg=str(new_text),background=event.widget.cget('background'))
                event.widget.update()


        def focus_reset(event,old_bg,old_text,number):

            if(number==0):
                event.widget.configure(background=old_bg,fg=event.widget.cget('fg'))
                event.widget.update()

            if(number==1):
                print(old_text)
                event.widget.configure(fg=str(old_text),background=event.widget.cget('background'))
                event.widget.update()



        selected.bind('<Enter>',lambda event,arg=color_bg,arg2=color_text,arg3=flag:focus_change(event,arg,arg2,arg3))     #selected is the current widget
        selected.bind('<Leave>',lambda event,arg=current_color_bg,arg2=current_color_text,arg3=flag:focus_reset(event,arg,arg2,arg3))




