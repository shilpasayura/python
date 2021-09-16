import pygame
import random

WIDTH = 800
HEIGHT = 600
BACKGROUND = (0, 0, 0)

class Ball:
    def __init__(self):
        self.image = pygame.image.load("soccer_ball.png")
        self.speed = [random.uniform(-4,4), 2]
        self.rect = self.image.get_rect()

    def update(self):
        if self.rect.top < 0:
            self.speed[1] = -self.speed[1]
            self.speed[0] = random.uniform(-4, 4)
        elif self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed[0] = -self.speed[0]
        self.move()

    def move(self):
        self.rect = self.rect.move(self.speed)

def main():
    clock = pygame.time.Clock()
    ball = Ball()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ball.rect.collidepoint(pygame.mouse.get_pos()):
                    ball.speed[0] = random.uniform(-4, 4)
                    ball.speed[1] = -2
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
				
        screen.fill(BACKGROUND)
        screen.blit(ball.image, ball.rect)
        ball.update()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
