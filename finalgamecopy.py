import pygame as py, os, random, time

# #Using Code from mainmenu code, andrew helped me
DISPLAY_MAIN_MENU=0
DISPLAY_INSTRUCTIONS=1
DISPLAY_LEVEL1=2
DISPLAY_LEVEL2=3
DISPLAY_SETTINGS=4
DISPLAY_SCOREBOARD=5
DISPLAY_SETTINGS_BACKGROUND_COLOR=6
DISPLAY_SETTINGS_OBJECT_COLOR=7
DISPLAY_SETTINGS_SOUND=8
DISPLAY_SETTINGS_SCREEN_SIZE=9
currentDisplay=DISPLAY_MAIN_MENU



#Level 1 Code:
from pygame.constants import K_LEFT


# from FinalGame import BLACK
py.init()
finish_collidex=(range(700,750))
finish_colldiey=(range(700, 750))

finish_collide2x=(range(700,750))
finish_colldie2y=(range(700, 750))

star_collide1x=(range(-5,54))
star_collide1y=(range(400,450))
star_collide2x=(range(430,479))
star_collide2y=(range(620,670))
star_collide3x=(range(720,771))
star_collide3y=(range(200,249))
score=0


Lvl2finish_collidex=(range(690,750))
Lvl2finish_colldiey=(range(720, 750))

Lvl2star_collide1x=(range(20,69))
Lvl2star_collide1y=(range(200,249))

Lvl2star_collide2x=(range(176,229))
Lvl2star_collide2y=(range(563,612))

Lvl2star_collide3x=(range(702,751)) 
Lvl2star_collide3y=(range(400,449))
score2=0

BLACK=(0,0,0)
WHITE=(255,255,255)
RED= (150, 0, 0)
BLUE=(0, 0,255)
GREEN=(0,128,0)

window = py.display.set_mode((800,800))



walkRight = [py.image.load('Game\R1.png'), py.image.load('Game\R2.png'), py.image.load('Game\R3.png'), py.image.load('Game\R4.png'), py.image.load('Game\R5.png'), py.image.load('Game\R6.png'), py.image.load('Game\R7.png'), py.image.load('Game\R8.png'), py.image.load('Game\R9.png')]
walkLeft = [py.image.load('Game\L1.png'), py.image.load('Game\L2.png'), py.image.load('Game\L3.png'), py.image.load('Game\L4.png'), py.image.load('Game\L5.png'), py.image.load('Game\L6.png'), py.image.load('Game\L7.png'), py.image.load('Game\L8.png'), py.image.load('Game\L9.png')]
bg = py.image.load('gameimages\grassbkgimage2.jpg')
bg2=py.image.load('gameimages\lightgraybkg.jpg')
char = py.image.load('Game\standing.png')
bush=py.image.load('gameimages\hedgeformazegame_adobespark300.png')
bushup=py.image.load('gameimages\hedgeformazegame_adobespark300up.png')
star=py.image.load('gameimages\pixelated_star_for_game50removedbkg.png')
finish= py.image.load('gameimages\endofmazegame100x100.png')
fence= py.image.load('gameimages\grassymazeFENCEnobkg100x97.png')
strawberrybush=py.image.load('gameimages\Bushofstrawberryformazegame150.png')
stonewall=py.image.load('gameimages\stone_wall_for_maze_game-removebg-preview.png')
stonewallup=py.image.load('gameimages\stonewallformazegameup2.png')
star=py.image.load('gameimages\pixelated_star_for_game50removedbkg - Copy.png')
finish= py.image.load('gameimages\endofmazegame100x100.png')

load_Star1=True
load_Star2=True
load_Star3=True
Level2load_Star1=True
Level2load_Star2=True
Level2load_Star3=True


MenuMessages=["Instructions", "Level 1", "Level 2", "Settings", "Scoreboard", "Exit"]
settingsmessages=["Background Color","Screen Size"]
bkgcolors=["Black", "Blue", "Green"]
scrnsizemessages=["1000x1000", "900x900", "800 x 800"]
InstructionsMessages=["Collect all the Stars", "Finish the maze", "Spam the arrow keys to move", "There is no jumping", "You will have to hit the stars with your head", "Due to the way the characters x is measured", "You can move up and down with arrows"]


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
text=TITLE_FONT.render("message", 1, WHITE)
wbox=25
hbox=25
square=py.Rect(10,10, wbox, hbox)


left = False
right = False
walkCount = 0


BLACK=(0,0,0)
WHITE=(255,255,255)
RED= (150, 0, 0)
BLUE=(0, 0,255)
GREEN=(0,128,0)


# myFile=open('scoreformazegame.txt', 'w')
# myFile.write("aklsdfj")
# myFile.close()
# #read and print the file
# # if you want to remove what you said b4 if you use write but if you use append it doesnt

# fileMy=open('score.txt', 'r')
# print(fileMy.read())
# fileMy.close()
# score=0
# anotherFile= open('score.txt','a')
# anotherFile.write("\n the highest score: \t" + str(score))
# anotherFile.close()

#############


#TITLE_FONT=pygame.font.SysFont(name, size, bold=False, italic=False)


#when you want to draw a rectangle you use 'rect' when you want to create a rectangle use 'Rect'

def display_Title(message,y):
    #py.time.delay(100)
    text= TITLE_FONT.render(message, 1, WHITE) #render prints text
    x=WIDTH/2-text.get_width()/2
   # window.blit(text, (WIDTH/2-text.get_width()/2), (HEIGHT/2-text.get_height()/2))
    window.blit(text, (x,y)) #TExt, (x,y)) text, (WIDTH/2-text.get_width()/2, 10
    py.display.update()
    py.time.delay(100)

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

def display_Instructions(messages):
    x=70
    y=190
    square.x=x
    square.y=y
    for i in range(0, len(messages)):
        word=messages[i]
        text=INSTRUCTIONS_FONT.render(word, 1, WHITE)
        window.blit(text, (x+wbox+10,y))
        py.display.flip()
        py.time.delay(100)
        y+=80
        square.y=y


# def display_Scoreboard(messages):
#     x=70
#     y=190
#     square.x=x
#     square.y=y
#     for i in range(0, len(messages)):
#         word=messages[i]
#         myFile=open('mazegamescore.txt', 'r')
#         text=INSTRUCTIONS_FONT.render(word, 1, WHITE)
#         window.blit(text, (x+wbox+10,y))
#         py.display.flip()
#         py.time.delay(100)
#         y+=80
#         square.y=y

def display_Scoreboard():
    global scoreboardBackRect
    window.fill(bkgcolor)
    display_Title("Scoreboard", 30)
    myFile = open('mazegamescore.txt', 'r')
    lines = myFile.readlines()
    lineYValue = 100
    for line in lines:
        display_Title(line, lineYValue)
        lineYValue = lineYValue + 100
        myFile.close()
    py.display.update()
    scoreboardBackRect = display_Title("Back", 750)
    return DISPLAY_SCOREBOARD


def redrawGameWindowlvl1():
    global walkCount

    window.blit(bg, (0,0))  
    if walkCount + 1 >= 27:
        walkCount = 0
    
    window.blit(bush,(0,50))
    window.blit(bush,(140,300))
    window.blit(bush,(450,300))
    window.blit(bush,(275, 700))
    window.blit(bush,(360, 500))
    window.blit(bush,(440,700))
    
    window.blit(bushup,(200,50))
    window.blit(bushup,(553,50))
    window.blit(bushup,(553,0))
    window.blit(bushup,(50,300))
    window.blit(bushup,(260,500))
    
    window.blit(fence,(-15, 300))

    window.blit(strawberrybush,(-15,145))
    window.blit(strawberrybush,(-15,195))
    window.blit(strawberrybush,(90, 145))
    window.blit(strawberrybush,(-15, 245))
    window.blit(strawberrybush,(90, 245))
    window.blit(strawberrybush,(90, 200))

    
    if load_Star1:
        window.blit(star,(5,450))

    if load_Star2:
        window.blit(star,(430, 620))

    if load_Star3:
        window.blit(star,(726,200))
    

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


def redrawGameWindowlvl2():
    global walkCount

    window.blit(bg2, (0,0))  
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
    



clock=py.time.Clock()
check=True
def charanimation(keys):
    global x
    global y
    print(x,y)
    run=True
    while run:
    #     while check:
    #         clock.tick(27)
    #         for event in py.event.get():
    #             if event.type == py.QUIT:
                 
    #         keys = py.key.get_pressed()
        if eve.type==py.KEYDOWN:
            if keys[py.K_LEFT] and x > vel: 
                x -= vel
                left = True
                right = False
            elif keys[py.K_RIGHT] and x < 800 - vel - width:  
                x += vel
                left = False
                right = True
            elif keys[py.K_UP] and y<800 - vel - width:
                y+=vel
            elif keys[py.K_DOWN] and y>vel:
                y-=vel
            else: 
                left = False
                right = False
                walkCount = 0
    redrawGameWindowlvl1(x,y) 

def charanimation2(keys):
    global x
    global y
    print(x,y)
    run=True
    while run:
    #     while check:
    #         clock.tick(27)
    #         for event in py.event.get():
    #             if event.type == py.QUIT:
                 
    #         keys = py.key.get_pressed()
        if eve.type==py.KEYDOWN:
            if keys[py.K_LEFT] and x > vel: 
                x -= vel
                left = True
                right = False
            elif keys[py.K_RIGHT] and x < 800 - vel - width:  
                x += vel
                left = False
                right = True
            elif keys[py.K_UP] and y<800 - vel - width:
                y+=vel
            elif keys[py.K_DOWN] and y>vel:
                y-=vel
            else: 
                left = False
                right = False
                walkCount = 0
    redrawGameWindowlvl2(x,y)             

def display_level1(keys):
    bg = py.image.load('gameimages\grassbkgimage2.jpg')
    window.blit(bg, (0,0))
    py.display.set_caption("Grassy Level Maze")
    levelBackRect=display_Title("Quit", 750)
    py.display.flip()
    x=70
    y=190
    if keys[py.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False
    elif keys[py.K_RIGHT] and x < 800 - vel - width:  
        x += vel
        left = False
        right = True
    elif keys[py.K_UP] and y<800 - vel - width:
        y+=vel
    elif keys[py.K_DOWN] and y>vel:
        y-=vel
    else: 
        left = False
        right = False
        walkCount = 0
    charanimation(keys)
        
    

def display_level2():
    bg = py.image.load('gameimages\lightgraybkg.jpg')
    window.blit(bg, (0,0))
    py.display.set_caption("Stone Maze")
    levelBackRect=display_Title("Quit", 750)
    py.display.flip()
    x=70
    y=190
    if keys[py.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False
    elif keys[py.K_RIGHT] and x < 800 - vel - width:  
        x += vel
        left = False
        right = True
    elif keys[py.K_UP] and y<800 - vel - width:
        y+=vel
    elif keys[py.K_DOWN] and y>vel:
        y-=vel
    else: 
        left = False
        right = False
        walkCount = 0
    charanimation2(keys)

    
    

bkgcolor=BLACK
window.fill(bkgcolor)
display_Title("Main Menu",70)
display_Menu(MenuMessages)
py.display.update()
currentDisplay=DISPLAY_MAIN_MENU

#counter=0
run=True 
while run:
    for eve in py.event.get():
        if eve.type == py.QUIT: #pygame.QUIT is looking for a key pressed, while pygame.quit() is a function
            run=False
        mouse_pos=(0,0)
        keys = py.key.get_pressed()
        if keys[py.K_UP]:
            print("UP")
        if eve.type==py.MOUSEBUTTONDOWN:
            mouse_pressed=py.mouse.get_pressed()
            if mouse_pressed[0]:
                mouse_pos=py.mouse.get_pos()
                print(py.mouse.get_pos())

            #MAIN MENU CODE:
            if currentDisplay==DISPLAY_MAIN_MENU:
                mouse_pos=py.mouse.get_pos()
                if mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=190 and mouse_pos[1]<=225:
                    window.fill(bkgcolor)
                    py.display.set_caption("Instructions Window")
                    display_Title("Instructions", 70)
                    display_Title("Back", 750)
                    display_Instructions(InstructionsMessages)
                    py.display.update()
                    currentDisplay=DISPLAY_INSTRUCTIONS
                   
                if mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=270 and mouse_pos[1]<=300: #71, 193. 93,193. 93, 212. 71, 211
                    # window.fill(bkgcolor)
                    # py.display.update()
                    # currentDisplay=DISPLAY_LEVEL1
                    # display_level1(keys)
                    #play game here
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

                            

                            if keys[py.K_RIGHT] and x>-10 and x<540 and y>=0 and y<=260:
                                x += vel
                                left = False
                                right = True
                            
                            elif keys[py.K_RIGHT] and x>140 and x<725 and y>400 and y<500:
                                x+=vel
                                left=False
                                right=True


                            # elif keys[py.K_RIGHT] and x>140 and x<790 and y>=370 and y<720:
                            #     x += vel
                            #     left=False
                            #     right=True


                            elif keys[py.K_RIGHT] and x>680 and x<725 and y>=0 and y<725:
                                x+=vel
                                left=False
                                right=True


                            elif keys[py.K_RIGHT] and x>=0 and x<200 and y>175 and y<300:
                                x+=vel
                                left=False
                                right=True

                            # elif keys[py.K_RIGHT] and x>-10 and x<250 and y>300 and y<800:
                            #     x+=vel
                            #     left=False
                            #     right=True


                            elif keys[py.K_RIGHT] and x>=-15 and x<=250 and y>460 and y<740:
                                x += vel
                                left=False
                                right=True


                            elif keys[py.K_RIGHT] and x>=55 and x<725 and y>=580 and y<715:
                                x += vel
                                left=False
                                right=True


                            elif keys[py.K_RIGHT] and x>=615 and x<780 and y>500 and y<=580:
                                x += vel
                                left=False
                                right=True

                            


                            elif keys[py.K_LEFT] and x>=0 and x<300 and y>=0 and y<60:
                                x -= vel
                                left=True
                                right=False

                            elif keys[py.K_LEFT] and x>300 and x<600 and y>=0 and y<=260:
                                x -= vel
                                left=True
                                right=False

                            elif keys[py.K_LEFT] and y>=370 and y<580 and x>150 and x<=250:
                                x -= vel
                                left=True
                                right=False

                            elif keys[py.K_LEFT] and y>=420 and y<500 and x>150 and x<=250:
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


                            elif keys[py.K_LEFT] and x>370 and x<=725 and y>=600 and y<715:
                                x -= vel
                                left=True
                                right=False

                            elif keys[py.K_LEFT] and x>-15 and x<=250 and y>600 and y<740:
                                x -= vel
                                left=True
                                right=False

                            elif keys[py.K_LEFT] and x>=625 and x<780 and y>500 and y<580:
                                x -= vel
                                left=True
                                right=False

                            elif keys[py.K_LEFT] and x>155 and x<=725 and y>=400 and y<=460:
                                x -= vel
                                left=True
                                right=False
                        

                            elif keys[py.K_DOWN] and x>270 and x<540 and y>=-10 and y<=250:
                                y+=vel
                            
                            elif keys[py.K_DOWN] and x>380 and x<=435 and y>=0 and y<460: #need to change this y i think its wrong, character stops in mid bush
                                y+=vel

                            elif keys[py.K_DOWN] and x>=0 and x<800 and y>=370 and y<460:
                                y+=vel

                            elif keys[py.K_DOWN] and x>670 and x<800 and y>-20 and y<260:
                                y+=vel

                            elif keys[py.K_DOWN] and x>630 and x<800 and y>-20 and y<725:
                                y+=vel
                            
                            elif keys[py.K_DOWN] and x>140 and x<265 and y>=380 and y<725:
                                y+=vel
                            
                            elif keys[py.K_DOWN] and x>=0 and x<175 and y>600 and y<725:
                                y+=vel

                            elif keys[py.K_DOWN] and x>-10 and x<150 and y>=380 and y<725:
                                y+=vel



                            

                            
                            
                            # elif keys[py.K_UP] and y>vel:
                            #     y-=vel
                            

                            elif keys[py.K_UP] and x>270 and x<540 and y>10 and y<=260:
                                y-=vel

                            elif keys[py.K_UP] and x>380 and x<430 and y>=0 and y<=460:
                                y-=vel

                            elif keys[py.K_UP] and x>=0 and x<800 and y>370 and y<=460:
                                y-=vel

                            elif keys[py.K_UP] and x>670 and x<800 and y>=0 and y<800:
                                y-=vel

                            
                            elif keys[py.K_UP] and x>140 and x<265 and y>430 and y<800:
                                y-=vel

                            elif keys[py.K_UP] and x>=0 and x<175 and y>600 and y<725:
                                y-=vel

                            elif keys[py.K_UP] and x>-10 and x<150 and y>380 and y<800:
                                y-=vel

                            elif keys[py.K_UP] and x>-10 and x<185 and y>=160 and y<250:
                                y-=vel
                            
                            



                            else: 
                                left = False
                                right = False
                                walkCount = 0
                            print(x,y)

                            if x in star_collide1x and y in star_collide1y and load_Star1:
                                score+=1
                                myFile=open('mazegamescore.txt', 'w') #here we creat the file object
                                myFile.write("Level 1 score: " + str(score))
                                myFile.write("\n Level 2 score: " + str(score2))
                                myFile.close()
                                load_Star1=False

                            if x in star_collide2x and y in star_collide2y and load_Star2:
                                score+=1
                                myFile=open('mazegamescore.txt', 'w') #here we creat the file object
                                myFile.write("Level 1 score: " + str(score))
                                myFile.write("\n Level 2 score: " + str(score2))
                                myFile.close()
                                load_Star2=False

                            if x in star_collide3x and y in star_collide3y and load_Star3:
                                score+=1
                                myFile=open('mazegamescore.txt', 'w') #here we creat the file object
                                myFile.write("Level 1 score: " + str(score))
                                myFile.write("\n Level 2 score: " + str(score2))
                                myFile.close()
                                load_Star3=False


                            
                            

                            redrawGameWindowlvl1() 

                            
                            # if x in finishcollidex
                        if x in finish_collidex and y in finish_colldiey:
                            window.fill(BLACK)
                            py.display.set_caption("Main Menu Window")
                            display_Title("Main Menu", 70)
                            display_Menu(MenuMessages)
                            py.display.flip()
                            check=False
                            currentDisplay=DISPLAY_MAIN_MENU     
    


                if mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=345 and mouse_pos[1]<=375: #71, 193. 93,193. 93, 212. 71, 211
                    keys=py.key.get_pressed()
                    check2=True
                    x=0
                    y=40
                    
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

                            elif keys[py.K_RIGHT] and x>=-25 and x<170 and y>=60 and y<=290:
                                x += vel
                                left = False
                                right = True


                            elif keys[py.K_RIGHT] and x>=-25 and x<=155 and y>=145 and y<=290:
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

                            print(x,y)

                            
                            
                            if x in Lvl2star_collide1x and y in Lvl2star_collide1y and Level2load_Star1:
                                score2+=1
                                myFile=open('mazegamescore.txt', 'w') #here we creat the file object
                                myFile.write("Level 1 score: " + str(score))
                                myFile.write("\n Level 2 score: " + str(score2))
                                myFile.close()
                                Level2load_Star1=False

                            if x in Lvl2star_collide2x and y in Lvl2star_collide2y and Level2load_Star2:
                                score2+=1
                                myFile=open('mazegamescore.txt', 'w') #here we creat the file object
                                myFile.write("Level 1 score: " + str(score))
                                myFile.write("\n Level 2 score: " + str(score2))
                                myFile.close()
                                Level2load_Star2=False

                            if x in Lvl2star_collide3x and y in Lvl2star_collide3y and Level2load_Star3:
                                score2+=1
                                myFile=open('mazegamescore.txt', 'w') #here we creat the file object
                                myFile.write("Level 1 score: " + str(score))
                                myFile.write("\n Level 2 score: " + str(score2))
                                myFile.close()
                                Level2load_Star3=False




                            
                            

                            redrawGameWindowlvl2() 

                            
                            # if x in finishcollidex
                        if x in finish_collide2x and y in finish_colldie2y:
                            window.fill(BLACK)
                            py.display.set_caption("Main Menu Window")
                            display_Title("Main Menu", 70)
                            display_Menu(MenuMessages)
                            py.display.flip()
                            check2=False
                            currentDisplay=DISPLAY_MAIN_MENU  
                            
                                

                            

                           

                            # if x in Lvl2finish_collidex and y in Lvl2finish_colldiey:
                            #     window.fill(BLACK)
                            #     py.display.flip()

    

                         

                if mouse_pos[0] >= 70 and mouse_pos[0] <= 95 and mouse_pos[1]>=400 and mouse_pos[1]<=455:  #75, 435 (top left) 95, 435, (top right) bottom right: 95, 455,  bottom left: 75,
                    window.fill(bkgcolor)
                    py.display.set_caption("Settings Window")
                    display_Title("Settings", 70)
                    display_Title("Back", 750)
                    display_Menu(settingsmessages)
                    py.display.update()
                    currentDisplay=DISPLAY_SETTINGS

                if mouse_pos[0] >= 70 and mouse_pos[0] <= 95 and mouse_pos[1]>=505 and mouse_pos[1]<=535:  #75, 435 (top left) 95, 435, (top right) bottom right: 95, 455,  bottom left: 75,
                    window.fill(bkgcolor)
                    py.display.set_caption("Scoreboard Window")
                    display_Title("Scoreboard", 70)
                    display_Title("Back", 750)
                    display_Scoreboard()
                    py.display.update()
                    currentDisplay=DISPLAY_SCOREBOARD

                if mouse_pos[0] >= 70 and mouse_pos[0] <= 95 and mouse_pos[1]>=590 and mouse_pos[1]<=615:
                    py.quit()
                # END OF MAIN MENU CODE



            #BACK BUTTON CODE for Main MEnu:
            elif currentDisplay==DISPLAY_SETTINGS and mouse_pos[0] >= 355 and mouse_pos[0] <= 465 and mouse_pos[1]>=750 and mouse_pos[1]<=795:
                window.fill(bkgcolor)
                py.display.set_caption("Main Menu Window")
                display_Title("Main Menu", 70)
                display_Menu(MenuMessages)
                py.display.update()
                currentDisplay=DISPLAY_MAIN_MENU

            elif currentDisplay==DISPLAY_INSTRUCTIONS and mouse_pos[0] >= 355 and mouse_pos[0] <= 465 and mouse_pos[1]>=750 and mouse_pos[1]<=795:
                window.fill(bkgcolor)
                py.display.set_caption("Main Menu Window")
                display_Title("Main Menu", 70)
                display_Menu(MenuMessages)
                py.display.update()
                currentDisplay=DISPLAY_MAIN_MENU

            elif currentDisplay==DISPLAY_LEVEL1 and mouse_pos[0] >= 355 and mouse_pos[0] <= 465 and mouse_pos[1]>=750 and mouse_pos[1]<=795:
                window.fill(bkgcolor)
                py.display.set_caption("Main Menu Window")
                display_Title("Main Menu", 70)
                display_Menu(MenuMessages)
                py.display.update()
                currentDisplay=DISPLAY_MAIN_MENU

            elif currentDisplay==DISPLAY_LEVEL2 and mouse_pos[0] >= 355 and mouse_pos[0] <= 465 and mouse_pos[1]>=750 and mouse_pos[1]<=795:
                window.fill(bkgcolor)
                py.display.set_caption("Main Menu Window")
                display_Title("Main Menu", 70)
                display_Menu(MenuMessages)
                py.display.update()
                currentDisplay=DISPLAY_MAIN_MENU

            elif currentDisplay==DISPLAY_SCOREBOARD and mouse_pos[0] >= 355 and mouse_pos[0] <= 465 and mouse_pos[1]>=750 and mouse_pos[1]<=795:
                window.fill(bkgcolor)
                py.display.set_caption("Main Menu Window")

                display_Title("Main Menu", 70)
                display_Menu(MenuMessages)
                py.display.update()
                currentDisplay=DISPLAY_MAIN_MENU
            #End of Back Button Code for Main Menu

        #Settings Code:
            elif currentDisplay==DISPLAY_SETTINGS and mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=190 and mouse_pos[1]<=220:
                window.fill(bkgcolor)
                display_Title("Background Color", 70)
                display_Menu(bkgcolors)
                display_Title("Back", 750)
                py.display.update()
                currentDisplay=DISPLAY_SETTINGS_BACKGROUND_COLOR

            elif currentDisplay==DISPLAY_SETTINGS and mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=270 and mouse_pos[1]<=300:
                window.fill(bkgcolor)
                display_Title("Screen Size", 70)
                display_Menu(scrnsizemessages)
                display_Title("Back", 750)
                py.display.update()
                currentDisplay=DISPLAY_SETTINGS_SCREEN_SIZE



        # elif currentDisplay==DISPLAY_SETTINGS and mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=430 and mouse_pos[1]<=460:
        #     window.fill(bkgcolor)
        #     display_Title("Screen Size", 70)
        #     display_Menu(scrnsizemessages)
        #     display_Title("Back", 750)
        #     py.display.update()
        #     currentDisplay=DISPLAY_SETTINGS_SCREEN_SIZE

        # Back Button Code for Settings:
            elif currentDisplay==DISPLAY_SETTINGS_BACKGROUND_COLOR and mouse_pos[0] >= 355 and mouse_pos[0] <= 465 and mouse_pos[1]>=750 and mouse_pos[1]<=795:
                window.fill(bkgcolor)
                display_Title("Settings", 70)
                display_Title("Back", 750)
                display_Menu(settingsmessages)
                py.display.update()
                currentDisplay=DISPLAY_SETTINGS
            
            elif currentDisplay==DISPLAY_SETTINGS_BACKGROUND_COLOR and mouse_pos[0] >= 355 and mouse_pos[0] <= 465 and mouse_pos[1]>=750 and mouse_pos[1]<=795:
                window.fill(bkgcolor)
                display_Title("Settings", 70)
                display_Title("Back", 750)
                display_Menu(settingsmessages)
                py.display.update()
                currentDisplay=DISPLAY_SETTINGS
            

            elif currentDisplay==DISPLAY_SETTINGS_SCREEN_SIZE and mouse_pos[0] >= 355 and mouse_pos[0] <= 465 and mouse_pos[1]>=750 and mouse_pos[1]<=795:
                window.fill(bkgcolor)
                display_Title("Settings", 70)
                display_Title("Back", 750)
                display_Menu(settingsmessages)
                py.display.update()
                currentDisplay=DISPLAY_SETTINGS

            elif currentDisplay==DISPLAY_SETTINGS_BACKGROUND_COLOR and mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=200 and mouse_pos[1]<=225:
                bkgcolor=BLACK
                window.fill(bkgcolor)
                display_Title("Background Color", 70)
                display_Menu(bkgcolors)
                display_Title("Back", 750)
                py.display.update()  

            elif currentDisplay==DISPLAY_SETTINGS_BACKGROUND_COLOR and mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=269 and mouse_pos[1]<=290:
                bkgcolor=BLUE
                window.fill(bkgcolor)
                display_Title("Background Color", 70)
                display_Menu(bkgcolors)
                display_Title("Back", 750)
                py.display.update()

            elif currentDisplay==DISPLAY_SETTINGS_BACKGROUND_COLOR and mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=350 and mouse_pos[1]<=375:
                bkgcolor=GREEN
                window.fill(bkgcolor)
                display_Title("Background Color", 70)
                display_Menu(bkgcolors)
                display_Title("Back", 750)
                py.display.update()


            elif currentDisplay==DISPLAY_SETTINGS_SCREEN_SIZE and mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=200 and mouse_pos[1]<=225:
                window=py.display.set_mode((1000,1000))
                window.fill(bkgcolor)
                display_Title("Background Color", 70)
                display_Menu(scrnsizemessages)
                display_Title("Back", 750)
                py.display.update()  

            elif currentDisplay==DISPLAY_SETTINGS_SCREEN_SIZE and mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=250 and mouse_pos[1]<=300:
                window=py.display.set_mode((900,900))
                window.fill(bkgcolor)
                display_Title("Screen Size", 70)
                display_Menu(scrnsizemessages)
                display_Title("Back", 750)
                py.display.update()

            elif currentDisplay==DISPLAY_SETTINGS_SCREEN_SIZE and mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=350 and mouse_pos[1]<=375:
                window=py.display.set_mode((800,800))
                window.fill(bkgcolor)
                display_Title("Screen Size", 70)
                display_Menu(scrnsizemessages)
                display_Title("Back", 750)
                py.display.update()    
py.quit()

#way to force images togther:
#py.transform
