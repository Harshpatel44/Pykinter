__author__ = 'Harsh'


import tkinter as tk
from widgets import first_click
from application_standards import constants as const


class WidgetsTab:
    def __init__(self, main):
        self.main = main
        self.widget_area_width = self.main.w*const.widget_frame_width
        self.widget_area_height = self.main.h * const.widget_area_height
        self.button_width = self.main.h * const.button_width
        self.button_height = self.main.h * const.button_height
        self.tab_gui()

    def tab_gui(self):
        """ Creating UI Layout"""

        # def on_configure(event):
        #     """ update scrollregion after starting 'mainloop', when all widgets are in canvas """
        #     widget_area_canvas.configure(scrollregion=widget_area_canvas.bbox('all'))

        title = tk.Frame(self.main.widget_frame, height=self.main.h*const.widget_frame_width, width=self.main.w*const.widget_frame_width, bd=1, relief="raised", background=const.bg_color,
                 highlightbackground=const.main_border)
        title.pack(side="top", fill="both", expand=1)

        # widget_area_canvas= tk.Canvas(self.main.widget_frame,scrollregion=(0,0,600,600),
        #                               width=self.widget_area_width,
        #                               height=self.widget_area_height)
        #
        # scrollbar=tk.Scrollbar(self.main.widget_frame,command=widget_area_canvas.yview)
        # scrollbar.place(x=231,y=26,height=self.widget_area_height)
        #
        # widget_area_canvas.configure(yscrollcommand=scrollbar.set)
        # widget_area_canvas.bind('<Configure>', on_configure)
        # widget_area_canvas.pack(side="top")

        widget_frame=tk.Frame(self.main.widget_frame, background=const.bg_color, width=self.widget_area_width,
                                      height=self.widget_area_height)
        # widget_area_canvas.create_window((0,0),window=widget_frame,anchor='nw')

        """ UI Layout Complete """

        title_label = tk.Label(title, text="Widgets", background = const.bg_color, fg=const.primary_font_color)
        title_label.config(font=(const.primary_font, 9))
        title_label.pack()


        button=tk.Button(widget_frame,text="Button",height=1,width=10, bd=0, background="#6D7993",fg="#FFFFFF",
                         relief=tk.SUNKEN, command=lambda: first_click.button(working_window,self.main.dev_frame))
        button.config(font=('Copperplate Gothic Light',12))
        button.pack( pady=5, padx = 5)
        widget_frame.pack(side="top")
        #
        # tool_button=tk.Button(widget_frame,text="Tool Button",height=1,width=10, bd=0, background="#6D7993",fg="#FFFFFF",
        #                       relief=tk.RAISED)
        # tool_button.config(font=('Copperplate Gothic Light',12))
        # tool_button.pack(side="top", pady=5, padx = 5)
        #
        # radio_button=tk.Button(widget_frame,text="Radio Button",height=1,bd=0,width=15,background="#6D7993",fg="#FFFFFF",relief=tk.SUNKEN,command= lambda: first_click.radio_button(working_window))
        # radio_button.config(font=('Copperplate Gothic Light',12))
        # radio_button.place(x=10,y=90)
        #
        # check_button=tk.Button(widget_frame,text="Check Button",height=1,bd=0,width=15,background="#6D7993",fg="#FFFFFF",relief=tk.GROOVE,command= lambda: first_click.check_button(working_window))
        # check_button.config(font=('Copperplate Gothic Light',12))
        # check_button.place(x=10,y=120)
        #
        # entrybox=tk.Button(widget_frame,text="Entry Box",height=1,bd=0,width=15,background="#6D7993",fg="#FFFFFF",relief=tk.SOLID,command= lambda: first_click.entry_button(working_window))
        # entrybox.config(font=('Copperplate Gothic Light',12))
        # entrybox.place(x=10,y=150)
        #
        # label=tk.Button(widget_frame,text="Label",height=1,bd=0,width=15,background="#6D7993",fg="#FFFFFF",relief="solid",command=lambda:first_click.label_click(working_window))
        # label.config(font=('Copperplate Gothic Light',12))
        # label.place(x=10,y=180)
        #
        # scroll_bar=tk.Button(widget_frame,text="Scroll Bar",height=1,bd=0,width=15,background="#6D7993",fg="#FFFFFF",relief="solid",command=lambda:first_click.scroll_click(working_window))
        # scroll_bar.config(font=('Copperplate Gothic Light',12))
        # scroll_bar.place(x=10,y=210)
        #
        # progress_bar=tk.Button(widget_frame,text="Progress Bar",height=1,bd=0,width=15,background="#6D7993",fg="#FFFFFF",relief="solid",command=lambda:first_click.progressbar_click(working_window))
        # progress_bar.config(font=('Copperplate Gothic Light',12))
        # progress_bar.place(x=10,y=240)
        #
        # spin_box=tk.Button(widget_frame,text="Spin Box",height=1,bd=0,width=15,background="#6D7993",fg="#FFFFFF",relief="solid",command=lambda:first_click.spinbox_click(working_window))
        # spin_box.config(font=('Copperplate Gothic Light',12))
        # spin_box.place(x=10,y=270)
        #
        # combo_box=tk.Button(widget_frame,text="Combo Box",height=1,bd=0,width=15,background="#6D7993",fg="#FFFFFF",relief="solid",command=lambda:first_click.combobox_click(working_window))
        # combo_box.config(font=('Copperplate Gothic Light',12))
        # combo_box.place(x=10,y=300)
        #
        # drop_view=tk.Button(widget_frame,text="Drop View",height=1,bd=0,width=15,background="#6D7993",fg="#FFFFFF",relief="solid",command=lambda:first_click.dropmenu_click(working_window))
        # drop_view.config(font=('Copperplate Gothic Light',12))
        # drop_view.place(x=10,y=330)
        #
        # list_view=tk.Button(widget_frame,text="List View",height=1,bd=0,width=15,background="#6D7993",fg="#FFFFFF",relief="solid",command=lambda:first_click.listbox_click(working_window))
        # list_view.config(font=('Copperplate Gothic Light',12))
        # list_view.place(x=10,y=360)
        #
        # frame=tk.Button(widget_frame,text="Frame",height=1,bd=0,width=15,background="#6D7993",fg="#FFFFFF",relief="solid")
        # frame.config(font=('Copperplate Gothic Light',12))
        # frame.place(x=10,y=390)
        #
        # spiner=tk.Button(widget_frame,text="Spiner",height=1,bd=0,width=15,background="#6D7993",fg="#FFFFFF",relief="solid")
        # spiner.config(font=('Copperplate Gothic Light',12))
        # spiner.place(x=10,y=420)
        #
        # shapes=tk.Button(widget_frame,text="Shapes",height=1,bd=0,width=15,background="#6D7993",fg="#FFFFFF",relief="solid")
        # shapes.config(font=('Copperplate Gothic Light',12))
        # shapes.place(x=10,y=450)
        #
        # image_insert=tk.Button(widget_frame,text="Image",height=1,bd=0,width=15,background="#6D7993",fg="#FFFFFF",relief="solid",command=lambda:first_click.image_click(working_window))
        # image_insert.config(font=('Copperplate Gothic Light',12))
        # image_insert.place(x=10,y=480)




        """ dev window code """

        # centre_frame=tk.Frame(self.main.dev_frame,height=400,width=400,background="#6D7993",highlightthickness=3,highlightbackground="#555555",relief=tk.SOLID)
        # centre_frame.place(x=100,y=100)
        #
        # taskbar=tk.Frame(centre_frame,height=20,width=394,background="#9099A2")
        # taskbar.place(x=0,y=0)
        # maximizeButton=tk.Canvas(centre_frame,height=10,width=10,background="#333333",relief='flat')
        # maximizeButton.place(x=355,y=2)
        # closeButton=tk.Canvas(centre_frame,height=10,width=10,background="#333333",relief='flat')
        # closeButton.place(x=375,y=2)
        #
        #
        # working_window=tk.Canvas(centre_frame,height=374,width=394,highlightthickness=0,bd=0,background="#ffffff")
        # working_window.place(x=0,y=20)


        # title_label=tk.Label(centre_frame,text=" ")
        # title_label.place(x=7,y=1)
        # centre_frame.bind("<Enter>",lambda event,arg=centre_frame,arg2=taskbar,arg3=working_window:first_click.moveIn_Frame(event,arg,arg2,arg3))    #bindings when entered in frame
        # self.main.dev_frame.bind('<Enter>',lambda event,arg=centre_frame:first_click.moveIn_MF(event,arg))

        #Creating a centre_frame and changing the coordinates on binding

        # def change_x(event):
        #     widget=event.widget
        #     w=(int(widget.get())/1920.0)*700
        #     centre_frame.configure(width=w)
        #     working_window.configure(width=w-6)
        #     taskbar.configure(width=w-6)
        #     maximizeButton.place(x=w-45)
        #     closeButton.place(x=w-25)
        #
        # def change_y(event):
        #     widget=event.widget
        #
        #     h=(int(widget.get())/1080.0)*480
        #
        #     centre_frame.configure(height=h)
        #     working_window.configure(height=h-26)
        #
        # first_click.allTime(working_window,self.main.dev_frame,centre_frame)    #by default initializing selections lines using this function

        #
        # screenx_name=tk.Label(self.main.dev_frame,text="X:",width=2,bd=1,background="#333333",fg="#fef1e8")
        # screenx_name.place(x=1,y=0)
        #
        # screenx=tk.Entry(self.main.dev_frame,width=5,background="#999999")
        # screenx.bind("<Return>",change_x)
        # screenx.place(x=20,y=0)
        #
        # screeny_name=tk.Label(self.main.dev_frame,text="Y:",width=2,bd=1,background="#333333",fg="#fef1e8")
        # screeny_name.place(x=55,y=0)
        #
        # screeny=tk.Entry(self.main.dev_frame,width=5,background="#999999")
        # screeny.bind("<Return>",change_y)
        # screeny.place(x=74,y=0)
