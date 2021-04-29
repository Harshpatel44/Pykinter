from widget_properties.iwidget_properties import IProperties
from singleton import singleton
import injector

@singleton
class Properties(IProperties):

    def __init__(self, custom_injector=None):
        super().__init__()
        if custom_injector:
            self.Injector = custom_injector
        else:
            self.Injector = injector.Injector()
        self.properties = {}

    def get_properties(self):
        return self.properties

    def set_properties(self, properties):
        self.properties = properties

    def add_properties(self, property):
        self.properties.update(property)

    def update_x_geometry(self, property_widget):
        x_value = property_widget.get()
        widgets_model = self.Injector.get_widgets_factory().get_widgets_model()
        selected_widgets = widgets_model.get_selected_widgets()
        for widget in selected_widgets:
            y_value = widget.place_info()['y']
            widget.place(x=x_value, y=y_value)

    def update_y_geometry(self, property_widget):
        y_value = property_widget.get()
        widgets_model = self.Injector.get_widgets_factory().get_widgets_model()
        selected_widgets = widgets_model.get_selected_widgets()
        for widget in selected_widgets:
            x_value = widget.place_info()['x']
            widget.place(x=x_value, y=y_value)



