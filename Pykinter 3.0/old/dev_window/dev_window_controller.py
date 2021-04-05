import tkinter as tk
from PIL import ImageTk, Image
from widgets import first_click
from common import constants as const
from old.dev_window import dev_window_properties


class DevWindow:
    def __init__(self, main):
        self.main = main


        self.taskbar_height = const.center_frame_taskbar_height
        self.taskbar_width = self.center_frame_width - const.center_frame_taskbar_width
        self.center_frame_x = (self.dev_frame_width - self.center_frame_width) / 2
        self.center_frame_y = (self.dev_frame_height - self.center_frame_height) / 2
        self.window_layout()
        self.working_window_geometry()

        # first_click.allTime(working_window, self.main.dev_frame,centre_frame)  # by default initializing selections lines using this function

    def window_layout(self):
        self.centre_frame = tk.Frame(self.main.dev_frame,
                                     height=self.center_frame_height, width=self.center_frame_width,
                                     highlightthickness=3, highlightbackground=const.center_frame_highlightbg,
                                     relief=tk.SOLID)
        self.centre_frame.place(x=self.center_frame_x, y=self.center_frame_y)

        self.taskbar = tk.Frame(self.centre_frame, height=self.taskbar_height, width=self.taskbar_width,
                                background=const.center_frame_taskbar_bg)
        self.taskbar.place(x=0, y=0)
        self.maximize_button = tk.Canvas(self.centre_frame,
                                         height=const.center_frame_taskbar_button_height,
                                         width=const.center_frame_taskbar_button_width,
                                         background=const.center_frame_taskbar_buttons_bg, relief='flat')
        self.maximize_button.place(x=self.taskbar_width - const.center_frame_maximize_button_x,
                                   y=self.taskbar_height * const.center_frame_buttons_y)
        self.close_button = tk.Canvas(self.centre_frame,
                                      height=const.center_frame_taskbar_button_height,
                                      width=const.center_frame_taskbar_button_width,
                                      background=const.center_frame_taskbar_buttons_bg, relief='flat')
        self.close_button.place(x=self.taskbar_width - const.center_frame_close_button_x,
                                y=self.taskbar_height * const.center_frame_buttons_y)

        self.working_window = tk.Canvas(self.centre_frame, highlightthickness=0, bd=0,
                                        background=const.center_frame_working_window_bg,
                                        height=self.center_frame_height - const.center_frame_working_window_height,
                                        width=self.center_frame_width - const.center_frame_working_window_width)
        self.working_window.place(x=0, y=self.taskbar_height)

        self.title_label = tk.Label(self.centre_frame, text=const.center_frame_taskbar_title,
                                    background=const.center_frame_taskbar_bg, fg=const.center_frame_taskbar_title_fg)
        self.title_label.config(font=("Arial", const.center_frame_taskbar_title_fontsize))
        self.title_label.place(x=const.center_frame_title_x, y=0)

        image = Image.open(const.logo_location)
        resized_img = image.resize((round(self.taskbar_width * const.center_frame_logo_width),
                                    round(self.taskbar_height * const.center_frame_logo_height)), Image.ANTIALIAS)
        photoimage = ImageTk.PhotoImage(resized_img, master=self.main)
        taskbar_logo = tk.Label(self.centre_frame, image=photoimage)
        taskbar_logo.place(x=const.center_frame_logo_x, y=self.taskbar_height * const.center_frame_logo_y)

        # bindings when entered in frame
        self.centre_frame.bind("<Enter>", lambda event, arg=self.centre_frame, arg2=self.taskbar,
                                                 arg3=self.working_window: first_click.moveIn_Frame(event, arg, arg2,
                                                                                                    arg3))
        self.main.dev_frame.bind('<Enter>', lambda event, arg=self.centre_frame: first_click.moveIn_MF(event, arg))

        first_click.allTime(self)  # by default initializing selections lines using this function

    def working_window_geometry(self):
        screenx_name = tk.Label(self.main.dev_frame, text="X:", width=2, bd=1, background="#333333", fg="#fef1e8")
        screenx_name.place(x=self.dev_frame_width*const.dev_window_screenx_name_x, y=self.dev_frame_height*const.dev_window_screenxy_y)

        screenx = tk.Entry(self.main.dev_frame, width=5, background="#999999")
        screenx.bind("<Return>", lambda event, obj=self: dev_window_properties.on_change_x(event, obj))
        screenx.place(x=self.dev_frame_width*const.dev_window_screenx_entry_x, y=self.dev_frame_height*const.dev_window_screenxy_y)

        screeny_name = tk.Label(self.main.dev_frame, text="Y:", width=2, bd=1, background="#333333", fg="#fef1e8")
        screeny_name.place(x=self.dev_frame_width*const.dev_window_screeny_name_x, y=self.dev_frame_height*const.dev_window_screenxy_y)

        screeny = tk.Entry(self.main.dev_frame, width=5, background="#999999")
        screeny.bind("<Return>", lambda event, obj=self: dev_window_properties.on_change_y(event, obj))
        screeny.place(x=self.dev_frame_width*const.dev_window_screeny_entry_x, y=self.dev_frame_height*const.dev_window_screenxy_y)
