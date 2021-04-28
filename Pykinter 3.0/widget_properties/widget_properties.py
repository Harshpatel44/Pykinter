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

    def update_properties_for_widget(self, widget):
        properties = self.Injector.get_properties_factory().get_properties_model()
        self.update_x_geometry(widget, properties)
        self.update_y_geometry(widget, properties)

    def update_x_geometry(self, widget, properties = None):
        widget_x = widget.place_info()['x']
        x_geometry_widget = properties.get_properties()['X_geometry']
        x_geometry_widget.variable.set(widget_x)

    def update_y_geometry(self, widget, properties = None):
        widget_y = widget.place_info()['y']
        y_geometry_widget = properties.get_properties()['Y_geometry']
        y_geometry_widget.variable.set(widget_y)




