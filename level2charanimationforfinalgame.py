import pygame as py
py.init()

window = py.display.set_mode((800,800))
py.display.set_caption("First Game")
windowRect = window.get_rect()

walkRight = [py.image.load('Game\R1.png'), py.image.load('Game\R2.png'), py.image.load('Game\R3.png'), py.image.load('Game\R4.png'), py.image.load('Game\R5.png'), py.image.load('Game\R6.png'), py.image.load('Game\R7.png'), py.image.load('Game\R8.png'), py.image.load('Game\R9.png')]
walkLeft = [py.image.load('Game\L1.png'), py.image.load('Game\L2.png'), py.image.load('Game\L3.png'), py.image.load('Game\L4.png'), py.image.load('Game\L5.png'), py.image.load('Game\L6.png'), py.image.load('Game\L7.png'), py.image.load('Game\L8.png'), py.image.load('Game\L9.png')]
bg = py.image.load('gameimages\lightgraybkg.jpg')
char = py.image.load('Game\standing.png')
stonewall=py.image.load('gameimages\stone_wall_for_maze_game-removebg-preview.png')
stonewallup=py.image.load('gameimages\stonewallformazegameup2.png')
star=py.image.load('gameimages\pixelated_star_for_game50removedbkg - Copy.png')
finish= py.image.load('gameimages\endofmazegame100x100.png')



            
# Bush1 = py.Rect(23, 158, -97, windowRect.height-496)
# Bush2 = py.Rect(125, 458, 174-125, windowRect.height-458)
# Bush3 = py.Rect(232, 372, 308-232, windowRect.height-372)
# Bush4 = py.Rect(175, 250, 231-175, windowRect.height-250)


x = 0
y = 0
width = 40
height = 60
vel = 5

clock = py.time.Clock()


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
    window.blit(stonewall,(236,147))
    

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
    


check=True

while check:
    clock.tick(27)

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
            mouse_pos=(0,0)

        if event.type==py.MOUSEBUTTONDOWN:
            mouse_pressed=py.mouse.get_pressed()
            if mouse_pressed[0]:
                mouse_pos=py.mouse.get_pos()
                print(py.mouse.get_pos())

    keys = py.key.get_pressed()
    
    if keys[py.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False

    elif keys[py.K_RIGHT] and x < 800 - vel - width:  
        x += vel
        left = False
        right = True
    
    elif keys[py.K_DOWN] and y<800 - vel - width:
        y+=vel
   
    elif keys[py.K_UP] and y>vel:
        y-=vel
    else: 
        left = False
        right = False
        walkCount = 0
        
    redrawGameWindow() 
    
    
py.quit()