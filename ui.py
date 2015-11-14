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

						if self.menuRect.collidepoint(mouseX, mouseY):
							self.screen = 2
							self.display()
							pygame.display.update()

					if self.screen == 2:
						mouseX, mouseY = event.pos

						if self.overlayRect.collidepoint(mouseX, mouseY):
							self.screen = 1
							self.display()
							pygame.display.update()

				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()

	def display(self):
		if self.screen == 1:

			self.surface.fill((255, 255, 255))

			navBar = pygame.image.load("Images/NavbarMain.png")
			nW, nH = navBar.get_size()
			self.newNav = pygame.transform.scale(navBar, (nW / 3, nH / 2))
			self.surface.blit(self.newNav, (-5, -2))

			title = pygame.image.load("Images/NoteStocks.png")
			tW, tH = title.get_size()
			self.newTitle = pygame.transform.scale(title, (tW / 2, tH / 2))
			self.surface.blit(self.newTitle, (110, 5))

			menuIcon = pygame.image.load("Images/MenuButtonLong.png")
			mW, mH = menuIcon.get_size()
			self.newMenu = pygame.transform.scale(menuIcon, (mW / 2, mH / 2))
			self.surface.blit(self.newMenu, (self.width - 59, -1))
			self.menuRect = Rect(self.width - 59, -1, mW / 2, mH / 2)

			notes = pygame.image.load("Images/NoteIcon.png")
			nW, nH = notes.get_size()
			self.newNote = pygame.transform.scale(notes, (nW, nH))
			self.surface.blit(self.newNote, (0, 0))

		elif self.screen == 2:

			navBar = pygame.image.load("Images/NavbarMain.png")
			nW, nH = navBar.get_size()
			self.newNav = pygame.transform.scale(navBar, (nW / 2, nH / 2))
			self.surface.blit(self.newNav, (-60, -2))

			menuIcon = pygame.image.load("Images/MenuButtonLong.png")
			mW, mH = menuIcon.get_size()
			self.newMenu = pygame.transform.scale(menuIcon, (mW / 2, mH / 2))
			self.surface.blit(self.newMenu, (self.width - 70, 12))

			notes = pygame.image.load("Images/NoteIcon.png")
			nW, nH = notes.get_size()
			self.newNote = pygame.transform.scale(notes, (nW, nH))
			self.surface.blit(self.newNote, (0, 0))

			menuScreen = pygame.image.load("Images/MenuBackgroundBlue.png")
			sW, sH = menuScreen.get_size()
			self.newMenuScreen = pygame.transform.scale(menuScreen, (sW, sH))
			self.surface.blit(self.newMenuScreen, (self.width - 270, -2))

			overlay = pygame.image.load("Images/MenuBackgroundBlack.png")
			oW, oH = overlay.get_size()
			self.newOverlay = pygame.transform.scale(overlay, (oW / 2, oH / 2))
			self.newOverlay.set_colorkey((99, 99, 99))
			self.surface.blit(self.newOverlay, (-58, -1))
			self.overlayRect = Rect(-58, -1, oW / 2, oH / 2)

			profileButton = pygame.image.load("Images/ProfileButton.png")
			pW, pH = profileButton.get_size()
			self.newProfile = pygame.transform.scale(profileButton, (pW / 3, pH / 3))
			self.surface.blit(self.newProfile, (self.width - 250, 100))

		elif self.screen == 3:

			




	# def mouseClick(self):
	# 	mouseX, mouseY = event.pos()
	# 	if self.newNav.collidepoint(mouseX, mouseY):
	# 		print "clicked on nav bar"

	# 	if self.newMenu.collidepoint(mouseX, mouseY):
	# 		print "clicked on menu icon"


if __name__ == "__main__":
	UI(414, 736, 30)
