import pygame
import pygame.locals

# This controls user interface

class UI:

	def __init__(self, width, height, fps):
		pygame.init()
		self.width = width
		self.height = height
		self.fps = fps
		self.surface = pygame.display.set_mode((self.width, self.height))

	def evolve(self):
		self.running = True
		while self.running:
			for event in pygame.event.get():
				if event.type == QUIT():
					pygame.quit()
					sys.exit()
			pygame.display.update()

if __name__ == "__main__":
	UI(600, 400, 60)