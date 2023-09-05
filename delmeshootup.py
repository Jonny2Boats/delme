import pygame

from settings import Settings


class DelMeShootup:

	def __init__(self):
		print("in init")
		pygame.init()

		self.settings= Settings()

		print(self.settings.screen_height, "in init")

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

		self.background_img= pygame.image.load('img/background/smash.png').convert_alpha()
		self.panel_image= pygame.image.load('img/background/panel.png').convert_alpha()
	def draw_bg(self):
		self.screen.blit(self.background_img, (0, 0))

	def draw_panel(self):
		self.screen.blit(self.panel_image, (0,self.settings.screen_height - self.settings.bottom_panel))
		#print(bottom_panel)

	def run_game(self):

		while self.settings.run:
			self.settings.clock.tick(self.settings.FPS)   # sets animation frame rate
			self.draw_bg()
			self.draw_panel()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.settings.run= False
					#print(run)
			pygame.display.update()

		pygame.quit()
		

if __name__ == '__main__':
	print("calling")

	dm= DelMeShootup()
	dm.run_game()
