from typing import List

import pygame

from point import Point
from colors import *

class Drawer:
    def __init__(self, screen, color=BLACK, thickness=1):
        self.screen = screen
        self._color = color
        self.thickness = thickness
        # self.draw_mode = circle_draw

    # def draw(self, start_pos: Point, end_pos: Point, pressed_pos: Point, field_states: List[pygame.Surface]):
    #     print(start_pos)
    #     pygame.draw.line(field_states[-1], self.color, (0, 0), (1, 1), 1)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: pygame.Color):
        self._color = color

    def change_thickness(self, thickness: int):
        self.thickness = thickness


class CircleDrawer(Drawer):
    def draw(self, field_states: List[pygame.Surface], start_pos: Point, end_pos: Point, pressed_pos: Point):
        """Draw a circle."""
        # super().draw(start_pos, end_pos, pressed_pos, field_states)
        field_states[-1] = field_states[-2].copy()
        radius = int(((end_pos.x - pressed_pos.x) ** 2 + (end_pos.y - pressed_pos.y) ** 2) ** 0.5)
        pygame.draw.circle(field_states[-1], self.color, pressed_pos.to_tuple(), radius, self.thickness)

class PenDrawer(Drawer):
    def draw(self, field_states: List[pygame.Surface], start_pos: Point, end_pos: Point, pressed_pos: Point):
        """Draw freehand with a pen tool."""
        pygame.draw.line(field_states[-1], self.color, start_pos.to_tuple(), end_pos.to_tuple(), self.thickness)

class RectDrawer(Drawer):
    def draw(self, field_states: List[pygame.Surface], start_pos: Point, end_pos: Point, pressed_pos: Point):
        """Draw a rectangle, handling cases where end_pos may be less than start_pos."""
        # Make a copy of the previous field state to draw on
        field_states[-1] = field_states[-2].copy()

        # Calculate the top-left corner and size of the rectangle
        top_left_x = min(pressed_pos.x, end_pos.x)
        top_left_y = min(pressed_pos.y, end_pos.y)
        width = abs(end_pos.x - pressed_pos.x)
        height = abs(end_pos.y - pressed_pos.y)

        # Create the rect object with calculated top-left position and size
        rect = pygame.Rect(top_left_x, top_left_y, width, height)

        # Draw the rectangle on the latest field state
        pygame.draw.rect(field_states[-1], self.color, rect, self.thickness)

