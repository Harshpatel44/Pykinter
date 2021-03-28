import tkinter as tk
from frames.IFrame import IFrame
from singleton import singleton
from common import constants as const
from widgets import WidgetsController


@singleton
class WidgetsFrame(IFrame):
    def __init__(self, developer_frame):
        IFrame.__init__(self)
        self.developer_frame = developer_frame
        creator_frame = self.developer_frame.creator_frame

        self.widgets_frame_height = creator_frame.creator_frame_height * const.frame_height
        self.widgets_frame_width = creator_frame.creator_frame_width * const.widget_frame_width

        self.widgets_frame_title_height = creator_frame.creator_frame_height * const.widget_frame_title_height
        self.widgets_frame_title_width = creator_frame.creator_frame_width * const.widget_frame_width

        self.widget_buttons_frame_height = creator_frame.creator_frame_height * const.widget_button_frame_height
        self.widget_buttons_frame_width = creator_frame.creator_frame_width * const.widget_frame_width

        self.widget_button_width = round(creator_frame.creator_frame_width * const.widgets_button_width)
        self.widget_button_height = round(self.widget_buttons_frame_height * const.widgets_button_height)
        self.widget_button_x = (self.widget_buttons_frame_width - self.widget_button_width) / 2
        self.widget_button_y = (self.widget_buttons_frame_height / 12)

        self.widget_font_size = const.widgets_font_size
        self.widget_font = 'Courier New'

        self.widgets_frame = None
        self.layout()

    def layout(self):
        self.widget_frame()  # creates widget frame
        self.widget_title_frame()  # creates widget_title frame inside widget frame
        self.widget_buttons()

    def widget_frame(self):
        creator_frame = self.developer_frame.creator_frame

        self.widgets_frame = tk.Frame(creator_frame,
                                      height=self.widgets_frame_height,
                                      width=self.widgets_frame_width,
                                      relief='ridge',
                                      background=const.bg_color,
                                      bd=0)
        self.widgets_frame.pack(side='left')


    def widget_title_frame(self):
        widgets_tab_title = tk.Frame(self.widgets_frame,
                                     height=self.widgets_frame_title_height,
                                     width=self.widgets_frame_title_width,
                                     bd=1,
                                     relief='raised',
                                     background=const.bg_color,
                                     highlightbackground=const.main_border)
        widgets_tab_title.pack(side='top', fill='both', expand=1)

        self.widget_buttons_frame = tk.Frame(self.widgets_frame,
                                             background=const.bg_color,
                                             width=self.widget_buttons_frame_width,
                                             height=self.widget_buttons_frame_height)
        self.widget_buttons_frame.pack(side="top")
        # widget_area_canvas.create_window((0,0),window=widget_frame,anchor='nw')

        title_label = tk.Label(widgets_tab_title,
                               text='Widgets',
                               background=const.bg_color,
                               fg=const.primary_font_color)
        title_label.config(font=(const.primary_font, 9))
        title_label.pack(side='top')


    def widget_buttons(self):
        button = tk.Button(self.widget_buttons_frame,
                           text='Button',
                           bd=0,
                           background='#6D7993',
                           fg='#FFFFFF',
                           relief=tk.SUNKEN)
        button.config(font=(self.widget_font, self.widget_font_size))
        # button.pack(side='top')
        button.place(x=self.widget_button_x,
                     y=self.widget_button_y - self.widget_button_height,
                     height=self.widget_button_height,
                     width=self.widget_button_width)
