from colors import *
from drawer import CircleDrawer
from field_visible_part import FieldVisiblePart
from point import Point
from typing import Union


class Field:
    def __init__(self, draw_point_coords = Point((160, 0)),
                 visible_width=640, visible_height=600, full_width=10000,
                 full_height=10000, starting_color=WHITE):

        self.center = Point((full_width/2, full_height/2))

        self.visible_part = FieldVisiblePart(visible_width, visible_height,
                                             draw_point_coords, self.center)

        self.field_states = [pygame.Surface((full_width, full_height))]
        self.field_states[0].fill(starting_color)

    def change_coords_from_screen_to_field(self, coords: Point):
        coords += self.visible_part.coords_on_field - self.visible_part.coords_on_screen
        return coords

    @property
    def is_mouse_collided(self):
        return self.visible_part.is_mouse_collided()

    def draw(self, drawer: Union[CircleDrawer], start_pos, end_pos, pressed_pos):
        start_pos = self.change_coords_from_screen_to_field(start_pos)
        end_pos = self.change_coords_from_screen_to_field(end_pos)
        pressed_pos = self.change_coords_from_screen_to_field(pressed_pos)
        drawer.draw(self.field_states, start_pos, end_pos, pressed_pos)

    def update(self, screen: pygame.Surface):
        screen.blit(self.field_states[-1], self.visible_part.coords_on_screen.to_tuple(),
                    self.visible_part.rect_to_draw)

    def move(self, start_pos: Point, end_pos: Point):
        delta = end_pos - start_pos
        self.visible_part.move(delta)

    def add_field_state(self):
        self.field_states.append(self.field_states[-1])

    