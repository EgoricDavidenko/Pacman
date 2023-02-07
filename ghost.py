import pygame

import game_temp
import level1
import copy
import game_temp


class Ghost(pygame.sprite.Sprite):
    def __init__(self, number, x, y, movement_direction, offset_left, offset_right):  # right = up, left = down
        super(Ghost, self).__init__().__init__()

        self.level = copy.deepcopy(level1.boards)

        self.ghost_images = []
        for i in range(1, 6):
            self.ghost_images.append(pygame.transform.scale(pygame.image.load(f'ghost_images/{i}.png'), (30, 30)))

        self.image = self.ghost_images[number]

        self.rect = pygame.Rect(0, 0, 40, 40)

        self.mx = x
        self.my = y
        self.partx = 0
        self.party = 0
        self.movement_direction = movement_direction
        self.offset_left = offset_left
        self.offset_right = offset_right

        if self.movement_direction == "horizontal":
            self.dir = "right"
        elif self.movement_direction == "vertical":
            self.dir = "up"

        self.moving = "stop"

        self.temp_x = 0
        self.temp_y = 0

        self.counter = 3

    def move(self):
        if self.movement_direction == "horizontal":
            if self.dir == "right":
                if self.temp_x < self.offset_right * 6:
                    self.partx += 1
                    self.temp_x += 1
                    print(self.temp_x)
                else:
                    self.dir = "left"
            elif self.dir == "left":
                if self.temp_x > -1 * self.offset_left * 6:
                    self.partx -= 1
                    self.temp_x -= 1
                else:
                    self.dir = "right"
        elif self.movement_direction == "vertical":
            if self.dir == "up":
                if self.temp_y > -1 * self.offset_right * 6:
                    self.party -= 1
                    self.temp_y -= 1
                else:
                    self.dir = "down"
            elif self.dir == "down":
                if self.temp_y < self.offset_left * 6:
                    self.party += 1
                    self.temp_y += 1
                else:
                    self.dir = "up"


    def update(self):
        self.rect.x, self.rect.y = self.coord_to_pos(self.mx, self.my)

        if game_temp.start_game:
            if self.counter % 3 == 0:
                self.move()


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