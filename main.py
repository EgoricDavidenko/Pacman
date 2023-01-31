import copy

import ghost
from level1 import boards
import pygame
import math
import player

pygame.init()

WIDTH = 900
HEIGHT = 1000
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 120
level = copy.deepcopy(boards)
PI = math.pi

flicker = False

player = player.Player()

ghost1 = ghost.Ghost(0)

all_sprites = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(ghost1)

def draw_board():
    rows = 33
    cols = 30
    for i in range(rows):
        for j in range(cols):
            if boards[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * 30 + (0.5 * 30), i * 30 + (0.5 * 30)), 4)
            if boards[i][j] == 2 and not flicker:
                pygame.draw.circle(screen, 'white', (j * 30 + (0.5 * 30), i * 30 + (0.5 * 30)), 10)
            if boards[i][j] == 3:
                pygame.draw.line(screen, 'blue', (j * 30 + (0.5 * 30), i * 30),
                                 (j * 30 + (0.5 * 30), i * 30 + 30), 3)
            if boards[i][j] == 4:
                pygame.draw.line(screen, 'blue', (j * 30, i * 30 + (0.5 * 30)),
                                 (j * 30 + 30, i * 30 + (0.5 * 30)), 3)
            if boards[i][j] == 5:
                pygame.draw.arc(screen, 'blue', [(j * 30 - (30 * 0.4)) - 2, (i * 30 + (0.5 * 30)), 30, 30],
                                0, PI / 2, 3)
            if boards[i][j] == 6:
                pygame.draw.arc(screen, 'blue',
                                [(j * 30 + (30 * 0.5)), (i * 30 + (0.5 * 30)), 30, 30], PI / 2, PI, 3)
            if boards[i][j] == 7:
                pygame.draw.arc(screen, 'blue', [(j * 30 + (30 * 0.5)), (i * 30 - (0.4 * 30)), 30, 30], PI,
                                3 * PI / 2, 3)
            if boards[i][j] == 8:
                pygame.draw.arc(screen, 'blue',
                                [(j * 30 - (30 * 0.4)) - 2, (i * 30 - (0.4 * 30)), 30, 30], 3 * PI / 2,
                                2 * PI, 3)
            if boards[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * 30, i * 30 + (0.5 * 30)),
                                 (j * 30 + 30, i * 30 + (0.5 * 30)), 3)



run = True
while run:
    timer.tick(fps)

    screen.fill('black')
    draw_board()
    all_sprites.update()
    all_sprites.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move("up")
            if event.key == pygame.K_DOWN:
                player.move("down")
            if event.key == pygame.K_LEFT:
                player.move("left")
            if event.key == pygame.K_RIGHT:
                player.move("right")

    pygame.display.flip()
pygame.quit()
