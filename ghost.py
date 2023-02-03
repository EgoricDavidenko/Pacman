import pygame

import game_temp
import level1
import copy
import game_temp


class Ghost(pygame.sprite.Sprite):
    def __init__(self, number):
        super(Ghost, self).__init__().__init__()

        self.level = copy.deepcopy(level1.boards)

        self.ghost_images = []
        for i in range(1, 6):
            self.ghost_images.append(pygame.transform.scale(pygame.image.load(f'ghost_images/{i}.png'), (30, 30)))

        self.image = self.ghost_images[0]

        self.rect = pygame.Rect(0, 0, 40, 40)

        self.mx = 15
        self.my = 16
        self.partx = 0
        self.party = 0

        self.dir = "up"
        self.prev_dir = "up"
        self.inbox = True
        self.moving = "stop"

        self.counter = 3

    def move(self, direction):
        # self.prev_dir = self.dir
        # self.dir = direction
        if direction == "up":
            self.party -= 1

    def update(self):
        self.rect.x, self.rect.y = self.coord_to_pos(self.mx, self.my)

        if game_temp.start_game:
            if self.counter % 3 == 0:
                if self.inbox:
                    self.move("up")


        self.counter += 1
        self.rect.x, self.rect.y = self.coord_to_pos(self.mx, self.my)

    def coord_to_pos(self, mx, my):
        if self.partx == 6:
            self.mx += 1
            mx += 1
            self.partx = 0
        elif self.partx == -6:
            self.mx -= 1
            mx -= 1
            self.partx = 0
        if self.party == 6:
            self.my += 1
            my += 1
            self.party = 0
        if self.party == -6:
            self.my -= 1
            my -= 1
            self.party = 0

        return mx * 30 + self.partx * 5, my * 30 + self.party * 5