from widgets.iwidgets import IWidgets
from utils import window_basic_functions, selection_dots
from singleton import singleton
import injector


@singleton
class Widgets(IWidgets):
    def __init__(self, custom_injector=None):
        super().__init__()
        if custom_injector:
            self.Injector = custom_injector
        else:
            self.Injector = injector.Injector()
        self.active_widgets = []
        self.selected_widgets = []
        self.deleted_widgets = []

    def get_active_widgets(self):
        return self.active_widgets

    def set_active_widgets(self, widgets):
        self.active_widgets.extend(widgets)

    def get_selected_widgets(self):
        return self.selected_widgets

    def set_selected_widgets(self, selected_widgets):
        self.selected_widgets.extend(selected_widgets)

    def unset_selected_widgets(self):
        self.selected_widgets = []

    def unselect_widgets(self, *args):
        # self.unhighlight_widgets(self.selected_widgets)
        self.Injector.get_selection_dots_utils().hide_selection_for_widget()
        self.unset_selected_widgets()

    def get_deleted_widgets(self):
        return self.deleted_widgets

    def set_deleted_widgets(self, deleted_widgets):
        self.deleted_widgets.extend(deleted_widgets)

    def widget_bind_button1(self, event):
        window_basic_functions.start_widget_drag(event)
        self.update_properties_for_widget(event.widget)

        self.unselect_widgets()
        self.set_selected_widgets([event.widget])
        self.Injector.get_selection_dots_utils().create_selection_for_widget(event.widget)
        # self.highlight_widgets([event.widget])

    def widget_bind_button1_release(self, event):
        self.update_properties_for_widget(event.widget)

    def widget_bind_command_click(self, event):
        widget = event.widget
        self.update_properties_for_widget(event.widget)

        self.set_selected_widgets([widget])
        self.highlight_widgets([widget])

    def highlight_widgets(self, widgets):
        for widget in widgets:
            widget.config(bd=2)

    def unhighlight_widgets(self, widgets=None):
        if not widgets:
            widgets = self.selected_widgets
        for widget in widgets:
            widget.config(bd=0)
            widget.update()

    def update_properties_for_widget(self, widget):
        self.update_x_geometry(widget)
        self.update_y_geometry(widget)

    def __check_if_multi_selection(self):
        return True if len(self.selected_widgets) != 1 else False

    def update_x_geometry(self, widget):
        is_multi_selection = self.__check_if_multi_selection()
        properties_model = self.Injector.get_properties_factory().get_properties_model()
        x_geometry_widget = properties_model.get_properties()['X_geometry']
        if is_multi_selection:
            x_geometry_widget.variable.set(0)
        else:
            widget_x = widget.place_info()['x']
            x_geometry_widget.variable.set(widget_x)

    def update_y_geometry(self, widget):
        is_multi_selection = self.__check_if_multi_selection()
        properties_model = self.Injector.get_properties_factory().get_properties_model()
        y_geometry_widget = properties_model.get_properties()['Y_geometry']
        if is_multi_selection:
            y_geometry_widget.variable.set(0)
        else:
            widget_y = widget.place_info()['y']
            y_geometry_widget.variable.set(widget_y)

