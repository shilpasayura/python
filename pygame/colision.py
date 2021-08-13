
import pygame as pg
#vec = pg.math.Vector2

WIDTH = 800
HEIGHT = 600
FPS = 60


RED = (255, 0, 0, 128)
GREEN = (0, 255, 0, 128)
CYAN = (0, 255, 255, 128)
YELLOW = (255, 255, 0)
DARKGRAY=(40, 40, 40)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

enemy = pg.Rect(0, 0, 150, 150)
enemy.center = (WIDTH / 3, HEIGHT / 3)

player = pg.Rect(0, 0, 50, 50)
#Define a Rect value of the surface for m_r
m = pg.Surface((50, 50))#.convert_alpha()
msg = ""

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    player.center = (pg.mouse.get_pos())
    in_x = player.left < enemy.right and player.right > enemy.left
    in_y = player.top < enemy.bottom and player.bottom > enemy.top
    if in_x and in_y:
        # col = RED
        m.fill(RED)
        msg = "Colliding!"
    elif in_x or in_y:
        # col = CYAN
        m.fill(CYAN)
        msg = "Not colliding"
    else:
        # col = GREEN
        m.fill(GREEN)
        msg = "Not colliding"

    screen.fill(DARKGRAY)
    pg.draw.rect(screen, YELLOW, enemy)
    
    #place rectangle (overlap) on  surface on canvas 
    screen.blit(m, player)
    print(msg)
    
    pg.display.flip()
