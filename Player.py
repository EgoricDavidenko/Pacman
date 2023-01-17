import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__()
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("yellow"),
                           (radius, radius), radius)

        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)

        self.rect.x = x
        self.rect.y = y
        self.speed = 10
        self.dir = "stop"

    def move(self, direction):
        self.dir = direction
        print(direction)

    def update(self):
        if self.dir == "up":
            self.rect.y -= self.speed
            print("up")
        if self.dir == "down":
            self.rect.y += self.speed
        if self.dir == "left":
            self.rect.x -= self.speed
        if self.dir == "right":
            self.rect.x += self.speed
        if self.dir == "stop":
            pass

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def stop(self):
        self.dir = "stop"

