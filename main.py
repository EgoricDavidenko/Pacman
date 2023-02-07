import copy

import pygame
import ghost
from level1 import boards
import math
import player

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

pygame.mixer.music.load("sounds/1-track-1.mp3")
pygame.mixer.music.play(-1)

WIDTH = 900
HEIGHT = 1030
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
level = copy.deepcopy(boards)
PI = math.pi


flicker = False

player = player.Player()

ghost1 = ghost.Ghost(0, 15, 6, "horizontal", 12, 12)
ghost2 = ghost.Ghost(0, 22, 16, "vertical", 8, 10)

all_sprites = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(ghost1)
all_sprites.add(ghost2)

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

    ###########################счёт############################################

    font = pygame.font.Font(None, 50)
    if player.update() == 2620:
        text1 = font.render(f'Вы победили!', True, (0, 255, 0))
        screen.blit(text1, (600, 980))
    text = font.render(f'Счёт: {player.update()}', True, (255, 255, 255))
    screen.blit(text, (125, 980))

    ###########################счёт############################################

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
