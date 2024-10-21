import pygame

from button import Button
from drawer import Drawer
from field import Field
from mouse import Mouse
from point import Point
from toolbar import Toolbar
from colors import *

class Paint:
    def __init__(self, width=800, height=600):

        self.screen = pygame.display.set_mode((width, height))
        pygame.init()
        pygame.display.set_caption('Paint')

        self.is_drawing = False
        self.is_moving = False

        self.mouse = Mouse()
        self.drawer = Drawer(self.screen)
        self.field = Field(self.drawer)
        self.toolbar = Toolbar(screen=self.screen)
    
    def left_mouse_was_pressed(self):
        self.mouse.pressed_pos = Point(pygame.mouse.get_pos())
        self.toolbar.check_click()
        if self.field.is_mouse_collided:
            print(self.mouse.current_pos, self.mouse.previous_pos)
            self.is_drawing = True
            self.field.add_field_state()

    def midlle_mouse_was_pressed(self):
        if self.field.is_mouse_collided:
            self.is_moving = True
        
    def mouse_was_released(self):
        self.is_drawing = False
        self.is_moving = False
        self.mouse.released_pos = Point(pygame.mouse.get_pos())
        print(self.field.field_states)

    def mouse_was_moved(self):
        self.mouse.previous_pos = self.mouse.current_pos
        self.mouse.current_pos = Point(pygame.mouse.get_pos())

        if self.toolbar.need_to_update():
            self.toolbar.update(self.screen)


        if self.is_drawing:
            drawer = self.toolbar.button_to_drawer[self.toolbar.last_pressed_button]
            self.is_drawing = self.field.is_mouse_collided
            self.field.draw(drawer, self.mouse.previous_pos, self.mouse.current_pos, self.mouse.pressed_pos)
            self.field.update(self.screen)
        if self.is_moving:
            self.field.move(self.mouse.previous_pos, self.mouse.current_pos)
            self.field.update(self.screen)


    def wheel_was_moved(self):
        pass

    def draw_starting_interface(self):
        self.toolbar.draw_starting_toolbar(self.screen)
        self.field.draw_starting_state(self.screen)
