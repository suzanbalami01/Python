import pygame
import time
import random
pygame.init()
x=0

enemies=[]
enemy_y = -100
start_time=time.time()
y=0
car_width = 94
car_height = 200
screen_height = 600
screen_width = 900
flag = 2
player_width = 94
lane_width =300
player_y = 400


screen=pygame.display.set_mode((screen_width,screen_height))
background_img= pygame.image.load('road.png').convert()
playerx_img = pygame.image.load('game_sprite.png').convert_alpha()
playery_img = pygame.image.load('enemy.png').convert_alpha()
running=True
def move_background(x,y,screen_height,screen,background_img,playery_img):                
               
    rel_y=y % screen_height
    screen.blit(background_img,(x,rel_y-screen_height))
    
    #print("rel_y-height{}".format(rel_y-screen_height))
    if rel_y<screen_height:
        screen.blit(background_img,(x,rel_y))
    y+=1
    return y

def generate_enemies(enemy_y,lane_width,enemies,player_width):
    flag = random.randrange(1,4,1)
    enemies.append([int(flag*lane_width-(lane_width+player_width)/2),enemy_y,flag])
def enemy_moment(enemies,screen,playery_img):
    if len(enemies) <= 0: return
    for enemy in enemies:
        screen.blit(playery_img,(enemy[0],enemy[1]))
        enemy[1]+= 1
def splice_enemies(enemies):
    for enemy in enemies:
        if enemy[1]>=600:
            index_enemy=enemies.index(enemy)
            enemies.pop(index_enemy)
    return enemies
def car_collision(enemies,player_y,car_height,flag):
    for enemy in enemies:
        if enemy[2]==flag and enemy[1]+car_height >=player_y:
            print("collision")
while running:
    car_collision(enemies,player_y,car_height,flag)  
    for event in pygame.event.get():
        if time.time()-start_time >= 1:
            generate_enemies(enemy_y,lane_width,enemies,player_width)
            start_time = time.time()

        if event.type==pygame.QUIT:
            running =False
        if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    if flag <= 1:
                        continue
                    flag =flag -1
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    if flag >= 3:
                        continue
                    flag+=1
        if event.type == pygame.KEYUP:
            pass
        player_x = int(flag*lane_width-(lane_width+player_width)/2)

        
    y= move_background(x,y,screen_height,screen,background_img,playery_img)

    screen.blit(playerx_img,(player_x,player_y))
    enemy_moment(enemies,screen,playery_img)
    pygame.display.update( )  
    enemies=splice_enemies(enemies)   
     