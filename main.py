import pygame


if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('pacman')

    fps = 30
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(fps)

        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pygame.display.flip()
    pygame.quit()