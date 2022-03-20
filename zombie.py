import pygame
import random
from pygame.sprite import Sprite 
from settings import Settings

class Zombie(Sprite):
	"""A class to initialize a single zombie"""
	def __init__(self, df_game):
		super().__init__()
		self.settings = Settings()
		self.screen = df_game.screen 

		#Load the image
		self.zombieload = pygame.image.load('zombie.png')
		self.zombiescale = pygame.transform.scale(self.zombieload, (70,50))
		self.image = pygame.transform.rotate(self.zombiescale, 270)
		self.rect = self.image.get_rect()


		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		#Sets image at random x 
		self.rect.x = random.randint(10, self.settings.SCREEN_WIDTH - 10)
		self.rect.y = 0

		#Random speed of zombie
		self.speed = random.randint(1, 5)

	def update(self):
		#Movement of zombie going down screen
		self.rect.y += self.speed

	def draw(self):
		self.screen.blit(self.image, self.rect)
