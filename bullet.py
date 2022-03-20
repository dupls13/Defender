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

		#Sets bullet location equal to player location 
		self.x = df_game.player.rect.x + 35
		self.y = df_game.player.rect.y + 35

		self.settings = df_game.settings

		#Bullet position origin
		self.origin = df_game.player.rect.midbottom 


		#Store bullet x and y position 
		self.x = float(self.x)
		self.y = float(self.y)

		#Get mouse x and y 
		mouse_x, mouse_y = pygame.mouse.get_pos()
		self.mouse_x = mouse_x
		self.mouse_y = mouse_y 

		#Bullet Settings
		self.lifetime = 50
		self.speed = 15
		self.angle = math.atan2(mouse_y - self.y, mouse_x - self.x )
		self.x_vel = math.cos(self.angle) * self.speed
		self.y_vel = math.sin(self.angle) * self.speed
		self.radius = 5

	def update(self):
		#Update bullet position 
		self.x += int(self.x_vel)
		self.y += int(self.y_vel)

	def draw_bullet(self):
		#Draw bullet onto screen 
		pygame.draw.circle(self.screen , (0, 0, 0), (self.x, self.y), self.radius)
