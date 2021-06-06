import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600,600))

background = pygame.image.load("backgroundblue.jpg")

list = [0.1,0.3,-0.1,-0.3,]
deltaY = random.choice(list)

ballImg = pygame.image.load("ball.png")
ballX = 300
ballY = 300
ball_Xchange = -0.2
ball_Ychange = deltaY

playerImg = pygame.image.load("rectangle 256.png")
playerXL = -168
playerYL = 250
player_XLchange = 0
player_YLchange = 0

playerXR = 512
playerYR = 250
player_XRchange = 0
player_YRchange = 0

def playerleft(x,y):
    screen.blit(playerImg, (x,y))

def playerright(x,y):
    screen.blit(playerImg, (x,y))

def ball(x,y):
    screen.blit(ballImg, (x,y))

game_running = True
while game_running:
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_YRchange = -0.3

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_YRchange = 0.3

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_YLchange = -0.3

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player_YLchange = 0.3
        #
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         ball_Xchange = -0.2
        #         ball_Ychange = deltaY

    playerleft(playerXL, playerYL)
    playerYL += player_YLchange
    if playerYL < 0:
        playerYL = 0
    elif playerYL > 344:
        playerYL = 344

    playerright(playerXR, playerYR)
    playerYR += player_YRchange
    if playerYR < 0:
        playerYR = 0
    elif playerYR > 344:
        playerYR = 344

    ball(ballX, ballY)
    ballX += ball_Xchange
    ballY += ball_Ychange
    if (ballX < 0 and ballX > -1) and (ballY>playerYL and ballY < (playerYL+256)):
        ball_Xchange = -ball_Xchange
    if (ballX > 570 and ballX < 571) and (ballY>playerYR and ballY < (playerYR+256)):
        ball_Xchange = -ball_Xchange
    if ballY < 0:
        ball_Ychange = -ball_Ychange
    if ballY > 570:
        ball_Ychange = -ball_Ychange

    pygame.display.update()