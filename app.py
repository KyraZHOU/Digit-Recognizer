import pygame
from pygame.locals import *
from sys import exit
import numpy as np
from imageProcess import getOutput

# pre defined colors, pen radius and font color
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
drawOn = False
lastPos = (0, 0)
color = (255, 128, 0)
radius = 6

# Initialize pygame
pygame.init()

# Screen settings
scrWidth = 800
scrHeight = 600
screen = pygame.display.set_mode((scrWidth,scrHeight))

# canvas
cvsWidth = 600
cvsHeight = 530

# initializing screen
# canvas = pygame.display.set_mode((cvsWidth*2, cvsHeight))

# Display screen caption
pygame.display.set_caption('Digit Recognizer')

# Set up background
background = pygame.image.load('title.png').convert()
# Set up button
startButton = pygame.image.load('startButton.png')
flashLight = pygame.image.load('flashLight.png')

# Set two boolean flags for the first screen and second screen
firstFlag = True
secondFlag = False

# Module - Draw Text
def drawText(text,posx,posy,textHeight=48,fontColor=(255,255,255),backgroudColor=(0,0,0)):
	# Set the font of the text
	fontObj = pygame.font.Font('font.ttf', textHeight)

	# Set the text contents and positions
	textSurfaceObj = fontObj.render(text, True,fontColor,backgroudColor)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (posx, posy)

	return textSurfaceObj,textRectObj

def firstScreen():
	# Display background
	screen.blit(background,(0,0))

	# Display button
	screen.blit(startButton,(300,470))

	# Draw Title
	# textSurfaceObj,textRectObj = drawText("Digit",400,120,textHeight = 87)
	# screen.blit(textSurfaceObj, textRectObj)
	# textSurfaceObj,textRectObj = drawText("Recognizer",400,220,textHeight = 66)
	# screen.blit(textSurfaceObj, textRectObj)

def secondScreen():	
	background = pygame.image.load('background7.png').convert()
	startButton = pygame.image.load('transparent.png')
	flashLight = pygame.image.load('brush1.png')

	# Display background
	screen.blit(background,(0,0))
	#screen.fill(white)
	#pygame.draw.line(screen, black, [scrWidth, 0], [scrWidth,scrHeight], 8)

	# Display button
	screen.blit(startButton,(300,470))
	
	# display the RESET button on the second screen
	downBut = pygame.image.load('down1.png').convert()
	
	screen.blit(downBut,(350,525))
	return background, flashLight,downBut


def roundLine(screen, color, start, end, radius=1):
	dx = end[0] - start[0]
	dy = end[1] - start[1]
	distance = max(abs(dx), abs(dy))
	for i in range(distance):
		x = int(start[0] + (float(i) / distance) * dx)
		y = int(start[1] + (float(i) / distance) * dy)
		pygame.draw.circle(screen, color, (x, y), radius)

def outputImage(cropImg):
   surface = pygame.pixelcopy.make_surface(cropImg)
   surface = pygame.transform.rotate(surface,-270)
   surface = pygame.transform.flip(surface,0,1)
   screen.blit(surface,(cvsWidth-200,0))

def crope(original,downBut):
	cropped = pygame.Surface((cvsWidth-200,cvsHeight-5))
	cropped.blit(original,(0,0),(0,0,cvsWidth-200,cvsHeight-5))
	return cropped


while True:
	# Display the moving flashLight
	x, y = pygame.mouse.get_pos()
	x-= flashLight.get_width() / 2
	y-= flashLight.get_height() / 2

	# call firstScreen
	if firstFlag:
		firstScreen()
		screen.blit(flashLight, (x, y))

	# call secondScreen
	if secondFlag:
		background, flashLight,downBut = secondScreen()
		secondFlag = False

	event = pygame.event.wait()
	# Handle keyboard events
	# Quit screen: Key Q / Key ESC / Quit button
	if event.type == pygame.QUIT or (event.type == KEYDOWN and ((event.key == K_ESCAPE) or (event.key == K_q))):
		pygame.quit()
		exit()

	if ((event.type == MOUSEBUTTONDOWN) and ((300 <= event.pos[0] <= 500) and (400 <= event.pos[1] <= 600))):
		firstFlag = False
		secondFlag = True
		# tkinter.messagebox.showinfo('Info','Keep Calm')

	#if ((event.type == MOUSEBUTTONDOWN) and (0 <= event.pos[0] <= 200) and (5 <= event.pos[1] <= 50)):
	#	tkinter.messagebox.showinfo('Info','Keep Calm')

	# start drawing after left click
	if (event.type == pygame.MOUSEBUTTONDOWN): # and event.button != 3 and (20 <= event.pos[0] <= 500) and (5 <= event.pos[1] <= 50)):
		color = black
		pygame.draw.circle(screen, color, event.pos, radius)
		drawOn = True

	# stop drawing after releasing left click
	if (event.type == pygame.MOUSEBUTTONUP): #and event.button != 3 and (20 <= event.pos[0] <= 500) and (5 <= event.pos[1] <= 50)):
		drawOn = False
		fname = "out.png"
		cropImg = crope(screen,downBut)
		pygame.image.save(cropImg, fname)

		output = getOutput(fname)
		outputImage(output)
		screen.blit(downBut,(350,525))

	# start drawing line on screen if draw is true
	if (event.type == pygame.MOUSEMOTION): #and (20 <= event.pos[0] <= 500) and (5 <= event.pos[1] <= 50)):
		if drawOn:
			pygame.draw.circle(screen, color, event.pos, radius)
			roundLine(screen, color, event.pos, lastPos, radius)
		lastPos = event.pos

	pygame.display.flip()

# Screen update
#pygame.display.update()