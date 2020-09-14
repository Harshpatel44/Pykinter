def start_window_drag(event):
    widget = event.widget
    widget.drag_start_x = 0
    widget.drag_start_y = 0


def motion_window_drag(event):
    widget = event.widget
    x = widget.winfo_x() - widget.drag_start_x + event.x
    y = widget.winfo_y() - widget.drag_start_y + event.y
    widget.place(x=x, y=y)


def toolbar_btn_hoverin(event):
    widget = event.widget
    widget.configure(background='#CC1166')


def toolbar_btn_hoverout(event):
    widget = event.widget
    widget.configure(background="#333333")


def maximize_window(window_obj,w,h):
    print(w,h)
    window_obj.geometry("%dx%d+0+0" % (w*0.70, h*0.70))
    # window_obj.state('zoomed')

def minimize_window(window_obj):
    window_obj.state('withdrawn')
    # window_obj.update_idletasks()
    window_obj.overrideredirect(False)
    window_obj.state('iconic')
    print("Window Minimized")

def close_window(window_obj):
    # window_obj.destroy()
    window_obj.quit()
    print("Window destroyed")
