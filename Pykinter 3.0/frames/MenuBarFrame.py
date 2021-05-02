import tkinter as tk
from frames.IFrame import IFrame
from singleton import singleton
from common import constants as const


@singleton
class MenuBarFrame(IFrame):
    def __init__(self, creator_frame):
        IFrame.__init__(self)
        self.creator_frame = creator_frame
        self.menubar_height = self.creator_frame.creator_frame_height * const.menubar_height
        self.menubar_width = self.creator_frame.creator_frame_width
        self.layout()

    def layout(self):
        menubar = tk.Frame(self.creator_frame,
                            height=self.menubar_height,
                            width=self.menubar_width,
                            bd=1,
                            relief='raised',
                            background=const.bg_color,
                            highlightbackground=const.main_border)

        menubar_text = tk.Label(menubar, text='Menubar text')
        menubar_text.place(x=0, y=0)

        menubar.pack(side='top', fill='x')
