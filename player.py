import pygame 
from settings import Settings

class Player:
	"""A class to manage the player"""

	def __init__(self, df_game):

		self.settings = df_game.settings

		"""Initializes the player and set its starting position"""
		self.screen = df_game.screen 
		self.screen_rect = df_game.screen.get_rect()

		#Load the player image and get rect
		PLAYER_WIDTH, PLAYER_HEIGHT = (70, 50)
		self.imageload = pygame.image.load('player.png')
		self.image = pygame.transform.scale(self.imageload, (PLAYER_WIDTH, PLAYER_HEIGHT))
		self.rect = self.image.get_rect()

		#Player initial position 
		self.rect.midbottom = self.screen_rect.midbottom 

		#Decimal value for player horizontal and vertical position 
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		#Movement flag
		self.moving_left = False
		self.moving_right = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update player position based on movement flag"""
		if self.moving_left and self.rect.left > 0 :
			self.rect.x -= 5 
		if self.moving_right and self.rect.right < self.settings.SCREEN_WIDTH:
			self.rect.x += 5
		if self.moving_up and self.rect.top > 0:
			self.rect.y -= 5
		if self.moving_down and self.rect.bottom < self.settings.SCREEN_HEIGHT:
			self.rect.y += 5

	def blitme(self):
		"""Draw the player at the current location"""
		self.screen.blit(self.image, self.rect)
