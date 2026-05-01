import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Practice 11")

clock = pygame.time.Clock()

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

color = BLACK
tool = "brush"

drawing = False
start_pos = (0,0)

running = True
while running:
    screen.fill((200,200,200))
    screen.blit(canvas, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

            if tool == "brush":
                pygame.draw.circle(canvas, color, event.pos, 5)

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if tool == "square":
                size = abs(end_pos[0] - start_pos[0])
                pygame.draw.rect(canvas, color, (start_pos[0], start_pos[1], size, size), 2)

            if tool == "r_triangle":
                pygame.draw.polygon(canvas, color, [
                    start_pos,
                    (end_pos[0], start_pos[1]),
                    (start_pos[0], end_pos[1])
                ], 2)

            if tool == "e_triangle":
                x, y = start_pos
                pygame.draw.polygon(canvas, color, [
                    (x, y),
                    (x+60, y),
                    (x+30, y-50)
                ], 2)

            if tool == "rhombus":
                x, y = start_pos
                pygame.draw.polygon(canvas, color, [
                    (x, y),
                    (x+40, y+20),
                    (x, y+40),
                    (x-40, y+20)
                ], 2)

    if drawing and tool == "brush":
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(canvas, color, pos, 5)

    if drawing and tool == "eraser":
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(canvas, WHITE, pos, 15)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_b]: tool = "brush"
    if keys[pygame.K_e]: tool = "eraser"
    if keys[pygame.K_s]: tool = "square"
    if keys[pygame.K_r]: tool = "r_triangle"
    if keys[pygame.K_t]: tool = "e_triangle"
    if keys[pygame.K_h]: tool = "rhombus"

    if keys[pygame.K_1]: color = BLACK
    if keys[pygame.K_2]: color = RED
    if keys[pygame.K_3]: color = GREEN
    if keys[pygame.K_4]: color = BLUE

    pygame.display.update()
    clock.tick(60)

pygame.quit()