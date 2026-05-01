import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Practice 11")

clock = pygame.time.Clock()

BLACK = (0,0,0)
GREEN = (0,200,0)
RED = (200,0,0)
WHITE = (255,255,255)

snake = [(100,100), (80,100), (60,100)]
direction = (CELL, 0)

def random_food():
    while True:
        pos = (random.randrange(0, WIDTH, CELL),
               random.randrange(0, HEIGHT, CELL))
        if pos not in snake:
            return pos

food = random_food()

food_value = random.choice([1,2,3])

food_time = pygame.time.get_ticks()

score = 0
level = 1
speed = 7

running = True
while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_UP] and direction != (0, CELL):
        direction = (0, -CELL)
    elif keys[pygame.K_DOWN] and direction != (0, -CELL):
        direction = (0, CELL)
    elif keys[pygame.K_LEFT] and direction != (CELL, 0):
        direction = (-CELL, 0)
    elif keys[pygame.K_RIGHT] and direction != (-CELL, 0):
        direction = (CELL, 0)
        
    x, y = snake[0]
    head = (x + direction[0], y + direction[1])

    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        running = False

    if head in snake:
        running = False

    snake.insert(0, head)

    if head == food:
        score += food_value
        food = random_food()
        food_value = random.choice([1,2,3])
        food_time = pygame.time.get_ticks()

        if score % 5 == 0:
            level += 1
            speed += 1

    else:
        snake.pop()

    if pygame.time.get_ticks() - food_time > 5000:
        food = random_food()
        food_value = random.choice([1,2,3])
        food_time = pygame.time.get_ticks()

    screen.fill(BLACK)

    if food_value == 1:
        color = (255,100,100)
        size = CELL
    elif food_value == 2:
        color = (255,0,0)
        size = CELL+5
    else:
        color = (150,0,0)
        size = CELL+10

    pygame.draw.rect(screen, color, (*food, CELL, CELL))

    for s in snake:
        pygame.draw.rect(screen, GREEN, (*s, CELL, CELL))

    font = pygame.font.SysFont(None, 30)
    text = font.render(f"Score: {score}  LVL: {level}", True, WHITE)
    screen.blit(text, (10,10))

    pygame.display.update()

pygame.quit()