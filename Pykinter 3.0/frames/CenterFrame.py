import tkinter as tk
from frames.IFrame import IFrame
from frames.GUIFrame import GUIFrame
from singleton import singleton
from common import constants as const
import injector


@singleton
class CenterFrame(IFrame):
    def __init__(self, developer_frame):
        super().__init__()
        self.developer_frame = developer_frame
        creator_frame = self.developer_frame.creator_frame

        self.center_frame_height = creator_frame.creator_frame_height * const.frame_height
        self.center_frame_width = creator_frame.creator_frame_width * const.center_frame_width
        self.layout()

    def layout(self):
        creator_frame = self.developer_frame.creator_frame

        self.center_frame = tk.Frame(creator_frame,
                                      height=self.center_frame_height,
                                      width=self.center_frame_width,
                                      relief='ridge',
                                      background=const.center_frame_color,
                                      bd=0)
        self.center_frame.pack(side='left')

        self.gui_window_geometry_tool()
        GUIFrame(self)
        # update the object
        Injector = injector.Injector()
        Injector.get_current_properties().add_frames({
            'CenterFrame': self.center_frame
        })

    def gui_window_geometry_tool(self):
        x_geometry_label = tk.Label(
            self.center_frame,
            text='X:',
            width=2,
            bd=1,
            background='#333333',
            fg='#fef1e8'
        )
        x_geometry_label.place(
            x=self.center_frame_width * const.dev_window_screenx_name_x,
            y=self.center_frame_height * const.dev_window_screenxy_y
        )

        x_geometry = tk.Entry(self.center_frame, width=5, background="#999999")
        # screenx.bind("<Return>", lambda event, obj=self: dev_window_properties.on_change_x(event, obj))
        x_geometry.place(
            x=self.center_frame_width * const.dev_window_screenx_entry_x,
            y=self.center_frame_height * const.dev_window_screenxy_y
        )

        y_geometry_label = tk.Label(
            self.center_frame,
            text='Y:',
            width=2,
            bd=1,
            background='#333333',
            fg='#fef1e8'
        )
        y_geometry_label.place(
            x=self.center_frame_width * const.dev_window_screeny_name_x,
            y=self.center_frame_height * const.dev_window_screenxy_y
        )

        y_geometry = tk.Entry(self.center_frame, width=5, background='#999999')
        # screeny.bind("<Return>", lambda event, obj=self: dev_window_properties.on_change_y(event, obj))
        y_geometry.place(
            x=self.center_frame_width * const.dev_window_screeny_entry_x,
            y=self.center_frame_height * const.dev_window_screenxy_y
        )

        """ on changing the settings here, it will be updated to the current_properties, and either update the frame
        or call the function to update the configuration of GUIFrame"""