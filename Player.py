import pygame
import main

class Player(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__()
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)

        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)

        self.rect.x = x
        self.rect.y = y
