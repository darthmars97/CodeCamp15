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
		self.scroll = 0
		self.surface = pygame.display.set_mode((self.width, self.height))
		# self.intermediate = pygame.surface.Surface(self.width, self.height + 600)
		self.surface.fill((255, 255, 255))
		self.screen = 0
		self.display()
		self.evolve()

	def evolve(self):
		self.running = True
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:

					if self.screen == 0:
						mouseX, mouseY = event.pos

						if self.enterRect.collidepoint(mouseX, mouseY):
							self.screen = 1
							self.display()
							pygame.display.update()

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

						elif self.profileRect.collidepoint(mouseX, mouseY):
							self.screen = 3
							self.display()
							pygame.display.update()

					if self.screen == 3:
						mouseX, mouseY = event.pos

						if self.backRect.collidepoint(mouseX, mouseY):
							self.screen = 2
							self.display()
							pygame.display.update()

				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()

	def display(self):
		if self.screen == 0:

			background = pygame.image.load("Images/LoginPage.png")
			loginW, loginH = background.get_size()
			self.background = pygame.transform.scale(background, (loginW / 2, loginH / 2))
			self.surface.blit(self.background, (-10, -9))

			welcome = pygame.image.load("Images/WelcomeBack.png")
			wW, wH = welcome.get_size()
			self.welcome = pygame.transform.scale(welcome, (wW / 2, wH / 2))
			self.surface.blit(self.welcome, (80, 360))

			username = pygame.image.load("Images/Username.png")
			uW, uH = username.get_size()
			self.username = pygame.transform.scale(username, (uW / 2, uH / 2))
			self.surface.blit(self.username, (70, 410))

			userText = pygame.image.load("Images/LoginTextBox.png")
			userW, userH = userText.get_size()
			self.userText = pygame.transform.scale(userText, (userW / 3, userH / 3))
			self.surface.blit(self.userText, (60, 440))

			password = pygame.image.load("Images/Password.png")
			passW, passH = password.get_size()
			self.password = pygame.transform.scale(password, (passW / 2, passH / 2))
			self.surface.blit(self.password, (70, 480))

			passField = pygame.image.load("Images/LoginTextBox.png")
			self.passField = pygame.transform.scale(passField, (userW / 3, userH / 3))
			self.surface.blit(self.passField, (60, 510))

			enter = pygame.image.load("Images/EnterButton.png")
			enterW, enterH = enter.get_size()
			self.enter = pygame.transform.scale(enter, (enterW / 3, enterH / 3))
			self.surface.blit(self.enter, (140, 550))
			self.enterRect = Rect(140, 550, enterW / 3, enterH / 3)

		elif self.screen == 1:

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

			self.surface.fill((255, 255, 255))

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
			self.profileRect = Rect(self.width - 250, 100, pW / 3, pH / 3)

			groups = pygame.image.load("Images/GroupsButton.png")
			gW, gH = groups.get_size()
			self.groupsButton = pygame.transform.scale(groups, (gW / 3, gH / 3))
			self.surface.blit(self.groupsButton, (self.width - 250, 170))
			self.groupsRect = Rect(self.width - 250, 170, gW / 3, gH / 3)

			top = pygame.image.load("Images/TopChartsButton.png")
			tW, tH = top.get_size()
			self.topCharts = pygame.transform.scale(top, (tW / 3, tH / 3))
			self.surface.blit(self.topCharts, (self.width - 250, 240))
			self.topRect = Rect(self.width - 250, 240, tW / 3, tH / 3)

			search = pygame.image.load("Images/SearchBar.png")
			sW, sH = search.get_size()
			self.searchBar = pygame.transform.scale(search, (sW / int(2.7), sH / 2))
			self.surface.blit(self.searchBar, (self.width - 260, 20))

			signOut = pygame.image.load("Images/SignOutButton.png")
			iW, iH = signOut.get_size()
			self.signOut = pygame.transform.scale(signOut, (iW / 2, iH / 2))
			self.surface.blit(self.signOut, (self.width - 220, self.height - 60))

		elif self.screen == 3:

			self.surface.fill((255, 255, 255))

			navProfile = pygame.image.load("Images/NavbarProfile.png")
			navW, navH = navProfile.get_size()
			self.navBarProfile = pygame.transform.scale(navProfile, (navW / 2, navH / 2))
			self.surface.blit(self.navBarProfile, (0, -1))

			backProfile = pygame.image.load("Images/BackButton.png")
			bW, bH = backProfile.get_size()
			self.backProfile = pygame.transform.scale(backProfile, (bW / 2, bH / 2))
			self.surface.blit(self.backProfile, (0, 0))
			self.backRect = Rect(0, 0, bW / 2, bH / 2)

			image = pygame.image.load("Images/Profile.png")
			mW, mH = image.get_size()
			self.profileImage = pygame.transform.scale(image, (mW / 3, mH / 3))
			self.surface.blit(self.profileImage, (155, 150))




	# def mouseClick(self):
	# 	mouseX, mouseY = event.pos()
	# 	if self.newNav.collidepoint(mouseX, mouseY):
	# 		print "clicked on nav bar"

	# 	if self.newMenu.collidepoint(mouseX, mouseY):
	# 		print "clicked on menu icon"


if __name__ == "__main__":
	UI(414, 736, 30)
