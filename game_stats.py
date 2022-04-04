import pygame
from settings import Settings
from player import Player

class GameStats:
	"""Track statisitcs for Defender"""

	def __init__(self):
		"""Initializes statistics"""
		self.settings = Settings()
		self.reset_stats()

	def reset_stats(self):
		"""Initialize statistics that can change during the game"""
		self.players_left = self.settings.player_limit