import pygame, sys
from pygame.locals import *
import time

# This controls user interface

class UI:

	def __init__(self, width, height, fps):
		pygame.init()
		pygame.display.set_caption("StockNotes")
		self.width = width
		self.height = height
		self.fps = fps
		self.fpsClock = pygame.time.Clock()
		self.surface = pygame.display.set_mode((self.width, self.height))
		self.surface.fill((255, 255, 255))
		self.screen = 1
		self.menu()
		self.evolve()

	def evolve(self):
		self.running = True
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					
					if self.screen == 1:
						mouseX, mouseY = event.pos

						if self.newNav.get_rect().collidepoint(mouseX, mouseY):
							print "clicked on nav bar"

						if self.newMenu.get_rect().collidepoint(mouseX, mouseY):
							print "clicked on menu icon"

				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()

	def menu(self):
		navBar = pygame.image.load("Images/Navbar Images/Navbar.png")
		nW, nH = navBar.get_size()
		self.newNav = pygame.transform.scale(navBar, (nW / 2, nH / 3))
		self.surface.blit(self.newNav, (0, 0))

		menuIcon = pygame.image.load("Images/Navbar Images/Menu Icon.png")
		mW, mH = menuIcon.get_size()
		self.newMenu = pygame.transform.scale(menuIcon, (mW / 2, mH / 2))
		self.surface.blit(self.newMenu, (self.width - 70, 12))

	# def mouseClick(self):
	# 	mouseX, mouseY = event.pos()
	# 	if self.newNav.collidepoint(mouseX, mouseY):
	# 		print "clicked on nav bar"

	# 	if self.newMenu.collidepoint(mouseX, mouseY):
	# 		print "clicked on menu icon"


if __name__ == "__main__":
	UI(414, 736, 30)