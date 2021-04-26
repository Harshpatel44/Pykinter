import tkinter as tk
from frames.IFrame import IFrame
from singleton import singleton
from common import constants as const
import injector


@singleton
class WidgetsFrame(IFrame):
    def __init__(self, developer_frame):
        super().__init__()
        self.developer_frame = developer_frame
        creator_frame = self.developer_frame.creator_frame

        self.widgets_frame_height = creator_frame.creator_frame_height * const.widget_frame_height
        self.widgets_frame_width = creator_frame.creator_frame_width * const.widget_frame_width

        self.widgets_frame_title_height = creator_frame.creator_frame_height * const.widget_frame_title_height
        self.widgets_frame_title_width = creator_frame.creator_frame_width * const.widget_frame_width

        self.widget_buttons_frame_height = creator_frame.creator_frame_height * const.widget_button_frame_height
        self.widget_buttons_frame_width = creator_frame.creator_frame_width * const.widget_frame_width

        self.widget_button_width = round(creator_frame.creator_frame_width * const.widgets_button_width)
        self.widget_button_height = round(self.widget_buttons_frame_height * const.widgets_button_height)

        # /2 to keep button at the center horizontally
        self.widget_button_x = (self.widget_buttons_frame_width - self.widget_button_width) / 2

        distance_between_buttons_metric = 15
        self.widget_button_y = (self.widget_buttons_frame_height / distance_between_buttons_metric)

        self.widget_font_size = const.widgets_font_size
        self.widget_font = const.widgets_button_font

        self.widgets_frame = None
        self.layout()

    def layout(self):
        creator_frame = self.developer_frame.creator_frame
        self.widget_frame(creator_frame)  # creates widget frame
        self.widget_title_frame()  # creates widget_title frame inside widget frame
        self.widget_buttons()

    def widget_frame(self, creator_frame):
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
        self.widget_buttons_frame.pack(side='top')
        # widget_area_canvas.create_window((0,0),window=widget_frame,anchor='nw')

        title_label = tk.Label(widgets_tab_title,
                               text='Widgets',
                               background=const.bg_color,
                               fg=const.primary_font_color)
        title_label.config(font=(const.primary_font, 9))
        title_label.pack(side='top')

    def widget_buttons(self):
        widgets_text_list = [
            'Button',
            'Tool Button',
            'Radio Button',
            'Check Button',
            'Scroll Bar',
            'Progress Bar',
            'Spin Box',
            'Combo Box',
            'Drop View',
            'List View',
            'Frame',
            'Spinner',
            'Shapes',
            'Image'
        ]
        widget_button_properties_dict = {
            'bd': 0,
            'background': '#6D7993',
            'fg': '#FFFFFF',
            'relief': tk.SUNKEN
        }
        # self.widget_objects_dictionary = {}
        Injector = injector.Injector()
        widget_controller = Injector.get_widgets_factory().get_widget_controller()

        for i, j in zip(range(1, len(widgets_text_list) + 1), widgets_text_list):
            widget = tk.Button(self.widget_buttons_frame,
                               text=j,
                               bd=widget_button_properties_dict['bd'],
                               background=widget_button_properties_dict['background'],
                               fg=widget_button_properties_dict['fg'],
                               relief=widget_button_properties_dict['relief'])
            widget.bind('<Button-1>', lambda event: widget_controller.create_button(event))
            widget.config(font=(self.widget_font, self.widget_font_size))
            widget.place(x=self.widget_button_x,
                         y=(self.widget_button_y * i) - self.widget_button_height,
                         height=self.widget_button_height,
                         width=self.widget_button_width)
            # self.widget_objects_dictionary[j] = widget