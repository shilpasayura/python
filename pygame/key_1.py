import pygame  
  
pygame.init()  
screen = pygame.display.set_mode((400, 300))  
done = False  
is_blue = True  
x = 30  
y = 30  
  
while not done:
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  
            is_blue = not is_blue
        

    key=""
    pressed = pygame.key.get_pressed()  
        
    if pressed[pygame.K_UP]:
        y =y- 3
        key="UP"
    if pressed[pygame.K_DOWN]:
        y =y+ 3
        key="DOWN"
    if pressed[pygame.K_LEFT]:
        x = x-3
        key="LEFT"
    if pressed[pygame.K_RIGHT]:
        x = x+ 3
        key="RIGHT"
  
    if is_blue:  
        color = (0, 128, 255)  
    else:   
        color = (255, 100, 0)  

    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))  
    print(key)
    pygame.display.flip()  

