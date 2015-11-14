import pygame, sys
from pygame.locals import *
import time


# This controls user interface

class UI:

	def __init__(self, width, height, fps):
		pygame.init()
		pygame.font.init()
		pygame.display.set_caption("StockNotes")
		self.songNameFont = pygame.font.SysFont("Gujarati Sangam MN", 26)
		self.notesFont = pygame.font.SysFont("Gujarati Sangam MN", 36)
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

						elif self.signUpRect.collidepoint(mouseX, mouseY):
							self.screen = 4
							self.display()

					if self.screen == 1:
						mouseX, mouseY = event.pos

						if self.menuRect.collidepoint(mouseX, mouseY):
							self.screen = 2
							self.display()

						elif self.albumFrameRect.collidepoint(mouseX, mouseY):
							self.screen = 6
							self.display()

					if self.screen == 2:
						mouseX, mouseY = event.pos

						if self.overlayRect.collidepoint(mouseX, mouseY):
							self.screen = 1
							self.display()

						elif self.profileRect.collidepoint(mouseX, mouseY):
							self.screen = 3
							self.display()

						elif self.topRect.collidepoint(mouseX, mouseY):
							self.screen = 5
							self.display()

						elif self.signOutRect.collidepoint(mouseX, mouseY):
							self.screen = 0
							self.display()

					if self.screen == 3:
						mouseX, mouseY = event.pos

						if self.backRect.collidepoint(mouseX, mouseY):
							self.screen = 2
							self.display()

					if self.screen == 4:
						mouseX, mouseY = event.pos

						if self.enterRect.collidepoint(mouseX, mouseY):
							self.screen = 1
							self.display()

						if self.logInRect.collidepoint(mouseX, mouseY):
							self.screen = 0
							self.display()

					if self.screen == 5:
						mouseX, mouseY = event.pos

						if self.menuRect.collidepoint(mouseX, mouseY):
							self.screen = 2
							self.display()

					if self.screen == 6:
						mouseX, mouseY = event.pos

						if self.albumRect.collidepoint(mouseX, mouseY):
							self.screen = 1
							self.display()

				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()

	def drawSongName(self, surface, text, color, x, y, font):
		textobj = font.render(text, False, color)
		textrect = textobj.get_rect()
		textrect.bottomleft = (x, y)
		surface.blit(textobj, textrect)
		return

	def drawMainNotes(self, surface, text, color, x, y, font):
		textobj = font.render(text, False, color)
		textrect = textobj.get_rect()
		textrect.bottomleft = (x, y)
		surface.blit(textobj, textrect)
		return


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

			signUp = pygame.image.load("Images/SignUpButton.png")
			signUpW, signUpH = signUp.get_size()
			self.signUp = pygame.transform.scale(signUp, (signUpW / 3, signUpH / 3))
			self.surface.blit(self.signUp, (0, 630))
			self.signUpRect = Rect(0, 630, signUpW / 3, signUpH / 3)

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

			hotTracks = pygame.image.load("Images/HotTracks.png")
			hW, hH = hotTracks.get_size()
			self.hotTracks = pygame.transform.scale(hotTracks, (hW / 3, hH / 3))
			self.surface.blit(self.hotTracks, (40, 130))

			albumFrame = pygame.image.load("Images/AlbumFrame.png")
			aW, aH = albumFrame.get_size()
			self.albumFrame = pygame.transform.scale(albumFrame, (aW / 2, aH / 2))
			self.surface.blit(self.albumFrame, (15, 160))
			self.albumFrameRect = Rect(15, 160, aW / 2, aH / 2)

			noteLine = pygame.image.load("Images/MainNoteLine.png")
			lW, lH = noteLine.get_size()
			self.noteLine = pygame.transform.scale(noteLine, (lW / 2, lH / 2))
			self.surface.blit(self.noteLine, (130, 232))

			songName = "Song Name"
			songY = 230
			songX = 135
			self.drawSongName(self.surface, songName, (0, 0, 0), songX, songY, self.songNameFont)

			notes = 2048
			notesX = 100
			notesY = 100
			self.drawMainNotes(self.surface, str(notes), (255, 255, 255), notesX, notesY, self.notesFont)


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

			mX = self.width - 270
			mY = -2
			oX = -58
			oY = -1
			pX = self.width - 250
			pY = 100
			gX = self.width - 250
			gY = 170
			tX = self.width - 250
			tY = 240
			sX = self.width - 260
			sY = 20
			x = self.width - 220
			y = self.height - 60

			menuScreen = pygame.image.load("Images/MenuBackgroundBlue.png")
			sW, sH = menuScreen.get_size()
			self.newMenuScreen = pygame.transform.scale(menuScreen, (sW, sH))
			self.surface.blit(self.newMenuScreen, (mX, mY))

			overlay = pygame.image.load("Images/MenuBackgroundBlack.png")
			oW, oH = overlay.get_size()
			self.newOverlay = pygame.transform.scale(overlay, (oW / 2, oH / 2))
			self.newOverlay.set_colorkey((99, 99, 99))
			self.surface.blit(self.newOverlay, (oX, oY))
			self.overlayRect = Rect(oX, oY, oW / 2, oH / 2)

			profileButton = pygame.image.load("Images/ProfileButton.png")
			pW, pH = profileButton.get_size()
			self.newProfile = pygame.transform.scale(profileButton, (pW / 3, pH / 3))
			self.surface.blit(self.newProfile, (pX, pY))
			self.profileRect = Rect(pX, pY, pW / 3, pH / 3)

			groups = pygame.image.load("Images/GroupsButton.png")
			gW, gH = groups.get_size()
			self.groupsButton = pygame.transform.scale(groups, (gW / 3, gH / 3))
			self.surface.blit(self.groupsButton, (gX, gY))
			self.groupsRect = Rect(gX, gY, gW / 3, gH / 3)

			top = pygame.image.load("Images/TopChartsButton.png")
			tW, tH = top.get_size()
			self.topCharts = pygame.transform.scale(top, (tW / 3, tH / 3))
			self.surface.blit(self.topCharts, (tX, tY))
			self.topRect = Rect(tX, tY, tW / 3, tH / 3)

			search = pygame.image.load("Images/SearchBar.png")
			sW, sH = search.get_size()
			self.searchBar = pygame.transform.scale(search, (sW / int(2.7), sH / 2))
			self.surface.blit(self.searchBar, (sX, sY))

			signOut = pygame.image.load("Images/SignOutButton.png")
			iW, iH = signOut.get_size()
			self.signOut = pygame.transform.scale(signOut, (iW / 2, iH / 2))
			self.surface.blit(self.signOut, (x, y))
			self.signOutRect = Rect(x, y, iW / 2, iH / 2)

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

			username = pygame.image.load("Images/Username.png")
			uW, uH = username.get_size()
			self.username = pygame.transform.scale(username, (uW / 2, uH / 2))
			self.surface.blit(self.username, (140, 105))

			notes = pygame.image.load("Images/ProfileNoteLine.png")
			nW, nH = notes.get_size()
			self.notesLine = pygame.transform.scale(notes, (nW / 2, nH / 2))
			self.surface.blit(self.notesLine, (40, 250))

			blueLine = pygame.image.load("Images/DarkBlueLine.png")
			bW, bH = blueLine.get_size()
			self.line = pygame.transform.scale(blueLine, (bW / 2, bH / 2))
			self.surface.blit(self.line, (-1, 350))

			graph = pygame.image.load("Images/Progress Graph.png")
			gW, gH = graph.get_size()
			self.graph = pygame.transform.scale(graph, (gW / 3, gH / 3))
			self.surface.blit(self.graph, (5, 380))

			refresh = pygame.image.load("Images/RefreshButton.png")
			rW, rH = refresh.get_size()
			self.refresh = pygame.transform.scale(refresh, (rW / 2, rH / 2))
			self.surface.blit(self.refresh, (self.width - 100, 360))
			self.refreshRect = Rect(self.width - 100, 360, rW / 2, rH / 2)

		elif self.screen == 4:

			background = pygame.image.load("Images/LoginPage.png")
			loginW, loginH = background.get_size()
			self.background = pygame.transform.scale(background, (loginW / 2, loginH / 2))
			self.surface.blit(self.background, (-10, -9))

			welcome = pygame.image.load("Images/WhoAreYou.png")
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

			logIn = pygame.image.load("Images/LoginButton.png")
			signUpW, signUpH = logIn.get_size()
			self.logIn = pygame.transform.scale(logIn, (signUpW / 3, signUpH / 3))
			self.surface.blit(self.logIn, (self.width - 150, 630))
			self.logInRect = Rect(self.width - 150, 630, signUpW / 3, signUpH / 3)

		elif self.screen == 5:

			self.surface.fill((255, 255, 255))

			navBar = pygame.image.load("Images/NavbarMain.png")
			nW, nH = navBar.get_size()
			self.newNav = pygame.transform.scale(navBar, (nW / 3, nH / 2))
			self.surface.blit(self.newNav, (-5, -2))

			title = pygame.image.load("Images/TopCharts.png")
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

			albumFrame = pygame.image.load("Images/AlbumFrame.png")
			aW, aH = albumFrame.get_size()
			self.albumFrame = pygame.transform.scale(albumFrame, (aW / 2, aH / 2))
			self.surface.blit(self.albumFrame, (15, 140))

			noteLine = pygame.image.load("Images/MainNoteLine.png")
			lW, lH = noteLine.get_size()
			self.noteLine = pygame.transform.scale(noteLine, (lW / 2, lH / 2))
			self.surface.blit(self.noteLine, (130, 212))

			songName = "Song Name"
			songY = 210
			songX = 135
			self.drawSongName(self.surface, songName, (0, 0, 0), songX, songY, self.songNameFont)

		elif self.screen == 6:

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

			hotTracks = pygame.image.load("Images/HotTracks.png")
			hW, hH = hotTracks.get_size()
			self.hotTracks = pygame.transform.scale(hotTracks, (hW / 3, hH / 3))
			self.surface.blit(self.hotTracks, (40, 130))

			albumFrame = pygame.image.load("Images/AlbumFrame.png")
			aW, aH = albumFrame.get_size()
			self.albumFrame = pygame.transform.scale(albumFrame, (aW / 2, aH / 2))
			self.surface.blit(self.albumFrame, (15, 160))

			noteLine = pygame.image.load("Images/MainNoteLine.png")
			lW, lH = noteLine.get_size()
			self.noteLine = pygame.transform.scale(noteLine, (lW / 2, lH / 2))
			self.surface.blit(self.noteLine, (130, 232))

			songName = "Song Name"
			songY = 230
			songX = 135
			self.drawSongName(self.surface, songName, (0, 0, 0), songX, songY, self.songNameFont)

			buy = pygame.image.load("Images/BuyingOverlay.png")
			bW, bH = buy.get_size()
			self.buy = pygame.transform.scale(buy, (bW / 2, bH / 2))
			self.buy.set_colorkey((99, 99, 99))
			self.surface.blit(self.buy, (0, -120))

			album = pygame.image.load("Images/AlbumFrame.png")
			aW, aH = album.get_size()
			self.album = pygame.transform.scale(album, (aW / 2, aH / 2))
			self.surface.blit(self.album, (10, 330))
			self.albumRect = Rect(30, 330, aW / 2, aH / 2)

			line = pygame.image.load("Images/BuyingLine.png")
			lW, lH = line.get_size()
			self.line = pygame.transform.scale(line, (lW / 2, lH / 2))
			self.surface.blit(self.line, (-5, 480))

			buyText = pygame.image.load("Images/BuyNotes.png")
			tW, tH = buyText.get_size()
			self.buyText = pygame.transform.scale(buyText, (tW / 2, tH / 2))
			self.surface.blit(self.buyText, (150, 500))

			buy10 = pygame.image.load("Images/10Button.png")
			b10W, b10H = buy10.get_size()
			self.buy10 = pygame.transform.scale(buy10, (b10W / 3, b10H / 3))
			self.surface.blit(self.buy10, (155, 545))

			buy1 = pygame.image.load("Images/1Button.png")
			b1W, b1H = buy1.get_size()
			self.buy1 = pygame.transform.scale(buy1, (b1W / 3, b1H / 3))
			self.surface.blit(self.buy1, (70, 553))

			buy100 = pygame.image.load("Images/100Button.png")
			b100W, b100H = buy100.get_size()
			self.buy100 = pygame.transform.scale(buy100, (b100W / 3, b100H / 3))
			self.surface.blit(self.buy100, (250, 537))

			sellText = pygame.image.load("Images/SellNotes.png")
			sellW, sellH = sellText.get_size()
			self.sellText = pygame.transform.scale(sellText, (sellW / 2, sellH / 2))
			self.surface.blit(self.sellText, (150, 600))

			self.sell10 = self.buy10
			self.surface.blit(self.sell10, (155, 640))

			self.sell1 = self.buy1
			self.surface.blit(self.sell1, (70, 645))

			self.sell100 = self.buy100
			self.surface.blit(self.sell100, (250, 630))

			text = "Name of Song"
			textY = 490
			textX = 10
			self.drawSongName(self.surface, text, (255, 255, 255), textX, textY, self.songNameFont)


		pygame.display.update()



if __name__ == "__main__":
	UI(414, 736, 30)
