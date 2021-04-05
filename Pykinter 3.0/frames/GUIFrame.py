import tkinter as tk
from frames.IFrame import IFrame
from singleton import singleton
from common import constants as const
import Injector


@singleton
class GUIFrame(IFrame):
    def __init__(self):
        super().__init__()
        self.layout()

    def layout(self):
        pass