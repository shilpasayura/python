import pygame

pygame.init()   

window_width=700
window_height=400

BLACK = (0, 0, 0)
FPS=30

size = (window_width, window_height)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("Hello Scrolling Background") 
run = True

clock = pygame.time.Clock()

background_image0 = pygame.image.load("bg0.jpg").convert()
background_image1 = pygame.image.load("bg1.jpg").convert()


dx=5
dy=5
by=0
bx0=0
bx1=window_width

while run:  
     # keep loop running at the right speed
    clock.tick(FPS)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
    #keys

    
    screen.blit(background_image0, [bx0, by])
    screen.blit(background_image1, [bx1, by])
    pygame.display.update() 

    bx0 -=dx
    bx1 -=dx

    if bx0 <=-window_width:
        bx0=700

    if bx1 <=-window_width:
        bx1=700
    
pygame.quit()


