import tkinter as tk
from singleton import singleton
import constants as const
from widgets import WidgetsController


@singleton
class WidgetsFrame:
    def __init__(self, developer_frame):
        self.developer_frame = developer_frame
        self.widgets_frame_height = developer_frame.creator_frame.creator_frame_height * const.frame_height
        self.widgets_frame_width = developer_frame.creator_frame.creator_frame_width * const.widget_frame_width
        self.widgets_frame = None
        self.layout()

    def layout(self):
        print(self)
        creator_frame = self.developer_frame.creator_frame

        self.widgets_frame = tk.Frame(creator_frame,
                                      height=self.widgets_frame_height,
                                      width=self.widgets_frame_width,
                                      relief='ridge',
                                      background=const.bg_color,
                                      bd=0)
        self.widgets_frame.pack(side='left')

        WidgetsController.WidgetsController(self)

