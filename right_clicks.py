__author__ = 'harsh'
import tkinter as tk

import update
bg_color="#fef1e8"
def button_id(event,org_widget,rc):

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
    title_lbl=tk.Label(title_bar,text="Change Button id",background="#6D7993",fg="white")
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

    popup.title('Change Button id')
    lbl=tk.Label(popup,text="Button id",width=200)
    lbl.pack()
    default=tk.StringVar(popup,value=update.find_key(org_widget))     #setting a textvariable for default value of entry widget
    def close_save(event,default):
        #print('in fn',org_widget)
        update.change_key(org_widget,event.widget.get(),default)
        #widget_data.get_data(event.widget,'id',event.widget.get())
        popup.destroy()
    #print('in right click',default)
    Entry=tk.Entry(popup,textvariable=default)
    Entry.pack()
    Entry.bind("<Return>", lambda event,arg=default:close_save(event,arg))
    Entry.focus()
    popup.focus_force()
    popup.mainloop()


def copy(event,org_widget,rc,start_btn,motion,stop_btn,l1,l2,r1,r2,u,d,l,r):
    rc.place_forget()
    c=0
    if(org_widget.winfo_class()=="Button"):

        B1=tk.Button(org_widget.master,text="Button",height=1,bd=0,width=10,background=bg_color,relief=tk.RAISED)
        B1.bind("<Button-1>",lambda event,arg2=org_widget.master,arg3=rc,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d,a7=l,a8=r:start_btn(event,arg2,arg3,a1,a2,a3,a4,a5,a6,a7,a8))
        B1.bind("<ButtonRelease-1>",lambda event,arg2=org_widget.master: stop_btn(event,arg2))
        B1.bind("<B1-Motion>", lambda event,arg=B1,arg2=org_widget.master,a1=l1,a2=l2,a3=r1,a4=r2,a5=u,a6=d,a7=l,a8=r: motion(event,arg2,a1,a2,a3,a4,a5,a6,a7,a8))
        update.copy_widget=B1      # added this widget in copy_widgets list to paste it when required
        #copy_properties(org_widget,B1)    #this is called to copy the properties of widgets
        update.init_widget(B1)
        B1.place(x=org_widget.winfo_x(),y=org_widget.winfo_y())

def copy_properties(org_widget,new):
    for i in org_widget.keys():
        #fetches each property of the widget and according to conditions , provides it to the widget that is copied
        print(i,org_widget.cget(i))
        if(org_widget.cget(i)=="SystemButtonFace" or org_widget.cget(i)=="SystemButtonText"):
             continue
        elif(org_widget.cget(i)=="center"):
            print('in')
            new.config(i=tk.CENTER)

        else:
            new.config(i=org_widget.cget(i))


