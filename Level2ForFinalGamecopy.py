import pygame as py
from pygame.constants import K_LEFT




# from FinalGame import BLACK
py.init()
Lvl2finish_collidex=(range(690,750))
Lvl2finish_colldiey=(range(720, 750))

Lvl2star_collide1x=(range(20,69))
Lvl2star_collide1y=(range(200,249))

Lvl2star_collide2x=(range(176,229))
Lvl2star_collide2y=(range(563,612))

Lvl2star_collide3x=(range(702,751)) 
Lvl2star_collide3y=(range(400,449))
score2=0









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
py.display.set_caption("Stone Level Maze")
windowRect = window.get_rect()

walkRight = [py.image.load('Game\R1.png'), py.image.load('Game\R2.png'), py.image.load('Game\R3.png'), py.image.load('Game\R4.png'), py.image.load('Game\R5.png'), py.image.load('Game\R6.png'), py.image.load('Game\R7.png'), py.image.load('Game\R8.png'), py.image.load('Game\R9.png')]
walkLeft = [py.image.load('Game\L1.png'), py.image.load('Game\L2.png'), py.image.load('Game\L3.png'), py.image.load('Game\L4.png'), py.image.load('Game\L5.png'), py.image.load('Game\L6.png'), py.image.load('Game\L7.png'), py.image.load('Game\L8.png'), py.image.load('Game\L9.png')]
bg = py.image.load('gameimages\lightgraybkg.jpg')
char = py.image.load('Game\standing.png')
stonewall=py.image.load('gameimages\stone_wall_for_maze_game-removebg-preview.png')
stonewallup=py.image.load('gameimages\stonewallformazegameup2.png')
star=py.image.load('gameimages\pixelated_star_for_game50removedbkg - Copy.png')
finish= py.image.load('gameimages\endofmazegame100x100.png')

Level2load_Star1=True
Level2load_Star2=True
Level2load_Star3=True

vel=10

MenuMessages=["Instructions", "Level 1", "Level 2", "Settings", "Scoreboard", "Exit"]

x = 5
y = 40
width = 40
height = 60


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

def redrawGameWindowlvl2():
    global walkCount

    window.blit(bg, (0,0))  
    if walkCount + 1 >= 27:
        walkCount = 0
    
    window.blit(stonewall,(0,100))
    window.blit(stonewall,(140,290))
    window.blit(stonewall,(450,290))

    window.blit(stonewall,(280, 490))
    window.blit(stonewall,(50,490))
    window.blit(stonewall,(636,650))
    window.blit(stonewall,(236,100))
    
    

    window.blit(stonewallup,(195,100))
   
    window.blit(stonewallup,(605,0))
    window.blit(stonewallup,(50,300))
    
    window.blit(stonewallup,(246,490))
    window.blit(stonewallup,(605,335))
    window.blit(stonewallup,(605,530))
    window.blit(stonewallup,(246, 685))
    
    if Level2load_Star1:
        window.blit(star,(20,200))
    
    if Level2load_Star2:
        window.blit(star,(176,563))

    if Level2load_Star3:
        window.blit(star,(702, 400))

    window.blit(finish,(700,700))

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
check2=True

while check2:
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


        # if keys[py.K_LEFT] and x > vel: 
        #     x -= vel
        #     left = True
        #     right = False


        if keys[py.K_LEFT] and x>=0 and x<=575 and y>=0 and y<=110:
            x -=vel
            left = True
            right = False

        elif keys[py.K_LEFT] and x>=230 and x<=575 and y>=110 and y<=290:
            x -=vel
            left = True
            right = False
            
        elif keys[py.K_LEFT] and x>=-10 and x<185 and y>=60 and y<=290:
            x -=vel
            left = True
            right = False


        elif keys[py.K_LEFT] and x>=210 and x<800 and y>=190 and y<=250:
            x -= vel
            left = True
            right = False

        elif keys[py.K_LEFT] and x>=65 and x<=565 and y>=330 and y<=440:
            x -= vel
            left = True
            right = False

        elif keys[py.K_LEFT] and x>=265 and x<=575 and y>=500 and y<=710:
            x -= vel
            left = True
            right = False


        elif keys[py.K_LEFT] and x>=265 and x<=800 and y>=710 and y<=800:
            x -= vel
            left = True
            right = False

        elif keys[py.K_LEFT] and x>=620 and x<=800 and y>-10 and y<=610:
            x -= vel
            left = True
            right = False


        elif keys[py.K_LEFT] and x>=615 and x<=800 and y>-10 and y<=610:
            x-= vel
            left = True
            right = False

        elif keys[py.K_LEFT] and x>=-15 and x<=170 and y>=130 and y<=230:
            x-=vel
            left = True
            right = False

        elif keys[py.K_LEFT] and x>=-15 and x<=225 and y>=520 and y<=780:
            x-=vel
            left = True
            right = False

       
       
       
        elif keys[py.K_RIGHT] and x>=-10 and x<=565 and y>=40 and y<=60:
            x += vel
            left = False
            right = True

        elif keys[py.K_RIGHT] and x>=205 and x<=565 and y>=60 and y<=290:
            x += vel
            left = False
            right = True

        elif keys[py.K_RIGHT] and x>=-10 and x<170 and y>=60 and y<=290:
            x += vel
            left = False
            right = True


        elif keys[py.K_RIGHT] and x>=-15 and x<=155 and y>=145 and y<=290:
            x += vel
            left = False
            right = True

        elif keys[py.K_RIGHT] and x>=215 and x<730 and y>=190 and y<=250:
            x += vel
            left = False
            right = True

        elif keys[py.K_RIGHT] and x>=55 and x<=565 and y>=330 and y<=440:
            x += vel
            left = False
            right = True

        elif keys[py.K_RIGHT] and x>=255 and x<=565 and y>=500 and y<=710:
            x += vel
            left = False
            right = True


        elif keys[py.K_RIGHT] and x>=255 and x<=730 and y>=710 and y<=730:
            x += vel
            left = False
            right = True

        elif keys[py.K_RIGHT] and x>=600 and x<=730 and y>-10 and y<=610:
            x += vel
            left = False
            right = True

        elif keys[py.K_RIGHT] and x>=-25 and x<=215 and y>=530 and y<=800:
            x += vel
            left = False
            right = True


        

        elif keys[py.K_DOWN] and x>=400 and x<=575 and y>-10 and y<230:
            y+=vel

        elif keys[py.K_DOWN] and x>=205 and x<=575 and y>=120 and y<=230:
            y+=vel 

        elif keys[py.K_DOWN] and x>=305 and x<=425 and y>=230 and y<=430:
            y+=vel

        elif keys[py.K_DOWN] and x>=55 and x<=575 and y>=330 and y<=430:
            y+=vel

        elif keys[py.K_DOWN] and x>265 and x<=575 and y>=330 and y<=430:
            y+=vel

        elif keys[py.K_DOWN] and x>445 and x<=575 and y>=440 and y<=730:
            y+=vel

        elif keys[py.K_DOWN] and x>=255 and x<=575 and y>=500 and y<=730:
            y+=vel

        elif keys[py.K_DOWN] and x>=620 and x<=800 and y>-10 and y<=600:
            y+=vel

        elif keys[py.K_DOWN] and x>=55 and x<=115 and y>=130 and y<=430:
            y+=vel

        elif keys[py.K_DOWN] and x>=-25 and x<=170 and y>=120 and y<=230:
            y+=vel

        elif keys[py.K_DOWN] and x>=-25 and x<=10 and y>=230 and y<=730:
            y+=vel

        elif keys[py.K_DOWN] and x>=-25 and x<=215 and y>=520 and y<=730:
            y+=vel


    
        elif keys[py.K_UP] and x>=400 and x<=575 and y>=50 and y<=240:
            y-=vel

        elif keys[py.K_UP] and x>=205 and x<=575 and y>=120 and y<=240:
            y-=vel 

        elif keys[py.K_UP] and x>=305 and x<=425 and y>=230 and y<=440:
            y-=vel

        elif keys[py.K_UP] and x>=55 and x<=575 and y>330 and y<=440:
            y-=vel

        elif keys[py.K_UP] and x>265 and x<=575 and y>330 and y<=440:
            y-=vel
        
        elif keys[py.K_UP] and x>445 and x<=575 and y>=450 and y<=800:
            y-=vel

        elif keys[py.K_UP] and x>=255 and x<=575 and y>=500 and y<=800:
            y-=vel

        elif keys[py.K_UP] and x>=620 and x<=800 and y>=40 and y<=610:
            y-=vel

        elif keys[py.K_UP] and x>=55 and x<=115 and y>=140 and y<=430:
            y-=vel

        elif keys[py.K_UP] and x>=-35 and x<=170 and y>=130 and y<=240:
            y-=vel

        elif keys[py.K_UP] and x>=-25 and x<=10 and y>=230 and y<=800:
            y-=vel
        
        elif keys[py.K_UP] and x>=-25 and x<=215 and y>=530 and y<=800:
            y-=vel
        


        #265,520
        # elif keys[py.K_UP] and y>vel:
        #     y-=vel
        else: 
            left = False
            right = False
            walkCount = 0

        if x in Lvl2star_collide1x and y in Lvl2star_collide1y and Level2load_Star1:
            score2+=1
            Level2load_Star1=False
            

        if x in Lvl2star_collide2x and y in Lvl2star_collide2y and Level2load_Star2:
            score2+=1
            Level2load_Star2=False

        if x in Lvl2star_collide3x and y in Lvl2star_collide3y and Level2load_Star3:
            score2+=1
            Level2load_Star3=False

        if x in Lvl2finish_collidex and y in Lvl2finish_colldiey:
            window.fill(BLACK)
            py.display.flip()



        redrawGameWindowlvl2()      
py.quit()

#elif right:
#(20,70) (320, 70)



#if event.key==pygame.KEYDOWN:


#if left and x>5 and:
    #then can move