import pygame as py
from pygame.constants import K_LEFT




# from FinalGame import BLACK
py.init()
finish_collidex=(range(700,750))
finish_colldiey=(range(700, 750))

star_collide1x=(range(20,65))
star_collide1y=(range(200,245))
star_collide2x=(range(430,479))
star_collide2y=(range(620,670))
star_collide3x=(range(726,771))
star_collide3y=(range(200,249))
score=0


#add colllide point

# window.blit(star,(20,200))
#     window.blit(star,(726,200))
#     window.blit(star,(415, 656))
# window.blit(star,(430, 620))

BLACK=(0,0,0)
WHITE=(255,255,255)
RED= (150, 0, 0)
BLUE=(0, 0,255)
GREEN=(0,128,0)

window = py.display.set_mode((800,800))
py.display.set_caption("Grassy Level Maze")
windowRect = window.get_rect()

walkRight = [py.image.load('Game\R1.png'), py.image.load('Game\R2.png'), py.image.load('Game\R3.png'), py.image.load('Game\R4.png'), py.image.load('Game\R5.png'), py.image.load('Game\R6.png'), py.image.load('Game\R7.png'), py.image.load('Game\R8.png'), py.image.load('Game\R9.png')]
walkLeft = [py.image.load('Game\L1.png'), py.image.load('Game\L2.png'), py.image.load('Game\L3.png'), py.image.load('Game\L4.png'), py.image.load('Game\L5.png'), py.image.load('Game\L6.png'), py.image.load('Game\L7.png'), py.image.load('Game\L8.png'), py.image.load('Game\L9.png')]
bg = py.image.load('gameimages\lightgraybkg.jpg')
char = py.image.load('Game\standing.png')
stonewall=py.image.load('gameimages\stone_wall_for_maze_game-removebg-preview.png')
stonewallup=py.image.load('gameimages\stonewallformazegameup2.png')
star=py.image.load('gameimages\pixelated_star_for_game50removedbkg - Copy.png')
finish= py.image.load('gameimages\endofmazegame100x100.png')

load_Star1=True
load_Star2=True
load_Star3=True


MenuMessages=["Instructions", "Level 1", "Level 2", "Settings", "Scoreboard", "Exit"]

x = 5
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
square=py.Rect(10,10, wbox, hbox)


def display_Menu(messages):
    x=70
    y=190
    square.x=x
    square.y=y
    for i in range(0, len(messages)):
        word=messages[i]
        py.draw.rect(window, RED, square)
        text=TITLE_FONT.render(word, 1, WHITE)
        window.blit(text, (x+wbox+10,y))
        py.display.flip()
        py.time.delay(100)
        y+=80
        square.y=y


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
    
    window.blit(stonewall,(0,100))
    window.blit(stonewall,(140,295))
    window.blit(stonewall,(450,300))
    # window.blit(stonewall,(50,645))
    # window.blit(stonewall,(138, 675))
    window.blit(stonewall,(280, 490))
    window.blit(stonewall,(50,490))
    window.blit(stonewall,(636,465))
    window.blit(stonewall,(236,100))
    # window.blit(stonewall,(245,147))
    # window.blit(stonewall,(245,90))
    

    window.blit(stonewallup,(195,100))
    window.blit(stonewallup,(553,50))
    window.blit(stonewallup,(553,0))
    window.blit(stonewallup,(50,300))
    window.blit(stonewallup,(246,490))
    window.blit(stonewallup,(605,335))
    window.blit(stonewallup,(435,530))
    window.blit(stonewallup,(605,530))
    # window.blit(stonewallup,(246, 335))
    window.blit(stonewallup,(246, 685))
    

    
    window.blit(star,(20,200))
    window.blit(star,(176,563))
    window.blit(star,(702, 112))
    

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

        

        if keys[py.K_RIGHT] and x>-10 and x<540 and y>=0 and y<260:
            x += vel
            left = False
            right = True
        
        elif keys[py.K_RIGHT] and x>-10 and x<800 and y>400 and y<500:
            x+=vel
            left=False
            right=True


        elif keys[py.K_RIGHT] and x>140 and x<790 and y>=370 and y<720:
            x += vel
            left=False
            right=True


        elif keys[py.K_RIGHT] and x>680 and x<800 and y>=0 and y<800:
            x+=vel
            left=False
            right=True


        elif keys[py.K_RIGHT] and x>=0 and x<200 and y>175 and y<300:
            x+=vel
            left=False
            right=True

        elif keys[py.K_RIGHT] and x>-10 and x<250 and y>300 and y<800:
            x+=vel
            left=False
            right=True


        elif keys[py.K_RIGHT] and x>=365 and x<790 and y>600 and y<715:
            x += vel
            left=False
            right=True






            
        # elif keys[py.K_LEFT] and x>=0 and x<600:
        #     x -= vel
        #     left = True
        #     right = False

        elif keys[py.K_LEFT] and x>=0 and x<300 and y>=0 and y<60:
            x -= vel
            left=True
            right=False

        elif keys[py.K_LEFT] and x>300 and x<600 and y>=0 and y<=260:
            x -= vel
            left=True
            right=False

        elif keys[py.K_LEFT] and y>=370 and y<580 and x>150 and x<800:
            x -= vel
            left=True
            right=False

        elif keys[py.K_LEFT] and y>560 and y<720 and x>=0 and x<290:
            x -= vel
            left=True
            right=False



        elif keys[py.K_LEFT] and x>=0 and x<200 and y>175 and y<300:
            x-=vel
            left=True
            right=False


        elif keys[py.K_LEFT] and x>370 and x<790 and y>600 and y<715:
            x -= vel
            left=True
            right=False

            #175,150, 0,150, 185,260
     

        elif keys[py.K_DOWN] and x>270 and x<540 and y>=0 and y<260:
            y+=vel
        
        elif keys[py.K_DOWN] and x>380 and x<430 and y>=0 and y<460: #need to change this y i think its wrong, character stops in mid bush
            y+=vel

        elif keys[py.K_DOWN] and x>=0 and x<800 and y>370 and y<460:
            y+=vel

        elif keys[py.K_DOWN] and x>670 and x<800 and y>=0 and y<260:
            y+=vel

        elif keys[py.K_DOWN] and x>630 and x<800 and y>=0 and y<800:
            y+=vel
         
        elif keys[py.K_DOWN] and x>140 and x<265 and y>=370 and y<800:
            y+=vel
        
        elif keys[py.K_DOWN] and x>=0 and x<175 and y>600 and y<725:
            y+=vel

        elif keys[py.K_DOWN] and x>-10 and x<150 and y>=150 and y<725:
            y+=vel

        
        
        # elif keys[py.K_UP] and y>vel:
        #     y-=vel
        

        elif keys[py.K_UP] and x>270 and x<540 and y>=0 and y<260:
            y-=vel

        elif keys[py.K_UP] and x>380 and x<430 and y>=0 and y<=460:
            y-=vel

        elif keys[py.K_UP] and x>=0 and x<800 and y>370 and y<=460:
            y-=vel

        elif keys[py.K_UP] and x>640 and x<800 and y>=0 and y<800:
            y-=vel

         
        elif keys[py.K_UP] and x>140 and x<265 and y>430 and y<800:
            y-=vel

        elif keys[py.K_UP] and x>=0 and x<175 and y>600 and y<725:
            y-=vel

        elif keys[py.K_UP] and x>-10 and x<150 and y>150 and y<800:
            y-=vel
        
        



        else: 
            left = False
            right = False
            walkCount = 0
        print(x,y)

        if x in star_collide1x and y in star_collide1y and load_Star1:
            score+=1
            load_Star1=False

        if x in star_collide2x and y in star_collide2y and load_Star2:
            score+=1
            load_Star2=False

        if x in star_collide3x and y in star_collide3y and load_Star3:
            score+=1
            load_Star3=False


        
        

        redrawGameWindow() 

            
        # if x in finishcollidex
    if x in finish_collidex and y in finish_colldiey:
            window.fill(BLACK)
            py.display.set_caption("Main Menu Window")
            display_Title("Main Menu", 70)
            display_Menu(MenuMessages)
            py.display.flip()       
    
    
py.quit()

#elif right:
#(20,70) (320, 70)



#if event.key==pygame.KEYDOWN:


#if left and x>5 and:
    #then can move