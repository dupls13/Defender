import pygame

class Settings:
	"""A class to store all the settings for Defender"""

	def __init__(self):
		"""Initialize game settings"""
		#Screen settings

		self.SCREEN_WIDTH = 1200
		self.SCREEN_HEIGHT = 800
		self.BG_COLOR = (255, 255, 255)
		pygame.display.set_caption("Defender")



