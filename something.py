import pygame
import sys
import random
import math

pygame.init()

width, height = 550, 550

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake game")

x = width//2
y = height//2

directions = ("down", "up", "left", "right")
direction = directions[0]
velocity = 5
sideLength = 50
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
eventExit = False
appleExists = False
global counter
counter = 0
font = pygame.font.Font("freesansbold.ttf", 35)

class Face:
    def __init__(self, x, y):
        self.radius = 25
        self.x = x
        self.y = y
    def drawFace(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), self.radius)
        pygame.draw.circle(screen, (0, 0, 0), (self.x + 12, self.y + 7), self.radius - 17)
        pygame.draw.circle(screen, (0, 0, 0), (self.x - 12, self.y + 7), self.radius - 17)
        #print("Hello from drawface function!")
    def changeFaceToObject(self, face):
        tempX = face.x
        tempY = face.y
        pygame.draw.circle(screen, GREEN, (tempX, tempY), self.radius)


snakeParts = [Face(x, y)]

def isAlive():
    global x
    global y
    if x < 0 or x > 550 or y < 0 or y > 550:
        return False 
    if eventExit is not True:
        return True
    return False

def changeDirection():
    global snakeParts
    global direction
    global directions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            eventExit = True
            print("Game Over!")
            pygame.quit()
            sys.exit()
    keys= pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and (direction != directions[1] or len(snakeParts) == 1):
        direction = directions[0]
    if keys[pygame.K_UP] and (direction != directions[0] or len(snakeParts) == 1):
        direction = directions[1]
    if keys[pygame.K_LEFT] and (direction != directions[3] or len(snakeParts) == 1):
        direction = directions[2]
    if keys[pygame.K_RIGHT] and (direction != directions[2] or len(snakeParts) == 1):
        direction = directions[3]

radius = 25

def spawnApple():
    global appleExists
    if appleExists == False:
        global xCircle
        xCircle = random.randint(25, 525)
        global yCircle
        yCircle = random.randint(25, 525)
        appleExists = True

def collision():
    global counter
    global velocity
    global x
    global y
    global appleExists
    if math.sqrt((x - xCircle)**2 + (y - yCircle)**2) < radius + sideLength // 2:
        counter+= 1
        velocity+= 0.25
        appleExists = False
        snakeParts.append(Face(x, y))
        #print("collision detected")

while isAlive():
    pygame.time.delay(100)
    changeDirection()
    spawnApple()
    if direction == directions[0]:
        y+= velocity
    if direction == directions[1]:
        y-= velocity
    if direction == directions[2]:
        x-= velocity
    if direction == directions[3]:
        x+= velocity
    for i in snakeParts:
        if math.sqrt((i.x - x)**2 + (i.y - y)**2) < velocity:
            screen.fill((255, 255, 255))
            gameOverText = font.render("Game Over!", False, (0, 0, 0))
            scoreText = font.render(f"Your current score is {counter}", False, (0, 0, 0))
            rechtangle = gameOverText.get_rect()
            rech = scoreText.get_rect()
            rechtangle.center = (width // 2, height // 2)
            rech.center = (width // 2, height // 2 + 50)
            screen.blit(gameOverText, rechtangle)
            screen.blit(scoreText, rech)
            pygame.display.update()
            pygame.time.delay(5000)
            print("it works")
            pygame.quit()
            sys.exit()
    screen.fill(BLUE)
    text = font.render(f"{counter}", False, (255, 255, 255))
    rectangle = text.get_rect()
    rectangle.center = (30, 30)
    screen.blit(text, rectangle)
    snakeParts.append(Face(x, y))
    snakeParts = snakeParts[1:]
    pygame.draw.circle(screen, RED, (xCircle, yCircle), radius)
    for i in snakeParts:
        #print(type(i))
        if isinstance(i, Face):
            i.drawFace(screen)
            #print("hello from if!")
        else:
            pygame.draw.circle(screen, GREEN, (i[0], i[1]), sideLength / 2)
    collision()
    pygame.display.update()
