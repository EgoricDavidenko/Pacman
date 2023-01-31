import pygame
import level1
from level1 import boards
import copy


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.level = copy.deepcopy(boards)
        self.schet = 0

        self.player_images = []
        for i in range(1, 17):
            self.player_images.append(pygame.transform.scale(pygame.image.load(f'player_images/{i}.png'), (30, 30)))

        # self.image = pygame.Surface((2 * 20, 2 * 20),
        #                             pygame.SRCALPHA, 32)
        # pygame.draw.circle(self.image, pygame.Color("yellow"),
        #                    (20, 20), 20)
        self.image = self.player_images[0]

        self.rect = pygame.Rect(x, y, 40, 40)

        # self.rect.x = x
        # self.rect.y = y

        self.mx = 15 # !!! normal cords in our opinion -1
        self.my = 24
        self.partx = 0
        self.party = 0

        self.dir = "right"
        self.prev_dir = "right"
        self.start_game = False
        self.animation_counter = 0
        self.flicker = False
        self.moving = "stop"

        self.counter = 3

    def move(self, direction):
        self.start_game = True
        self.prev_dir = self.dir
        self.dir = direction

    def posle_togo_kak_pacman_syedaet_energeticheskuyu_tabletku(self):
        print('призраки стали уязвимыми, скорее съешь их!')

    def update(self):
        self.rect.x, self.rect.y = self.coord_to_pos(self.mx, self.my)

        if self.start_game:

            if self.counter % 3 == 0:
                self.counter = 0
                if self.dir == "up":
                    if self.level[self.my - 1][self.mx] in [0, 1, 2]:
                        self.prev_dir = "up"
                        self.party -= 1
                        self.moving = "up"
                    else:
                        self.dir = self.prev_dir
                if self.dir == "down":
                    if self.level[self.my + 1][self.mx] in [0, 1, 2]:
                        self.prev_dir = "down"
                        self.party += 1
                        self.moving = "down"
                    else:
                        self.dir = self.prev_dir
                if self.dir == "left":
                    if self.level[self.my][self.mx - 1] in [0, 1, 2]:
                        self.prev_dir = "left"
                        self.partx -= 1
                        self.moving = "left"
                    else:
                        self.dir = self.prev_dir
                if self.dir == "right":
                    if self.level[self.my][self.mx + 1] in [0, 1, 2]:
                        self.prev_dir = "right"
                        self.partx += 1
                        self.moving = "right"
                    else:
                        self.dir = self.prev_dir

            ###########################счёт############################################

            if self.level[self.my][self.mx] == 1:
                level1.boards[self.my][self.mx] = 0
                self.schet += 10
            if self.level[self.my][self.mx] == 2:
                level1.boards[self.my][self.mx] = 0
                self.schet += 50
                self.posle_togo_kak_pacman_syedaet_energeticheskuyu_tabletku()
            self.counter += 1

            ###########################счёт############################################

        self.rect.x, self.rect.y = self.coord_to_pos(self.mx, self.my)
        # print(self.coord_to_pos(self.mx, self.my))

        if self.animation_counter < 19:
            self.animation_counter += 1
            if self.animation_counter > 3:
                self.flicker = False
        else:
            self.animation_counter = 0
            self.flicker = True

        self.draw_player()

    def draw_player(self):
        # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
        ###########################счёт############################################

        font = pygame.font.Font(None, 100)
        text = font.render(f'{self.schet}', True, (255, 255, 255))

        ###########################счёт############################################

        if self.dir == "right":
            self.image = self.player_images[self.animation_counter // 5]
        elif self.dir == "left":
            self.image = self.player_images[self.animation_counter // 5 + 8]
        elif self.dir == "up":
            self.image = self.player_images[self.animation_counter // 5 + 12]
        elif self.dir == "down":
            self.image = self.player_images[self.animation_counter // 5 + 4]

        return text

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
