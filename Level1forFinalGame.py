import pygame as py
from pygame.constants import K_LEFT


# from FinalGame import BLACK
py.init()
finish_collidex=(range(750,750))
finish_colldiey=(range(750, 750))
star_collide2x=(range(415,460))
star_collide2y=(range(656,711))
score=0


#add colllide point

# window.blit(star,(20,200))
#     window.blit(star,(726,200))
#     window.blit(star,(415, 656))

BLACK= (0,0,0)

window = py.display.set_mode((800,800))
py.display.set_caption("Only 1% Can Complete")
windowRect = window.get_rect()

walkRight = [py.image.load('Game\R1.png'), py.image.load('Game\R2.png'), py.image.load('Game\R3.png'), py.image.load('Game\R4.png'), py.image.load('Game\R5.png'), py.image.load('Game\R6.png'), py.image.load('Game\R7.png'), py.image.load('Game\R8.png'), py.image.load('Game\R9.png')]
walkLeft = [py.image.load('Game\L1.png'), py.image.load('Game\L2.png'), py.image.load('Game\L3.png'), py.image.load('Game\L4.png'), py.image.load('Game\L5.png'), py.image.load('Game\L6.png'), py.image.load('Game\L7.png'), py.image.load('Game\L8.png'), py.image.load('Game\L9.png')]
bg = py.image.load('gameimages\grassbkgimage2.jpg')
char = py.image.load('Game\standing.png')
bush=py.image.load('gameimages\hedgeformazegame_adobespark300.png')
bushup=py.image.load('gameimages\hedgeformazegame_adobespark300up.png')
star=py.image.load('gameimages\pixelated_star_for_game50removedbkg.png')
finish= py.image.load('gameimages\endofmazegame100x100.png')

load_Star2=True




x = 0
y = 0
width = 40
height = 60
vel = 10

WIDTH=800
HEIGHT=800

clock = py.time.Clock()

TITLE_FONT=py.font.SysFont('comicsans', 40)
INSTRUCTIONS_FONT=py.font.SysFont('comicsans', 20)
SubTitle=py.font.SysFont('comicsans', 20, italic=True)
text=TITLE_FONT.render("message", 1, BLACK)
wbox=25
hbox=25
x=70
y=190
square=py.Rect(10,10, wbox, hbox)


def display_Title(message,y):
    #py.time.delay(100)
    text= TITLE_FONT.render(message, 1, BLACK) #render prints text
    x=WIDTH/2-text.get_width()/2
   # window.blit(text, (WIDTH/2-text.get_width()/2), (HEIGHT/2-text.get_height()/2))
    window.blit(text, (x,y)) #TExt, (x,y)) text, (WIDTH/2-text.get_width()/2, 10
    py.display.update()
    py.time.delay(100)

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
    if load_Star2:
        window.blit(star,(415, 656))
    

    window.blit(finish,(700,700))

    # if x>720 and x<790 and y>750 and y<785:
    #     window.fill(BLACK)
    #     py.display.set_caption("Main Menu Window")
    #     py.display.update()
    # # x>717 x<790, and y>710 y<790

    # if x>20 and x<193 and y>324 and y<4523:
        #remove star
        #starcount+=1

    
    

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
    

keys=py.key.get_pressed()
check=True

while check:
    clock.tick(27)

    for event in py.event.get():
        if event.type == py.QUIT:
            check = False
            mouse_pos=(0,0)

        elif event.type==py.MOUSEBUTTONDOWN:
            mouse_pressed=py.mouse.get_pressed()
            if mouse_pressed[0]:
                mouse_pos=py.mouse.get_pos()
                print(py.mouse.get_pos())
        elif event.type==py.KEYDOWN:   
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
        
        elif keys[py.K_RIGHT] and y>350 and y<800:
            x += vel
            left = False
            right = True
            
        # elif keys[py.K_LEFT] and x>=0 and x<600:
        #     x -= vel
        #     left = True
        #     right = False

        elif keys[py.K_LEFT] and x>=0 and x<300 and y>=0 and y<60:
            x -= vel
            left=True
            right=False

        elif keys[py.K_LEFT] and x>300 and x<600 and y>=0 and y<260:
            x -= vel
            left=True
            right=False

        elif keys[py.K_LEFT] and y>170 and y<580 and x>150 and x<800:
            x -= vel
            left=True
            right=False

        elif keys[py.K_LEFT] and y>580 and y<720 and x>=0 and x<800:
            x -= vel
            left=True
            right=False
        
     

        elif keys[py.K_DOWN] and x>270 and x<540 and y>=0 and y<260:
            y+=vel
        
        elif keys[py.K_DOWN] and x>360 and x<430 and y>=0 and y<460: #need to change this y i think its wrong, character stops in mid bush
            y+=vel

        elif keys[py.K_DOWN] and x>=0 and x<800 and y>400 and y<460:
            y+=vel

        elif keys[py.K_DOWN] and x>610 and x<800 and y>=0 and y<800:
            y+=vel
        
        elif keys[py.K_DOWN] and x>140 and x<265 and y>430 and y<660:
            y+=vel
        
        
    
        elif keys[py.K_UP] and y>vel:
            y-=vel
        else: 
            left = False
            right = False
            walkCount = 0
        print(x,y)
        if x in star_collide2x and y in star_collide2y:

            print("i am here")
            score+=1
            load_Star2=False
        
        if x in finish_collidex and y in finish_colldiey:
            window.fill(BLACK)
            py.display.set_caption("Main Menu Window")
            py.display.update()
            
        # if x in finishcollidex
        redrawGameWindow() 
    
    
py.quit()

#elif right:
#(20,70) (320, 70)



#if event.key==pygame.KEYDOWN:


#if left and x>5 and:
    #then can move