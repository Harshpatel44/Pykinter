from widget_properties import widget_properties
from widget_properties import widget_properties_controller


class PropertiesFactory:
    def __init__(self):
        pass

    def get_properties_controller(self):
        return widget_properties_controller.PropertiesController()

    def get_properties_model(self):
        return widget_properties.Properties()
