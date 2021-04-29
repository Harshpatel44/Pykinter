import injector


class PropertiesController:
    def __init__(self, custom_injector=None):
        if custom_injector:
            self.Injector = custom_injector
        else:
            self.Injector = injector.Injector()
        self.properties_model = self.Injector.get_properties_factory().get_properties_model()

    def set_x_geometry_property(self, event):
        property_widget = event.widget
        self.properties_model.update_x_geometry(property_widget)

    def set_y_geometry_property(self, event):
        property_widget = event.widget
        self.properties_model.update_y_geometry(property_widget)
