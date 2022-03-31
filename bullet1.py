import pygame 
from pygame.sprite import Sprite
import math 

from player import Player
from settings import Settings

class Bullet(Sprite):
	"""A class to manage bullets fired from player"""

	def __init__(self, df_game):
		"""Create a bullet object at player position"""
		super().__init__()
		self.screen = df_game.screen 
		self.settings = df_game.settings

		#Load bullet image 
		self.imageload = pygame.image.load('bullet.png')
		self.imagescale = pygame.transform.imageload(self.imageload,
			10, 10)
		self.rect = self.imagescale.get_rect()

		#Get rect for bullet
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		#Bullet position origin 
		self.origin = df_game.player.rect.midbottom

		#Set bullet location equal to player location 
		self.x = df_game.player.rect.x + 35
		self.y = df_game.player.rect.y + 35

		#Get mouse x and y 
		mouse_x, mouse_y = pygame.mouse.get_pos()
		self.mouse_x = mouse_x
		self.mouse_y = mouse_y

		#Bullet trajectory settings 
		self.speed = 15
		self.angle = math.atan2(mouse_y - self.y, mouse_x -self.x)
		self.x_vel = math.cos(self.angle) * self.speed
		self.y_vel = math.sin(self.angle) * self.speed

	def update(self):
		#Update bullet position 
		self.rect.x += int(self.x_vel)
		self.rect.y += int(self.y_vel)

	def draw_bullet(self):
		#Draw bullet on screen 
		self.screen.blit(self.imagescale, self.rect)

