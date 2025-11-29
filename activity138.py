import pygame
import random
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2
BLUE = pygame.Color('blue')
RED = pygame.Color('red')
GREEN = pygame.Color('green')
YELLOW = pygame.Color('yellow')
COLOURS = [BLUE, RED, GREEN, YELLOW]
class sprite(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.velocity = [random.randint(-5, 5), random.randint(-5, 5)]
    def update(self):
        self.rect.move_ip(self.velocity)    
        boundary_hit = False
        if self.rect.left < 0 or self.rect.right > 800:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
    def change_colour(self):
        self.image.fill(random.choice(COLOURS))
def change_background_colour():
    global bg_colour
    bg_colour = random.choice(COLOURS)
all_sprites = pygame.sprite.Group()
sp1 = sprite(BLUE, 50, 50)
sp1.rect.x = random.randint (0,100)
sp1.rect.y = random.randint (0,100)
all_sprites.add(sp1)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sprite Colour Change on Boundary Hit")
bg_colour = pygame.Color('black')
screen.fill(bg_colour)
exit = False
clock = pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_colour()
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_colour()
    all_sprites.update()
    screen.fill(bg_colour)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()