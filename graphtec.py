# Import a library of functions called 'pygame'
import pygame, turtle
from math import pi
from randomizer import songs, hello
import matplotlib.pyplot as plt


radius = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
area = [int(hello[0]), int(hello[1]), int(hello[2]), int(hello[3]), int(hello[4]), int(hello[5])]
plt.plot(radius, area, label='Hello - Adele')
ax = plt.gca()
ax.set_axis_bgcolor('#A0A0A0')
plt.xlabel('Time')
plt.ylabel('Notes')
plt.title('Stats')
plt.legend()
plt.show()
"""
def drawBar(t, height):
     Get turtle t to draw one bar, of height. 
    t.speed(0)
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape

def fillColor(t,height):
    t.fillcolor('#F9A01B')
    drawBar(t,height)


xs = [songs["Hello - Adele"],songs['Hotline Bling - Drake'],songs['The Hills - The Weeknd'],songs['Sorry - Justin Beiber'],songs['What Do You Mean? - Justin Beiber'],songs['Stiches - Shawn Mendes'],songs['Focus - Ariana Grande']]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10

tess = turtle.Turtle()           # create tess and set some attributes
#tess.color("blue")
#tess.fillcolor("red")
tess.pensize(10)


wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("grey")
wn.setworldcoordinates(0-border,0-border,40*numbars+border,maxheight+border)


for i in xs:
    fillColor(tess,i)

wn.exitonclick()
"""
"""
posx = 100 * resetCounter

posy = (())

points {
    [posx, posy],
}"""
# Initialize the game engine
"""pygame.init()

# Define the colors we will use in RGB format
WHITE = (255, 255, 255)
ORANGE = (249, 160, 27)

# Set the height and width of the screen
size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)


    pygame.draw.lines(screen, ORANGE, False, [[0, 300], [100, 10], [200, 150], [300, 65], [400, 200]], 10)


    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()"""
