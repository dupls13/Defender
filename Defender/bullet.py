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
		self.imagescale = pygame.transform.scale(self.imageload, (20,20))
		self.rect = self.imagescale.get_rect()

		#Set bullet initial location 
		self.rect.midtop = df_game.player.rect.midtop


		#Get rect for bullet
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		#Get mouse x and y 
		mouse_x, mouse_y = pygame.mouse.get_pos()
		self.mouse_x = mouse_x
		self.mouse_y = mouse_y

		#Bullet trajectory settings 
		self.speed = 15
		self.angle = math.atan2(mouse_y - self.y, mouse_x -self.x)
		self.x_vel = math.cos(self.angle) * self.speed
		self.y_vel = math.sin(self.angle) * self.speed

		#Set direction of bullet image towards mouse
		self.rotimage = pygame.transform.rotate(self.imagescale, -math.degrees(self.angle) + 270)
		self.rect = self.rotimage.get_rect()


	def update(self):
		#Update bullet position  

		self.x += int(self.x_vel)
		self.y += int(self.y_vel)

		self.rect.x = self.x 
		self.rect.y = self.y 



	def draw_bullet(self):
		#Draw bullet on screen 
		self.screen.blit(self.rotimage, self.rect)

