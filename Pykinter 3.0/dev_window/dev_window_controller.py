import tkinter as tk
from widgets import first_click
from application_standards import constants as const
from dev_window import dev_window_properties


class DevWindow:
    def __init__(self, main):
        self.main = main
        self.center_frame_height = self.main.h * const.center_frame_height
        self.center_frame_width = self.main.w * const.center_frame_width

        self.taskbar_height = const.center_frame_taskbar_height
        self.taskbar_width = self.main.w * const.center_frame_taskbar_width
        self.center_frame_x = (self.main.dev_frame.cget("width") - self.center_frame_width)/2
        self.center_frame_y = (self.main.dev_frame.cget("height") - self.center_frame_height)/2
        self.window_layout()
        self.working_window_geometry()

        # first_click.allTime(working_window, self.main.dev_frame,centre_frame)  # by default initializing selections lines using this function

    def window_layout(self):
        self.centre_frame = tk.Frame(self.main.dev_frame, background="#6D7993",
                                     height=self.center_frame_height, width=self.center_frame_width,
                                     highlightthickness=3, highlightbackground="#555555", relief=tk.SOLID)
        self.centre_frame.place(x=self.center_frame_x, y=self.center_frame_y)

        self.taskbar = tk.Frame(self.centre_frame, height=self.taskbar_height, width=self.taskbar_width, background="#9099A2")
        self.taskbar.place(x=0, y=0)
        self.maximize_button = tk.Canvas(self.centre_frame, height=self.taskbar_height * const.center_frame_taskbar_button_height,
                                         width=self.taskbar_width * const.center_frame_taskbar_button_width,
                                         background="#333333", relief='flat')
        self.maximize_button.place(x=self.center_frame_width*const.center_frame_maximize_button, y=2)
        self.close_button = tk.Canvas(self.centre_frame, height=self.taskbar_height * const.center_frame_taskbar_button_height,
                                      width=self.taskbar_width * const.center_frame_taskbar_button_width,
                                      background="#333333", relief='flat')
        self.close_button.place(x=self.center_frame_width*const.center_frame_close_button, y=2)

        self.working_window = tk.Canvas(self.centre_frame, highlightthickness=0, bd=0, background="#ffffff",
                                        height=self.center_frame_height-26, width=self.center_frame_width-6)
        self.working_window.place(x=0, y=20)
        self.title_label = tk.Label(self.centre_frame, text="")
        self.title_label.place(x=7, y=1)

        # bindings when entered in frame
        self.centre_frame.bind("<Enter>", lambda event, arg=self.centre_frame, arg2=self.taskbar,
                        arg3=self.working_window: first_click.moveIn_Frame(event, arg, arg2,arg3))
        self.main.dev_frame.bind('<Enter>', lambda event, arg=self.centre_frame: first_click.moveIn_MF(event, arg))

    def working_window_geometry(self):
        screenx_name = tk.Label(self.main.dev_frame, text="X:", width=2, bd=1, background="#333333", fg="#fef1e8")
        screenx_name.place(x=1, y=0)

        screenx = tk.Entry(self.main.dev_frame, width=5, background="#999999")
        screenx.bind("<Return>", lambda event, obj=self: dev_window_properties.on_change_x(event,obj))
        screenx.place(x=20, y=0)

        screeny_name = tk.Label(self.main.dev_frame, text="Y:", width=2, bd=1, background="#333333", fg="#fef1e8")
        screeny_name.place(x=55, y=0)

        screeny = tk.Entry(self.main.dev_frame, width=5, background="#999999")
        screeny.bind("<Return>", lambda event, obj=self: dev_window_properties.on_change_y(event,obj))
        screeny.place(x=74, y=0)
