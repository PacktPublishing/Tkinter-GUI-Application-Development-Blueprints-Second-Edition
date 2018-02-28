"""
Code illustration: 4.04

@ Tkinter GUI Application Development Blueprints
"""

NUMBER_OF_ROWS = 8
NUMBER_OF_COLUMNS = 8
DIMENSION_OF_EACH_SQUARE = 64
BOARD_COLOR_1 = "#e6a803"
BOARD_COLOR_2 = "#8b8350"

X_AXIS_LABELS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
Y_AXIS_LABELS = (1, 2, 3, 4, 5, 6, 7, 8)

SHORT_NAME = {  
'R':'Rook',  'N':'Knight',  'B':'Bishop',  
'Q':'Queen',  'K':'King',  'P':'Pawn'
}

# remember capital letters - White pieces, Small letters - Black pieces 
START_PIECES_POSITION  = { 
"A8": "r", "B8": "n", "C8": "b", "D8": "q", "E8": "k", "F8": "b", "G8": "n", "H8": "r",
"A7": "p", "B7": "p", "C7": "p", "D7": "p", "E7": "p", "F7": "p", "G7": "p", "H7": "p", 
"A2": "P", "B2": "P", "C2": "P", "D2": "P", "E2": "P", "F2": "P", "G2": "P", "H2": "P", 
"A1": "R", "B1": "N", "C1": "B", "D1": "Q", "E1": "K", "F1": "B", "G1": "N", "H1": "R" 
    }

ORTHOGONAL_POSITIONS  = ((-1,0),(0,1),(1,0),(0, -1))
DIAGONAL_POSITIONS  = ((-1,-1),(-1,1),(1,-1),(1,1))
KNIGHT_POSITIONS = ((-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1))
