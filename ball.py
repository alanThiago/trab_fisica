import pygame
import math

class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y, mass, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.mass = mass
        self.color = color
    
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
    
    def checkCollision(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = math.sqrt(dx**2 + dy**2)
        if distance < self.radius + other.radius:
            self.speed_x = -self.speed_x
            self.speed_y = -self.speed_y
            other.speed_x = -other.speed_x
            other.speed_y = -other.speed_y
    
    def checkBounds(self, screenLenght):
        if self.x - self.radius <= 0 or self.x + self.radius >= screenLenght:
            self.speed_x = -self.speed_x
        if self.y - self.radius <= 0 or self.y + self.radius >= screenLenght:
            self.speed_y = -self.speed_y
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)