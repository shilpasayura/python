import pygame

background_color = [60, 60, 60]
width = 640
height = 480
pos=(100,100)

pygame.init()
pygame.display.set_caption('Mario Rotation')
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)

img = pygame.image.load('maryo.png')
img_original = pygame.transform.scale(img, (36, 72))

rect = img_original.get_rect()
rect.center = (width // 2, height // 2)
angle = 0
running = True
da=5
dx=3
dy=5
screen.blit(img_original, pos)

clock = pygame.time.Clock()

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if (event.type == pygame.KEYUP):
            if event.key == pygame.K_LEFT:
                da= -1
            elif event.key == pygame.K_RIGHT:
                da= 1

    angle = (angle+ da) % 360
            
    image = pygame.transform.rotate(img_original, angle)

    rect.x += dx
    rect.y += dy
    if rect.x > width:
        dx=dx*-1
    elif rect.x < 0:
        dx=dx*-1
        
    if rect.y > height:
        dy=dy*-1
    elif rect.y < 0:
        dy=dy*-1
    
        
    center = rect.center
    rect = image.get_rect()
    rect.center = center
    screen.fill(background_color)
    screen.blit(image, rect)
    pygame.display.flip()
    
pygame.quit()
