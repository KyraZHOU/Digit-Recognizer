import pygame
from pygame.locals import *
from sys import exit
import tkinter.messagebox
from tkinter import *

# Initialize pygame
pygame.init()

# Screen settings
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width,display_height))

# Display screen caption
pygame.display.set_caption('Digit Recognizer')

# Set up background
background = pygame.image.load('title.png').convert()
# Set up button
startButton = pygame.image.load('startButton.png')
flashLight = pygame.image.load('flashLight.png')

# Two rectangle
value = 1

# Module - Draw Text
def drawText(text,posx,posy,textHeight=48,fontColor=(255,255,255),backgroudColor=(0,0,0)):
	# Set the font of the text
	fontObj = pygame.font.Font('font.ttf', textHeight)

	# Set the text contents and positions
	textSurfaceObj = fontObj.render(text, True,fontColor,backgroudColor)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (posx, posy)

	return textSurfaceObj,textRectObj


def secondScreen():
	# Display background
	background = pygame.image.load('technology.jpg').convert()
	screen.blit(background,(0,0))

while True:
	# Display background
	screen.blit(background,(0,0))

	# Display button
	screen.blit(startButton,(300,470))

	# Draw two rectangles
	# pygame.draw.rect(screen,[220,220,220],[20,20,350,500],value)
	# pygame.draw.rect(screen,[225,225,225],[420,20,350,500],value)	

	# Draw Title
	# textSurfaceObj,textRectObj = drawText("Digit",400,120,textHeight = 87)
	# screen.blit(textSurfaceObj, textRectObj)
	# textSurfaceObj,textRectObj = drawText("Recognizer",400,220,textHeight = 66)
	# screen.blit(textSurfaceObj, textRectObj)

	# Display the moving flashLight
	x, y = pygame.mouse.get_pos()
	x-= flashLight.get_width() / 2
	y-= flashLight.get_height() / 2
	screen.blit(flashLight, (x, y))

	# Handle keyboard events
	for event in pygame.event.get():
		# Quit screen: Key Q / Key ESC / Quit button
		if event.type == pygame.QUIT or (event.type == KEYDOWN and ((event.key == K_ESCAPE) or (event.key == K_q))):
			pygame.quit()
			exit()
		if event.type == MOUSEBUTTONDOWN:
			background = pygame.image.load('technology.jpg').convert()
			startButton = pygame.image.load('transparent.png')
			flashLight = pygame.image.load('brush1.png')
			value = 0

	# Screen update
	pygame.display.update()