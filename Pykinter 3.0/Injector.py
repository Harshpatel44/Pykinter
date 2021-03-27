import titlebar.Layout
import toolbar.Layout
import menubar1.Layout
import menubar2.Layout
import Frames.DeveloperFrame
import Frames.WidgetsFrame
import current_state.Properties


def get_titlebar_layout(self):
    return titlebar.Layout.Layout(self)


def get_toolbar_layout(self):
    return toolbar.Layout.Layout(self)


def get_menubar1_layout(self):
    return menubar1.Layout.Layout(self)


def get_menubar2_layout(self):
    return menubar2.Layout.Layout(self)


def get_developer_frame(self):
    return Frames.DeveloperFrame.DeveloperFrame(self)


def get_widget_frame(self):
    return Frames.WidgetsFrame.WidgetsFrame(self)


def get_current_properties():
    return current_state.Properties.Properties()
