__author__ = 'Harsh'
import tkinter as tk
import editor_tab
import properties_tab
import widgets_tab
import update

def start(event):
        widget=event.widget
        widget.drag_start_x=0
        widget.drag_start_y=0

def motion(event):
        widget=event.widget
        x=widget.winfo_x()-widget.drag_start_x+event.x
        y=widget.winfo_y()-widget.drag_start_y+event.y
        widget.place(x=x,y=y)


def entering(event):
        widget=event.widget
        widget.configure(background='#CC1166')
def leaving(event):
        widget=event.widget
        widget.configure(background="#333333")

main_instance=0
class main(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        global main_instance
        main_instance=self
        self.h=self.winfo_screenheight()/100.0
        self.w=self.winfo_screenwidth()/100.0
        print(self.w," ",self.h)
        #self.geometry("%dx%d+0+0"%(w,h))
        #self.state('zoomed')
        self.geometry("%dx%d+0+0"%(self.w*100,(self.h*100)-40))
        container = tk.Frame(self)
        container.pack(side='top',fill='both',expand='true')
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.overrideredirect('true')

        self.frames={}
        for f in (main_frame,final_frame,editor_frame):
            frame=f(container,self)
            self.frames[f]=frame
            frame.grid(row=0,column=0,sticky='nsew')
        self.show_frame(main_frame)
    def show_frame(self,con):
        frame=self.frames[con]
        frame.tkraise()

class main_frame(tk.Frame,main):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        tk.controller=controller
        self.tb(self)
        self.mb(self)
        self.ob(self,controller)
        self.eb(self,controller)
        #self.h=main.h
        #self.w=main.w
        self.mf1(self)

        #self.mf2(self)
        #self.mf3(self)

        self.bind('<Button-1>',start)
        self.bind('<B1-Motion>',motion)

    def tb(self,main):

            def maximize(event):
                print("maximize")

            def close(event):
                global main_instance
                self.destroy()
                main_instance.destroy()
                print("destroyed")

            title_bar=tk.Frame(self,height=20,width=1300,highlightthickness=1,relief='solid',background="white",highlightbackground="#555555")
            w = tk.Canvas(self, width=1280, height=20,bg='#6D7993',highlightthickness=0,background="#6D7993")
            w.place(x=0,y=0)


            titleName=tk.Label(self,text="PyKinter",background="White",fg="black")
            titleName.place(x=10,y=1)

            closeButton=tk.Canvas(self,height=10,width=10,background="#333333",relief='flat')
            closeButton.place(x=1260,y=2)
            closeButton.bind('<Enter>',entering)
            closeButton.bind("<Button-1>",close)
            closeButton.bind('<Leave>',leaving)

            maximize=tk.Canvas(self,height=10,width=10,background="#333333",relief='flat')
            maximize.place(x=1240,y=2)
            maximize.bind('<Enter>',entering)
            maximize.bind('<Leave>',leaving)
            maximize.bind("<Button-1>",maximize)
            title_bar.pack()




    def mb(self,main):       #menu bar
        menu_bar=tk.Frame(self,height=23,width=1300,highlightthickness=1,relief='solid',background="white",highlightbackground="#96858F")
        menu_bar.pack()
    def ob(self,main,controller):    #option bar
        option_bar=tk.Frame(self,height=81,width=1300,highlightthickness=1,highlightbackground="#555555",relief='solid',background='#96858F')
        option_bar.pack(side='top')

    def eb(self,main,controller):   #extra bar
        extra_bar=tk.Frame(self,height=25,width=1300,highlightthickness=1,highlightbackground="#555555",relief='solid',background='#6D7993')
        extra_bar.pack()

        editor_button=tk.Button(extra_bar,text="Editor",relief="flat",command=lambda:controller.show_frame(editor_frame))
        editor_button.place(x=400,y=1)
        design_button=tk.Button(extra_bar,text="Design",relief="flat",command=lambda:controller.show_frame(main_frame))
        design_button.place(x=450,y=1)
        save_button=tk.Button(extra_bar,text="Editor",command=lambda:update.save_data)

    def mf1(self,main):

        middle_frame1=tk.Frame(self,height=530,width=230,relief='solid',background="#96858F",highlightthickness=1,highlightbackground="#555555")
        global middle_frame1_instance
        middle_frame1_instance=self

        middle_frame2=tk.Frame(self,height=530,width=750,relief='solid',background="#999999",highlightthickness=1,highlightbackground="#555555")
        middle_frame3=tk.Frame(self,height=530,width=300,relief='solid',background="#d8c9c9",highlightthickness=1,highlightbackground="#555555")

        middle_frame1.pack(side='left')
        middle_frame2.pack(side="left")
        middle_frame3.pack(side='left')


        widgets_tab.wid_tab(self,main,middle_frame1,middle_frame2)   # function for widgets placement
        properties_tab.prop_tab(self,main,middle_frame3,middle_frame2)    #function for properties placement









    # def mf2(self,main):
    #     middle_frame2=tk.Frame(self,height=530,width=730,relief='solid',background="#faf2f2",highlightthickness=1,highlightbackground="#555555")
    #     global middle_frame2_instance
    #     middle_frame2_instance=self
    #     print('frame 2')
    #     middle_frame2.pack(side='left')

class final_frame(tk.Frame,main):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller


class editor_frame(tk.Frame,main):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller
        self.tb(self)
        self.mb(self)
        self.ob(self)
        self.eb(self,controller)
        self.program_area(self)

    def tb(self,main):

            def maximize(event):
                print("maximize")

            def close(event):
                global main_instance
                self.destroy()
                main_instance.destroy()
                print("destroyed")

            title_bar=tk.Frame(self,height=20,width=1300,highlightthickness=1,relief='solid',background="white",highlightbackground="#555555")
            w = tk.Canvas(self, width=1280, height=20,bg='#96858F',highlightthickness=0,background="#9099A2")
            w.place(x=0,y=0)


            titleName=tk.Label(self,text="PyKinter",background="#333333",fg="white")
            titleName.place(x=10,y=1)

            closeButton=tk.Canvas(self,height=10,width=10,background="#333333",relief='flat')
            closeButton.place(x=1260,y=2)
            closeButton.bind('<Enter>',entering)
            closeButton.bind("<Button-1>",close)
            closeButton.bind('<Leave>',leaving)

            maximize=tk.Canvas(self,height=10,width=10,background="#333333",relief='flat')
            maximize.place(x=1240,y=2)
            maximize.bind('<Enter>',entering)
            maximize.bind('<Leave>',leaving)
            maximize.bind("<Button-1>",maximize)
            title_bar.pack()

    def mb(self,main):
        menu_bar=tk.Frame(self,height=23,width=1300,highlightthickness=1,relief='solid',background="white",highlightbackground="#555555")
        menu_bar.pack()

    def ob(self,main):
        option_bar=tk.Frame(self,height=81,width=1300,highlightthickness=1,highlightbackground="#555555",relief='solid',background='#0B3CFD')
        option_bar.pack(side='top')
    def eb(self,main,controller):
        extra_bar=tk.Frame(self,height=25,width=1300,highlightthickness=1,highlightbackground="#555555",relief='solid',background='#96858F')
        extra_bar.pack()

        editor_button=tk.Button(extra_bar,text="Editor",command=lambda:controller.show_frame(editor_frame))
        editor_button.place(x=400,y=1)
        design_button=tk.Button(extra_bar,text="Design",command=lambda:controller.show_frame(main_frame))
        design_button.place(x=450,y=1)
    def program_area(self,main):

        frame1=tk.Frame(self,height=530,width=230,relief='solid',background="#96858F",highlightthickness=1,highlightbackground="#555555")
        frame2=tk.Frame(self,height=530,width=2000,relief='solid',background="#96858F",highlightthickness=1,highlightbackground="#555555")
        frame1.pack(side="left")
        frame2.pack(side="left")
        editor_tab.editor(self,main,frame1,frame2)
        editor_tab.left_side(self,main,frame1,frame2)

app=main()

app.mainloop()



