from properties import properties
from properties import properties_controller


class PropertiesFactory:
    def __init__(self):
        pass

    def get_properties_controller(self):
        return properties_controller.PropertiesController()

    def get_properties_model(self):
        return properties.Properties()
