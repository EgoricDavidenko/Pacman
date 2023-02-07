import pygame
import pygame_menu
from pygame_menu import themes
# import main

pygame.init()
surface = pygame.display.set_mode((600, 400))


def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)


def start_the_game():
    pass


def level_menu():
    mainmenu._open(level)


mainmenu = pygame_menu.Menu('Pac-Man', 600, 400, theme=themes.THEME_DARK)
# mainmenu.add.text_input('Name: ', default='username', maxchar=20)
mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Info', level_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

level = pygame_menu.Menu('Pac-Man от Егоров и Арсения', 600, 400)
level.add.label('Для передвижения используйте')
level.add.label('Стрелочки')
# level.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)

mainmenu.mainloop(surface)
