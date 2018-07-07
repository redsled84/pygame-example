# Description: A small game where you grab "food", eat or die
# Author: Lucas Black
import pygame, random

# Initialize pygame setup
pygame.init()

# Some global variables
DIMENSIONS = (600, 480)
SCREEN     = pygame.display.set_mode(DIMENSIONS)
CLOCK      = pygame.time.Clock()
TARGET_FPS = 60
is_running = True

pygame.display.set_caption('Simple Demo | Press \'Esc\' to close')

# Dictionary for key input detection
KEYS = {
	"d": False,
	"a": False,
	"s": False,
	"w": False,
}

def changeKeys(key, value):
	if key == pygame.K_d:
		KEYS['d'] = value
	if key == pygame.K_a:
		KEYS['a'] = value
	if key == pygame.K_s:
		KEYS['s'] = value
	if key == pygame.K_w:
		KEYS['w'] = value

# Width and height of player and food
tile_size = 24
# Player position
player = [0, 0]
speed = 5

def movement():
	if KEYS['d']:
		player[0] += speed
	elif KEYS['a']:
		player[0] -= speed
	if KEYS['s']:
		player[1] += speed
	if KEYS['w']:
		player[1] -= speed

# Food position
food = [random.randint(0, DIMENSIONS[0] - tile_size), \
	random.randint(0, DIMENSIONS[1] - tile_size)]

def updateEvents(event):
	global is_running
	if event.type == pygame.KEYDOWN:
		changeKeys(event.key, True)

		if event.key == pygame.K_ESCAPE:
			is_running = False
	if event.type == pygame.KEYUP:
		changeKeys(event.key, False)
	if event.type == pygame.QUIT:
		is_running = False

def updatePlayerFoodCollision():
	# AABB collision detection
	if food[0] < player[0] + tile_size and \
	food[0] + tile_size > player[0] and \
	food[1] < player[1] + tile_size and \
	food[1] + tile_size > player[1]:
		# Reset the food's position to another random pos
		food[0] = random.randint(0, DIMENSIONS[0] - tile_size)
		food[1] = random.randint(0, DIMENSIONS[1] - tile_size)

while is_running:
	for event in pygame.event.get():
		updateEvents(event)

	updatePlayerFoodCollision()

	# Fill white to draw over the previous frame's drawing updates
	SCREEN.fill((255,255,255)) # Comment this line to get a drawing program effect

	pygame.draw.rect(SCREEN, (255,0,0), (player[0], player[1], \
		tile_size, tile_size))
	pygame.draw.rect(SCREEN, (200,200,0), (food[0], food[1], \
		tile_size, tile_size))

	pygame.display.update()

	# Update player position
	movement()

	# Move onto the next frame
	CLOCK.tick(TARGET_FPS)

# Terminate pygame setup
pygame.quit()
