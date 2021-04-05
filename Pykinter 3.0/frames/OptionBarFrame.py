import tkinter as tk
from frames.IFrame import IFrame
from singleton import singleton
from common import constants as const
import Injector

@singleton
class OptionBarFrame(IFrame):
    def __init__(self, creator_frame):
        IFrame.__init__(self)
        self.creator_frame = creator_frame
        self.optionbar_height = self.creator_frame.creator_frame_height * const.bar_height
        self.optionbar_width = self.creator_frame.creator_frame_width
        self.layout()

    def layout(self):
        frames = Injector.get_current_properties().get_frames()
        extra_bar = tk.Frame(self.creator_frame,
                             height=self.optionbar_height,
                             width=self.optionbar_width,
                             bd=1,
                             relief='raised',
                             background=const.bg_color,
                             highlightbackground=const.main_border)
        extra_bar.pack(side='top')

        editor_button = tk.Button(extra_bar,
                                  text='Editor',
                                  relief="flat",
                                  command=lambda: self.parent.controller.show_frame(frames['EditorFrame']))
        editor_button.config(font=('Arial', const.gui_frame_taskbar_title_fontsize))
        editor_button.place(x=400, y=1)

        design_btn = tk.Button(extra_bar,
                               text="Design",
                               relief="flat",
                               command=lambda: self.parent.controller.show_frame(frames['CreatorFrame']))
        design_btn.place(x=450, y=1)

        save_button = tk.Button(extra_bar, text='save')
        save_button.place(x=550, y=1)
