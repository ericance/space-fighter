import pygame, os, time, random
pygame.font.init()

# Window
WIDTH, HEIGHT = 700, 750 
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# Ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Lasers

RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

class Ship:
	def __init__(self, x, y, health=100):
		self.x = x
		self.y = y
		self.health = health
		self.ship_img = None
		self.laser_img = None
		self.lasers = []
		self.cool_down_counter = 0

	def draw(self, window):
		window.blit(self.ship_img, (self.x, self.y))

	def get_width(self):
		return self.ship_img.get_width()
	
	def get_height(self):
		return self.ship_img.get_height()

class Player(Ship):
	def __init__(self, x, y, health=100):
		super().__init__(x, y, health)
		self.ship_img = YELLOW_SPACE_SHIP
		self.laser_img = YELLOW_LASER
		self.mask = pygame.mask.from_surface(self.ship_img)
		self.max_health = health

class Enemy(Ship):
	COLOR_MAP = {
		'red': (RED_SPACE_SHIP, RED_LASER),
		'green': (GREEN_SPACE_SHIP, GREEN_LASER),
		'blue': (BLUE_SPACE_SHIP, BLUE_LASER)
	}

	def __init__(self, x, y, color, health=100):
		super().__init__(x, y, health)
		self.ship_img, self.laser_img = self.COLOR_MAP[color]
		self.mask = pygame.mask.from_surface(self.ship_img)
	
	def move(self, vel):
		self.y += vel

def main():
	FPS = 60

	run = True
	level = 0
	lives = 3

	main_font = pygame.font.SysFont("Roboto", 50)

	enemies = []
	wave_length = 5
	enemy_val = 1
	player_vel = 5
	player = Player(300, 650)

	def redraw_window():
		WINDOW.blit(BACKGROUND, (0,0))
		# draw text
		lives_label = main_font.render(f'Lives: {lives}', 1, (255, 255, 255))
		level_label = main_font.render(f'Level: {level}', 1, (255, 255, 255))
		WINDOW.blit(lives_label, (10, 10))
		WINDOW.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

		for enemy in enemies:
			enemy.draw(WINDOW)

		player.draw(WINDOW)

		for enemy in enemies:
			enemy.draw(WINDOW)

		pygame.display.update()

	while run:
		pygame.time.Clock().tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a] and player.x - player_vel > 0: # left
			player.x -= player_vel
		if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # right 
			player.x += player_vel
		if keys[pygame.K_w] and player.y - player_vel > 0: # up 
			player.y -= player_vel
		if keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT: # down 
			player.y += player_vel

		redraw_window()


main()




