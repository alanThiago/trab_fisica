from ball import *
import random as rd

class Simulation:
    def __init__(self, numBalls, screenSize, time, screen):
        self.time = time
        self.numBalls = numBalls
        self.screenSize = screenSize
        self.screen = screen
        self.balls = []
        self.colors = [(0,0,255), (255,255,0), (255,0,0), (0,128,0)]
        self.createBalls()

    def createBalls(self):
        for _ in range(self.numBalls):
            radius = rd.randint(10, 50)
            x = rd.randint(radius, self.screenSize - radius)
            y = rd.randint(radius, self.screenSize - radius)
            speed_x = speed_y = 0
            while speed_x == 0 and speed_y == 0:
                speed_x = rd.randint(0, 10)
                speed_y = rd.randint(0, 10)
            mass = rd.randint(0, 30)
            color = self.colors[rd.randint(0, 3)]
            self.balls.append(Ball(x, y, radius, speed_x, speed_y, mass, color))

        self.drawBalls()

    def moveBalls(self):
        for ball in self.balls:
            ball.move()

    def checkCollisions(self):
        for i in range(self.numBalls-1):
            for j in range(i+1, self.numBalls):
                self.balls[i].checkCollision(self.balls[j])

    def checkBounds(self):
        for ball in self.balls:
            ball.checkBounds(self.screenSize)

    def drawBalls(self):
        for ball in self.balls:
            ball.draw(self.screen)

    def isRunning(self):
        return self.time > 0

    def run(self):
        self.checkCollisions()
        self.checkBounds()
        self.moveBalls()
        self.drawBalls()
        self.time -= 1
