#William Maher
#10/25/21 Learning Fonts and Blit

import pygame as py, os, random, time

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
settingsmessages=["Background Color", "Object Color", "Sound On/Off", "Screen Size"]
bkgcolors=["Black", "Blue", "Green"]
width=800
height=800


window=py.display.set_mode((width,height))
py.display.set_caption("Setting Window")

#TITLE_FONT=pygame.font.SysFont(name, size, bold=False, italic=False)
TITLE_FONT=py.font.SysFont('comicsans', 80)
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
    x=width/2-text.get_width()/2
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
                if mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=200 and mouse_pos[1]<=225:
                    window.fill(bkgcolor)
                    display_Title("Instructions", 70)
                    display_Title("Back", 750)
                    py.display.update()
                    currentDisplay=DISPLAY_INSTRUCTIONS
                
                if mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=250 and mouse_pos[1]<=275: #71, 193. 93,193. 93, 212. 71, 211
                    window.fill(bkgcolor)
                    display_Title("Level 1",  70)
                    display_Title("Back", 750)
                    py.display.update()
                    currentDisplay=DISPLAY_LEVEL1

                if mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=345 and mouse_pos[1]<=375: #71, 193. 93,193. 93, 212. 71, 211
                    window.fill(bkgcolor)
                    display_Title("Level 2", 70)
                    display_Title("Back", 750)
                    py.display.update()
                    currentDisplay=DISPLAY_LEVEL2

                if mouse_pos[0] >= 70 and mouse_pos[0] <= 95 and mouse_pos[1]>=400 and mouse_pos[1]<=455:  #75, 435 (top left) 95, 435, (top right) bottom right: 95, 455,  bottom left: 75,
                    window.fill(bkgcolor)
                    display_Title("Settings", 70)
                    display_Title("Back", 750)
                    display_Menu(settingsmessages)
                    py.display.update()
                    currentDisplay=DISPLAY_SETTINGS

                if mouse_pos[0] >= 70 and mouse_pos[0] <= 95 and mouse_pos[1]>=505 and mouse_pos[1]<=535:  #75, 435 (top left) 95, 435, (top right) bottom right: 95, 455,  bottom left: 75,
                    window.fill(bkgcolor)
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
                display_Title("Main Menu", 70)
                display_Menu(MenuMessages)
                py.display.update()
                currentDisplay=DISPLAY_MAIN_MENU

            elif currentDisplay==DISPLAY_INSTRUCTIONS and mouse_pos[0] >= 355 and mouse_pos[0] <= 465 and mouse_pos[1]>=750 and mouse_pos[1]<=795:
                window.fill(bkgcolor)
                display_Title("Main Menu", 70)
                display_Menu(MenuMessages)
                py.display.update()
                currentDisplay=DISPLAY_MAIN_MENU

            elif currentDisplay==DISPLAY_LEVEL1 and mouse_pos[0] >= 355 and mouse_pos[0] <= 465 and mouse_pos[1]>=750 and mouse_pos[1]<=795:
                window.fill(bkgcolor)
                display_Title("Main Menu", 70)
                display_Menu(MenuMessages)
                py.display.update()
                currentDisplay=DISPLAY_MAIN_MENU

            elif currentDisplay==DISPLAY_LEVEL2 and mouse_pos[0] >= 355 and mouse_pos[0] <= 465 and mouse_pos[1]>=750 and mouse_pos[1]<=795:
                window.fill(bkgcolor)
                display_Title("Main Menu", 70)
                display_Menu(MenuMessages)
                py.display.update()
                currentDisplay=DISPLAY_MAIN_MENU

            elif currentDisplay==DISPLAY_SCOREBOARD and mouse_pos[0] >= 355 and mouse_pos[0] <= 465 and mouse_pos[1]>=750 and mouse_pos[1]<=795:
                window.fill(bkgcolor)
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
                display_Title("Object Color", 70)
                display_Title("Back", 750)
                py.display.update()
                currentDisplay=DISPLAY_SETTINGS_OBJECT_COLOR
            
            elif currentDisplay==DISPLAY_SETTINGS and mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=340 and mouse_pos[1]<=370:
                window.fill(bkgcolor)
                display_Title("Sound On/Off", 70)
                display_Title("Back", 750)
                py.display.update()
                currentDisplay=DISPLAY_SETTINGS_SOUND
            
            elif currentDisplay==DISPLAY_SETTINGS and mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>=430 and mouse_pos[1]<=460:
                window.fill(bkgcolor)
                display_Title("Screen Size", 70)
                display_Title("Back", 750)
                py.display.update()
                currentDisplay=DISPLAY_SETTINGS_SCREEN_SIZE

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
           

            
            
           

           

                
                    #change double equals
                    # if mouse_pos[0] >= 330 and mouse_pos[0] <= 465 and mouse_pos[1]>=750 and mouse_pos[1]<=785 and currentDisplay==DISPLAY_SETTINGS:
                    #     window.fill(BLACK)
                    #     display_Title("Main Menu", 70)
                    #     display_Menu(MenuMessages)
                    #     py.display.update()
                    #     currentDisplay==DISPLAY_MAIN_MENU


                # mouse_pos=py.mouse.get_pos()
                # if currentDisplay==DISPLAY_MAIN_MENU and mouse_pos[0] >= 70 and mouse_pos[0] <= 95 and mouse_pos[1]>=350 and mouse_pos[1]<=425:
                #     window.fill(BLACK)
                #     display_Title("Scoreboard", 70)
                #     py.display.update
                
            # #70, 513, 91, 515, 93, 531, 71, 535

            #70, 510, 95, 455
            # elif currentDisplay== DISPLAY_MAIN_MENU:   
            #     if mouse_pos[0] >= 390 and mouse_pos[0] <= 335 and mouse_pos[1]>=450 and mouse_pos[1]<=800:
            #         window.fill(BLACK)
            #         display_Title("Main Menu", 20)
            #         display_Menu()
            #         py.display.update()
            #         currentDisplay==DISPLAY_MAIN_MENU
        #google images for game characters 64 x 64
py.quit()
     
        
#jump=false
#jump=true

# xmove, ymove



#create main menu with levels with rectangles, settings, instructions, 

#Instructions
# Level 1
# #level 2
#Scoreboard
#Settings
#Exit




#if mouse_pos[0]>=75 and mouse_pos[0]<=260 and mouse_pos[1]>=95 and mouse_pos[1]<=300:




#if counter==0:
# display_Title("SETTINGS", WIDTH/2-text.get_width()/2, 170)
        # display_message2("Background Color")
        # display_message3("Object Color")
        # display_message4("Sound=On/Off")
        # display_message5("Screen Size")
        # py.time.delay(300)
        # py.display.update()
        # counter+=1
#print the rest of your menu for settings
# 
# Windows
# Background Color
# Objet COlors
# Sound= on/off
# for (display_message (x,y)) 
#for (i in range)
