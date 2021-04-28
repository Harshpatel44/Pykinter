import injector


class PropertiesController:
    def __init__(self, custom_injector=None):
        if custom_injector:
            self.Injector = custom_injector
        else:
            self.Injector = injector.Injector()
