#William Maher
#10/15/21
#Learning display
#  opening windows
# changing size window
#  basic game loop
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow 
# K_LEFT                left arrow

import pygame,os
import random

from pygame.constants import CONTROLLER_AXIS_INVALID
from pygame.display import update

from pygame.mouse import get_pressed
#first thing to do is initialize pygame
pygame.init()

check=True
width2=600
height2=700
colors= {'purple':(150,0,150), 'pink':(200,0,200), 'cyan':(0,255,255), 'yellow':(255,255,50),'orange':(255,150,0) } 
colorName= ("purple", "pink", "cyan", "yellow", "orange")

#base colors, green=0,255,0 blue=0,0,255 red=25,0,0

randColor=random.choice(colorName)

# while check:
    # height=input("Height of the window: (100 - 1000): ")
    # width = input("Width of the window: (100-1000): ")
     #another way to do this is color=random.choice(list(colors.keys)), this is quicker but closes the list so 
     #color=input("what color do you prefer? purple, pink, cyan, yellow, or orange? : ")                        100
    
def moveRect():
    window.fill('purple')
    pygame.draw.circle(window,'orange', (xc,yc), radius)
    pygame.display.flip()
    pygame.draw.rect(window,color,rect) 
    pygame.display.flip()


    
     # try:
    #     height=int(height)
    #     width=int(width)
    #     check=False

    # except ValueError:
    #     print("sorry")
    #     check=True


    
        
color=colors.get('cyan')

window=pygame.display.set_mode((height2,width2))
window.fill(('purple')) #RGB- colors in comp sci are either Red, Green or Blue, or a combination of them. red=255, FF green=255,FF blue=255, FF, 
# combination could be 100,120,255(EF)
pygame.display.flip() # refresh window with new color
pygame.display.set_caption("My Game Window")
pygame.display.flip()
hbox=50
wbox=50
xc=random.randint(25,width2-wbox)
yc=random.randint(25,height2-hbox)
radius=wbox/2
speed=5
pygame.draw.circle(window, 'orange',(xc,yc),radius)

rect=pygame.Rect(width2/2, height2/2, wbox, hbox)
pygame.draw.rect(window,color,rect)
pygame.display.flip()

run=True
counter=0
circle=(window,'orange',(xc,yc), radius)
#main loop for the game:
while run:
    pygame.time.delay(20)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run= False
    rectPos=rect.x,rect.y
    circlePos=xc,yc


    #how to get position of mouse
    # x,y=pygame.mouse.get_pos()
    # print("(" + str(x) + " , " + str(y)+ ")")
    keyPressed=pygame.key.get_pressed()
    if keyPressed[pygame.K_UP]: #and rect.y-speed>=0
        rect.y -= speed
        moveRect()
    if keyPressed[pygame.K_DOWN]: #and (rect.y+hbox+speed)<=height
        rect.y +=speed
        moveRect()
    if keyPressed[pygame.K_LEFT]: #and rect.x-speed>=0:
        rect.x -=speed
        moveRect()
    if keyPressed[pygame.K_RIGHT]: #and (rect.x+wbox+speed)<=width: 
        rect.x +=speed  
        moveRect()

    if keyPressed[pygame.K_a] and xc-speed>=25:
        xc -= speed
        moveRect()
    if keyPressed[pygame.K_d] and xc<=470:
        xc +=speed
        moveRect()
    if keyPressed[pygame.K_w] and yc>=25:
        yc -=speed
        moveRect()
    if keyPressed[pygame.K_s]and yc<=470: 
        yc +=speed
        moveRect()

    if rect.y>height2:
        rect.y=0
    if rect.y<0:
        rect.y=height2
    if rect.x>width2:
        rect.x=0
    if rect.x<0:
        rect.x=width2

    
    if pygame.Rect.collidepoint(rect,(xc,yc)):
        radius+=radius/2
        rect.x=random.randint(10,width2-wbox)
        rect.y=random.randint(10,height2-hbox)
        counter+=1
    if counter==3:
        run=False
    pygame.draw.circle(window, 'orange',(xc,yc),radius)
    pygame.draw.rect(window,color,rect)
    pygame.display.flip()


pygame.quit()


#need x, y, w, h to defin circle
#x, y- center, W, h- radius
# y=wbox/2
#ball=pygame.draw.circle
#xc=wbox
#yc=hbox
#when circle touches square, circle grows
#gets smaller 
#if square hits here 
#xc=25
#yc=25
#ball=pygame.circle(x=widht/2, y=width/2)
#

#possible ideas:
#if position is hte same, no longer draw circle, create a new one in a random area
#make variable for x position of both shapes, and variable for their y postions
#rect pos= x and y , ciclepos= x, and y
#Draw a rectangle:
#     Move your rectangle up, down, left, right using arrow keys
#     make sure your rectangle goes over your screen when it reaches the border 
# Draw a circle:
#     Move your circle up, down, left, right using w,s,d, a keys
#     make sure your circle stops when it reaches the border 
# When both objects are moving, as the circle touches the rectangle it should eat it! (Rect disappear and circle should increase its size (wbox at the time)
# create another rectangle in another random part of the sccreen.
# Decide when the game should be over!

#rect pos= rect X and rect Y
#circle pos= circle X and cicle Y
#if circle pos=rect pos:



#HW- CIRCLE BORDERSSSS
