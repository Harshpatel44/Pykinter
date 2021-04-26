from properties.iproperties import IProperties
from singleton import singleton


@singleton
class Properties(IProperties):

    def __init__(self):
        super().__init__()
        pass

    def update_properties_for_widget(self, widget):
        pass