import pygame

def enemie():
    global speed_x
    ball.rect.y += speed_x
    if ball.rect.colliderect(player.rect):
        player.kill()

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# ball sprite
ball = pygame.sprite.Sprite()
ball.rect = pygame.Rect(250, 0, 20, 20)
ball.image = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(ball.image, (255, 0, 0), (10, 10), 10)
speed_x = 2

# player sprite
player = pygame.sprite.Sprite()
player.rect = pygame.Rect(250, 450, 50, 50)
player.image = pygame.Surface((50, 50), pygame.SRCALPHA)
pygame.draw.circle(player.image, (0, 0, 255), (25, 25), 25)

# group with all sprites
group = pygame.sprite.Group()
group.add(ball)
group.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
    enemie()

    screen.fill((255, 255, 255)) #color
    group.draw(screen)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
