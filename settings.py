import pygame

class Settings:

	def __init__(self):
		# Screen settings
		self.game_panel= 400
		self.bottom_panel= 150
		#png needs to reflect these sizes

		self.screen_height = self.game_panel + self.bottom_panel
		self.screen_width = 800

		RED = {255,0,0}
		BLACK = {0,0,0}
		# game vars
		self.clock= pygame.time.Clock()
		self.FPS=60

		self.run= True
