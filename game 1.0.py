import pygame
import random
x = pygame.init()

# colors_________________________________
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
#_______________________________________________


#game specific variable__________________________________
clock = pygame.time.Clock()
screen_width = 820
screen_height = 680
font = pygame.font.SysFont(None,50)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color, snk_list,snakesize):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color,[x, y, snakesize, snakesize])


#_______________________________________________________

# Initial Game window______________________________
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(('Snake Game'))
#________________________________________________

# creating game loop()_______________________________
def game_loop():
    exit_game = False
    game_over = False
    snakex = 500
    snakey = 500
    snakesize = 30
    fps = 30
    velocity_x = 0
    velocity_y = 0
    speed = 5
    food_x = random.randint(50, screen_width - 100)
    food_y = random.randint(50, screen_height - 100)
    food_size = 30
    score = 0
    snk_list = []
    snk_lenght = 1

    while exit_game != True :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    velocity_x = 0
                    velocity_y = speed
                if event.key == pygame.K_UP:
                    velocity_x = 0
                    velocity_y = -speed
                if event.key == pygame.K_LEFT:
                    velocity_x = -speed
                    velocity_y = 0
                if event.key == pygame.K_RIGHT:
                    velocity_x = speed
                    velocity_y = 0
        if abs(snakex-food_x)<6 and abs(snakey-food_y)<6 :
            score += 1
            food_x = random.randint(50, screen_width - 100)
            food_y = random.randint(50, screen_height - 100)
            print('Score: ', score)
            snk_lenght += 5
        if snakex==0 or snakey==0 or snakex==screen_width or snakey==screen_height :
            exit_game = True
        snakex += velocity_x
        snakey += velocity_y

        head = []
        head.append(snakex)
        head.append(snakey)
        snk_list.append(head)
        if head in snk_list[:-2]:
            exit_game = True

        if len(snk_list)>snk_lenght:
            del snk_list[0]

        gameWindow.fill(red)
        # pygame.draw.rect(gameWindow, black, [snakex, snakey, snakesize, snakesize])
        pygame.draw.rect(gameWindow, blue, [food_x, food_y, food_size,food_size])

        text_screen('Score: ' +  str(score),white,5,5)
        plot_snake(gameWindow,black, snk_list,snakesize)
        pygame.display.update()
        clock.tick(fps)
game_loop()

pygame.quit()
quit()  #END game_loop function

