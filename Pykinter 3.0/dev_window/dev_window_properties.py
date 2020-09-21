def on_change_x(event,self):
    widget = event.widget
    w = (int(widget.get()) / self.main.w) * 700
    self.centre_frame.configure(width=w)
    self.working_window.configure(width=w - 6)
    self.taskbar.configure(width=w - 6)
    self.maximize_button.place(x=w - 45)
    self.close_button.place(x=w - 25)

def on_change_y(event,self):
    widget = event.widget
    h = (int(widget.get()) / self.main.h) * 480
    self.centre_frame.configure(height=h)
    self.working_window.configure(height=h - 26)