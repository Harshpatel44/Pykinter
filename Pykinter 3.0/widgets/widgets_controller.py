import tkinter as tk
import injector
from utils import windowBasicFunctions


class WidgetsController:
    def __init__(self, custom_injector=None):
        if custom_injector:
            self.Injector = custom_injector
        else:
            self.Injector = injector.Injector()

    def create_button(self, button_event):
        center_frame = self.Injector.get_current_properties().get_frame('guiFrameAppWindow')
        button = tk.Button(
            center_frame,
            text='Button',
            height=1,
            bd=0,
            highlightthickness=5,
            highlightbackground='black',
            width=10,
            relief=tk.RAISED)

        widgets_model = self.Injector.get_widgets_factory().get_widgets_model()
        button.bind('<Button-1>', lambda event: widgets_model.widget_bind_button1(event))
        button.bind('<B1-Motion>', lambda event: windowBasicFunctions.motion_widget_drag(event))
        button.bind('<ButtonRelease-1>', lambda event: widgets_model.widget_bind_button1_release(event))
        button.bind('<Control-1>', lambda event: widgets_model.widget_bind_command_click(event))
        button.place(x=10, y=10)

        widgets_model = self.Injector.get_widgets_factory().get_widgets_model()
        widgets_model.set_active_widgets([button])
        # Call method to update the properties in current_properties
        # A method to update the properties widgets in Properties Frame (widget_properties module)
        # update Properties from current_properties.properties in widget_properties module
