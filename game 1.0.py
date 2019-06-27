import pygame
x = pygame.init()

# colors_________________________________
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
#_______________________________________________

# Initial Game window______________________________
gameWindow = pygame.display.set_mode((820,620))
pygame.display.set_caption(('flappy bird'))
#________________________________________________

#game specific variable__________________________________
exit_game = False
game_over = False
#_______________________________________________________

# creating game loop()
while exit_game != True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print('You hae press right arrow key')

pygame.quit()
quit()
