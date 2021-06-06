import pygame
import random
import time
from pygame import mixer

pygame.init()

delay = 1

mixer.music.load("sfx_wing.wav")
mixer.music.play(-1)

screen = pygame.display.set_mode((300,600))

pygame.display.set_caption("Flappy Bird With Vivek")

icon = pygame.image.load("flappy.png")
pygame.display.set_icon(icon)

background = pygame.image.load("background2.jpg")

playerImg = pygame.image.load("bird.png")
playerX = 20
playerY = 300
playerX_change = 0
playerY_change = 0

pipeUImg = pygame.image.load("pipegreenupper.png")
pipeUX = 200
pipeUY = -300
pipeU_change = -0.3

pipeLImg = pygame.image.load("pipegreenlower.png")
pipeLX = 200
pipeLY = 350
pipeL_change = -0.3

items = [-100, -150, -200, -250, -300, -350, -400, -450, -500,]

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (0,0,0))
    screen.blit(score, (x,y))

def player(x,y):
    screen.blit(playerImg, (x,y))

def pipeU(x,y):
    screen.blit(pipeUImg, (x,y))

def pipeL(x,y):
    screen.blit(pipeLImg, (x,y))

running = True
while running:
    screen.blit(background, (0,-300))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -0.5

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerY_change = 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    player(playerX, playerY)
    playerY += playerY_change
    if playerY > 536:
        playerY = 536
    if playerY < 0:
        playerY = 0

    pipeUX += pipeU_change
    pipeLX += pipeL_change

    pipeU(pipeUX, pipeUY)
    pipeL(pipeLX, pipeLY)

    if pipeLX<20 and pipeUX>(19):
        score_value += 10
        point = mixer.Sound("sfx_point.wav")
        point.play()

    if pipeLX < -300 or pipeUX < -300:
        pipeLX = 300
        pipeUX = 300
        upper = random.choice(items)

        pipeUY = upper
        pipeLY = int(pipeUY) + int(662)

    if (abs(playerY-pipeUY)<500 and abs(playerX-pipeUX)<50) or ((int(pipeLY)-int(playerY))<50 and abs(playerX-pipeLX)<50):
        mixer.music.play()
        pipeU_change = 0
        pipeL_change = 0
        collision = mixer.Sound("sfx_hit.wav")
        collision.play()
        time.sleep(delay)
        playerY = 536
        pipeLX = 5000
        pipeUX = 5000
        die = mixer.Sound("sfx_die.wav")
        die.play()
        swoosh = mixer.Sound("sfx_swooshing.wav")
        swoosh.play()

    show_score(20,20)
    pygame.display.update()