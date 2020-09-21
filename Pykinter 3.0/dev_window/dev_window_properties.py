def on_change_x(event,self):
    widget = event.widget
    w = (int(widget.get()) / 1920.0) * 700
    self.centre_frame.configure(width=w)
    self.working_window.configure(width=w - 6)
    self.taskbar.configure(width=w - 6)
    self.maximizeButton.place(x=w - 45)
    self.closeButton.place(x=w - 25)

def on_change_y(event,self):
    widget = event.widget
    h = (int(widget.get()) / 1080.0) * 480
    self.centre_frame.configure(height=h)
    self.working_window.configure(height=h - 26)