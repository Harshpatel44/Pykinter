from singleton import singleton


@singleton
class Properties:
    def __init__(self):
        self.frames = {}
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
