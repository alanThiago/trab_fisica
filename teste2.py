import pygame
import random
import math

# Definimos as constantes da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Inicializamos o Pygame
pygame.init()

# Definimos as cores que vamos usar
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Criamos a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Esferas na caixa")

# Definimos o raio das esferas
radius = 50

# Definimos a posição inicial das esferas
x1 = random.randint(radius, SCREEN_WIDTH - radius)
y1 = random.randint(radius, SCREEN_HEIGHT - radius)
x2 = random.randint(radius, SCREEN_WIDTH - radius)
y2 = random.randint(radius, SCREEN_HEIGHT - radius)

# Definimos a velocidade das esferas
speed_x1 = 5
speed_y1 = 5
speed_x2 = 5
speed_y2 = 5

clock = pygame.time.Clock()

# Definimos o loop principal do jogo
running = True
while running:
    clock.tick(60)

    # Preenchemos a tela com a cor preta
    screen.fill(BLACK)
    
    # Desenhamos as esferas
    pygame.draw.circle(screen, WHITE, (x1, y1), radius)
    pygame.draw.circle(screen, WHITE, (x2, y2), radius)
    
    # Verificamos a colisão entre as esferas
    dx = x1 - x2
    dy = y1 - y2
    distance = math.sqrt(dx**2 + dy**2)
    if distance < 2 * radius:
        # Invertemos a direção das esferas após a colisão
        speed_x1 = -speed_x1
        speed_y1 = -speed_y1
        speed_x2 = -speed_x2
        speed_y2 = -speed_y2
    
    # Atualizamos a posição das esferas
    x1 += speed_x1
    y1 += speed_y1
    x2 += speed_x2
    y2 += speed_y2
    
    # Verificamos se as esferas estão saindo da tela
    if x1 - radius <= 0 or x1 + radius >= SCREEN_WIDTH:
        speed_x1 = -speed_x1
    if y1 - radius <= 0 or y1 + radius >= SCREEN_HEIGHT:
        speed_y1 = -speed_y1
    if x2 - radius <= 0 or x2 + radius >= SCREEN_WIDTH:
        speed_x2 = -speed_x2
    if y2 - radius <= 0 or y2 + radius >= SCREEN_HEIGHT:
        speed_y2 = -speed_y2
    
    # Atualizamos a tela
    pygame.display.update()
    
    # Verificamos se o usuário fechou a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Finalizamos o Pygame
pygame.quit()
