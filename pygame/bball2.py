import pygame as pg


class Ball(pg.sprite.Sprite):

    def __init__(self, pos):
        super(Ball, self).__init__()
        self.image = pg.image.load('ball.png')
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.velocity = [1, 1]

    def update(self):
        self.rect.move_ip(self.velocity)
       
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.velocity[0] = -self.velocity[0]
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.velocity[1] = -self.velocity[1]

        

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Initialise pygame
pg.init()
clock = pg.time.Clock()

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Create sprites
ball = Ball((100, 200))
ball1 = Ball((200, 100))

group = pg.sprite.RenderPlain()
group.add(ball)
group.add(ball1)

# Main loop, run until window closed
running = True
while running:

    # Check events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    group.update()
    group.draw(screen)
    pg.display.flip()

    #clock.tick(30)

# close pygame
pg.quit()
