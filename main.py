import pygame
import Player

all_sprites = pygame.sprite.Group()

if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('pacman')

    fps = 30
    running = True
    clock = pygame.time.Clock()

    player = Player.Player(20, 100, 100)
    all_sprites.add(player)

    while running:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move("up")
                if event.key == pygame.K_DOWN:
                    player.move("down")
                if event.key == pygame.K_LEFT:
                    player.move("left")
                if event.key == pygame.K_RIGHT:
                    player.move("right")

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
    pygame.quit()
    #zxc