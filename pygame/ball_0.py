
import pygame  
pygame.init()  
white = (255, 255, 255)  

h = 400  
w = 400  

#create surface
surface = pygame.display.set_mode((h, w))  
  
# set window name   
pygame.display.set_caption('Image')  
  
# create surface object, image is drawn on it.   
image = pygame.image.load('ball.png')
  
# infinite loop   
while True:  
    surface.fill(white)  
    surface.blit(image, (0, 0))  
  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            pygame.quit()  
            # quit the program.   
            quit() 
 
        # Draws the surface object to the screen.   
        pygame.display.update()   
