import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

background = pygame.image.load("background2.jpg")

mixer.music.load("background.wav")
mixer.music.play(-1)

playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(1)
    enemyY_change.append(40)


bulletImg = []
bulletX = []
bulletY = []
bulletX_change = []
bulletY_change = []
num_of_bullets = 6
bullet_state = []

for i in range(num_of_bullets):
    bulletImg.append(pygame.image.load("bullet.png"))
    bulletX.append(0)
    bulletY.append(480)
    bulletX_change.append(0)
    bulletY_change.append(2)
    bullet_state.append("ready")

score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)
font1 = pygame.font.Font("freesansbold.ttf",24)
over_font = pygame.font.Font("freesansbold.ttf",64)

textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score: "+str(score_value), True, (255,0,0))
    desc = font1.render("Press arrow keys for left-right and spacebar to fire", True, (0,0,225))
    screen.blit(score, (x,y))
    screen.blit(desc, (200,10))

def game_over_text():
    over_text = over_font.render("GAME OVER!!!", True, (255,255,255))
    screen.blit(over_text, (200,250))

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x,y,i):
    global bullet_state
    bullet_state[i] = "fire"
    screen.blit(bulletImg, (x+16,y+10, i))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX[i],2)) + (math.pow(enemyY-bulletY[i],2)))
    if distance < 21:
        return True
    return False

running = True
while running:
    screen.fill((0,0,150))
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1

            if event.key == pygame.K_RIGHT:
                playerX_change = 1

            if bulletY[i] < 0:
                bulletY[i] = 480
                bullet_state[i] = "ready"

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX[i] = playerX
                    fire_bullet(bulletX[i],bulletY[i])

        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_of_enemies):
        if enemyY[i]>440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX[i], bulletY[i])
        if collision:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 10
            enemyX[i] = random.randint(0,800)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i],enemyY[i], i)

    if bullet_state[i] is "fire":
        fire_bullet(bulletX[i],bulletY[i])
        bulletY[i] -= bulletY_change[i]

    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()