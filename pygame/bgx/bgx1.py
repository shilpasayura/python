import pygame 
pygame.init()   

window_width=700
window_height=400

player_width=50
player_height=50

animation_increment=10
clock_tick_rate=20
BLACK = (0, 0, 0)
FPS=30

size = (window_width, window_height)
screen = pygame.display.set_mode(size)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
	
        # create a plain rectangle for the sprite image
        self.image = pygame.Surface((player_width,player_height))
        self.image.fill(BLACK)
        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        # center the sprite on the screen
        self.rect.center = (window_width/2,275)

    def update(self):
        self.rect.x += 5
        if self.rect.left > window_width:
            self.rect.right = 0
            self.rect.x =-player_width

        if self.rect.right < 0:
            self.rect.left = window_width
            self.rect.x =window_width
            
    
pygame.display.set_caption("Hello Bg") 
run = True


clock = pygame.time.Clock()
background_image = pygame.image.load("bg0.jpg").convert()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

while run:  
     # keep loop running at the right speed
    clock.tick(FPS)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
    #keys
            
    all_sprites.update()
    screen.blit(background_image, [0, 0])
    all_sprites.draw(screen)
    # Update
    
    pygame.display.update() 

pygame.quit()


