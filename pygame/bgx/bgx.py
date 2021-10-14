import pygame
pygame.init()

window_width=700
window_height=400

animation_increment=10
clock_tick_rate=20

size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("Hello Sea")

running =True

clock = pygame.time.Clock()
background_image = pygame.image.load("bg0.jpg").convert()
bg_num=0
x=0
y=0
while(running==True):

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False

   
    screen.blit(background_image, [0, 0])

    #pygame.draw.rect(window, (255, 255, 255), (x, y, width, height)) 
    #pygame.display.update()
    pygame.display.flip()
    clock.tick(clock_tick_rate)

pygame.quit()  


      
    
    
    

