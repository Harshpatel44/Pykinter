import tkinter as tk
from frames.IFrame import IFrame
from singleton import singleton
from common import constants as const
import utils.windowBasicFunctions as windowBasicFunc


@singleton
class TitleBarFrame(IFrame):
    def __init__(self, parent):
        IFrame.__init__(self)
        self.parent = parent
        self.layout()

    def layout(self):
        """ Creation of Title bar and its buttons """
        title_bar = tk.Frame(self.parent, height=24, width=self.parent.w, relief='solid', background=const.bg_color,
                             highlightbackground="#555555")
        title_bar.place(x=0, y=0)
        title_name_frame = tk.Frame(title_bar, height=24, width=self.parent.w * 0.90, background="green")
        title_name_frame.pack(side="left", fill="both", expand=True)
        title_bar_btns_frame = tk.Frame(title_bar, height=24, width=self.parent.w * 0.10, background="green")
        title_bar_btns_frame.pack(side="left", fill="both", expand=True)

        title_name = tk.Label(title_name_frame, text="PyKinter", background="green", fg=const.bg_color, font="bold")
        title_name.place(x=0, y=0)

        minimize = tk.Canvas(title_bar_btns_frame, height=12, width=12, background="#333333", relief='flat')
        minimize.pack(side="left", padx=16)
        minimize.bind('<Enter>', windowBasicFunc.toolbar_btn_hoverin)
        minimize.bind('<Leave>', windowBasicFunc.toolbar_btn_hoverout)
        minimize.bind("<Button-1>", lambda event, window_obj=self.parent: windowBasicFunc.minimize_window(window_obj))

        maximize = tk.Canvas(title_bar_btns_frame, height=12, width=12, background="#333333", relief='flat')
        maximize.pack(side="left", padx=16)
        maximize.bind('<Enter>', windowBasicFunc.toolbar_btn_hoverin)
        maximize.bind('<Leave>', windowBasicFunc.toolbar_btn_hoverout)
        maximize.bind("<Button-1>",
                      lambda event, window_obj=self.parent, w=self.parent.w,
                             h=self.parent.h: windowBasicFunc.maximize_window(window_obj, w, h))

        close_button = tk.Canvas(title_bar_btns_frame, height=12, width=12, background="#333333", relief='flat')
        close_button.pack(side="left", padx=16)
        close_button.bind('<Enter>', windowBasicFunc.toolbar_btn_hoverin)
        close_button.bind("<Button-1>", lambda event, window_obj=self.parent: windowBasicFunc.close_window(window_obj))
        close_button.bind('<Leave>', windowBasicFunc.toolbar_btn_hoverout)
