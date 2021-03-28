from common import constants as const


def on_change_x(event, self):
    widget = event.widget
    w = (int(widget.get())) * 0.60
    self.centre_frame.configure(width=w)
    self.working_window.configure(width=w - const.center_frame_working_window_width)
    self.taskbar.configure(width=w - const.center_frame_taskbar_width)
    self.maximize_button.place(x=w * const.center_frame_maximize_button_x)
    self.close_button.place(x=w * const.center_frame_taskbar_button_width)


def on_change_y(event, self):
    widget = event.widget
    h = (int(widget.get())) * 0.60
    self.centre_frame.configure(height=h)
    self.working_window.configure(height=h - 26)
