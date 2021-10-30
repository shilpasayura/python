import pygame

pygame.init()
window = pygame.display.set_mode((250, 250))
rect = pygame.Rect((100, 100), (50, 50))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    point = pygame.mouse.get_pos()
    #print(point)
    collide = rect.collidepoint(point)
    if collide:        
        color = (255, 0, 0)
    else:
        color= (255, 255, 255)

    window.fill(0)
    pygame.draw.rect(window, color, rect)
    pygame.display.flip()

pygame.quit()

