import pygame

from colors import *
from drawer import Drawer, CircleDrawer
from point import Point
from typing import Union


class Field:
    def __init__(self, drawer: Drawer, draw_point_coords = Point((160, 0)), width=640, height=600, background=WHITE):

        self.visible_width = width
        self.visible_height = height
        self.full_width = 10000
        self.full_height = 10000
        self.draw_point = draw_point_coords

        self.center = Point((-self.full_width/2, -self.full_height/2))
        self.rect = pygame.Rect(self.draw_point.to_tuple(), (width, height))

        self.drawer = drawer

        self.background = background

        self.field_states = []
        self.field_states.append(pygame.Surface((self.full_width, self.full_height)))
        self.field_states[0].fill(self.background)

    def change_coords_to_field(self, coords: Point):
        coords -= self.center
        return coords

    @property
    def is_mouse_collided(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)

    def draw(self, drawer: Union[CircleDrawer], start_pos, end_pos, pressed_pos):
        start_pos = self.change_coords_to_field(start_pos)
        end_pos = self.change_coords_to_field(end_pos)
        pressed_pos = self.change_coords_to_field(pressed_pos)
        drawer.draw(self.field_states, start_pos, end_pos, pressed_pos)

    def update(self, screen: pygame.Surface):
        coords = (self.draw_point - self.center).to_tuple()
        part_to_draw = pygame.Rect(coords, (self.visible_width, self.visible_height))
        screen.blit(self.field_states[-1], self.draw_point.to_tuple(), part_to_draw)

    def move(self, start_pos: Point, end_pos: Point):
        delta = end_pos - start_pos
        self.center += delta

    def draw_starting_state(self, screen: pygame.Surface):
        visible_part = pygame.Rect(self.draw_point.to_tuple(), (self.visible_width, self.visible_height))
        pygame.draw.rect(screen, self.background, visible_part)

    def add_field_state(self):
        self.field_states.append(self.field_states[-1])

    