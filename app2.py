import pygame
from pygame.locals import *
from sys import exit
import tkinter.messagebox
from tkinter import *
import cv2
import numpy as np

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
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width,display_height))

# canvas
# canvas_width = 200
# canvas_height = 200

# initializing screen
# canvas = pygame.display.set_mode((canvas_width*2, canvas_height))

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
	background = pygame.image.load('background5.png').convert()
	startButton = pygame.image.load('transparent.png')
	flashLight = pygame.image.load('brush1.png')

	# Display background
	screen.blit(background,(0,0))

	# Display button
	screen.blit(startButton,(300,470))
	
	# display buttons on the second screen
	upBut1 = pygame.image.load('up1.png').convert()
	upBut2 = pygame.image.load('up2.png').convert()
	upBut3 = pygame.image.load('up3.png').convert()
	upBut4 = pygame.image.load('up4.png').convert()
	downBut1 = pygame.image.load('down1.png').convert()
	downBut2 = pygame.image.load('down2.png').convert()
	downBut3 = pygame.image.load('down3.png').convert()
	downBut4 = pygame.image.load('down4.png').convert()
	
	screen.blit(upBut1,(0,5))
	screen.blit(upBut2,(200,5))
	screen.blit(upBut3,(400,5))
	screen.blit(upBut4,(600,5))
	screen.blit(downBut1,(60,530))
	screen.blit(downBut2,(210,530))
	screen.blit(downBut3,(460,530))
	screen.blit(downBut4,(610,530))
	return background, flashLight


def roundLine(screen, color, start, end, radius=1):
	dx = end[0] - start[0]
	dy = end[1] - start[1]
	distance = max(abs(dx), abs(dy))
	for i in range(distance):
		x = int(start[0] + (float(i) / distance) * dx)
		y = int(start[1] + (float(i) / distance) * dy)
		pygame.draw.circle(screen, color, (x, y), radius)

#def outputImage(img):
#   surface = pygame.pixelcopy.make_surface(img)
#   surface = pygame.transform.rotate(surface,-270)
#   surface = pygame.transform.flip(surface,0,1)
#   screen.blit(surface,(display_width+2,0))

#def crope(original):
#   cropped = pygame.Surface((display_width-5,display_height-5))
#   cropped.blit(original,(0,0),(0,0,display_width-5,display_height-5))
#   return cropped


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
		background, flashLight = secondScreen()
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

	#if ((event.type == MOUSEBUTTONDOWN) and (0 <= event.pos[0] <= 200) and (5 <= event.pos[1] <= 50)):
		#tkinter.messagebox.showinfo('Info','Keep Calm')

	# start drawing after left click
	if (event.type == pygame.MOUSEBUTTONDOWN): # and event.button != 3 and (20 <= event.pos[0] <= 500) and (5 <= event.pos[1] <= 50)):
		color = black
		pygame.draw.circle(screen, color, event.pos, radius)
		drawOn = True

	# stop drawing after releasing left click
	if (event.type == pygame.MOUSEBUTTONUP): #and event.button != 3 and (20 <= event.pos[0] <= 500) and (5 <= event.pos[1] <= 50)):
		drawOn = False
		fname = "out.png"

		'''img = crope(screen)
		pygame.image.save(img, fname)

		output_img = get_output_image(fname)
		show_output_image(output_img)
'''
	# start drawing line on screen if draw is true
	if (event.type == pygame.MOUSEMOTION): #and (20 <= event.pos[0] <= 500) and (5 <= event.pos[1] <= 50)):
		if drawOn:
			pygame.draw.circle(screen, color, event.pos, radius)
			roundLine(screen, color, event.pos, lastPos, radius)
		lastPos = event.pos

	pygame.display.flip()

# Screen update
#pygame.display.update()