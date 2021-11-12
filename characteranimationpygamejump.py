import os
import pygame as py
from pygame import event
from pygame.constants import K_SPACE
WIDTH=800
HEIGHT=800
left = False
right = False
walkCount = 0

# walkRight = [py.image.load('R1.png'), py.image.load('R2.png'), py.image.load('R3.png'), py.image.load('R4.png'), py.image.load('R5.png'), py.image.load('R6.png'), py.image.load('R7.png'), py.image.load('R8.png'), py.image.load('R9.png')]
# walkLeft = [py.image.load('L1.png'), py.image.load('L2.png'), py.image.load('L3.png'), py.image.load('L4.png'), py.image.load('L5.png'), py.image.load('L6.png'), py.image.load('L7.png'), py.image.load('L8.png'), py.image.load('L9.png')]
# bg = py.image.load('bg.jpg')
# char = py.image.load('standing.png')

boulder=py.Rect(WIDTH-300, HEIGHT-200, 100, 200)

#first thing
py.init()
 
#create window
height= 700
width = 800
colors = {'red':(150,0,0),'green':(0,200,0), 'blue':(0,0,255), 'purple':(150, 0, 150), 'white':(255,255,255), 'black':(0,0,0) }
screen=py.display.set_mode((width, height))
myColor= colors.get('purple')
screen.fill(myColor)
py.display.set_caption("Moving Square")
py.display.flip()
#parameters to define our square
x=width/2
y=height/2
wbox=50
hbox=50
bg=py.image.load("gameimages//bgSmaller.jpg")
# FIG=py.image.load('images//')
py.display.set_caption('MY SHAPES')
py.display.flip()
py.time.delay(100)
# screen.blit(figx, figy)
#creating out object square
square=py.Rect(x,y,wbox, hbox )
#draw object
objColor=colors.get('red')
boulderColor=colors.get('blue')
py.draw.rect(screen, objColor, square)
py.draw.rect(screen, boulderColor, boulder)
py.display.update()
#create speed to move the object on the screen
speed = 10
run=True #Variable to control the main loop
#boolean to check for jump
move=True
Jumping=False
jumpCount=10
while run:

    py.time.delay(100) #milliseconds
    for anyThing in py.event.get():
        if anyThing.type == py.QUIT:
            run =False
    keyPressed= py.key.get_pressed()
    # if square.y <HEIGHT-200-hbox:
    if keyPressed[py.K_RIGHT] and square.x <WIDTH-wbox-speed and move:
        if square.colliderect(boulder):
            square.x-=5
        else:
            square.x += speed
    if keyPressed[py.K_LEFT] and square.x>speed:
            square.x -= speed
    
    elif square.x <=boulder.x-wbox-5:
        if keyPressed[py.K_RIGHT]:
            square.x+=speed
    

       
    if not(Jumping):
        if keyPressed[py.K_DOWN] and square.y >speed:
            square.y += speed
        if keyPressed[py.K_UP] and square.y>speed:
                square.y-=5

            # figx+=speed
        if keyPressed[py.K_SPACE]:
            Jumping=True
    
    else:
        if jumpCount >=-10:
            square.y -= jumpCount*abs(jumpCount)*0.5
            jumpCount-=1
        else:
            jumpCount=10
            Jumping=False
    if(py.Rect.collidepoint(boulder, (square.x+wbox/2, square.y))):
        move=False
        square.x=square.x-wbox
        move=True

    screen.blit(bg,(0,0))
    py.draw.rect(screen, objColor, square)
    py.draw.rect(screen, boulderColor, boulder)
    py.display.flip()
py.quit()


#for pictures, 64 x 64, get find a picture with no background
#500-525, 600