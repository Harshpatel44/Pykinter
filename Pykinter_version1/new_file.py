import tkinter as tk
def start(event,arg,arg2):

    widget=event.widget
    print(widget)
    widget.drag_start_x=event.x
    widget.drag_start_y=event.y

def motion(event,arg,arg2):
    widget=event.widget

    print(widget)
    x=widget.winfo_x()-widget.drag_start_x+event.x
    y=widget.winfo_y()-widget.drag_start_y+event.y
    app.geometry("400x400+%d+%d"%(x,y))

def entering(event):

    widget=event.widget
    widget.configure(background='#CC1166')
def leaving(event):
    widget=event.widget
    widget.configure(background="#333333")

def maximize(event):
    print("maximize")

def close(event,arg,arg2):
    app.destroy()
    print("destroyed")

class main(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.wm_resizable(self,0,0)
        self.geometry("400x400")
        self.overrideredirect('true')
        container=tk.Frame(self)
        container.pack(side='top',fill='both',expand='true')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames = {}


        for F in (frame1,frame2):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(frame1)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class frame1(tk.Frame,main):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller
        centre_frame=tk.Frame(self,height=400,width=400,background="#FFFFFF",highlightthickness=3,highlightbackground="#555555",relief=tk.SOLID)
        centre_frame.place(x=0,y=0)
        taskbar=tk.Frame(centre_frame,height=20,width=394,background="#555555")
        taskbar.place(x=0,y=0)
        taskbar.bind('<Button-1>',lambda event,arg=self,arg2=main:start(event,arg,arg2))
        taskbar.bind('<B1-Motion>',lambda event,arg=self,arg2=main:motion(event,arg,arg2))

        maximizeButton=tk.Canvas(centre_frame,height=10,width=10,background="#333333",relief='flat')
        maximizeButton.place(x=355,y=2)
        maximizeButton.bind('<Enter>',entering)
        maximizeButton.bind('<Leave>',leaving)
        maximizeButton.bind("<Button-1>",maximize)
        closeButton=tk.Canvas(centre_frame,height=10,width=10,background="#333333",relief='flat')
        closeButton.place(x=375,y=2)
        closeButton.bind('<Enter>',entering)
        closeButton.bind("<Button-1>",lambda event,arg=self,arg2=main:close(event,arg,arg2))
        closeButton.bind('<Leave>',leaving)
        Buttonhina=tk.Button(self,text="hina",height=1,width=10,background="#fef1e8",foreground="SystemButtonText",relief=tk.RAISED,bd=0)
        Buttonhina.place(x=143,y=84)
        ButtonHarsh=tk.Button(self,text="Harsh",height=1,width=10,background="#fef1e8",foreground="SystemButtonText",relief=tk.RAISED,bd=0)
        ButtonHarsh.place(x=140,y=128)
        ButtonTesting=tk.Button(self,text="Testing",height=1,width=10,background="#fef1e8",foreground="SystemButtonText",relief=tk.RAISED,bd=0)
        ButtonTesting.place(x=140,y=175)

class frame2(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller

app=main()
app.mainloop()

