import pygame

from colors import *
from drawer import Drawer, CircleDrawer, PenDrawer, RectDrawer
from button import Button


class Toolbar:
    button_to_drawer_dict_draft = {
        Button(color=RED): CircleDrawer,
        Button(color=GREEN): PenDrawer,
        Button(color=BLUE): RectDrawer,
    }
    # def __init__(self, drawer: Drawer, coords=(0, 0),
    def __init__(self, screen: pygame.Surface, coords=(0, 0),
                 width=160, height=200, color=WHITE):
        
        self.last_pressed_button = Button()
        self.coords = coords
        self.width = width
        self.height = height
        self.rect = pygame.Rect(coords, (width, height))
        self.is_hovered = False
        
        self.color = color
    
        self.screen = screen
        self.button_to_drawer = {}

        self.button_list = []

        for button, drawer in self.button_to_drawer_dict_draft.items():
            self.button_to_drawer[button] = drawer(self.screen)
            self.last_pressed_button = button
            self.add_button(button, drawer(self.screen))

        
    def get_new_button_pos(self, button_width: int, button_height: int):
        
        cols = self.width / button_width
        
        if self.button_list:
            last_button_coords = self.button_list[-1].coords
        else:
            return self.coords
        
        last_col_num = (last_button_coords[0] - self.coords[0])/button_width + 1
        if last_col_num >= cols:
            new_button_coords = list(self.coords)
            new_button_coords[1] = last_button_coords[1] + button_height
        else:
            new_button_coords = list(last_button_coords)
            new_button_coords[0] +=  button_width

        return new_button_coords

    def add_button(self, button: Button, draw_mode, button_width=80, button_height=40):
        
        coords = self.get_new_button_pos(button_width, button_height)
        if coords[1] >= self.height:
            print("Toolbar is full!")
            return

        # self.connect(button, draw_mode)

        button.rect = pygame.Rect(coords, (button_width, button_height))
        button.coords = coords
        self.button_list.append(button)

    def draw_starting_toolbar(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, self.rect)
        for button in self.button_list:
            button.draw_unhovered(screen)

    def update(self, screen: pygame.Surface):
        self.is_hovered = self.mouse_collision()
        pygame.draw.rect(screen, self.color, self.rect)
        for button in self.button_list:
            button.draw(screen)

    def check_click(self):
        if self.mouse_collision():
            for button in self.button_list:
                button.check_click()
                if button.mouse_collision():
                    self.last_pressed_button = button

    def mouse_collision(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)

    def need_to_update(self):
        if self.is_hovered != self.mouse_collision():
            return True
        if self.mouse_collision():
            return self.buttons_need_to_update()
        return False


    def buttons_need_to_update(self):
        for button in self.button_list:
            if button.need_to_update():
                return True
        return False


