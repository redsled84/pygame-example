import pygame

pygame.init()

DIMENSIONS = (600, 480)
SCREEN = pygame.display.set_mode(DIMENSIONS)
CLOCK = pygame.time.Clock()
TARGET_FPS=60

pygame.display.set_caption('Simple Game')

is_running = True

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

tile_size = 24
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

while is_running:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			changeKeys(event.key, True)
			if event.key == pygame.K_ESCAPE:
				is_running = False
		if event.type == pygame.KEYUP:
			changeKeys(event.key, False)
		if event.type == pygame.QUIT:
			is_running = False

	SCREEN.fill((255,255,255))

	# Draw here
	pygame.draw.rect(SCREEN, (255,0,0), (player[0], player[1], \
		tile_size, tile_size))

	pygame.display.update()

	movement()

	CLOCK.tick(TARGET_FPS)

pygame.quit()