import time
import pygame

from pygameJump import Jumping
pygame.init()

win = pygame.display.set_mode((800,800))
pygame.display.set_caption("First Game")

# walkRight = [pygame.image.load(pygame.path.join('Game','R1.png')), pygame.image.load(pygame.path.join('Game','R2.png')), pygame.image.load((pygame.path.join('Game','R3.png')), pygame.image.load((pygame.path.join('Game','R4.png')), pygame.image.load((pygame.path.join('Game','R5.png')), pygame.image.load((pygame.path.join('Game','R6.png')), pygame.image.load((pygame.path.join('Game','R7.png')), pygame.image.load((pygame.path.join('Game','R8.png')), pygame.image.load((pygame.path.join('Game','R9.png'))
# walkLeft = [pygame.image.load(pygame.path.join('Game','L1.png')), pygame.image.load(pygame.path.join('Game','L2.png')), pygame.image.load(pygame.path.join('Game','L3.png')), pygame.image.load(pygame.path.join('Game','L4.png')), pygame.image.load(pygame.path.join('Game','L5.png')), pygame.image.load(pygame.path.join('Game','L6.png')), pygame.image.load(pygame.path.join('Game','L7.png')), pygame.image.load(pygame.path.join('Game','L8.png')), pygame.image.load(pygame.path.join('Game','L9.png'))
# bg = pygame.image.load('bg.jpg')
# char = pygame.image.load('standing.png')

walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]
walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'), pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]
bg = pygame.image.load('gameimages/bgSmaller.jpg')
char = pygame.image.load('Game/standing.png')

#if x >137, then can keep going right. Only way to move is jump. Jump. need to check if x, and y reach these x,y levels

x = 0
y = 650
width = 40
height = 60
vel = 5

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
        if eve.type == pygame.QUIT: #pygame.QUIT is looking for a key pressed, while pygame.quit() is a function
            run=False
        #mouse_pos=(0,0)

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

    elif keys[pygame.K_RIGHT] and x < 800 - vel - width:  
        x += vel
        left = False
        right = True
    
   

    else: 
        left = False
        right = False
        walkCount = 0
        
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

    if keys[pygame.K_RIGHT] and x<130 and y<705 - vel- width:
        x += vel
        left = False
        right = True
    
    
    redrawGameWindow() 

        # if x>=(130, 705):

    
    
pygame.quit()
# (137, 684)
# (137, 690)
# (137, 690)
# (132, 703)
# (132, 703)
# (132, 703)
# (132, 703)