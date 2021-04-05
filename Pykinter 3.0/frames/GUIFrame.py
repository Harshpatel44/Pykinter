import tkinter as tk
from frames.IFrame import IFrame
from singleton import singleton
from common import constants as const
import Injector


@singleton
class GUIFrame(IFrame):
    def __init__(self, center_frame):
        super().__init__()
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
        center_frame = Injector.get_current_properties().get_frame('CenterFrame')
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
