import pygame
pygame.init()
screen_width=800
screen_height=600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Jump Game")

x = 50
y = 50
pw = 40
ph = 40
vel = 5
g=5
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK=(0,0,0)

platforms=[]
platforms.append(7)
platforms.append(9)
platforms.append(11)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((pw,ph))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def update(self):
        self.rect.x=x
        self.rect.y=y
        

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    
isJump = False
jumpCount = 10

platform_group = pygame.sprite.Group()

player = Player()
platform_group.add(player)

lx=50
ly=250
platforms[0]=Platform(lx, ly, 100, 20)
platforms[1]=Platform(lx+150, ly+150, 150, 20)
platforms[2]=Platform(lx+250, ly+250, 250, 20)
platforms.append(Platform(lx+500, ly+130, 100, 20))
platforms.append(Platform(lx+700, ly+70, 100, 20))

platform_group.add(platforms)


run = True


while run:
    pygame.time.delay(100)
    
    platform_hit=False
    #If remove set to True, all colliding sprites removed from the group.
    remove=False 
    hits = pygame.sprite.spritecollide(player, platforms, remove)
    #print(hits)
    
    if hits:
       platform_hit=True
        
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
            if not(platform_hit):
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
        y=5
        
    if x > screen_width:
        x=0

    if x < 0:
        x=screen_width

    
    #pygame.draw.rect(screen, (255,0,0), (x, y, width, height))  
    #player.update()

    
    platform_group.update()
    
    
    screen.fill(BLACK)
    platform_group.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

    pygame.display.update() 
    
pygame.quit()

