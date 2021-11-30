import pygame as py, os, random, time

#Using Code from mainmenu code, andrew helped me
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



py.init()
BLACK=(0,0,0)
WHITE=(255,255,255)
RED= (150, 0, 0)
BLUE=(0, 0,255)
GREEN=(0,128,0)
MenuMessages=["Instructions", "Level 1", "Level 2", "Settings", "Scoreboard", "Exit"]
settingsmessages=["Background Color","Screen Size"]
bkgcolors=["Black", "Blue", "Green"]
scrnsizemessages=["900 x 900", "1400 x 1400", "800 x 800"]
InstructionsMessages=["Collect all the Stars", "Finish the maze", "Use arrow keys to move", "There is no jumping", "You can move up and down with arrows"]
WIDTH=800
HEIGHT=800
window=py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("Main Menu Window")

#TITLE_FONT=pygame.font.SysFont(name, size, bold=False, italic=False)
TITLE_FONT=py.font.SysFont('comicsans', 80)
INSTRUCTIONS_FONT=py.font.SysFont('comicsans', 40)
SubTitle=py.font.SysFont('comicsans', 40, italic=True)
text=TITLE_FONT.render("message", 1, WHITE)
wbox=25
hbox=25
x=70
y=190
square=py.Rect(10,10, wbox, hbox)
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

# def Screen_Size():
#     x=70
#     y=190
#     square.x=x
#     square.y=y
#     for i in range(0, len(scrnsizemessages)):
#         word=scrnsizemessages[i]
#         py.draw.rect(window, RED, square)
#         text=TITLE_FONT.render(word, 1, WHITE)
#         window.blit(text, (x+wbox+10,y))
#         py.display.flip()
#         py.time.delay(100)
#         y+=80
#         square.y=y
    
def display_level1():
    bg = py.image.load('gameimages/grassbkgimage2.jpg')
    window.blit(bg, (0,0))
    py.display.set_caption("Grassy Level Maze")
    levelBackRect=display_Title("Quit", 750)
    py.display.flip()

def display_level2():
    bg = py.image.load('gameimages/stonebkgimage2.png')
    window.blit(bg, (0,0))
    py.display.set_caption("Stone Maze")
    levelBackRect=display_Title("Quit", 750)
    py.display.flip()


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
                    window.fill(bkgcolor)
                    py.display.update()
                    currentDisplay=DISPLAY_LEVEL1
                    display_level1()
                    #play game here

                if mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=345 and mouse_pos[1]<=375: #71, 193. 93,193. 93, 212. 71, 211
                    window.fill(bkgcolor)
                    py.display.update()
                    currentDisplay=DISPLAY_LEVEL2
                    display_level2()

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
            
            elif currentDisplay==DISPLAY_SETTINGS and mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=340 and mouse_pos[1]<=370:
                window.fill(bkgcolor)
                display_Title("Sound On/Off", 70)
                display_Title("Back", 750)
                py.display.update()
                currentDisplay=DISPLAY_SETTINGS_SOUND
            
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
            
            elif currentDisplay==DISPLAY_SETTINGS_OBJECT_COLOR and mouse_pos[0] >= 355 and mouse_pos[0] <= 465 and mouse_pos[1]>=750 and mouse_pos[1]<=795:
                window.fill(bkgcolor)
                display_Title("Settings", 70)
                display_Title("Back", 750)
                display_Menu(settingsmessages)
                py.display.update()
                currentDisplay=DISPLAY_SETTINGS

            elif currentDisplay==DISPLAY_SETTINGS_SOUND and mouse_pos[0] >= 355 and mouse_pos[0] <= 465 and mouse_pos[1]>=750 and mouse_pos[1]<=795:
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

            elif currentDisplay==DISPLAY_SETTINGS_BACKGROUND_COLOR and mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=250 and mouse_pos[1]<=280:
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
                window=py.display.set_mode((900,900))
                window.fill(bkgcolor)
                display_Title("Background Color", 70)
                display_Menu(scrnsizemessages)
                display_Title("Back", 750)
                py.display.update()  

            elif currentDisplay==DISPLAY_SETTINGS_SCREEN_SIZE and mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=250 and mouse_pos[1]<=300:
                window=py.display.set_mode((1400,1400))
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