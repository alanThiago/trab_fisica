from simulation import Simulation
import random as rd
import pygame
import sys

# Definimos as constantes da tela
SCREEN_SIZE = int(sys.argv[2])

# Inicializamos o Pygame
pygame.init()

#Setamos a cor da janela
screenColor = (255, 255, 255)

# Criamos a tela
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption(f'Simulação com {sys.argv[1]} esfera(s)')
clock = pygame.time.Clock()

numBalls = int(sys.argv[1])
time = int(sys.argv[3])
simulation = Simulation(numBalls, SCREEN_SIZE, time, screen)

while simulation.isRunning():
    clock.tick(60)

    # Preenchemos a tela com a cor preta
    screen.fill(screenColor)
    
    simulation.run()
    
    # Atualizamos a tela
    pygame.display.update()

# Finalizamos o Pygame
pygame.quit()