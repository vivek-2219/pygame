import pygame
import random
from pygame import mixer

X = [0.83,0.93,1.03,1.13]
Y = [0.78,0.87,0.94,1.3]
deltaX = random.choice(X)
deltaY = random.choice(Y)

pygame.init()

screen = pygame.display.set_mode((640,900))

pygame.display.set_caption("PlayWithVivek")

background = pygame.image.load("backgroundblue.jpg")

mixer.music.load("backgroundmusic.mp3")
mixer.music.play(-1)

playerImg = pygame.image.load("rectangle128rotate.png")
playerX = 300
playerY = 850
player_Xchange = 0

stopleftImg = pygame.image.load("rectangle 256 rotate.png")
stopleftX = 0
stopleftY = -150

stoprightImg = pygame.image.load("rectangle 256 rotate.png")
stoprightX = 384
stoprightY = -150

sliderImg = pygame.image.load("slider.png")
sliderX = 300
sliderY = -10
slider_Xchange = 1

ballImg = pygame.image.load("ball.png")
ballX = 350
ballY = 250
ball_Xchange = -deltaX
ball_Ychange = deltaY

score_bot = 0
score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)
textX = 10
textY = 30


def player(x,y):
    screen.blit(playerImg, (x,y))

def slider(x,y):
    screen.blit(sliderImg, (x,y))

def stopleft(x,y):
    screen.blit(stopleftImg, (x,y))

def stopright(x,y):
    screen.blit(stoprightImg, (x,y))

def ball(x, y):
    screen.blit(ballImg, (x, y))

def show_score(x,y):
    score = font.render("SCORE: "+str(score_value), True, (0,0,0))
    screen.blit(score, (x,y))
    scoreb = font.render("BOT: "+str(score_bot), True, (0,0,0))
    screen.blit(scoreb, (x+480,y))

game_running = True
while game_running:
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_Xchange = -0.7

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_l:
                player_Xchange = 0.7

        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         player_Xchange = 0

    slider(sliderX,sliderY)
    sliderX += slider_Xchange
    if sliderX < 0:
        slider_Xchange = -slider_Xchange
    if sliderX > 520:
        slider_Xchange = -slider_Xchange

    if slider_Xchange > 0 and ball_Xchange > 0 :
        if ((ballY < sliderY+80) and (ballX > sliderX - 50) and (ballX < sliderX + 178)):
            ball_Ychange = -ball_Ychange
            ball_Xchange = ball_Xchange

    elif slider_Xchange > 0 and ball_Xchange < 0:
        if ((ballY < sliderY+80) and (ballX > sliderX - 50) and (ballX < sliderX + 178)):
            ball_Xchange = -ball_Xchange
            ball_Ychange = -ball_Ychange

    elif slider_Xchange < 0 and ball_Xchange < 0:
        if ((ballY < sliderY+80) and (ballX > sliderX - 50) and (ballX < sliderX + 178)):
            ball_Ychange = -ball_Ychange
            ball_Xchange = ball_Xchange

    elif slider_Xchange < 0 and ball_Xchange > 0:
        if ((ballY < sliderY+80) and (ballX > sliderX - 50) and (ballX < sliderX + 178)):
            ball_Xchange = -ball_Xchange
            ball_Ychange = -ball_Ychange

    player(playerX, playerY)
    playerX += player_Xchange
    if playerX < 0:
        playerX = 0
    if playerX >512:
        playerX = 512

    ball(ballX,ballY)
    ballX += ball_Xchange
    ballY += ball_Ychange
    if ballX < 0 or ballX > 615:
        ball_Xchange = -ball_Xchange

    if player_Xchange > 0 and ball_Xchange > 0 :
        if ((ballY > playerY and ballY < playerY+1) and ballX > playerX-50) and ((ballY > playerY and ballY < playerY+1) and ballX < playerX+176):
            ball_Ychange = -ball_Ychange
            ball_Xchange = ball_Xchange

    elif player_Xchange > 0 and ball_Xchange < 0:
        if ((ballY > playerY and ballY < playerY+1) and ballX > playerX-50) and ((ballY > playerY and ballY < playerY+1) and ballX < playerX+176):
            ball_Xchange = -ball_Xchange
            ball_Ychange = -ball_Ychange

    elif player_Xchange < 0 and ball_Xchange < 0:
        if ((ballY > playerY and ballY < playerY+1) and ballX > playerX-50) and ((ballY > playerY and ballY < playerY+1) and ballX < playerX+176):
            ball_Ychange = -ball_Ychange
            ball_Xchange = ball_Xchange

    elif player_Xchange < 0 and ball_Xchange > 0:
        if ((ballY > playerY and ballY < playerY+1) and ballX > playerX-50) and ((ballY > playerY and ballY < playerY+1) and ballX < playerX+176):
            ball_Xchange = -ball_Xchange
            ball_Ychange = -ball_Ychange

    else:
        if ((ballY > playerY and ballY < playerY+1) and ballX > playerX-50) and ((ballY > playerY and ballY < playerY+1) and ballX < playerX+176):
            ball_Xchange = ball_Xchange
            ball_Ychange = -ball_Ychange

    stopleft(stopleftX,stopleftY)
    stopright(stoprightX,stoprightY)
    if ((ballY < stopleftY+170 and ballY > stopleftY+170-1) or (ballY < stoprightY+170 and ballY > stoprightY+170-1)) and ((ballX > stopleftX and ballX < stopleftX+256) or (ballX > stoprightX and ballX < stoprightX+256)):
        ball_Xchange = ball_Xchange
        ball_Ychange = -ball_Ychange

    if ballY < -0:
        ballY = 250
        ballX = 350
        ball(ballX,ballY)
        score_value += 10
    if  ballY > 1100:
        ballY = 250
        ballX = 350
        ball(ballX,ballY)
        score_bot += 10

    show_score(textX,textY)
    pygame.display.update()