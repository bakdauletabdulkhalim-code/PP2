import pygame
import random

pygame.init()  # pygame-ді іске қосу

WIDTH, HEIGHT = 600, 400
CELL = 20  # тор өлшемі

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # терезе
clock = pygame.time.Clock()  # FPS басқару

# түстер
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
WHITE = (255, 255, 255)

# жылан денесі (сегменттер тізімі)
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL, 0)  # бастапқы қозғалыс бағыты

def random_food():
    while True:
        pos = (random.randrange(0, WIDTH, CELL),
               random.randrange(0, HEIGHT, CELL))  # тор бойынша кездейсоқ позиция
        if pos not in snake:
            return pos

food = random_food()  # тамақ пайда болады

score = 0
level = 1
speed = 7

running = True

while running:
    clock.tick(speed)  # ойын жылдамдығын басқару

    for event in pygame.event.get():  # оқиғаларды тексеру
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # бағытты басқару (кері жүрмеу үшін)
    if keys[pygame.K_UP] and direction != (0, CELL):
        direction = (0, -CELL)
    elif keys[pygame.K_DOWN] and direction != (0, -CELL):
        direction = (0, CELL)
    elif keys[pygame.K_LEFT] and direction != (CELL, 0):
        direction = (-CELL, 0)
    elif keys[pygame.K_RIGHT] and direction != (-CELL, 0):
        direction = (CELL, 0)

    # жаңа бас координатасы
    x, y = snake[0]
    head = (x + direction[0], y + direction[1])

    # қабырғаға соғылу
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        running = False

    # өзіне соғылу
    if head in snake:
        running = False

    snake.insert(0, head)  # жыланды алға жылжыту

    if head == food:
        score += 1
        food = random_food()  # жаңа тамақ

        # деңгей өсу логикасы
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()  # соңын өшіру

    screen.fill(BLACK)  # фон

    pygame.draw.rect(screen, RED, (*food, CELL, CELL))  # тамақты салу

    for s in snake:
        pygame.draw.rect(screen, GREEN, (*s, CELL, CELL))  # жыланды салу

    # ұпай мәтіні
    font = pygame.font.SysFont(None, 30)
    screen.blit(font.render(f"Score: {score} LVL: {level}", True, WHITE), (10, 10))

    pygame.display.update()  # экранды жаңарту

pygame.quit()  # шығу