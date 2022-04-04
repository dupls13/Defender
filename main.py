"""Creating a base defender game"""

#Package and file imports 
import sys 
import pygame
from time import sleep

from settings import Settings
from game_stats import GameStats
from player import Player
from bullet import Bullet 
from zombie import Zombie 

clock = pygame.time.Clock()



class Defender:
	"""Overall class to manage game assets and behavior"""

	def __init__(self):
		"""Initialize the game, and create the game resources"""
		pygame.init()

		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))

		self.player = Player(self)
		self.bullets = pygame.sprite.Group()
		self.zombies = pygame.sprite.Group()

		#Create an instance to store game statistics 
		self.stats = GameStats()
		

		#Creates new event for adding zombie in certain time interval 
		self.ADDENEMY = pygame.USEREVENT + 1
		pygame.time.set_timer(self.ADDENEMY, 1000)



	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			#Updates all events
			clock.tick(60)
			self._check_events()
			self.player.update()
			self.bullets.update()
			self.zombies.update()

			#Deletes bullets if reaches edges of screen 
			for bullet in self.bullets.copy():
				if bullet.rect.x <= 0:
					self.bullets.remove(bullet)
				if bullet.rect.x >= self.settings.SCREEN_WIDTH:
					self.bullets.remove(bullet)
				if bullet.rect.y <= 0:
					self.bullets.remove(bullet)
				if bullet.rect.y >= self.settings.SCREEN_HEIGHT:
					self.bullets.remove(bullet)



			print(len(self.bullets))
			print(len(self.zombies))
			self._update_screen()

	def _check_events(self):
		#Respond to button and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()



			#Movement keys
			#Respond to keydown
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					self.player.moving_left = True 
				if event.key == pygame.K_d:
					self.player.moving_right = True
				if event.key == pygame.K_w:
					self.player.moving_up = True
				if event.key == pygame.K_s:
					self.player.moving_down = True

			#Respond to keyup		
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_a:
					self.player.moving_left = False
				if event.key == pygame.K_d:
					self.player.moving_right = False
				if event.key == pygame.K_w:
					self.player.moving_up = False
				if event.key == pygame.K_s:
					self.player.moving_down = False

			#Respond to Mouse down 
			elif event.type == pygame.MOUSEBUTTONDOWN:
				self._fire_bullet()

			#Event for adding zombie 
			elif event.type == self.ADDENEMY:
				zombie = Zombie(self)
				self.zombies.add(zombie)



	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group"""
		self.bullets_allowed = 5
		if len(self.bullets) < self.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)


	def _player_hit(self):
		"""Respond to the player being hit by a zombie"""

		#Decrease players left
		self.stats.players_left -= 1

		#Get rid of any remaining zombies and bullets
		self.zombies.empty()
		self.bullets.empty()

		#Pause
		sleep(0.5)




	def _update_screen(self):
		#Redraw the screen during each pass through the loop 
		self.screen.fill(self.settings.BG_COLOR)
		self.player.blitme()
		for Bullet in self.bullets.sprites():
			Bullet.draw_bullet()
		for Zombie in self.zombies.sprites():
			Zombie.draw()

		collisions = pygame.sprite.groupcollide(
			self.bullets, self.zombies, True, True)

		if pygame.sprite.spritecollideany(self.player, self.zombies):
			self._player_hit()


		#Make the most recently drawn screen visible 
		pygame.display.flip()


if __name__ == '__main__':
	#Make a game instance, and run the game
	df = Defender()
	df.run_game()