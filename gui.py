# import necessary packages
import pygame, sys, os, time, Adafruit_ADS1x15
from pygame.locals import *
import RPi.GPIO as GPIO

# initialize the display
os.environ["SDL_FBDEV"] = "/dev/fb1"

# setup GPIO pins
inputButtonOne = 20
inputButtonTwo = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(switchDisplayPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switchDisplayPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# verify they are working
checkInputOne = GPIO.input(inputButtonOne)
checkInputTwo = GPIO.input(inputButtonTwo)
print(str(checkInputOne)+str(checkInputTwo))

# create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
# verify they are working
# read all the ADC channel values in a list.
values = [0]*4
for i in range(4):
    # read the specified ADC channel using the previously set gain values
    values[i] = adc.read_adc(i, gain=GAIN)
print(values)

# initialize pygame
pygame.init()

# set up the pygame window
display_Width = 160
display_Height = 128
uiDisplay = pygame.display.set_mode((display_Width, display_Height), 0, 32)
pygame.display.set_caption('userInterface')

# set up the colors
black = (  0,   0,   0)
white = (255, 255, 255)
red   = (255,   0,   0)
green = (  0, 255,   0)
blue  = (  0,   0, 255)

# draw on the surface object
uiDisplay.fill(black)
pygame.draw.polygon(uiDisplay, green, ((16, 0), (111, 106), (36, 160), (56, 27), (0, 106)))
pygame.draw.line(uiDisplay, red, (60, 60), (120, 60), 4)
pygame.draw.line(uiDisplay, red, (120, 60), (60, 120))
pygame.draw.line(uiDisplay, blue, (60, 120), (120, 120), 4)
pygame.draw.circle(uiDisplay, blue, (40, 50), 20, 0)
pygame.draw.ellipse(uiDisplay, red, (110, 200, 40, 80), 1)
box = pygame.draw.rect(uiDisplay, red, (100, 150, 100, 50))

#pixObj = pygame.PixelArray(uiDisplay)
#pixObj[120][144] = black
#pixObj[122][146] = black
#pixObj[124][148] = black
#pixObj[126][158] = black
#pixObj[126][158] = black
#del pixObj

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()   
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Pos: %sx%s\n" % pygame.mouse.get_pos())
            if box.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
    if(GPIO.input(inputButtonOne) = False):
        pygame.quit()
        sys.exit()
        quit()
    pygame.display.update()
