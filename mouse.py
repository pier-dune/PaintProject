import pygame

class Mouse:
    def __init__(self):
        self.pressed_pos = None
        self.released_pos = None
        self.current_pos = None
        self.previous_pos = None