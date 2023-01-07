import pygame
import random

# Define as constantes para o tamanho da tela
SCREEN_SIZE = 600

# Classe da esfera
class Ball:
    def __init__(self, x, y, dx, dy, size, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.size = size
        self.color = color

    def update(self):
        self.x += self.dx
        self.y += self.dy

        # Verifica se a esfera colidiu com as bordas da tela
        if self.x < self.size or self.x > SCREEN_SIZE - self.size:
            self.dx = -self.dx
        if self.y < self.size or self.y > SCREEN_SIZE - self.size:
            self.dy = -self.dy

        # Verifica colisões entre as esferas
        for ball in balls:
            if ball != self:
                # Calcula a distância entre as esferas
                dx = self.x - ball.x
                dy = self.y - ball.y
                distance = (dx**2 + dy**2)**0.5

                # Verifica se houve colisão
                if distance <= self.size + ball.size:
                    # Inverte a direção das esferas
                    self.dx = -self.dx
                    self.dy = -self.dy
                    ball.dx = -ball.dx
                    ball.dy = -ball.dy

# Cria a janela do jogo
screen = pygame.display.set_mode((SCREEN_SIZE,SCREEN_SIZE))

# Cria as esferas
balls = []
for i in range(3):
    x = random.randint(0, SCREEN_SIZE)
    y = random.randint(0, SCREEN_SIZE)
    dx = random.randint(-5, 5)
    dy = random.randint(-5, 5)
    size = random.randint(20, 50)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    ball = Ball(x, y, dx, dy, size, color)
    balls.append(ball)

# Inicia o relógio do jogo
clock = pygame.time.Clock()

# Executa o jogo por 1 minuto (60 segundos)
while True:
    # Controla a velocidade do jogo
    clock.tick(60)

    # Verifica se o jogador fechou a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualiza a posição das esferas
    for ball in balls:
        ball.update()

    # Limpa a tela
    screen.fill((255, 255, 255))

    # Desenha as esferas na tela
    for ball in balls:
        pygame.draw.circle(screen, ball.color, (ball.x, ball.y), ball.size)

    # Atualiza a tela
    pygame.display.flip()
