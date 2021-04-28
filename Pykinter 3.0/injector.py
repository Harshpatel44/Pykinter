from frames.TitleBarFrame import TitleBarFrame
from frames.ToolBarFrame import ToolBarFrame
from frames.MenuBarFrame import MenuBarFrame
from frames.OptionBarFrame import OptionBarFrame
import frames.DeveloperFrame
import frames.WidgetsFrame
from widgets.widgets_factory import WidgetsFactory
from widget_properties.widget_properties_factory import PropertiesFactory
import common.properties


class Injector:
    def __init__(self):
        pass

    def get_titlebar_frame(self):
        return TitleBarFrame(self)

    def get_toolbar_frame(self):
        return ToolBarFrame(self)

    def get_menubar_frame(self):
        return MenuBarFrame(self)

    def get_optionbar_frame(self):
        return OptionBarFrame(self)

    def get_developer_frame(self):
        return frames.DeveloperFrame.DeveloperFrame(self)

    def get_widget_frame(self):
        return frames.WidgetsFrame.WidgetsFrame(self)

    def get_current_properties(self):
        return common.properties.Properties()

    def get_widgets_factory(self):
        return WidgetsFactory()

    def get_properties_factory(self):
        return PropertiesFactory()
