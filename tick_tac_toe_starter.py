import pygame, sys
from pygame.locals import *
import os.path
import time

#TODO: 
#(1) Need check if the game is a draw
#(2) Need reset the game after either a player wins or the game is a draw.

# define global variables
width  = 400
height = 400

white = (255, 255, 255)
line_color = (10,10,10)

filepath = os.path.dirname(__file__)
print(f"filepath: {filepath}")
x_img = pygame.image.load(os.path.join(filepath, 'x.png'))
o_img = pygame.image.load(os.path.join(filepath, 'o.png'))

#resizing images
x_img = pygame.transform.scale(x_img, (80,80))
o_img = pygame.transform.scale(o_img, (80,80))

pygame.init()
DISPLAYSURF = pygame.display.set_mode((width, height+100))
pygame.display.set_caption('Tick Tac Toe')

XO = 'x'          # the current player, either 'x' or 'o'
winner = None     # the winner of the game, either 'x', 'o' or None, which means not yet decided
draw = False      # indicate the game is a draw

board = [ [None, None, None],                 
          [None, None, None],                 
          [None, None, None]]



def game_start():
    DISPLAYSURF.fill(white)

    # horizontal line
    pygame.draw.line(DISPLAYSURF, line_color, (0, height//3), (width, height//3), 5)
    pygame.draw.line(DISPLAYSURF, line_color, (0, height*2//3), (width, height*2//3), 5)

    # vertical line
    pygame.draw.line(DISPLAYSURF, line_color, (width//3,0), (width//3, height), 5 )
    pygame.draw.line(DISPLAYSURF, line_color, (width*2//3, 0), (width*2//3, height), 5)

    draw_status()

def drawXO(row, col):
    global XO
    pos_x = 30 + col * width//3
    pos_y = 30 + row * height//3

    if XO == 'x':
        DISPLAYSURF.blit(x_img, (pos_x, pos_y))
        XO = 'o'
    else:
        DISPLAYSURF.blit(o_img, (pos_x, pos_y))
        XO = 'x'
    # draw_status()
    # pygame.display.update()


def draw_status():  
    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " win!"
    
    if draw: 
        message = 'Game Draw'

    font = pygame.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))

    # copy the rendered message onto the board
    DISPLAYSURF.fill ((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    DISPLAYSURF.blit(text, text_rect)
    pygame.display.update()

  
#based on the board status, decide which player 
def check_win():
    global board, winner, draw

    #check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            winner=board[row][0]
            break

    #check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            winner=board[0][col]
            break

    #top-left to bottom-right diagonal 
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        winner=board[0][0]

    #top-right to bottom-left diagonal 
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        winner=board[0][2]

    #Todo: check draw
    filled = True
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                filled = False
                break
    if filled and winner is None:
        draw = True

    draw_status()

def reset_game():
    global XO, winner, draw, board
    time.sleep(3)
    XO = 'x'          # the current player, either 'x' or 'o'
    winner = None     # the winner of the game, either 'x', 'o' or None, which means not yet decided
    draw = False      # indicate the game is a draw

    board = [ [None, None, None], 
          [None, None, None], 
          [None, None, None]]
    
    game_start()


def userclick():
    global XO, board

    #get coordinates of mouse click
    x,y = pygame.mouse.get_pos()
    print(f"x coordinate: {x}  y_coordinate: {y}")

    # compute (col, row) of the position (x, y) if we partion the width x height rectangle into 3x3 grid.
    if x < width/3:
        col = 0
    elif x < width*2/3:
        col = 1
    elif x < width:
        col = 2
    else: 
        col = None

    if y < height/3:
        row = 0
    elif y < height*2/3:
        row = 1
    elif y < height:
        row = 2
    else: 
        row = None
    
    print(f"row: {row}, col: {col}")

    if row != None and col != None and board[row][col] is None:
        board[row][col] = XO
        drawXO(row, col)
        check_win()

if __name__ == '__main__':
    game_start()

    while True: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type is MOUSEBUTTONDOWN:
                userclick()
                if winner or draw: 
                    reset_game()

        pygame.display.update()

