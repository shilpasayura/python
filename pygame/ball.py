import pygame

WIDTH = 800
HEIGHT = 600
BACKGROUND = (255, 255, 255)
dir=0;

class Ball:
    def __init__(self):
        self.image = pygame.image.load("soccer_ball.png")
        self.rect = self.image.get_rect()
        #w, h = pygame.display.get_surface().get_size()
        self.rect.x=0 #w/2
        self.rect.y=0 # h/2
        
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    ball = Ball()

    while True:
        screen.fill(BACKGROUND)
        screen.blit(ball.image, ball.rect)
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
