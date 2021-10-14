import pygame

pygame.init()
window_width=700
window_height=400

size = (window_width, window_height)
screen = pygame.display.set_mode(size)


background_images=["bg0.jpg", "bg1.jpg", "bg2.jpg", "bg3.jpg"]
bgx=[]
for i in range(4):
    bg="bg"+str(i)+ ".jpg"
    bgx.append(pygame.image.load("bg0.jpg").convert())
    #bgx.append(pygame.image.load(background_images[i]).convert()
    

print(bgx)


