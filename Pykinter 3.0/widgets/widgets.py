from widgets.iwidgets import IWidgets
from utils import windowBasicFunctions
from singleton import singleton
import injector

@singleton
class Widgets(IWidgets):
    def __init__(self, custom_injector=None):
        super().__init__()
        if custom_injector:
            self.Injector = custom_injector
        else:
            self.Injector = injector.Injector()
        self.active_widgets = []
        self.selected_widgets = []
        self.deleted_widgets = []

    def get_active_widgets(self):
        return self.active_widgets

    def set_active_widgets(self, widgets):
        self.active_widgets.extend(widgets)

    def get_selected_widgets(self):
        return self.selected_widgets

    def set_selected_widgets(self, selected_widgets):
        self.selected_widgets.extend(selected_widgets)

    def get_deleted_widgets(self):
        return self.deleted_widgets

    def set_deleted_widgets(self, deleted_widgets):
        self.deleted_widgets.extend(deleted_widgets)

    def widget_bind_button1(self, event):
        windowBasicFunctions.start_widget_drag(event)
        properties_model = self.Injector.get_properties_factory().get_properties_model()
        properties_model.update_properties_for_widget(event.widget)
