__author__ = 'harsh'
import tkinter as tk

import update



#this file deals from clicking on any right click context menu item
#all the functions binded to the items of the right click context menu
bg_color="#fef1e8"

def id_change(event,org_widget,rc):

    rc.place_forget()                    #closes the right click menu as soon as function is inovoked
    popup=tk.Tk()

    popup.geometry("200x80+%d+%d"%(400,300))

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
    title_lbl=tk.Label(title_bar,text="Change "+org_widget.winfo_class()+" id",background="#6D7993",fg="white")
    title_lbl.place(x=0,y=0)
    title_bar.bind("<Button-1>",StartMove)
    title_lbl.bind("<Button-1>",StartMove)
    title_bar.bind("<B1-Motion>",OnMotion)
    title_lbl.bind("<B1-Motion>",OnMotion)
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

    popup.title("Change "+org_widget.winfo_class()+" id")
    lbl=tk.Label(popup,text=org_widget.winfo_class()+" id",width=200)
    lbl.pack()
    default=tk.StringVar(popup,value=update.find_key(org_widget))     #setting a textvariable for default value of entry widget
    def close_save(event,default):
        #print('in fn',org_widget)
        update.change_key(org_widget,event.widget.get(),default)
        #widget_data.get_data(event.widget,'id',event.widget.get())
        popup.destroy()
    #print('in right click',default)
    Entry=tk.Entry(popup,textvariable=default)
    Entry.select_range(0,tk.END)
    Entry.icursor(tk.END)
    Entry.pack()
    Entry.bind("<Return>", lambda event,arg=default:close_save(event,arg))
    Entry.focus()
    popup.focus_force()
    popup.mainloop()

def copy(event,org_widget,rc,start_btn,motion,stop_btn,l1,l2,r1,r2,u,d,l,r):
    rc.place_forget()
    c=0
    if(org_widget.winfo_class()=="Button"):
        print('copy')
        for i in update.selected_widget:
            B1=tk.Button(org_widget.master,text="Button",height=1,bd=0,width=10,background=bg_color,relief=tk.RAISED)
            B1.bind("<Button-1>",lambda event,arg2=org_widget.master,arg3=rc:start_btn(event,arg2,arg3))
            B1.bind("<ButtonRelease-1>",lambda event,arg2=org_widget.master: stop_btn(event,arg2))
            B1.bind("<B1-Motion>", lambda event,arg=B1,arg2=org_widget.master: motion(event,arg2))
            update.copy_widget=B1      # added this widget in copy_widgets list to paste it when required
            update.init_widget(B1)     # adds to the list of widgets as soon as created
            B1.place(x=i.winfo_x()+10,y=i.winfo_y()+10)
    if(org_widget.winfo_class()=="Entry"):
        print('copy')
        for i in update.selected_widget:   #for all the widgets in the list
            entry=tk.Entry(org_widget.master,background=bg_color)
            entry.bind("<Button-1>",lambda event,arg2=org_widget.master,arg3=rc: start_btn(event,arg2,arg3))
            entry.bind("<ButtonRelease-1>",lambda event,arg2=org_widget.master: stop_btn(event,arg2))
            entry.bind("<B1-Motion>", lambda event,arg=entry,arg2=org_widget.master: motion(event,arg2))
            update.copy_widget=entry      # added this widget in copy_widgets list to paste it when required
            update.init_widget(entry)
            entry.place(x=i.winfo_x()+10,y=i.winfo_y()+10)

def copy_props(event,org_widget,rc,start_btn,motion,stop_btn,l1,l2,r1,r2,u,d,l,r):
    rc.place_forget()
    c=0
    if(org_widget.winfo_class()=="Button"):
        print('copy props')
        B1=tk.Button(org_widget.master,text="Button",height=1,bd=0,width=10,background=bg_color,relief=tk.RAISED)
        B1.bind("<Button-1>",lambda event,arg2=org_widget.master,arg3=rc,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d,a7=l,a8=r:start_btn(event,arg2,arg3,a1,a2,a3,a4,a5,a6,a7,a8))
        B1.bind("<ButtonRelease-1>",lambda event,arg2=org_widget.master: stop_btn(event,arg2))
        B1.bind("<B1-Motion>", lambda event,arg=B1,arg2=org_widget.master,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d,a7=l,a8=r: motion(event,arg2,a1,a2,a3,a4,a5,a6,a7,a8))
        update.copy_widget=B1      # added this widget in copy_widgets list to paste it when required
        copy_properties(org_widget,B1)    #this is called to copy the properties of widgets
        update.init_widget(B1)
        B1.place(x=org_widget.winfo_x(),y=org_widget.winfo_y())
    elif(org_widget.winfo_class()=="Entry"):
        print('copy props')
        B1=tk.Button(org_widget.master,text="Button",height=1,bd=0,width=10,background=bg_color,relief=tk.RAISED)
        B1.bind("<Button-1>",lambda event,arg2=org_widget.master,arg3=rc,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d,a7=l,a8=r:start_btn(event,arg2,arg3,a1,a2,a3,a4,a5,a6,a7,a8))
        B1.bind("<ButtonRelease-1>",lambda event,arg2=org_widget.master: stop_btn(event,arg2))
        B1.bind("<B1-Motion>", lambda event,arg=B1,arg2=org_widget.master,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d,a7=l,a8=r: motion(event,arg2,a1,a2,a3,a4,a5,a6,a7,a8))
        update.copy_widget=B1      # added this widget in copy_widgets list to paste it when required
        copy_properties(org_widget,B1)    #this is called to copy the properties of widgets
        update.init_widget(B1)
        B1.place(x=org_widget.winfo_x(),y=org_widget.winfo_y())
    elif(org_widget.winfo_class()=="Label"):
        print('copy props')
        B1=tk.Button(org_widget.master,text="Button",height=1,bd=0,width=10,background=bg_color,relief=tk.RAISED)
        B1.bind("<Button-1>",lambda event,arg2=org_widget.master,arg3=rc,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d,a7=l,a8=r:start_btn(event,arg2,arg3,a1,a2,a3,a4,a5,a6,a7,a8))
        B1.bind("<ButtonRelease-1>",lambda event,arg2=org_widget.master: stop_btn(event,arg2))
        B1.bind("<B1-Motion>", lambda event,arg=B1,arg2=org_widget.master,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d,a7=l,a8=r: motion(event,arg2,a1,a2,a3,a4,a5,a6,a7,a8))
        update.copy_widget=B1      # added this widget in copy_widgets list to paste it when required
        copy_properties(org_widget,B1)    #this is called to copy the properties of widgets
        update.init_widget(B1)
        B1.place(x=org_widget.winfo_x(),y=org_widget.winfo_y())

def copy_properties(org_widget,new):     #checks each property of the widget and copy it to another
    skip_list=["SystemButtonFace","SystemButtonText","SystemDisabledText","SystemButtonFace","SystemWindowFrame","TkDefaultFont","disabled","none","SystemWindowText","TkTextFont"]
    for i in org_widget.keys():
        print('value',i,org_widget.cget(i))
        # print(org_widget.cget(i) not in skip_list)
        # input()
        #fetches each property of the widget and according to conditions , provides it to the widget that is copied
        if(org_widget.cget(i) not in skip_list):
            if(i=="anchor"):
                new.config(anchor=tk.CENTER)
            elif(i=="background"):
                print(i,org_widget.cget(i))
                new.config(background=str(org_widget.cget(i)))
            elif(i=="bg"):
                print(i,org_widget.cget(i))
                new.config(bg=str(org_widget.cget(i)))
            elif(i=="bd"):
                print(i,org_widget.cget(i))
                new.config(bd=int(org_widget.cget(i)))
            elif(i=="borderwidth"):
                print(i,org_widget.cget(i))
                new.config(borderwidth=int(org_widget.cget(i)))
            elif(i=="height"):
                print(i,org_widget.cget(i))
                new.config(height=int(org_widget.cget(i)))
            elif(i=="width"):
                print(i,org_widget.cget(i))
                new.config(width=int(org_widget.cget(i)))
            elif(i=="highlightthickness"):
                print(i,org_widget.cget(i))
                new.config(highlightthickness=int(str(org_widget.cget(i))))
            elif(i=="padx"):
                print(i,org_widget.cget(i))
                new.config(padx=int(str(org_widget.cget(i))))
            elif(i=="pady"):
                print(i,org_widget.cget(i))
                new.config(pady=int(str(org_widget.cget(i))))
            elif(i=="relief"):
                #left
                print(i,org_widget.cget(i))
                new.config(relief=tk.RAISED)
            elif(i=="repeatdelay"):
                print(i,org_widget.cget(i))
                #print(i,org_widget.cget(i))
                new.config(repeatdelay=int(str(org_widget.cget(i))))
            elif(i=="repeatinterval"):
                print(i,org_widget.cget(i))
                #print(i,org_widget.cget(i))
                new.config(repeatinterval=int(str(org_widget.cget(i))))
            elif(i=="underline"):
                print(i,org_widget.cget(i))
                #print(i,org_widget.cget(i))
                new.config(underline=int(str(org_widget.cget(i))))

            elif(i=="state"):
                #left
                print(i,org_widget.cget(i))
                #print(i,org_widget.cget(i))
                new.config(state=tk.NORMAL)
            elif(i=="text"):
                print(i,org_widget.cget(i))
                #print(i,org_widget.cget(i))
                new.config(text=str(org_widget.cget(i)))
            elif(i=="wraplength"):
                print(i,org_widget.cget(i))
                #print(i,org_widget.cget(i))
                new.config(wraplength=int(str(org_widget.cget(i))))
            elif(i=="justify"):
                print(i,org_widget.cget(i))
                new.config(justify=str(org_widget.cget(i)))
            elif(i=="cursor"):
                print(i,org_widget.cget(i))
                new.config(cursor=str(org_widget.cget(i)))
            elif(i=="insertborderwidth"):
                print(i,org_widget.cget(i))
                new.config(borderwidth=int(str(org_widget.cget(i))))
            elif(i=="insertofftime"):
                print(i,org_widget.cget(i))
                new.config(insertOffTime=int(str(org_widget.cget(i))))
            elif(i=="exportselection"):
                pass
                # print(i,org_widget.cget(i))
                # new.config(exportselection=int(str(org_widget.cget(i))))
            else:
                print(i,org_widget.cget(i))
                new.config(i=str(org_widget.cget(i)))

        #print(i,org_widget.cget(i))
        # if(i=="activebackground"):
        #     print(i,org_widget.cget(i))
        #     print()
        # elif(i=="activeforeground"):
        #     print(i,org_widget.cget(i))
        # elif(i=="anchor"):
        #     print(i,org_widget.cget(i))
        # elif(i=="background"):
        #     print(i,org_widget.cget(i))
        # elif(i=="bd"):
        #     print
        # if(org_widget.cget(i)=="SystemButtonFace" or org_widget.cget(i)=="SystemButtonText"):
        #      continue
        # elif(org_widget.cget(i)=="center"):
        #     print('in')
        #     new.config(i=tk.CENTER)

        # else:
        #     print('')
        #     print(i)
        #     new.config(i=org_widget.cget(i))
def delete(event,org_widget,rc,start_btn,motion,stop_btn,l1,l2,r1,r2,u,d,l,r):
    print('harsh')
    rc.place_forget()
    for i in update.selected_widget:
        i.destroy()
    update.clear_selectiondots()
    l1.place_forget()
    l2.place_forget()
    r1.place_forget()
    r2.place_forget()
    u.place_forget()
    d.place_forget()
    l.place_forget()
    r.place_forget()
    update.remove_wid(org_widget)     #removes the widget from the list of all the widgets


def change_name(event,org_widget,rc,start_btn,motion,stop_btn,l1,l2,r1,r2,u,d,l,r):
    #creating a window and changing the variables[0] of properties tab and also changing the widget name
    import properties_tab

    rc.place_forget()                    #closes the right click menu as soon as function is inovoked
    popup=tk.Tk()

    popup.geometry("200x80+%d+%d"%(400,300))

    popup.overrideredirect(True)


    x_1=0
    y_1=0
    def StartMove(event):   #dragging the window
        global x_1,y_1
        x_1 = event.x
        y_1 = event.y

    def StopMove(event):    #dragging the window
        event.widget.move.x = None
        event.widget.move.y = None

    def OnMotion(event):    #dragging the window
        global x_1,y_1
        deltax = event.x - x_1
        deltay = event.y - y_1
        x = popup.winfo_x() + deltax
        y = popup.winfo_y() + deltay
        popup.geometry("+%s+%s" % (x, y))


    title_bar=tk.Frame(popup,width=200,height=22,background="#6D7993",highlightbackground="#6d7993",highlightthickness=1)
    title_lbl=tk.Label(title_bar,text="Change "+org_widget.winfo_class()+" Name",background="#6D7993",fg="white")
    title_lbl.place(x=0,y=0)
    title_bar.bind("<Button-1>",StartMove)
    title_lbl.bind("<Button-1>",StartMove)
    title_bar.bind("<B1-Motion>",OnMotion)
    title_lbl.bind("<B1-Motion>",OnMotion)
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

    popup.title("Change "+org_widget.winfo_class()+" Name")
    lbl=tk.Label(popup,text=org_widget.winfo_class()+" Name",width=200)
    lbl.pack()
    default=tk.StringVar(popup,value=properties_tab.variables[0].get())     #setting a textvariable for default value of entry widget
    def close_save(event,default):
        #print('in fn',org_widget)
        org_widget.configure(text=event.widget.get())
        properties_tab.variables[0].set(str(event.widget.get()))
        #widget_data.get_data(event.widget,'id',event.widget.get())
        popup.destroy()
    #print('in right click',default)
    Entry=tk.Entry(popup,textvariable=default)
    Entry.select_range(0,tk.END)
    Entry.icursor(tk.END)
    Entry.pack()
    Entry.bind("<Return>", lambda event,arg=default:close_save(event,arg))
    Entry.focus()
    popup.focus_force()
    popup.mainloop()

def command(event,org_widget,rc,start_btn,motion,stop_btn,l1,l2,r1,r2,u,d,l,r):
    print('harsh')
    rc.place_forget()                    #closes the right click menu as soon as function is inovoked
    popup=tk.Tk()

    popup.geometry("200x80+%d+%d"%(400,300))

    popup.overrideredirect(True)


    x_1=0
    y_1=0
    def StartMove(event):   #dragging the window
        global x_1,y_1
        x_1 = event.x
        y_1 = event.y

    def StopMove(event):    #dragging the window
        event.widget.move.x = None
        event.widget.move.y = None

    def OnMotion(event):    #dragging the window
        global x_1,y_1
        deltax = event.x - x_1
        deltay = event.y - y_1
        x = popup.winfo_x() + deltax
        y = popup.winfo_y() + deltay
        popup.geometry("+%s+%s" % (x, y))


    title_bar=tk.Frame(popup,width=200,height=22,background="#6D7993",highlightbackground="#6d7993",highlightthickness=1)
    title_lbl=tk.Label(title_bar,text="Change "+org_widget.winfo_class()+" Name",background="#6D7993",fg="white")
    title_lbl.place(x=0,y=0)
    title_bar.bind("<Button-1>",StartMove)
    title_lbl.bind("<Button-1>",StartMove)
    title_bar.bind("<B1-Motion>",OnMotion)
    title_lbl.bind("<B1-Motion>",OnMotion)
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

    popup.title("Change "+org_widget.winfo_class()+" Name")
    lbl=tk.Label(popup,text=org_widget.winfo_class()+" Name",width=200)
    lbl.pack()
    default=tk.StringVar(popup,value=update.find_command(org_widget))     #setting a textvariable for default value of entry widget
    def close_save(event,default):
        #print('in fn',org_widget)
        #org_widget.configure(text=event.widget.get())
        update.change_command(org_widget,event.widget.get(),default)
        #properties_tab.variables[0].set(str(event.widget.get()))
        #widget_data.get_data(event.widget,'id',event.widget.get())
        popup.destroy()
    #print('in right click',default)
    Entry=tk.Entry(popup,textvariable=default)
    Entry.select_range(0,tk.END)
    Entry.icursor(tk.END)
    Entry.pack()
    Entry.bind("<Return>", lambda event,arg=default:close_save(event,arg))
    Entry.focus()
    popup.focus_force()
    popup.mainloop()

def select_all_specific(event,root,org_widget,rc,start_btn,motion,stop_btn,l1,l2,r1,r2,u,d,l,r):
    rc.place_forget()   #place forget the right click menu

    print(org_widget.master.winfo_children())
    update.clear_selectiondots()
    update.selected_widget.clear()      #clear the selection list before adding new items to the selection list
    length=len(org_widget.master.winfo_children())
    print(length)
    count=0
    print('selected list before select all',update.selected_widget)

    for i in range(0,length):
        if(org_widget.master.winfo_children()[count].winfo_class()==org_widget.winfo_class()):
            widget_main=(org_widget.master.winfo_children()[count])
            print(widget_main)
            count+=1
            l1=tk.Canvas(root,bd=0,highlightthickness=0,height=4,width=4,background="#666666",cursor="ul_angle")   #creation of 6 dots which makes the selected part of the widget
            l2=tk.Canvas(root,bd=0,highlightthickness=0,height=4,width=4,background="#666666",cursor="ll_angle")
            r1=tk.Canvas(root,bd=0,highlightthickness=0,height=4,width=4,background="#666666",cursor="ur_angle")
            r2=tk.Canvas(root,bd=0,highlightthickness=0,height=4,width=4,background="#666666",cursor="lr_angle")
            u=tk.Canvas(root,bd=0,highlightthickness=0,height=4,width=4,background="#666666",cursor="top_tee")
            d=tk.Canvas(root,bd=0,highlightthickness=0,height=4,width=4,background="#666666",cursor="bottom_tee")
            l=tk.Canvas(root,bd=0,highlightthickness=0,height=4,width=4,background="#666666",cursor="left_tee")
            r=tk.Canvas(root,bd=0,highlightthickness=0,height=4,width=4,background="#666666",cursor="right_tee")


            l1.place(x=widget_main.winfo_x()-4,y=widget_main.winfo_y()-6)
            u.place(x=widget_main.winfo_x()-1+(widget_main.winfo_width())/2,y=widget_main.winfo_y()-6)
            r1.place(x=widget_main.winfo_x()-0 + widget_main.winfo_width(),y=widget_main.winfo_y()-6)
            l2.place(x=widget_main.winfo_x()-4,y=widget_main.winfo_y()+widget_main.winfo_height()+2)
            d.place(x=widget_main.winfo_x()-1+(widget_main.winfo_width())/2,y=widget_main.winfo_y()+widget_main.winfo_height()+2)
            r2.place(x=widget_main.winfo_x()+0+widget_main.winfo_width(),y=widget_main.winfo_y()+widget_main.winfo_height()+2)
            r.place(x=widget_main.winfo_x()+0+widget_main.winfo_width(),y=widget_main.winfo_y()+(widget_main.winfo_height()/2)-2)
            l.place(x=widget_main.winfo_x()-4,y=widget_main.winfo_y()+(widget_main.winfo_height()/2)-2)
            update.selectiondots_list.extend([l1,l2,r1,r2,u,d,r,l])   #adding the selection dots to the list to pack.forget() it afterwards

            update.selected_widget.append(widget_main)
    print('selected list in select all',update.selected_widget)

def select_all(event,root,org_widget,rc,start_btn,motion,stop_btn,l1,l2,r1,r2,u,d,l,r):
    rc.place_forget()   #place forget the right click menu

    print(org_widget.master.winfo_children())
    update.clear_selectiondots()
    update.selected_widget.clear()      #clear the selection list before adding new items to the selection list
    length=len(org_widget.master.winfo_children())
    print(length)
    count=0
    print('selected list before select all',update.selected_widget)

    for i in range(0,length):

            widget_main=(org_widget.master.winfo_children()[count])
            print(widget_main)
            count+=1
            l1=tk.Canvas(root,bd=0,highlightthickness=0,height=4,width=4,background="#666666",cursor="ul_angle")   #creation of 6 dots which makes the selected part of the widget
            l2=tk.Canvas(root,bd=0,highlightthickness=0,height=4,width=4,background="#666666",cursor="ll_angle")
            r1=tk.Canvas(root,bd=0,highlightthickness=0,height=4,width=4,background="#666666",cursor="ur_angle")
            r2=tk.Canvas(root,bd=0,highlightthickness=0,height=4,width=4,background="#666666",cursor="lr_angle")
            u=tk.Canvas(root,bd=0,highlightthickness=0,height=4,width=4,background="#666666",cursor="top_tee")
            d=tk.Canvas(root,bd=0,highlightthickness=0,height=4,width=4,background="#666666",cursor="bottom_tee")
            l=tk.Canvas(root,bd=0,highlightthickness=0,height=4,width=4,background="#666666",cursor="left_tee")
            r=tk.Canvas(root,bd=0,highlightthickness=0,height=4,width=4,background="#666666",cursor="right_tee")


            l1.place(x=widget_main.winfo_x()-4,y=widget_main.winfo_y()-6)
            u.place(x=widget_main.winfo_x()-1+(widget_main.winfo_width())/2,y=widget_main.winfo_y()-6)
            r1.place(x=widget_main.winfo_x()-0 + widget_main.winfo_width(),y=widget_main.winfo_y()-6)
            l2.place(x=widget_main.winfo_x()-4,y=widget_main.winfo_y()+widget_main.winfo_height()+2)
            d.place(x=widget_main.winfo_x()-1+(widget_main.winfo_width())/2,y=widget_main.winfo_y()+widget_main.winfo_height()+2)
            r2.place(x=widget_main.winfo_x()+0+widget_main.winfo_width(),y=widget_main.winfo_y()+widget_main.winfo_height()+2)
            r.place(x=widget_main.winfo_x()+0+widget_main.winfo_width(),y=widget_main.winfo_y()+(widget_main.winfo_height()/2)-2)
            l.place(x=widget_main.winfo_x()-4,y=widget_main.winfo_y()+(widget_main.winfo_height()/2)-2)
            update.selectiondots_list.extend([l1,l2,r1,r2,u,d,r,l])   #adding the selection dots to the list to pack.forget() it afterwards

            update.selected_widget.append(widget_main)
    print('selected list in select all',update.selected_widget)

    # def start_multiple(event):
    #     print('inside')
    #     for i in update.selected_widget:
    #
    #         i.drag_start_x=event.x
    #         i.drag_start_y=event.y
    # def motion_multiple(event):
    #     for i in update.selectiondots_list:
    #         i.place_forget()
    #
    #     for i in update.selected_widget:
    #         widget=i
    #         x=widget.winfo_x()-widget.drag_start_x+event.x
    #         y=widget.winfo_y()-widget.drag_start_y+event.y
    #         widget.place(x=x,y=y)
    #
    # def stop_multiple(event):
    #     count=1
        # for i in update.selected_widget:
        #     for j in range(0,8):
        #
        #
        #         if(count%8==1):
        #             update.selectiondots_list[count-1].place(x=i.winfo_x()-4,y=i.winfo_y()-6)
        #         if(count%8==2):
        #             update.selectiondots_list[count-1].place(x=i.winfo_x()-4,y=i.winfo_y()+i.winfo_height()+2)
        #         if(count%8==3):
        #             update.selectiondots_list[count-1].place(x=i.winfo_x()-0 + i.winfo_width(),y=i.winfo_y()-6)
        #         if(count%8==4):
        #             update.selectiondots_list[count-1].place(x=i.winfo_x()+0+i.winfo_width(),y=i.winfo_y()+i.winfo_height()+2)
        #         if(count%8==5):
        #             update.selectiondots_list[count-1].place(x=i.winfo_x()-1+(i.winfo_width())/2,y=i.winfo_y()-6)
        #         if(count%8==6):
        #             update.selectiondots_list[count-1].place(x=i.winfo_x()-1+(i.winfo_width())/2,y=i.winfo_y()+i.winfo_height()+2)
        #         if(count%8==7):
        #             update.selectiondots_list[count-1].place(x=i.winfo_x()+0+i.winfo_width(),y=i.winfo_y()+(i.winfo_height()/2)-2)
        #         if(count%8==0):
        #             update.selectiondots_list[count-1].place(x=i.winfo_x()-4,y=i.winfo_y()+(i.winfo_height()/2)-2)
        #         count+=1
        #         print(count)


    # org_widget.bind("<Button-1>",start_multiple)
    # org_widget.bind("<B1-Motion>",motion_multiple)
    # org_widget.bind("<ButtonRelease-1>",stop_multiple)


