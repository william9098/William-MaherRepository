from os import walk
import pygame
from pygame.constants import FINGERDOWN
pygame.init()

win = pygame.display.set_mode((800,800))
winRect=win.get_rect()
pygame.display.set_caption("First Game")

Rock1= pygame.Rect(136, 688, 167-136, winRect.height-688)
# Rock2= pygame.draw.rect(, Rect, width=0)
# Rock3=
# Rock4=
walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]
walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'), pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]
bg = pygame.image.load('gameimages/grassbkgimage4.png')
char = pygame.image.load('Game/standing.png')


x = 0
y = 650
width = 40
height = 60
vel = 5

move=True

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    
    win.blit(bg, (0,0))  
    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:  
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0
        
    pygame.display.update() 
    


run = True

while run:
    clock.tick(27)
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT: #
            run=False

        elif eve.type==pygame.MOUSEBUTTONDOWN:
            mouse_pressed=pygame.mouse.get_pressed()
            if mouse_pressed[0]:
                mouse_pos=pygame.mouse.get_pos()
                print(pygame.mouse.get_pos())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False

    if keys[pygame.K_RIGHT] and x < 105:  
        x += vel
        left = False
        right = True
    
    elif keys[pygame.K_RIGHT] and isJump==True:
        x += vel
        left = False
        right = True
    
    elif keys[pygame.K_RIGHT] and pygame.winRect.colliderect(Rock1):
    # isJump==True and x>137 and x<167 and y< 688:
        x += vel
        left = False
        right = True
        
    
    
    else: 
        left = False
        right = False
        walkCount = 0

    
        
         #136, 687 AND 166, 671
        # if keys[pygame.K_RIGHT] and x<105 and y<690:
        #     x += vel
        #     left = False
        #     right = True
        # x>136 and x<166 and
    

    
    
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
   
    
        

   

    redrawGameWindow() 



    
pygame.quit()

#130, 690-705