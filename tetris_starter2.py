import pygame
import random

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS
s_width = 800
s_height = 700
rows = 20
columns = 10
block_size = 30
play_width = columns * block_size  # meaning 300 // 10 = 30 width per block
play_height = rows * block_size    # meaning 600 // 20 = 20 height per block

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height


# SHAPE FORMATS

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape


class Piece(object):
    rows = 20  # y
    columns = 10  # x

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0  # number from 0-3

# step 3: 
# create a matrix with 20 rows, each row has 10 elements
# each element is a 3-value tuple, representing color,e.g, (0,0,0)
# Note that we can ignor locked_positions for now.
def create_grid(locked_positions={}):
    grid = [[(0,0,0) for x in range(10)] for y in range(20)]
	
    #TODO: handle locked_positions

    return grid

def convert_shape_format(piece):
	pass

def valid_space(piece, grid):
	pass

def check_lost(positions):
	pass

def get_shape():
	pass

# Step 1: draw text in the middle of the play box
# text: mesage to display
# size: font size
# color: color of the text
# surface: the surface to draw on
def draw_text_middle(text, size, color, surface):
    font = pygame.font.Font(None, size)
    message = font.render(text, 1, color)
    text_rect = message.get_rect(center=(top_left_x + play_width//2, top_left_y + play_height//2))
    surface.blit(message, text_rect)
    
   
# Step 2: 
# line color is (128,128,128) 
def draw_grid(surface, row, col):
    sx = top_left_x
    sy = top_left_y
    #block_size = 30
    #TODO: draw row horizontal line and col vertical lines for form a grid
    

def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    pass

def draw_window(surface):
    surface.fill((0,0,0))
    # Tetris Title
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('TETRIS', 1, (255,255,255))

    surface.blit(label, (top_left_x + play_width // 2 - (label.get_width() // 2), 30))

    # draw grid
    # draw_grid(surface, 20, 10)

    # draw boarder
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)
    pygame.display.update()

def main():
	draw_window(win)

def main_menu():
	pass

if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption('Tetris')      
    win.fill((0,0,0))
    draw_text_middle('Press any key to begin.', 60, (255, 255, 255), win)
    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                main()
    pygame.quit()

    