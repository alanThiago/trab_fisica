import pygame
import random

# inicializa o Pygame
pygame.init()

# configura a janela
WIDTH = 600
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Caixa de Quiques')

# classe que representa uma esfera
class BouncingBall:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.vx = random.randint(-5, 5)
        self.vy = random.randint(-5, 5)

    # desenha a esfera na tela
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.r)

# cria a esfera
ball = BouncingBall(300, 200, 20, (0, 0, 255))

# loop do jogo
running = True
while running:
    # verifica os eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # atualiza a posição da esfera
    ball.x += ball.vx
    ball.y += ball.vy

    # verifica se a esfera colidiu com as paredes
    if ball.x-ball.r < 0 or ball.x+ball.r > WIDTH:
        ball.vx = -ball.vx
    if ball.y-ball.r < 0 or ball.y+ball.r > HEIGHT:
        ball.vy = -ball.vy

    # limpa a tela
    window.fill((255, 255, 255))

    # desenha a esfera
    ball.draw(window)

    # atualiza a tela
    pygame.display.update()

# finaliza o Pygame
pygame.quit()
