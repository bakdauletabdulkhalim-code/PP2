import pygame
import random

pygame.init() 

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("Racer Game")  

WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

car1_img = pygame.image.load("car1.png").convert_alpha()
car1_img = pygame.transform.scale(car1_img, (80, 80)) 

player_w = 80
player_h = 80
player_x = WIDTH // 2 - player_w // 2  
player_y = HEIGHT - 100
player_speed = 5

enemy_w = 50
enemy_h = 80
enemy_x = random.randint(0, WIDTH - enemy_w)
enemy_y = -100
enemy_speed = 5

coin_x = random.randint(0, WIDTH - 20)
coin_y = -50
coin_speed = 5

coin_value = random.choice([1, 3, 5])

coins_collected = 0

font = pygame.font.Font(None, 30)

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - player_w:
        player_x = WIDTH - player_w

    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(0, WIDTH - enemy_w)

    coin_y += coin_speed
    if coin_y > HEIGHT:
        coin_y = -50
        coin_x = random.randint(0, WIDTH - 20)
        coin_value = random.choice([1, 3, 5]) 

    player_rect = pygame.Rect(player_x, player_y, player_w, player_h)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_w, enemy_h)

    if player_rect.colliderect(enemy_rect):
        print("GAME OVER")
        running = False

    coin_rect = pygame.Rect(coin_x, coin_y, 20, 20)

    if player_rect.colliderect(coin_rect):
        coins_collected += coin_value  
        coin_y = -50
        coin_x = random.randint(0, WIDTH - 20)
        coin_value = random.choice([1, 3, 5])

    if coins_collected % 5 == 0 and coins_collected != 0:
        enemy_speed = 5 + coins_collected // 5

    screen.blit(car1_img, (player_x, player_y))

    pygame.draw.rect(screen, BLACK, (enemy_x, enemy_y, enemy_w, enemy_h))

    if coin_value == 1:
        color = (200, 200, 0)
        size = 10
    elif coin_value == 3:
        color = (255, 165, 0)
        size = 15
    else:
        color = (255, 215, 0)
        size = 20

    pygame.draw.circle(screen, color, (coin_x, coin_y), size)

    text = font.render(f"Coins: {coins_collected}", True, BLACK)
    screen.blit(text, (WIDTH - 150, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()