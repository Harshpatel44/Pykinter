import tkinter as tk
from frames.IFrame import IFrame
import injector
import utils.windowBasicFunctions as windowBasicFunc
from common import constants as const
from PIL import ImageTk, Image
from singleton import singleton


@singleton
class GUIFrame(IFrame):
    def __init__(self, center_frame, custom_injector=None):
        super().__init__()
        if custom_injector:
            self.Injector = custom_injector
        else:
            self.Injector = injector.Injector()

        self.center_frame_class_obj = center_frame
        center_frame_width = self.center_frame_class_obj.center_frame_width
        center_frame_height = self.center_frame_class_obj.center_frame_height

        self.gui_frame_width = center_frame_width * const.gui_frame_width
        self.gui_frame_height = center_frame_height * const.gui_frame_height
        self.gui_frame_x = (center_frame_width - self.gui_frame_width) / 2
        self.gui_frame_y = (center_frame_height - self.gui_frame_height) / 2

        self.gui_frame_taskbar_height = const.gui_frame_taskbar_height
        self.gui_frame_taskbar_width = self.gui_frame_width - (2 * const.gui_frame_highlight_thickness)
        self.layout()

    def layout(self):
        center_frame = self.center_frame_class_obj.center_frame
        self.gui_frame = tk.Frame(
            center_frame,
            height=self.gui_frame_height,
            width=self.gui_frame_width,
            highlightthickness=const.gui_frame_highlight_thickness,
            highlightbackground=const.gui_frame_highlightbg,
            relief=tk.SOLID
        )
        self.gui_frame.place(x=self.gui_frame_x, y=self.gui_frame_y)

        self.gui_frame_taskbar_layout()

        self.gui_frame_app_window = tk.Canvas(
            self.gui_frame,
            highlightthickness=0,
            bd=0,
            background=const.gui_frame_app_window_bg,
            height=self.gui_frame_height - self.gui_frame_taskbar_height - (2 * const.gui_frame_highlight_thickness),
            width=self.gui_frame_width - (2 * const.gui_frame_highlight_thickness)
        )
        widgets_model = self.Injector.get_widgets_factory().get_widgets_model()
        self.gui_frame_app_window.bind('<Button-1>', widgets_model.unselect_widgets)
        self.gui_frame_app_window.place(x=0, y=self.gui_frame_taskbar_height)

        Injector = injector.Injector()
        Injector.get_current_properties().add_frames({
            'guiFrame': self.gui_frame,
            'guiFrameAppWindow': self.gui_frame_app_window
        })

    def gui_frame_taskbar_layout(self):
        self.gui_frame_taskbar = tk.Frame(
            self.gui_frame,
            height=self.gui_frame_taskbar_height,
            width=self.gui_frame_taskbar_width,
            background=const.gui_frame_taskbar_bg
        )
        self.gui_frame_taskbar.place(x=0, y=0)

        self.maximize_button = tk.Canvas(
            self.gui_frame_taskbar,
            height=const.gui_frame_taskbar_button_height,
            width=const.gui_frame_taskbar_button_width,
            background=const.gui_frame_taskbar_buttons_bg,
            relief='flat'
        )
        self.maximize_button.place(
            x=self.gui_frame_taskbar_width - const.gui_frame_maximize_button_x,
            y=self.gui_frame_taskbar_height * const.gui_frame_taskbar_button_y
        )

        self.close_button = tk.Canvas(self.gui_frame_taskbar,
                                      height=const.gui_frame_taskbar_button_height,
                                      width=const.gui_frame_taskbar_button_width,
                                      background=const.gui_frame_taskbar_buttons_bg, relief='flat')
        self.close_button.place(
            x=self.gui_frame_taskbar_width - const.gui_frame_close_button_x,
            y=self.gui_frame_taskbar_height * const.gui_frame_taskbar_button_y
        )

        self.title_label = tk.Label(
            self.gui_frame_taskbar,
            text=const.gui_frame_taskbar_title,
            background=const.gui_frame_taskbar_bg,
            fg=const.gui_frame_taskbar_title_fg
        )
        self.title_label.config(font=('Arial', const.gui_frame_taskbar_title_fontsize))
        self.title_label.place(x=const.gui_frame_title_x, y=0)

        image = Image.open(const.logo_location)
        resized_img = image.resize(
            (
                round(self.gui_frame_taskbar_width * const.gui_frame_logo_width),
                round(self.gui_frame_taskbar_height * const.gui_frame_logo_height)
            ),
            Image.ANTIALIAS
        )
        master_tk_object = self.center_frame_class_obj.developer_frame.creator_frame.tk
        self.photoimage = ImageTk.PhotoImage(resized_img, master=master_tk_object)
        gui_frame_taskbar_logo = tk.Label(self.gui_frame_taskbar, borderwidth=0, image=self.photoimage)
        gui_frame_taskbar_logo.place(
            x=const.gui_frame_logo_x,
            y=self.gui_frame_taskbar_height * const.gui_frame_logo_y
        )

        self.gui_frame_taskbar.bind(
            '<Button-1>',
            lambda event, widget=self.gui_frame: windowBasicFunc.start_widget_drag(event, widget)
        )
        self.gui_frame_taskbar.bind(
            '<B1-Motion>',
            lambda event,
            widget=self.gui_frame: windowBasicFunc.motion_widget_drag(event, widget)
        )
