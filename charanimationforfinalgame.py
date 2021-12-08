import pygame as py
from pygame.constants import K_LEFT
py.init()

window = py.display.set_mode((800,800))
py.display.set_caption("First Game")
windowRect = window.get_rect()

walkRight = [py.image.load('Game\R1.png'), py.image.load('Game\R2.png'), py.image.load('Game\R3.png'), py.image.load('Game\R4.png'), py.image.load('Game\R5.png'), py.image.load('Game\R6.png'), py.image.load('Game\R7.png'), py.image.load('Game\R8.png'), py.image.load('Game\R9.png')]
walkLeft = [py.image.load('Game\L1.png'), py.image.load('Game\L2.png'), py.image.load('Game\L3.png'), py.image.load('Game\L4.png'), py.image.load('Game\L5.png'), py.image.load('Game\L6.png'), py.image.load('Game\L7.png'), py.image.load('Game\L8.png'), py.image.load('Game\L9.png')]
bg = py.image.load('gameimages\grassbkgimage2.jpg')
char = py.image.load('Game\standing.png')
bush=py.image.load('gameimages\hedgeformazegame_adobespark300.png')
bushup=py.image.load('gameimages\hedgeformazegame_adobespark300up.png')
star=py.image.load('gameimages\pixelated_star_for_game50removedbkg.png')
finish= py.image.load('gameimages\endofmazegame100x100.png')


#Bush1--> x between 20-320, y between 75

            
# Bush1 = py.Rect(20, 70, A-b windowRect.height-94)

# Bush4 = py.Rect(175, 250, 231-175, windowRect.height-94)


x = 0
y = 0
width = 40
height = 60
vel = 10

clock = py.time.Clock()


left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount

    window.blit(bg, (0,0))  
    if walkCount + 1 >= 27:
        walkCount = 0
    
    window.blit(bush,(0,50))
    window.blit(bush,(140,300))
    window.blit(bush,(450,300))
    window.blit(bush,(160, 700))
    window.blit(bush,(420, 700))
    window.blit(bush,(360, 500))
    
    window.blit(bushup,(200,50))
    window.blit(bushup,(553,50))
    window.blit(bushup,(553,0))
    window.blit(bushup,(50,300))
    window.blit(bushup,(260,500))
    
    window.blit(star,(20,200))
    window.blit(star,(726,200))
    window.blit(star,(415, 656))

    window.blit(finish,(700,700))
    # x>717 x<790, and y>710 y<790

    
    

    if left:  
        window.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    elif right:
        window.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        window.blit(char, (x, y))
        walkCount = 0
        
    py.display.update() 
    
bushpassed=0
keys=py.key.get_pressed()
check=True

while check:
    moveLeft=False
    moveRight=False
    moveUp=False
    clock.tick(27)

    for event in py.event.get():
        if event.type == py.QUIT:
            check = False
            mouse_pos=(0,0)

        if event.type==py.MOUSEBUTTONDOWN:
            mouse_pressed=py.mouse.get_pressed()
            if mouse_pressed[0]:
                mouse_pos=py.mouse.get_pos()
                print(py.mouse.get_pos())
        if event.type==py.KEYDOWN:   
            keys = py.key.get_pressed()


    # if event.type==py.KEYDOWN:
    #     if event.key== py.K_LEFT:
    #         moveRight=False
    #         moveLeft=True

    #     if event.key==py.K_RIGHT
    #         moveRight=True


        

        if keys[py.K_RIGHT] and x>=0 and x<540:
            x += vel
            left = False
            right = True
            

        elif keys[py.K_LEFT] and x>=0 and x<600:
            x -= vel
            left = True
            right = False
            

        elif keys[py.K_LEFT] and x>320 and x<600 and y>=0 and y<260:
            x -= vel
            left = True
            right = False

        elif keys[py.K_DOWN] and x>300 and x<540 and y>=0 and y<260:
            y+=vel
        
        elif keys[py.K_DOWN] and x>415 and x<470:
            y+=vel

    

        #320-540

    # elif keys[py.K_LEFT] and x>300 and x<600 and y>=0 and y<260:
    #     x -= vel
    #     left = True
    #     right = False


  


    # elif walkRight and x>=0 and x<540:
    #     x+=vel
    #     left=False
    #     right=True
    

    
    # elif keys[py.K_RIGHT] and y>350 and y<800:
    #     x += vel
    #     left = False
    #     right = True

    # elif keys[py.K_LEFT] and x>320 and x<540 and y>=0 and y<260:
    #     x -= vel
    #     left = True
    #     right = False
    # # 
    # elif keys[py.K_RIGHT] and x>320 and x<540 and y>=0 and y<260:
    #     x += vel
    #     left = False
    #     right = True
    #     bushpassed+=1

    # elif keys[py.K_RIGHT] and bushpassed==1 and x>300 and x<600 and y>=0 and y<420:
    #     x += vel
    #     left = False
        #right = True
        
   
   
    # elif keys [py.K_LEFT] and y>350 and y<800:
    #     x -= vel
    #     left = True
    #     right = False
    
    # elif keys[py.K_LEFT] and x>300 and x<600 and y>=0 and y<420:
    #     x -= vel
    #     left = True
    #     right = False

    
    # elif keys[py.K_LEFT] and x>300 and x<800 and y>580 and y<800:
    #     x -= vel
    #     left = True
    #     right = False
    
    

    # elif keys [py.K_LEFT] and x>650 and x<800 and y>=0 and y<320:
    #     x -= vel
    #     left = True
    #     right = False
    
    # elif keys [py.K_RIGHT] and x>650 and x<800 and y>=0 and y<320:
    #     x += vel
    #     left = False
    #     right = True

    # elif keys[py.K_RIGHT] and y>170 and y<320 and x>230 and x<800:
    #     x += vel
    #     left = False
    #     right = True


   

    # elif keys[py.K_LEFT] and x>420 and x<540:
    #     x -= vel
    #     left = True
    #     right = False
    
    
    
        # elif keys[py.K_DOWN]:
    
        #     y+=vel

        

        # #and x>=415 and x<470:
        #     # and y>=0 and y<260:
        #     #and x>300 and x<540:

        #     #  and x>320 and x<540: 
        #     # and x<540 and y>=0 and y<406:
        #     y+=vel

        # elif keys[py.K_DOWN] and x>415 and x<500 and y==260:
        #     y+=vel    
    
        elif keys[py.K_UP] and y>vel:
            y-=vel
        else: 
            left = False
            right = False
            walkCount = 0
        
        redrawGameWindow() 
    
    
py.quit()

#elif right:
#(20,70) (320, 70)



#if event.key==pygame.KEYDOWN:


#if left and x>5 and:
    #then can move