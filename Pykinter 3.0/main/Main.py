__author__ = 'Harsh'

import tkinter as tk
import Injector
from common import constants as const
from frames.DeveloperFrame import DeveloperFrame
from old.program_editor import editor_tab
import utils.windowBasicFunctions as windowBasicFunc


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        """ Initial configuration of the main window """
        self.title(const.title)
        self.iconbitmap(const.logo_location)
        self.main_window_obj = self
        self.h = self.winfo_screenheight()
        self.w = self.winfo_screenwidth()
        self.geometry("%dx%d+0+0" % (self.w, self.h))
        self.state("zoomed")
        print("Window width: {0} and height: {1}".format(self.w, self.h))

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand='true')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # self.overrideredirect('false')
        # Injector.get_titlebar_layout(self)
        # self.bind("<Map>",self.display_window)

        self.frames = {}
        get_current_properties = Injector.get_current_properties()
        Injector.get_current_properties().set_frames({
            'CreatorFrame': CreatorFrame,
            'EditorFrame': EditorFrames
        })
        for f in (CreatorFrame, EditorFrames):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(CreatorFrame)
        get_current_properties.set_main(self)

    def show_frame(self, con):
        frame = self.frames[con]
        frame.tkraise()

    def display_window(self, event):
        # self.update_idletasks()
        self.overrideredirect(True)
        self.state("normal")


class CreatorFrame(tk.Frame, Main):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.controller = controller
        self.controller = controller
        self.creator_frame_width = self.winfo_screenwidth()
        self.creator_frame_height = self.winfo_screenheight()
        self.parent = parent

        Injector.get_toolbar_frame(self)
        Injector.get_menubar_frame(self)
        Injector.get_optionbar_frame(self)
        DeveloperFrame(self)
        self.bind('<Button-1>', windowBasicFunc.start_window_drag)
        self.bind('<B1-Motion>', windowBasicFunc.motion_window_drag)


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
        menu_bar = tk.Frame(self, height=23, width=1300, highlightthickness=1, relief='solid',
                            background=const.bg_color,
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
