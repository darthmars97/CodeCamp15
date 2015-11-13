import pygame, sys
from pygame.locals import *
import time

# This controls user interface

class UI:

	def __init__(self, width, height, fps):
		pygame.init()
		self.width = width
		self.height = height
		self.fps = fps
		self.fpsClock = pygame.time.Clock()
		self.surface = pygame.display.set_mode((self.width, self.height))
		self.menu()
		self.evolve()

	def evolve(self):
		self.running = True
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					pygame.mouse.set_pos(100, 100)
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()

	def menu(self):
		self.menuIcon = pygame.image.load("Images/Navbar Images/Menu Icon.png")
		surface.blit(self.menuIcon, (10, 10))

if __name__ == "__main__":
	UI(414, 736, 30)