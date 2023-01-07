import pygame
import random

# Define as constantes para o tamanho da tela e o tamanho das esferas
SCREEN_SIZE = 600
BALL_SIZE = 50

# Cria a janela do jogo
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption('Simulação de Caixa de Esferas')

# Classe da esfera
class Ball:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def update(self):
        self.x += self.dx
        self.y += self.dy

        # Verifica se a esfera colidiu com as bordas da tela
        if self.x < BALL_SIZE or self.x > SCREEN_WIDTH - BALL_SIZE:
            self.dx = -self.dx
        if self.y < BALL_SIZE or self.y > SCREEN_HEIGHT - BALL_SIZE:
            self.dy = -self.dy

        # Verifica colisões entre as esferas
        for ball in balls:
            if ball != self:
                # Calcula a distância entre as esferas
                dx = self.x - ball.x
                dy = self.y - ball.y
                distance = (dx**2 + dy**2)**0.5

                # Verifica se houve colisão
                if distance <= BALL_SIZE*2:
                    # Inverte a direção das esferas
                    self.dx = -self.dx
                    self.dy = -self.dy
                    ball.dx = -ball.dx
                    ball.dy = -ball.dy

# Cria as esferas
balls = []
for i in range(3):
    x = random.randint(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    y = random.randint(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
    dx = random.randint(-5, 5)
    dy = random.randint(-5, 5)
    ball = Ball(x, y, dx, dy)
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

    # Desenha as esferas na tela
    for ball in balls:
        pygame.draw.circle(screen, (0, 0, 255), (ball.x, ball.y), BALL_SIZE)

    # Atualiza a tela
    pygame.display.flip()

