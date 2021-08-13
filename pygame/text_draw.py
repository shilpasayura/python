
import pygame as pg
#vec = pg.math.Vector2

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0, 128)
GREEN = (0, 255, 0, 128)
CYAN = (0, 255, 255, 128)
YELLOW = (255, 255, 0)


def draw_text(text, size, color, x, y, align="tr"):
    font_name = pg.font.match_font('hack')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    
    
    if (align == "c"):
        text_rect.center = (x, y)
    elif (align == "r"):
        text_rect.midright = (x, y)
    else:
        text_rect.topleft = (x, y)
        
    screen.blit(text_surface, text_rect)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)
draw_text("Hello", 24, WHITE, 100, 100, align="tl")
draw_text("Hello", 36, GREEN, 200, 200, align="c")
draw_text("olleH", 48, RED, 300, 300, align="r")
pg.display.flip()

