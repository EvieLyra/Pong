import pygame
from random import randint
BLACK = (0,0,0)
LPINK = (255,209,220)


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(LPINK)
        self.image.set_colorkey(LPINK)

        pygame.draw.rect(self.image, color, [0,0, width, height])

        self.velocity = [randint(4,8),randint(-8,8)]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)