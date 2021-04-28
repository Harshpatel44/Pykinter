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

# frames = {}
# properties = {}
# selected_widgets = {}
# active_widgets = [{}]
# deleted_widgets = [{}]
