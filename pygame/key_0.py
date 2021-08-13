
import pygame  
pygame.init()  
# sets the window title  
pygame.display.set_mode((400, 400))  
  
while True:  
    # gets an event from the event queue  
    event = pygame.event.wait()  
    # if the 'close' button of the window is pressed  
    if event.type == pygame.QUIT:  
        # stops the application  
        break  

    # Detects the 'KEYDOWN' and 'KEYUP' events  
    if event.type in (pygame.KEYDOWN, pygame.KEYUP):  
        # gets the key name  
        key_name = pygame.key.name(event.key)  
        # converts to uppercase the key name  
        key_name = key_name.upper()  
        # if any key is pressed  
        if event.type == pygame.KEYDOWN:  
         
            print(u'"{}" key pressed'.format(key_name))
 
        # if any key is released  
        elif event.type == pygame.KEYUP:  
             
            print(u'"{}" key released'.format(key_name)) 
