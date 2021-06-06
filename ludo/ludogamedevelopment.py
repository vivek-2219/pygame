import pygame

pygame.init()

screen = pygame.display.set_mode((900,900))

game_start = True
R_turn = True
B_turn = True
Y_turn = True
G_turn = True
game_end = True

def start():
    game_start = True

    while game_start:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_start = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_start = False

        pygame.display.update()
start()

def game_running():
    def red():
        R_turn = True
        while R_turn:
            screen.fill((255, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    R_turn = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        R_turn = False

            pygame.display.update()
    red()

    def blue():
        B_turn = True
        while B_turn:
            screen.fill((0, 0, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    B_turn = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        B_turn = False

            pygame.display.update()
    blue()

    def yellow():
        Y_turn = True
        while Y_turn:
            screen.fill((100, 100, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Y_turn = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Y_turn = False

            pygame.display.update()
    yellow()

    def green():
        G_turn = True
        while G_turn:
            screen.fill((0, 255, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    G_turn = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        G_turn = False

            pygame.display.update()
    green()
game_running()





