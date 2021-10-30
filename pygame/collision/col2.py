import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
rect1 = pygame.Rect(100, 100, 100, 100)
rect2 = pygame.Rect(0, 0, 75, 75)
green=(0, 255, 0)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    rect2.center = pygame.mouse.get_pos()
    collide = rect1.colliderect(rect2)
    if collide:        
        color = (255, 0, 0)
    else:
        color= (255, 255, 255)
        

    window.fill(0)
    pygame.draw.rect(window, color, rect1)
    pygame.draw.rect(window, green, rect2)
    pygame.display.flip()

pygame.quit()
exit()
