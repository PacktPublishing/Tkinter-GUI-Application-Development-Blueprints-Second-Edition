"""
Code illustration: 4.06

@ Tkinter GUI Application Development Blueprints
"""
from configurations import *
import sys
import exceptions


def create_piece(piece, color='white'):
    if isinstance(piece, str):
        if piece.upper() in SHORT_NAME.keys():
            color = "white" if piece.isupper() else "black"
            piece = SHORT_NAME[piece.upper()]
        piece = piece.capitalize()
        if piece in SHORT_NAME.values():
            return eval("{classname}(color)".format(classname=piece))
    raise exceptions.ChessError("invalid piece name: '{}'".format(piece))


def get_numeric_notation(rowcol):
    row, col = rowcol
    return int(col) - 1, X_AXIS_LABELS.index(row)


class Piece():

    def __init__(self, color):
        self.name = self.__class__.__name__.lower()
        if color == 'black':
            self.name = self.name.lower()
        elif color == 'white':
            self.name = self.name.upper()
        self.color = color

    def keep_reference(self, model):
        self.model = model

    def moves_available(self, current_position, directions, distance):
        model = self.model
        allowed_moves = []
        piece = self
        start_row, start_column = get_numeric_notation(current_position)
        for x, y in directions:
            collision = False
            for step in range(1, distance + 1):
                if collision:
                    break
                destination = start_row + step * x, start_column + step * y
                if self.possible_position(destination) not in model.all_occupied_positions():
                    allowed_moves.append(destination)
                elif self.possible_position(destination) in model.all_positions_occupied_by_color(piece.color):
                    collision = True
                else:
                    allowed_moves.append(destination)
                    collision = True
        allowed_moves = filter(model.is_on_board, allowed_moves)
        return map(model.get_alphanumeric_position, allowed_moves)

    def possible_position(self, destination):
        return self.model.get_alphanumeric_position(destination)


class King(Piece):
    directions = ORTHOGONAL_POSITIONS + DIAGONAL_POSITIONS
    max_distance = 1

    def moves_available(self, current_position):
        return super().moves_available(current_position, self.directions, self.max_distance)


class Queen(Piece):
    directions = ORTHOGONAL_POSITIONS + DIAGONAL_POSITIONS
    max_distance = 8

    def moves_available(self, current_position):
        return super().moves_available(current_position, self.directions, self.max_distance)


class Rook(Piece):
    directions = ORTHOGONAL_POSITIONS
    max_distance = 8

    def moves_available(self, current_position):
        return super().moves_available(current_position, self.directions, self.max_distance)


class Bishop(Piece):
    directions = DIAGONAL_POSITIONS
    max_distance = 8

    def moves_available(self, current_position):
        return super().moves_available(current_position, self.directions, self.max_distance)


class Knight(Piece):

    def moves_available(self, current_position):
        model = self.model
        allowed_moves = []
        start_col, start_row = get_numeric_notation(current_position.upper())
        piece = model.get(current_position)
        for x, y in KNIGHT_POSITIONS:
            destination = start_col + x, start_row + y
            if model.get_alphanumeric_position(destination) not in model.all_positions_occupied_by_color(piece.color):
                allowed_moves.append(destination)
        allowed_moves = filter(model.is_on_board, allowed_moves)
        return map(model.get_alphanumeric_position, allowed_moves)


class Pawn(Piece):

    def moves_available(self, current_position):
        model = self.model
        piece = self
        if self.color == 'white':
            initial_position, direction, enemy = 1, 1, 'black'
        else:
            initial_position, direction, enemy = 6, -1, 'white'
        allowed_moves = []
        # Moving
        prohibited = model.all_occupied_positions()
        start_position = get_numeric_notation(current_position.upper())
        forward = start_position[0] + direction, start_position[1]
        if model.get_alphanumeric_position(forward) not in prohibited:
            allowed_moves.append(forward)
            if start_position[0] == initial_position:
                # If pawn is in starting position allow double moves
                double_forward = (forward[0] + direction, forward[1])
                if model.get_alphanumeric_position(double_forward) not in prohibited:
                    allowed_moves.append(double_forward)
        # Attacking
        for a in range(-1, 2, 2):
            attack = start_position[0] + direction, start_position[1] + a
            if model.get_alphanumeric_position(attack) in model.all_positions_occupied_by_color(enemy):
                allowed_moves.append(attack)
        allowed_moves = filter(model.is_on_board, allowed_moves)
        return map(model.get_alphanumeric_position, allowed_moves)
