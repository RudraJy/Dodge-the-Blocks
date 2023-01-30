import pygame
import random
import mysql.connector
 
BLACK = (  255,   51,   51)
WHITE = (0, 204, 204)
RED   = (51,   255,   51)
GREEN = (0,0,0)
BLUE = (15,15,200)

print()
name=input('Enter name ')
print()
    
class Block(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()

pygame.init()

size=(900,600)
screen = pygame.display.set_mode((size), pygame.RESIZABLE)


block_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()

l1=[]
l2=[]
   
for i in range(1):
    block = Block(BLACK, 50, 50)
 
    block.rect.x = random.randrange(200,830)
    block.rect.y = random.randrange(200,530)
    
    block_list.add(block)
    all_sprites_list.add(block)

for k in range(15):
    xchange=random.randrange(0,5)
    l1.append(xchange)
    ychange=random.randrange(0,5)
    l2.append(ychange)
 
player = Block(RED, 20, 20)
player.rect.left=11
player.rect.top=11
all_sprites_list.add(player)

game_loop = True

clock = pygame.time.Clock()

wall_touch_count=0 
score = 100
level=1


while game_loop == True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            game_loop = False
    
    screen.fill(WHITE)
    i=0
    pygame.draw.line(screen,GREEN,[0,0],[0,600],20)
    pygame.draw.line(screen,GREEN,[0,0],[900,0],20)
    pygame.draw.line(screen,GREEN,[0,600],[900,600],20)
    pygame.draw.line(screen,GREEN,[900,0],[900,500],20)

    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    all_sprites_list.draw(screen)
 
    pygame.display.flip()
 
    for block in block_list:
        block.rect.x += l1[i]
        block.rect.y += l2[i]
        i=i+1
        if block.rect.x>=840 or block.rect.x<10:
            l1[i-1] = l1[i-1]*(-1)
        if block.rect.y>=540 or block.rect.y<10:
            l2[i-1] = l2[i-1]*(-1)
            
    if player.rect.left<11:
        wall_touch_count+=1
        print(wall_touch_count)
        player.rect.left=11
    if player.rect.right>890 and player.rect.top<=500:
        wall_touch_count+=1
        print(wall_touch_count)
        player.rect.right=890
    if player.rect.top<11:
        wall_touch_count+=1
        print(wall_touch_count)
        player.rect.top=11
    if player.rect.bottom>590:
        wall_touch_count+=1
        print(wall_touch_count)
        player.rect.bottom=590
    if player.rect.left>=900:
        score= score+1000
        level=level+1
        if level<7:
            font = pygame.font.SysFont('comicsansms', 85, True, False)
            text = font.render("NEXT LEVEL", True, BLUE)
            screen.blit(text, [180, 200])
            pygame.display.flip()
            pygame.time.wait(3000)
            

        if level ==7:
            font = pygame.font.SysFont('comicsansms', 45, True, False)
            text = font.render("YOU COMPLETED THE GAME", True, BLUE)
            screen.blit(text, [180, 200])
            pygame.display.flip()
            pygame.time.wait(3000)
            FINAL_SCORE=(score-wall_touch_count)
            print('YOUR FINAL SCORE IS ',FINAL_SCORE)
            game_loop = False

            
        for j in range(level):
            block = Block(BLACK, 50, 50)
            block.rect.x = random.randrange(100,830)
            block.rect.y = random.randrange(100,530)
            block_list.add(block)
            all_sprites_list.add(block)
            player.rect.left=11
            player.rect.top=11
        

    if event.type==pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.rect.x -= 3
        if event.key == pygame.K_RIGHT:
            player.rect.x += 3
        if event.key == pygame.K_UP:
            player.rect.y -= 3
        if event.key == pygame.K_DOWN:
            player.rect.y += 3
 
 
    for block in blocks_hit_list:
        font = pygame.font.SysFont('comicsansms', 85, True, False)
        text = font.render("YOU CRASHED", True, BLUE)
        screen.blit(text, [150, 200])
        pygame.display.flip()
        pygame.time.wait(3000)
        
        
        FINAL_SCORE=(score-wall_touch_count)
        print()
        print('GAME OVER\nYOUR FINAL SCORE IS ',FINAL_SCORE)
        print()
        game_loop = False
        
 
    clock.tick(60)

pygame.quit()