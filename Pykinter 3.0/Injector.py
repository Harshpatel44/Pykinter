from frames.TitleBarFrame import TitleBarFrame
from frames.ToolBarFrame import ToolBarFrame
from frames.MenuBarFrame import MenuBarFrame
from frames.OptionBarFrame import OptionBarFrame
import frames.DeveloperFrame
import frames.WidgetsFrame
import common.Properties


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


def get_current_properties():
    return common.Properties.Properties()
