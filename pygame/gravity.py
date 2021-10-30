import pygame
pygame.init()
screen_width=800
screen_height=600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Jump Game")

x = 50
y = 50
width = 40
height = 40
vel = 5
g=5

isJump = False
jumpCount = 10

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if not(isJump): 
        if keys[pygame.K_SPACE]:
            isJump = True
        if keys[pygame.K_LEFT]: 
            x -= vel
        if keys[pygame.K_RIGHT]:  
            x += vel
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        else:
            y +=g
    else:
        if jumpCount >= 0:
            y -= jumpCount 
            jumpCount -= 1
        else: 
            jumpCount = 20
            isJump = False
    
    if y < g*1.5:
        y=screen_height
        
    if y > screen_height:
        y=0
        
    if x > screen_width:
        x=0

    if x < 0:
        x=screen_width

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), (x, y, width, height))  

    
    pygame.display.update() 
    
pygame.quit()
