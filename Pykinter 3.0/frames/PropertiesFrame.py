import tkinter as tk
from frames.IFrame import IFrame
from singleton import singleton
from common import constants as const

@singleton
class PropertiesFrame(IFrame):
    def __init__(self, developer_frame):
        super().__init__()
        self.developer_frame = developer_frame
        creator_frame = self.developer_frame.creator_frame

        self.props_frame_title_height = creator_frame.creator_frame_height * const.props_frame_title_height
        self.props_frame_title_width = creator_frame.creator_frame_width * const.props_frame_width

        self.props_frame_width = round(creator_frame.creator_frame_width * const.props_frame_width)
        self.props_frame_height = round(creator_frame.creator_frame_height * const.props_frame_height)

        self.layout()

    def layout(self):
        creator_frame = self.developer_frame.creator_frame

        self.props_outer_frame = tk.Frame(creator_frame,
                                      height=self.props_frame_height,
                                      width=self.props_frame_width,
                                      relief='ridge',
                                      background=const.bg_color,
                                      bd=0)
        self.props_outer_frame.pack(side='left')
        print(self.props_frame_width)
        self.props_title_frame()

        props_canvas_yscrollbar = tk.Scrollbar(self.props_outer_frame)
        props_main_canvas = tk.Canvas(
            self.props_outer_frame,
            height=self.props_frame_height,
            width=self.props_frame_width,
            yscrollcommand=props_canvas_yscrollbar.set,
            scrollregion=(0, 0, self.props_frame_width, 1200),
            background=const.bg_color,
            highlightthickness=0
        )  # main canvas
        # props_canvas_yscrollbar.config(command=props_main_canvas.yview)
        props_canvas_yscrollbar.pack(side=tk.LEFT, fill=tk.Y)

        self.props_content_frame = tk.Frame(
            props_main_canvas,
            height=1200,
            width=self.props_frame_width,
            background=const.bg_color,
            bd=0
        )  # mainframe inside canvas
        props_main_canvas.pack(side='left', fill='both', expand=True)

        props_main_canvas.create_window((0, 0), window=self.props_content_frame, anchor='nw')

        self.props_frame_properties()
    def props_title_frame(self):
        props_tab_title = tk.Frame(self.props_outer_frame,
                                     height=self.props_frame_title_height,
                                     width=self.props_frame_title_width,
                                     bd=1,
                                     relief='raised',
                                     background=const.bg_color,
                                     highlightbackground=const.main_border)
        props_tab_title.pack(side='top', fill='both', expand=1)

        title_label = tk.Label(props_tab_title,
                               text='Properties',
                               background=const.bg_color,
                               fg=const.primary_font_color)
        title_label.config(font=(const.primary_font, 9))
        title_label.pack(side='top')
        
    def props_frame_properties(self):
        X_taskbar = tk.Label(self.props_content_frame, text='X', width=10, bd=1, background='#6D7993', fg='#fef1e8')
        X_taskbar.place(x=20, y=15)
        X_taskbar_enter = tk.Entry(self.props_content_frame, width=17)
        # X_taskbar_enter.bind("<Return>", backend_properties.enter_X)
        # X_taskbar_enter.bind('<FocusOut>', backend_properties.enter_X)
        # X_taskbar_enter.bind("<Return>", backend_properties.enter_X)
        X_taskbar_enter.place(x=90, y=15)

        Y_taskbar = tk.Label(self.props_content_frame, text='Y', width=10, bd=1, background='#6D7993', fg='#fef1e8')
        Y_taskbar.place(x=20, y=45)
        Y_taskbar_enter = tk.Entry(self.props_content_frame, width=17)
        # Y_taskbar_enter.bind("<Return>", backend_properties.enter_Y)
        # Y_taskbar_enter.bind('<FocusOut>', backend_properties.enter_Y)
        # Y_taskbar_enter.bind("<Return>", backend_properties.enter_Y)
        Y_taskbar_enter.place(x=90, y=45)