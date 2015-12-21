import time
from neopixel import *
import skywriter
import signal

grid_width=8
grid_height=5

# LED strip configuration:
LED_COUNT      = 96      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 50     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

def xy_to_strip(x, y, strip_len):
	return y*strip_len + x

def set_pixel(id, colour):
	if id>-10 and id<96:      
		strip.setPixelColor(id, colour)	
		print 'id {}, {} '.format(id, colour)
	else:
		print 'id {}, {} out of range'.format(id, colour)

def set_shape(x, y):
	for i in (-2, -1, 0, 1, 2):
		for j in (-2, -1, 0, 1, 2):
			mode = abs(i)+ abs(j)
			if mode == 0:
				set_pixel(xy_to_strip(x+i, y+j, 8), Color(250, 200, 200))
			if mode == 1:
				set_pixel(xy_to_strip(x+i, y+j, 8), Color(250, 0, 100))
			if mode == 2:
				set_pixel(xy_to_strip(x+i, y+j, 8), Color(100, 0, 100))	
			if mode == 3:
				set_pixel(xy_to_strip(x+i, y+j, 8), Color(50, 0, 50))
			if mode == 4:
				set_pixel(xy_to_strip(x+i, y+j, 8), Color(25, 0, 25))

				

strip.begin()

# this handles move events from the skywriter library
@skywriter.move()
def move(x,y,z):
    tx = ceil(x * grid_width)
    # if up and down are reversed remove the "grid_height - " bit
    ty = grid_height - ceil(y * grid_height)
    set_shape(tx, ty)
    strip.show()


signal.pause()


# Def 1 = 0,0
# Def 2 = 1,0
# Def 3 = 2,0
# Def 4 = 3,0
# Def 5 = 4,0
# Def 6 = 5,0
# Def 7 = 6,0
# Def 8 = 7,0
# Def 9 = 8,0
# Def 10 = 9,0
# Def 11 = 10,0
# Def 12 = 11,0
#----
# Def 13 = 0,1
# Def 14 = 1,1
# Def 15 = 2,1
# Def 16 = 3,1
# Def 17 = 4,1
# Def 18 = 5,1
# Def 19 = 6,1
# Def 20 = 7,1
# Def 21 = 8,1
# Def 22 = 9,1
# Def 23 = 10,1
# Def 24 = 11,1
#---
# Def 25 = 0,2
# Def 26 = 1,2
# Def 27 = 2,2
# Def 28 = 3,2
# Def 29 = 4,2
# Def 30 = 5,2
# Def 31 = 6,2
# Def 32 = 7,2
# Def 33 = 8,2
# Def 34 = 9,2
# Def 35 = 10,2
# Def 36 = 11,2
#----
# Def 37 = 0,3
# Def 38 = 1,3
# Def 39 = 2,3
# Def 40 = 3,3
# Def 41 = 4,3
# Def 42 = 5,3
# Def 43 = 6,3
# Def 44 = 7,3
# Def 45 = 8,3
# Def 46 = 9,3
# Def 47 = 10,3
# Def 48 = 11,3
#----
# Def 49 = 0,4
# Def 50 = 1,4
# Def 51 = 2,4
# Def 52 = 3,4
# Def 53 = 4,4
# Def 54 = 5,4
# Def 55 = 6,4
# Def 56 = 7,4
# Def 57 = 8,4
# Def 58 = 9,4
# Def 59 = 10,4
# Def 60 = 11,4
#----
# Def 61 = 0,5
# Def 62 = 1,5
# Def 63 = 2,5
# Def 64 = 3,5
# Def 65 = 4,5
# Def 66 = 5,5
# Def 67 = 6,5
# Def 68 = 7,5
# Def 69 = 8,5
# Def 70 = 9,5
# Def 71 = 10,5
# Def 72 = 11,5
#---
# Def 73 = 0,6
# Def 74 = 1,6
# Def 75 = 2,6
# Def 76 = 3,6
# Def 77 = 4,6
# Def 78 = 5,6
# Def 79 = 6,6
# Def 80 = 7,6
# Def 81 = 8,6
# Def 82 = 9,6
# Def 83 = 10,6
# Def 84 = 11,6
#----
# Def 85 = 0,7
# Def 86 = 1,7
# Def 87 = 2,7
# Def 88 = 3,7
# Def 89 = 4,7
# Def 90 = 5,7
# Def 91 = 6,7
# Def 92 = 7,7
# Def 93 = 8,7
# Def 94 = 9,7
# Def 95 = 10,7
# Def 96 = 11,7


