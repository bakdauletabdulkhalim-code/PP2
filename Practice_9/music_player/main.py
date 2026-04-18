import pygame
from player import Player

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 50)
player = Player()

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((255, 255, 255))

    text = font.render(f"Track: {player.index + 1}", True, (0, 0, 0))
    screen.blit(text, (150, 120))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next()
            elif event.key == pygame.K_b:
                player.prev()
            elif event.key == pygame.K_q:
                running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()