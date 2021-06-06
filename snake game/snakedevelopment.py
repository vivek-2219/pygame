import pygame
import random
from  pygame import mixer

pygame.init()

width = 900
height = 900

screen = pygame.display.set_mode((900,972))
pygame.display.set_caption("SnakesWithVivek")

mixer.music.load("background.mp3")
mixer.music.play(-1)

blue = (0,0,255)
white = (0,255,255)
red = (255,0,0)
black = (0,0,0)
grey = (100,100,100)

clock = pygame.time.Clock()

snakeX = 300
snakeY = 400
snakeX_change = 0
snakeY_change = 0
block = 25

snake_list = []
snake_length = 1

foodX = round(random.randrange(25, width - 50) / 25.0) * 25.0
foodY = round(random.randrange(25, height - 50) / 25.0) * 25.0

score_value = 0
tick = 5
font = pygame.font.Font("freesansbold.ttf", 32)
fontG = pygame.font.Font("freesansbold.ttf", 100)
desc = pygame.font.Font("freesansbold.ttf", 32)

def show_score(x,y):
    score = font.render("Score: "+str(score_value), True, (red))
    screen.blit(score, (x,y))

def description(x,y):
    score = desc.render("Play the game with arrow keys", True, (red))
    screen.blit(score, (x,y))

def wall(a,b,c,d):
    pygame.draw.rect(screen, grey, [a,b,c,d])

def plot_snake(screen, color, snake_list, block):
    for x,y in snake_list:
        pygame.draw.rect(screen, color, [x, y, block, block])

def introdesc(x, y):
    introdesc = font.render("Welcome To The World's Best Snake Game", True, (red))
    screen.blit(introdesc, (x, y))

def introbutton(x, y):
    introbutton = font.render("Press SPACEBAR to start the game", True, (red))
    screen.blit(introbutton, (x, y))

def gameover(x, y):
    gameover = fontG.render("GAME OVER...!!!", True, (red))
    screen.blit(gameover, (x, y))

def gameexit(x, y):
    gaemexit = font.render("Press ESCAPE key to exit the game", True, (red))
    screen.blit(gaemexit, (x, y))

def maingamefunction():
    pass

game_start = True
game_running = True
game_end = True

while game_start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_start = False
            game_running = False
            game_end = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_start = False

    screen.fill(white)

    background = pygame.image.load("backgroundimage.jpg")
    background = pygame.transform.scale(background, (900,700))
    def backgroundimage(x, y):
        screen.blit(background, (x, y))
    backgroundimage(0,150)
    introdesc(120,50)
    introbutton(170,900)

    pygame.display.update()

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_start = False
            game_running = False
            game_end = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snakeX_change = 25
                snakeY_change = 0

            elif event.key == pygame.K_LEFT:
                snakeX_change = -25
                snakeY_change = 0

            elif event.key == pygame.K_UP:
                snakeY_change = -25
                snakeX_change = 0

            elif event.key == pygame.K_DOWN:
                snakeY_change = 25
                snakeX_change = 0

    screen.fill(white)

    wall(0,0,400,25)
    wall(500,0,400,25)

    wall(0,0,25,400)
    wall(0,500,25,400)

    wall(875,0,25,400)
    wall(875,500,25,400)

    wall(0,875,400,25)
    wall(500,875,400,25)

    # interior walls
    # outermost interior walls
    wall(50,50,25,100)
    wall(50,50,100,25)
    wall(50,725,25,100)
    wall(50,825,100,25)
    wall(825,50,25,100)
    wall(750,50,100,25)
    wall(825,725,25,100)
    wall(750,825,100,25)
    # outermost interior wall end

    # inner walls
    wall(200,500,25,200)
    wall(200,500,75,25)
    wall(675,500,25,200)
    wall(625,500,75,25)
    wall(200,175,25,200)
    wall(200,375,75,25)
    wall(675,175,25,200)
    wall(625,375,75,25)
    # inner wall end

    # horizontal inner bars
    wall(300,300,300,25)
    wall(300,200,300,25)
    wall(300,575,300,25)
    wall(300,675,300,25)
    # horizontal inner bars end
    # interior walls end

    snakeX += snakeX_change
    snakeY += snakeY_change

    pygame.draw.rect(screen, black, [snakeX,snakeY,block,block])
    pygame.draw.rect(screen, red, [foodX,foodY,block,block])

    if (snakeX<25 and snakeY<400) or (snakeX<25 and snakeY>475) or (snakeX>width-50 and snakeY<400) or (snakeX>width-50 and snakeY>475) or (snakeY<25 and snakeX<400) or (snakeY<25 and snakeX>475) or (snakeY>height-50 and snakeX<400) or (snakeY>height-50 and snakeX>475) or (50<=snakeX<75 and 50<=snakeY<150) or (50<=snakeX<150 and 50<=snakeY<75) or (50<=snakeX<75 and 725<=snakeY<825) or (50<=snakeX<150 and 825<=snakeY<850) or (825<=snakeX<850 and 50<=snakeY<150) or (750<=snakeX<850 and 50<=snakeY<75) or (825<=snakeX<850 and 725<=snakeY<825) or (750<=snakeX<850 and 825<=snakeY<850) or (200<=snakeX<225 and 500<=snakeY<700) or (200<=snakeX<275 and 500<=snakeY<525) or (675<=snakeX<700 and 500<=snakeY<700) or (625<=snakeX<700 and 500<=snakeY<525) or (200<=snakeX<225 and 175<=snakeY<375) or (200<=snakeX<275 and 375<=snakeY<400) or (675<=snakeX<700 and 175<=snakeY<375) or (625<=snakeX<700 and 375<=snakeY<400) or (300<=snakeX<600 and 300<=snakeY<325) or (300<=snakeX<600 and 200<=snakeY<225) or (300<=snakeX<600 and 575<=snakeY<600) or (300<=snakeX<600 and 675<=snakeY<700):
        capture = mixer.Sound("collision.mp3")
        capture.play()
        snakeX_change = 0
        snakeY_change = 0
        snakeX = 300
        snakeY = 400
        snake_list.clear()
        snake_length = 1
        score_value = 0
        tick = 5
        game_running = False
    else:
        if 400<=snakeX<=475 and snakeY<0:
            snakeY = 900
        elif 400<=snakeX<=475 and snakeY>875:
            snakeY = 0
        elif 400<=snakeY<=475 and snakeX<0:
            snakeX = 900
        elif 400<=snakeY<=475 and snakeX>875:
            snakeX = 0

    head = []
    head.append(snakeX)
    head.append(snakeY)
    snake_list.append(head)

    if len(snake_list)>snake_length:
        del snake_list[0]

    if head in snake_list[:-1]:
        capture = mixer.Sound("collision.mp3")
        capture.play()
        snake_list.clear()
        snake_length = 1
        snakeX = 300
        snakeY = 400
        snakeX_change = 0
        snakeY_change = 0
        game_running = False

    if (50<=foodX<75 and 50<=foodY<150) or (50<=foodX<150 and 50<=foodY<75) or (50<=foodX<75 and 725<=foodY<825) or (50<=foodX<150 and 825<=foodY<850) or (825<=foodX<850 and 50<=foodY<150) or (750<=foodX<850 and 50<=foodY<75) or (825<=foodX<850 and 725<=foodY<825) or (750<=foodX<850 and 825<=foodY<850) or (200<=foodX<225 and 500<=foodY<700) or (200<=foodX<275 and 500<=foodY<525) or (675<=foodX<700 and 500<=foodY<700) or (625<=foodX<700 and 500<=foodY<525) or (200<=foodX<225 and 175<=foodY<375) or (200<=foodX<275 and 375<=foodY<400) or (675<=foodX<700 and 175<=foodY<375) or (625<=foodX<700 and 375<=foodY<400) or (300<=foodX<600 and 300<=foodY<325) or (300<=foodX<600 and 200<=foodY<225) or (300<=foodX<600 and 575<=foodY<600) or (300<=foodX<600 and 675<=foodY<700):
        foodX = round(random.randrange(25, width - 50) / 25.0) * 25.0
        foodY = round(random.randrange(25, height - 50) / 25.0) * 25.0
        snake_length += 1

    if (snakeX == foodX and snakeY == foodY):
        foodX = round(random.randrange(25, width - 50) / 25.0) * 25.0
        foodY = round(random.randrange(25, height - 50) / 25.0) * 25.0
        snake_length += 1
        score_value += 10
        capture = mixer.Sound("capture.mp3")
        capture.play()

        if 0>score_value>50:
            tick = 5.02
        elif 50>=score_value>100:
            tick = 5.03
        elif 100>=score_value>150:
            tick = 5.04
        elif 150>=score_value>200:
            tick = 5.05

    show_score(20,920)
    description(300,920)

    plot_snake(screen, black, snake_list, block)
    clock.tick(tick)
    pygame.display.update()

while game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_start = False
            game_running = False
            game_end = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_end = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_running = True

    screen.fill(white)
    gameexit(170,470)
    gameover(50,350)
    lowerimage = pygame.image.load("lowerimage.jpg")
    lowerimage = pygame.transform.scale(lowerimage, (900,450))
    def lower(x, y):
        screen.blit(lowerimage, (x, y))
    lower(0,532)

    upperimage = pygame.image.load("upperimage.jpg")
    upperimage = pygame.transform.scale(upperimage, (900,300))
    def upper(x, y):
        screen.blit(upperimage, (x, y))
    upper(0,0)

    pygame.display.update()
