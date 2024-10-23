import pygame
from point import Point

class FieldVisiblePart:
    def __init__(self, width, height, coords_on_screen: Point, coords_on_field: Point):

        self.collision_rect = pygame.Rect(coords_on_screen.to_tuple(), (width, height))
        self.rect_to_draw = pygame.Rect(coords_on_field.to_tuple(), (width, height))

    def is_mouse_collided(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.collision_rect.collidepoint(mouse_pos)

    def move(self, delta: Point):
        new_topleft = Point(self.rect_to_draw.topleft) - delta
        self.rect_to_draw.topleft = new_topleft.to_tuple()

    @property
    def coords_on_screen(self):
        return Point(self.collision_rect.topleft)

    @property
    def coords_on_field(self):
        return Point(self.rect_to_draw.topleft)