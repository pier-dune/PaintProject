import pygame

from paint import Paint

paint = Paint()
clock = pygame.time.Clock()

paint.draw_starting_interface()

run = True

while run:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                paint.left_mouse_was_pressed()
            elif event.button == 2:
                paint.middle_mouse_was_pressed()
        if event.type == pygame.MOUSEMOTION:
            paint.mouse_was_moved()
        if event.type == pygame.MOUSEBUTTONUP:
            paint.mouse_was_released()
        if event.type == pygame.MOUSEWHEEL:
            paint.wheel_was_moved()
    clock.tick(60)
pygame.quit()