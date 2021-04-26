from singleton import singleton


@singleton
class Properties:
    def __init__(self):
        self.frames = {}
        self.active_widgets = []
        self.selected_widgets = []
        self.deleted_widgets = []
        self.properties = {}
        self.main = None

    def get_main(self):
        return self.main

    def set_main(self, main):
        self.main = main

    def get_frames(self):
        return self.frames

    def get_frame(self, frame):
        return self.frames[frame]

    def set_frames(self, frames):
        self.frames = frames

    def add_frames(self, frames_with_names):
        self.frames.update(frames_with_names)

    def get_active_widgets(self):
        return self.active_widgets

    def set_active_widgets(self, widgets):
        self.active_widgets.extend(widgets)

    def get_selected_widgets(self):
        return self.selected_widgets

    def set_selected_widgets(self, selected_widgets):
        self.selected_widgets.extend(selected_widgets)

    def get_deleted_widgets(self):
        return self.deleted_widgets

    def set_deleted_widgets(self, deleted_widgets):
        self.deleted_widgets.extend(deleted_widgets)

    def get_properties(self):
        return self.properties

    def set_properties(self, properties):
        self.properties.update(properties)


# frames = {}
# properties = {}
# selected_widgets = {}
# active_widgets = [{}]
# deleted_widgets = [{}]
