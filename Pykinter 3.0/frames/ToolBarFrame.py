import tkinter as tk
from singleton import singleton
from common import constants as const


@singleton
class ToolBarFrame(object):
    def __init__(self, creator_frame):
        self.creator_frame = creator_frame
        self.toolbar_height = self.creator_frame.creator_frame_height * const.bar_height
        self.toolbar_width = self.creator_frame.creator_frame_width
        self.layout()

    def layout(self):
        toolbar = tk.Frame(self.creator_frame,
                           height=self.toolbar_height,
                           width=self.toolbar_width,
                           bd=1,
                           relief='raised',
                           background=const.bg_color,
                           highlightbackground=const.main_border)

        toolbar_text = tk.Label(toolbar, text='Tool bar')
        toolbar_text.place(x=0, y=0)

        toolbar.pack(side='top')
