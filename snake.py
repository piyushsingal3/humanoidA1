import pygame
import random
import sys
pygame.init()
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green=(0,177,64)
blue=(0,0,255)
power_apple_size=10
screen_width=900
screen_height=600
clock = pygame.time.Clock()
apple_size=20
gameWindow=pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snake Game")
pygame.display.update()
font=pygame.font.SysFont(None, 32)
def powerup():
    power_apple_x = random.randint(100, screen_width - 100)
    power_apple_y = random.randint(100, screen_height - 100)
    pygame.draw.rect(gameWindow, black, [power_apple_x, power_apple_y, power_apple_size, power_apple_size])
    return power_apple_x, power_apple_y        
def poisoning():
    poison_apple_x = random.randint(100, screen_width - 100)
    poison_apple_y = random.randint(100, screen_height - 100)
    pygame.draw.rect(gameWindow, green, [poison_apple_x, poison_apple_y, apple_size, apple_size])
    return poison_apple_x, poison_apple_y        
def screen_text(text,color,x,y):
    text_screen = font.render(text, True, color)
    gameWindow.blit(text_screen, [x,y])
def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
def gameloop():
    snake_list = []
    snake_length = 1
    exit_game = False
    game_over = False
    apple_x=random.randint(100, screen_width/2)
    apple_y=random.randint(200, screen_height/2)
   
    snake_x=45
    snake_y=55
    snake_size=20
    score=0
    poison=False
    velocity_x=0
    velocity_y=10
    fps=60
    power_up = False
    power_apple_x = 0
    power_apple_y = 0
    poison_apple_x = 0
    poison_apple_y = 0
    while not exit_game:
         if game_over:
            gameWindow.fill(white)
            screen_text("Game Over! Press Enter To Continue", red, 10,10)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game =True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
                    if event.key == pygame.K_PAUSE:
                         exit_game =True
         else :

             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=5
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-5
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=-5
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=5
                        velocity_x=0
             snake_x=snake_x+velocity_x
             snake_y=snake_y+velocity_y            
             if abs(snake_x-apple_x)<10 and abs(snake_y-apple_y)<10:
                score+=10
                print("Score: ", score)
                apple_x=random.randint(100, screen_width-100)
                apple_y=random.randint(100, screen_height-100)
                snake_length +=5
             if (score == 20 or score==40 or score==100 )and not power_up:
                power_up = True
                power_apple_x, power_apple_y = powerup()
             if (score == 30 or score==50 or score==70 )and not poison:
                poison = True
                poison_apple_x,poison_apple_y = poisoning()
             
                
             gameWindow.fill(white)
             screen_text("Score: "+str(score), red, 5, 5)
             pygame.draw.rect(gameWindow,red,[apple_x,apple_y,apple_size,apple_size])
             if power_up:
                pygame.draw.rect(gameWindow, blue, [power_apple_x, power_apple_y, power_apple_size, power_apple_size])
                if abs(snake_x - power_apple_x) < 7 and abs(snake_y - power_apple_y) < 7:
                    score += 20
                    power_up = False
             if poison:
                pygame.draw.rect(gameWindow, green, [poison_apple_x, poison_apple_y,apple_size,apple_size])
                if abs(snake_x - poison_apple_x) < 7 and abs(snake_y - poison_apple_y) < 7:
                    game_over=True
                    poison = False
             head = []
             head.append(snake_x)
             head.append(snake_y)
             snake_list.append(head)

             if len(snake_list)>snake_length:
                del snake_list[0]
             if head in snake_list[:-1]:
                game_over = True

             if snake_x<0:
               snake_x=screen_width
             if snake_x>screen_width:
               snake_x=0 
             if snake_y<0:
               snake_y=screen_height
             if snake_y>screen_height:
               snake_y=0   
        
             plot_snake(gameWindow, black, snake_list, snake_size)
             pygame.display.update()
             clock.tick(fps)
     

    pygame.quit()
    quit()

gameloop()        
