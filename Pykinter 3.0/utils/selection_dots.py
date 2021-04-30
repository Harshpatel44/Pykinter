import injector
from singleton import singleton
## this class will have functions to create, move, delete selection dots based on the event.


@singleton
class SelectionDots:
    def __init__(self):
        self.selection_rectangle = {}

    def create_selection_for_widget(self, widget):
        x, y, height, width = [int(widget.place_info()[i]) for i in ('x', 'y', 'height', 'width')]
        gui_frame_app_window = injector.Injector().get_current_properties().get_frame('guiFrameAppWindow')
        self.selection_rectangle[widget] = gui_frame_app_window.create_rectangle(
            x - 2,
            y - 2,
            x + width,
            y + height,
            outline='red'
        )

    def hide_selection_for_widget(self):
        gui_frame_app_window = injector.Injector().get_current_properties().get_frame('guiFrameAppWindow')
        for selection_rect in self.selection_rectangle.values():
            gui_frame_app_window.itemconfig(
                selection_rect,
                outline='black'
            )

    def move_selection_for_widget(self, widget):
        pass
