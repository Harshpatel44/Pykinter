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
        self.widgets_frame_height = developer_frame.creator_frame.creator_frame_height * const.frame_height
        self.widgets_frame_width = developer_frame.creator_frame.creator_frame_width * const.widget_frame_width
        self.widgets_frame = None
        self.create_widgets_frame()

    def create_widgets_frame(self):
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

