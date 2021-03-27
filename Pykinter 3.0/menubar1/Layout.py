import tkinter as tk
from singleton import singleton
import constants as const


@singleton
class Layout:
    def __init__(self, creator_frame):
        self.creator_frame = creator_frame
        self.menubar1_height = self.creator_frame.creator_frame_height * const.optionbar_height
        self.menubar1_width = self.creator_frame.creator_frame_width
        self.content()

    def content(self):
        menubar1 = tk.Frame(self.creator_frame,
                            height=self.menubar1_height,
                            width=self.menubar1_width,
                            bd=1,
                            relief='raised',
                            background=const.bg_color,
                            highlightbackground=const.main_border)

        menubar1_text = tk.Label(menubar1, text='Menubar text')
        menubar1_text.place(x=0, y=0)

        menubar1.pack(side='top')
