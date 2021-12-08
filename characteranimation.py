#  def charanimation():
#     x=0
#y=0
import pygame as py

clock = pygame.time.Clock()

while check:
    clock.tick(27)
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    keys = py.key.get_pressed()
    if keys[py.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False
    elif keys[py.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        left = False
        right = True
    elif keys[py.K_UP] and y<500 - vel - width:
        y+=vel
    elif keys[py.K_DOWN] and y>vel:
        y-=vel
    else: 
        left = False
        right = False
        walkCount = 0
redrawGameWindow()
