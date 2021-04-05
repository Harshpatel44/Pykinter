from frames.IFrame import IFrame
from frames.WidgetsFrame import WidgetsFrame
from frames.CenterFrame import CenterFrame
from singleton import singleton


@singleton
class DeveloperFrame(IFrame):
    def __init__(self, creator_frame):
        super().__init__()
        self.creator_frame = creator_frame
        self.layout()

    def layout(self):
        WidgetsFrame(self)
        CenterFrame(self)
        # self.creator_frame.widget_frame = tk.Frame(self.creator_frame, height=self.creator_frame.h * const.frame_height, width=self.creator_frame.w * const.widget_frame_width,
        #                              relief='ridge', background=const.bg_color,
        #                              bd=0)

        # self.creator_frame.props_frame = tk.Frame(self.creator_frame, height=self.creator_frame.h * const.frame_height, width=self.creator_frame.w * const.props_frame_width,
        #                             relief='ridge', background=const.bg_color,
        #                             bd=0)
        #
        # self.creator_frame.dev_frame.pack(side='left')
        # self.creator_frame.props_frame.pack(side='left')

        # dev_window = dev_window_controller.DevWindow(self.creator_frame)
        # properties_tab.prop_tab(self.creator_frame, self.creator_frame, self.creator_frame.props_frame,
        #                         self.creator_frame.dev_frame)  # function for properties placement
