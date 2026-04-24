import pygame
import random

pygame.init()  # pygame-ді іске қосамыз

# экран өлшемдері
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("Racer Game")  

# түстер
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 215, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

car_img = pygame.image.load("car1.png").convert_alpha()
car_img = pygame.transform.scale(car_img, (50, 80)) 

# көлік параметрлері
player_w = 50
player_h = 80
player_x = WIDTH // 2 - player_w // 2  # экран ортасына қою
player_y = HEIGHT - 100
player_speed = 5

# қарсы кедергі 
enemy_w = 50
enemy_h = 80
enemy_x = random.randint(0, WIDTH - enemy_w)  # кездейсоқ орын
enemy_y = -100
enemy_speed = 5

# ұпай параметрлері
coin_size = 20
coin_x = random.randint(0, WIDTH - coin_size)
coin_y = -50
coin_speed = 5

# жиналған ұпай саны
coins_collected = 0

# мәтін шығару үшін font
font = pygame.font.Font(None, 30)

running = True
while running:
    screen.fill(WHITE)  # фонды ақ қыламыз

    # терезені жабу
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # пернетақта арқылы басқару
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # экраннан шығып кетпеу
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - player_w:
        player_x = WIDTH - player_w

    # кедергі төмен түседі
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(0, WIDTH - enemy_w)

    # ұпай да төмен түседі
    coin_y += coin_speed
    if coin_y > HEIGHT:
        coin_y = -50
        coin_x = random.randint(0, WIDTH - coin_size)

    # соқтығысу 
    player_rect = pygame.Rect(player_x, player_y, player_w, player_h)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_w, enemy_h)

    if player_rect.colliderect(enemy_rect):
        print("GAME OVER")
        running = False

    # coin жинау
    coin_rect = pygame.Rect(coin_x, coin_y, coin_size, coin_size)

    if player_rect.colliderect(coin_rect):
        coins_collected += 1
        coin_y = -50
        coin_x = random.randint(0, WIDTH - coin_size)

    # көлікті экранға шығару 
    screen.blit(car_img, (player_x, player_y))

    # кедергі қара төртбұрыш
    pygame.draw.rect(screen, BLACK, (enemy_x, enemy_y, enemy_w, enemy_h))

    # ұпай сары шеңбер
    pygame.draw.circle(screen, YELLOW, (coin_x, coin_y), coin_size)

    # ұпай санын көрсету
    text = font.render(f"Coins: {coins_collected}", True, BLACK)
    screen.blit(text, (WIDTH - 120, 10))

    pygame.display.flip()  # экранды жаңарту
    clock.tick(60)  # FPS = 60

pygame.quit()  # ойыннан шығу