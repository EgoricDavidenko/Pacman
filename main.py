import pygame_menu
from pygame_menu import themes

import ghost
from level1 import boards
import math
import player as player
import pygame

dc = 0
schet = 0


def you_dead(screen):
    global dc, schet, run
    dc += 1
    if dc >= 3:
        death = True
        while death:
            screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 50)
            text = font.render(f'Game Over', True, (255, 255, 255))
            screen.blit(text, (370, 450))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    death = False
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            if '-' in str(boards[i][j]):
                boards[i][j] = int(boards[i][j].rstrip('-'))
    PacMan(player)


def you_winner(screen):
    global dc, schet, run
    win = True
    while win:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 50)
        text = font.render(f'Вы победили!', True, (0, 255, 0))
        screen.blit(text, (370, 450))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win = False
                dc = 3
    run = False


def PacMan(player):
    global dc, schet, run
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()

    pygame.mixer.music.load("sounds/1-track-1.mp3")
    pygame.mixer.music.play(-1)

    WIDTH = 900
    HEIGHT = 1030
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    timer = pygame.time.Clock()
    fps = 60
    PI = math.pi

    flicker = False

    player = player.Player(schet)

    ghost1 = ghost.Ghost(0, 2, 6, "horizontal", 0, 25)    # , px, py
    ghost2 = ghost.Ghost(2, 22, 2, "vertical", 25, 0)  # , px, py
    ghost3 = ghost.Ghost(3, 27, 30, "horizontal", 25, 0)   # , px, py
    ghost4 = ghost.Ghost(4, 7, 27, "vertical", 0, 25)   # , px, py

    all_sprites = pygame.sprite.Group()

    all_sprites.add(player)
    all_sprites.add(ghost1)
    all_sprites.add(ghost2)
    all_sprites.add(ghost3)
    all_sprites.add(ghost4)

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
    if dc == 3:
        run = False
    while run:
        schet = player.update()[0]
        if player.update()[3]:
            you_dead(screen)
            run = False
            break
        timer.tick(fps)

        screen.fill('black')
        draw_board()
        all_sprites.update()
        all_sprites.draw(screen)

        font = pygame.font.Font(None, 50)
        text = font.render(f'Счёт: {schet}', True, (255, 255, 255))
        screen.blit(text, (125, 980))
        if schet == 260:
            you_winner(screen)

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


player = player

pygame.init()
surface = pygame.display.set_mode((900, 1030))


def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)


def start_the_game():
    PacMan(player)


def level_menu():
    mainmenu._open(level)


mainmenu = pygame_menu.Menu('Pac-Man', 900, 1030, theme=themes.THEME_DARK)
mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Info', level_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

level = pygame_menu.Menu('Pac-Man от Егоров и Арсения', 900, 1030)
level.add.label('Для передвижения используйте стрелочки')
level.add.label('Для выхода из игры закройте окно с ней')

mainmenu.mainloop(surface)













