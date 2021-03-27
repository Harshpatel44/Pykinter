import tkinter as tk
from singleton import singleton
import constants as const
import Injector

@singleton
class Layout:
    def __init__(self, creator_frame):
        self.creator_frame = creator_frame
        self.menubar2_height = self.creator_frame.creator_frame_height * const.bar_height
        self.menubar2_width = self.creator_frame.creator_frame_width
        self.content()

    def content(self):
        frames = Injector.get_current_properties().get_frames()
        extra_bar = tk.Frame(self.creator_frame,
                             height=self.menubar2_height,
                             width=self.menubar2_width,
                             bd=1,
                             relief='raised',
                             background=const.bg_color,
                             highlightbackground=const.main_border)
        extra_bar.pack(side='top')

        editor_button = tk.Button(extra_bar,
                                  text="Editor",
                                  relief="flat",
                                  command=lambda: self.parent.controller.show_frame(frames['EditorFrame']))
        editor_button.config(font=("Arial", const.center_frame_taskbar_title_fontsize))
        editor_button.place(x=400, y=1)

        design_btn = tk.Button(extra_bar,
                               text="Design",
                               relief="flat",
                               command=lambda: self.parent.controller.show_frame(frames['CreatorFrame']))
        design_btn.place(x=450, y=1)

        save_button = tk.Button(extra_bar, text='save')
        save_button.place(x=550, y=1)
