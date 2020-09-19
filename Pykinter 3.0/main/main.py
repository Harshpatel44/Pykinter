__author__ = 'Harsh'

import tkinter as tk
from application_standards import constants as const
from program_editor import editor_tab
import window_basic_functions.functions as basic_func
from widgets import widgets_controller
from properties_bar import properties_tab


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("PyKinter")
        self.iconbitmap("../media/logo2.ico")

        """ Initial configuration of the main window """
        self.main_window_obj = self
        self.h = self.winfo_screenheight()
        self.w = self.winfo_screenwidth()
        print("Window width: {0} and height: {1}".format(self.w, self.h))
        self.geometry("%dx%d+0+0" % (self.w, self.h))
        self.state("zoomed")

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand='true')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # self.overrideredirect('false')

        # self.titlebar_func()
        # self.bind("<Map>",self.display_window)
        self.frames = {}
        for f in (CreatorFrames,EditorFrames):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(CreatorFrames)


    def show_frame(self, con):
        frame = self.frames[con]
        frame.tkraise()

    def display_window(self, event):
        # self.update_idletasks()
        self.overrideredirect(True)
        self.state("normal")

    def titlebar_func(self):
        """ Creation of Title bar and its buttons """
        title_bar = tk.Frame(self, height=24, width=self.w, relief='solid', background=const.bg_color,
                             highlightbackground="#555555")
        title_bar.place(x=0,y=0)
        title_name_frame = tk.Frame(title_bar, height=24, width=self.w*0.90, background="green")
        title_name_frame.pack(side="left", fill="both", expand=True)
        title_bar_btns_frame = tk.Frame(title_bar, height=24, width=self.w*0.10, background="green")
        title_bar_btns_frame.pack(side="left", fill="both", expand=True)

        title_name = tk.Label(title_name_frame, text="PyKinter", background="green", fg =const.bg_color, font="bold")
        title_name.place(x=0, y=0)

        minimize = tk.Canvas(title_bar_btns_frame, height=12, width=12, background="#333333", relief='flat')
        minimize.pack(side="left", padx=16)
        minimize.bind('<Enter>', basic_func.toolbar_btn_hoverin)
        minimize.bind('<Leave>', basic_func.toolbar_btn_hoverout)
        minimize.bind("<Button-1>", lambda event, window_obj=self: basic_func.minimize_window(window_obj))

        maximize = tk.Canvas(title_bar_btns_frame, height=12, width=12, background="#333333", relief='flat')
        maximize.pack(side="left", padx=16)
        maximize.bind('<Enter>', basic_func.toolbar_btn_hoverin)
        maximize.bind('<Leave>', basic_func.toolbar_btn_hoverout)
        maximize.bind("<Button-1>", lambda event, window_obj=self, w=self.w, h=self.h: basic_func.maximize_window(window_obj,w,h))

        close_button = tk.Canvas(title_bar_btns_frame, height=12, width=12, background="#333333", relief='flat')
        close_button.pack(side="left", padx=16)
        close_button.bind('<Enter>', basic_func.toolbar_btn_hoverin)
        close_button.bind("<Button-1>", lambda event, window_obj=self: basic_func.close_window(window_obj))
        close_button.bind('<Leave>', basic_func.toolbar_btn_hoverout)


class CreatorFrames(tk.Frame,Main):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.controller = controller
        self.controller = controller
        self.w = self.winfo_screenwidth()
        self.h = self.winfo_screenheight()
        self.parent = parent
        self.toolbar_func()
        self.menubar_func()
        self.optionbar_func()
        self.extrabar_func()
        self.middle_frames_func()
        self.bind('<Button-1>', basic_func.start_window_drag)
        self.bind('<B1-Motion>', basic_func.motion_window_drag)

    def toolbar_func(self):
        toolbar = tk.Frame(self, height=self.h*const.bar_height, width=self.w, bd=1, relief="raised", background=const.bg_color,
                            highlightbackground=const.main_border)
        toolbar.pack(side='top')

    def menubar_func(self):  # menu bar
        menu_bar = tk.Frame(self, height=self.h*const.bar_height, width=self.w, bd=1, relief="raised", background=const.bg_color,
                            highlightbackground=const.main_border)
        menu_bar.pack(side='top')

    def optionbar_func(self):  # option bar
        option_bar = tk.Frame(self, height=self.h*const.optionbar_height, width=self.w, bd=1, relief="raised", background=const.bg_color,
                              highlightbackground=const.main_border)
        option_bar.pack(side='top')

    def extrabar_func(self):  # extra bar
        extra_bar = tk.Frame(self, height=self.h*const.bar_height, width=self.w, bd=1, relief="raised", background=const.bg_color,
                             highlightbackground=const.main_border)
        extra_bar.pack(side='top')

        editor_button=tk.Button(extra_bar,text="Editor",relief="flat",command=lambda:self.controller.show_frame(EditorFrames))
        editor_button.place(x=400,y=1)
        design_btn = tk.Button(extra_bar, text="Design", relief="flat",
                                  command=lambda: self.controller.show_frame(CreatorFrames))
        design_btn.place(x=450, y=1)

        # save_button = tk.Button(extra_bar, text="Editor", command=lambda: update.save_data)
        # save_button.place(x=550, y=1)

    def middle_frames_func(self):
        self.widget_frame = tk.Frame(self, height=self.h*const.frame_height, width=self.w*const.widget_frame_width, relief='ridge', background=const.bg_color,
                                 bd=0)
        self.dev_frame = tk.Frame(self, height=self.h*const.frame_height, width=self.w*const.dev_frame_width, relief='ridge', background=const.dev_window_color,
                                 bd=0)
        self.props_frame = tk.Frame(self, height=self.h*const.frame_height, width=self.w*const.props_frame_width, relief='ridge', background=const.bg_color,
                                 bd=0)
        self.widget_frame.pack(side='left')
        self.dev_frame.pack(side="left")
        self.props_frame.pack(side='left')

        widgets_tab = widgets_controller.WidgetsTab(self)

        # widgets_tab.wid_tab(self, self.parent, middle_frame1, middle_frame2)  # function for widgets placement
        # properties_tab.prop_tab(self, self.parent, self.properties_frame, self.dev_frame)  # function for properties placement


class EditorFrames(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.toolbar_func()
        self.menubar_func()
        self.optionbar_func()
        self.program_editor()

    def toolbar_func(self):
        pass

    def menubar_func(self):
        menu_bar = tk.Frame(self, height=23, width=1300, highlightthickness=1, relief='solid', background=const.bg_color,
                            highlightbackground="#555555")
        menu_bar.pack()

    def optionbar_func(self):
        option_bar = tk.Frame(self, height=81, width=1300, highlightthickness=1, highlightbackground="#555555",
                              relief='solid', background='#0B3CFD')
        option_bar.pack(side='top')

    def program_editor(self):
        frame1 = tk.Frame(self, height=530, width=230, relief='solid', background="#96858F", highlightthickness=1,
                          highlightbackground="#555555")
        frame2 = tk.Frame(self, height=530, width=2000, relief='solid', background="#96858F", highlightthickness=1,
                          highlightbackground="#555555")
        frame1.pack(side="left")
        frame2.pack(side="left")
        editor_tab.editor(self, self.parent, frame1, frame2)
        editor_tab.left_side(self, self.parent, frame1, frame2)


app = Main()
app.mainloop()
