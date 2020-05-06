

FPS = 5 #frames per seconds
WIDTH = 400 #pixels, -> 640x480 resolution
HEIGHT = 400

GRID = 20
UNITS_WIDTH = WIDTH / GRID #dimensions of the grid
UNITS_HEIGHT = HEIGHT / GRID
UNITS = UNITS_WIDTH * UNITS_HEIGHT

#directions with inverted Y axis
UP = (0, -1)  
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

#colours
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)