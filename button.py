import pygame

from colors import *

class Button:
    def __init__(self, color = RED, coords=(0, 0), size=(20, 10),
                 border_color = BLACK, text='', border_width=3):

        self.coords = coords
        self.size = size
        self.rect = pygame.Rect(coords, size)
        self.is_hovered = False

        self.text = text
        self.border_width = border_width
        self.color = color
        self.border_color = border_color

        self.action = None

    def click(self):
        if self.action:
            self.action()

    def draw(self, screen: pygame.Surface):
        """Draw the button on the screen with an outline on hover."""
        self.is_hovered = self.mouse_collision()

        self.draw_unhovered(screen)

        if self.is_hovered:
            self.draw_border(screen)

        if self.text:
            text_surface = self.font.render(self.text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    def draw_unhovered(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, self.rect)

    def draw_border(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.border_color, self.rect, self.border_width)

    def check_click(self):
        """Check if the button was clicked."""

        if self.mouse_collision():
            self.click()

    def need_to_update(self):
        return self.is_hovered != self.mouse_collision()

    def mouse_collision(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)