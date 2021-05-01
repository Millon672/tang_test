import time
import random
import board
import adafruit_dotstar as dotstar
 
# On-board DotStar for boards including Gemma, Trinket, and ItsyBitsy
dots = dotstar.DotStar(board.SCK, board.MOSI, 11, brightness=0.2) 
 
# HELPERS
# a random color 0 -> 192
def random_color():
    return random.randrange(0, 7) * 32
 
 
# MAIN LOOP
n_dots = len(dots)

    # Fill each dot with a random color
for dot in range(n_dots):
	
	dots[dot] = (0, 0, 0)
 
 
