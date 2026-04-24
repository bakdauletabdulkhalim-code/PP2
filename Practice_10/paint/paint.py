import pygame

pygame.init()  # pygame кітапханасын іске қосу

# экран өлшемі
w, h = 800, 600
screen = pygame.display.set_mode((w, h))  # терезе ашу
clock = pygame.time.Clock()  # FPS бақылау

# сурет салатын қабат 
canvas = pygame.Surface((w, h))
canvas.fill((255, 255, 255))  # бастапқы фон (ақ)

# түстер
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

color = BLACK  
tool = "brush"  
drawing = False  
start_pos = (0, 0)  

running = True
while running:
    screen.fill((200, 200, 200))  # экранды сұр түске бояу
    screen.blit(canvas, (0, 0))  

    for event in pygame.event.get():  # барлық оқиғаларды тексеру
        if event.type == pygame.QUIT:
            running = False  

        # тышқан басылғанда
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos 

            if tool == "brush":
                pygame.draw.circle(canvas, color, event.pos, 5)

        # тышқан жіберілгенде
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos  

            # төртбұрыш салу
            if tool == "rect":
                x = min(start_pos[0], end_pos[0])
                y = min(start_pos[1], end_pos[1])
                w = abs(start_pos[0] - end_pos[0])
                h = abs(start_pos[1] - end_pos[1])
                pygame.draw.rect(canvas, color, (x, y, w, h), 2)

            # шеңбер салу
            if tool == "circle":
                r = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2) ** 0.5)
                pygame.draw.circle(canvas, color, start_pos, r, 2)

    # сурет режимі
    if drawing and tool == "draw":
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(canvas, color, pos, 5)

    # клавиатура оқу
    keys = pygame.key.get_pressed()

    # құрал таңдау
    if keys[pygame.K_r]: tool = "rect"   
    if keys[pygame.K_c]: tool = "circle"  
    if keys[pygame.K_d]: tool = "draw"    
    if keys[pygame.K_e]: tool = "eraser"  

    # түс таңдау
    if keys[pygame.K_1]: color = BLACK
    if keys[pygame.K_2]: color = RED
    if keys[pygame.K_3]: color = GREEN
    if keys[pygame.K_4]: color = BLUE

    # өшіргіш режимі
    if tool == "eraser" and drawing:
        pygame.draw.circle(canvas, WHITE, pygame.mouse.get_pos(), 15)

    pygame.display.update() 
    clock.tick(400)  # FPS (жылдамдық)

pygame.quit() 