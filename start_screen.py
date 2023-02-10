import pygame
import pygame_menu
from pygame_menu import themes

pygame.init()
surface = pygame.display.set_mode((600, 400))


def start_the_game():
    pass


def level_menu():
    mainmenu._open(level)


mainmenu = pygame_menu.Menu('Pac-Man', 600, 400, theme=themes.THEME_DARK)
mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Info', level_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

level = pygame_menu.Menu('Pac-Man от Егоров и Арсения', 600, 400)
level.add.label('Для передвижения используйте')
level.add.label('Стрелочки')

mainmenu.mainloop(surface)

