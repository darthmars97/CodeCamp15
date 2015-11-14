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
		self.display()
		self.evolve()

	def evolve(self):
		self.running = True
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:

					if self.screen == 1:
						mouseX, mouseY = event.pos

						if self.newMenu.get_rect().collidepoint(mouseX, mouseY):
							print "clicked on menu icon"
							self.screen = 2
							print self.screen
							self.display()
							pygame.display.update()
							print "I'm Working properly Matt! :D"

						elif self.newNav.get_rect().collidepoint(mouseX, mouseY):
							print "clicked on nav bar"

				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()

	def display(self):
		if self.screen == 1:

			navBar = pygame.image.load("Images/NavbarMain.png")
			nW, nH = navBar.get_size()
			self.newNav = pygame.transform.scale(navBar, (nW / 2, nH / 2))
			self.surface.blit(self.newNav, (-1, -2))

			title = pygame.image.load("Images/NoteStocks.png")
			tW, tH = title.get_size()
			self.newTitle = pygame.transform.scale(title, (tW / 2, tH / 2))
			self.surface.blit(self.newTitle, (110, 5))

			menuIcon = pygame.image.load("Images/MenuButton.png")
			mW, mH = menuIcon.get_size()
			self.newMenu = pygame.transform.scale(menuIcon, (mW / 2, mH / 2))
			self.surface.blit(self.newMenu, (self.width - 70, 12))

			notes = pygame.image.load("Images/NoteIcon.png")
			nW, nH = notes.get_size()
			self.newNote = pygame.transform.scale(notes, (nW, nH))
			self.surface.blit(self.newNote, (0, 0))

		elif self.screen == 2:

			navBar = pygame.image.load("Images/NavbarMain.png")
			nW, nH = navBar.get_size()
			self.newNav = pygame.transform.scale(navBar, (nW / 2, nH / 2))
			self.surface.blit(self.newNav, (-60, -2))

			menuIcon = pygame.image.load("Images/MenuButton.png")
			mW, mH = menuIcon.get_size()
			self.newMenu = pygame.transform.scale(menuIcon, (mW / 2, mH / 2))
			self.surface.blit(self.newMenu, (self.width - 70, 12))

			notes = pygame.image.load("Images/NoteIcon.png")
			nW, nH = notes.get_size()
			self.newNote = pygame.transform.scale(notes, (nW, nH))
			self.surface.blit(self.newNote, (0, 0))

			menuScreen = pygame.image.load("Images/MenuBackgroundOriginal.png")
			sW, sH = menuScreen.get_size()
			self.newMenuScreen = pygame.transform.scale(menuScreen, (sW, sH))
			self.newMenuScreen.set_colorkey((99, 99, 99))
			self.surface.blit(self.newMenuScreen, (-250, -2))

			profileButton = pygame.image.load("Images/ProfileButton.png")
			pW, pH = profileButton.get_size()
			self.newProfile = pygame.transform.scale(profileButton, (pW / 3, pH / 3))
			self.surface.blit(self.newProfile, (self.width - 250, 100))


	# def mouseClick(self):
	# 	mouseX, mouseY = event.pos()
	# 	if self.newNav.collidepoint(mouseX, mouseY):
	# 		print "clicked on nav bar"

	# 	if self.newMenu.collidepoint(mouseX, mouseY):
	# 		print "clicked on menu icon"


if __name__ == "__main__":
	UI(414, 736, 30)
