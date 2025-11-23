import pygame
pygame.init()
display = pygame.display.set_mode((300, 400))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(display, (0, 125, 125), (30, 30, 60, 60))
    pygame.display.flip()