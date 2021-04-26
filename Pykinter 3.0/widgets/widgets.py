from widgets.iwidgets import IWidgets
from utils import windowBasicFunctions
from singleton import singleton
import injector

@singleton
class Widgets(IWidgets):
    def __init__(self):
        super().__init__()
        pass

    def widget_bind_button1(self, event):
        windowBasicFunctions.start_widget_drag(event)
        properties_model = injector.Injector().get_properties_factory().get_properties_model()
        properties_model.update_properties_for_widget(event.widget)
