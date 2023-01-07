from simulation import Simulation
import random as rd
import pygame

SCREEN_SIZE = int(input("Insira o tamanho da tela: "))
numBalls = int(input("Insira a quantidade de bolas: "))
time = int(input("Insira o tempo de simulação: "))


# Inicializamos o Pygame
pygame.init()

#Setamos a cor da janela
screenColor = (255, 255, 255)

# Criamos a tela
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption(f'Simulação com {time} esfera(s)')
clock = pygame.time.Clock()

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
