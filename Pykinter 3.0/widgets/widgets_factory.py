from widgets import widgets_controller, widgets
from singleton import singleton


@singleton
class WidgetsFactory:
    def __init__(self):
        pass

    def get_widget_controller(self):
        return widgets_controller.WidgetsController()

    def get_widgets_model(self):
        return widgets.Widgets()
