import pygame
pygame.init()
display = pygame.display.set_mode((500, 500))
display.fill((255, 255, 255))
GREEN = (0, 255, 0)
pygame.draw.circle(display, GREEN, (100,101,),40)
pygame.draw.circle(display,GREEN, (100, 100,),50, 3)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()