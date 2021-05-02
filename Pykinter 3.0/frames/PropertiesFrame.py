import tkinter as tk
from frames.IFrame import IFrame
from singleton import singleton
from common import constants as const
import injector

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
        developer_frame = self.developer_frame.developer_frame

        self.props_outer_frame = tk.Frame(developer_frame,
                                      height=self.props_frame_height,
                                      width=self.props_frame_width,
                                      relief='ridge',
                                      background=const.bg_color,
                                      bd=0)
        self.props_outer_frame.pack(side='right', fill='y')
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
        props_tab_title.pack(side='top', fill='x')

        title_label = tk.Label(props_tab_title,
                               text='Properties',
                               background=const.bg_color,
                               fg=const.primary_font_color)
        title_label.config(font=(const.primary_font, 9))
        title_label.pack(side='top')
        
    def props_frame_properties(self):
        Injector = injector.Injector()
        properties_model = Injector.get_properties_factory().get_properties_model()
        properties_controller = Injector.get_properties_factory().get_properties_controller()

        X_geometry_variable = tk.StringVar()
        X_geometry = tk.Label(self.props_content_frame,
                              text='X',
                              width=10,
                              bd=1,
                              background='#6D7993',
                              fg='#fef1e8')
        X_geometry.place(x=20, y=15)
        X_geometry_enter = tk.Entry(self.props_content_frame,
                                    width=17,
                                    textvariable = X_geometry_variable)
        X_geometry_enter.variable = X_geometry_variable
        X_geometry_enter.bind('<Return>', properties_controller.set_x_geometry_property)
        X_geometry_enter.bind('<Tab>', properties_controller.set_x_geometry_property)
        X_geometry_enter.place(x=90, y=15)

        Y_geometry_variable = tk.StringVar()
        Y_geometry = tk.Label(self.props_content_frame,
                              text='Y',
                              width=10,
                              bd=1,
                              background='#6D7993',
                              fg='#fef1e8')
        Y_geometry.place(x=20, y=45)
        Y_geometry_enter = tk.Entry(self.props_content_frame,
                                    width=17,
                                    textvariable = Y_geometry_variable)
        Y_geometry_enter.variable = Y_geometry_variable
        Y_geometry_enter.bind('<Return>', properties_controller.set_y_geometry_property)
        Y_geometry_enter.bind('<Tab>', properties_controller.set_y_geometry_property)
        Y_geometry_enter.place(x=90, y=45)

        properties_model.add_properties({
            'X_geometry': X_geometry_enter,
            'Y_geometry': Y_geometry_enter
        })
