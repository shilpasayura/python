import pygame

# Initialise pygame
pygame.init()

# Set window size
size = width,height = 600, 600
screen = pygame.display.set_mode(size)

# Clock
clock = pygame.time.Clock()

# Load image
image = pygame.image.load('ball.png')

# Set the size for the image
DEFAULT_IMAGE_SIZE = (50, 50)

# Scale the image to your needed size
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

# Rotate the image by any degree
#image = pygame.transform.rotate(image, 90)

# Set a default position
DEFAULT_IMAGE_POSITION = (0,0)

# Prepare loop condition
running = True

# Event loop
while running:

	# Close window event
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Background Color
	screen.fill((0, 0, 0))
	image = pygame.transform.rotate(image, 5)
        
	# Show the image
	screen.blit(image, DEFAULT_IMAGE_POSITION)


	'''
        display.flip() updates the entire display
        display.update() allows to update a portion of the screen
        if no arguments passed, updates the entire display
        '''
	# Part of event loop
	pygame.display.flip()
	clock.tick(30)
