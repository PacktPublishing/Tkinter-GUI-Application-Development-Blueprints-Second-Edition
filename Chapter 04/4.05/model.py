"""
Code illustration: 4.05

    New methods added here:
        get_all_available_moves(color)


@ Tkinter GUI Application Development Blueprints
"""
from configurations import *
import piece


class Model(dict):

    captured_pieces = {'white': [], 'black': []}
    player_turn = None
    halfmove_clock = 0
    fullmove_number = 1
    history = []

    def __init__(self):
        self.reset_to_initial_locations()

    def get_all_available_moves(self, color):
        result = []
        for position in self.keys():
            piece = self.get_piece_at(position)
            if piece and piece.color == color:
                moves = piece.moves_available(position)
                if moves:
                    result.extend(moves)
        return result

    def all_positions_occupied_by_color(self, color):
        result = []
        for position in self.keys():
            piece = self.get_piece_at(position)
            if piece.color == color:
                result.append(position)
        return result

    def all_occupied_positions(self):
        return self.all_positions_occupied_by_color('white') + self.all_positions_occupied_by_color('black')

    def reset_game_data(self):
        captured_pieces = {'white': [], 'black': []}
        player_turn = None
        halfmove_clock = 0
        fullmove_number = 1
        history = []

    def reset_to_initial_locations(self):
        self.clear()
        for position, value in START_PIECES_POSITION.items():
            self[position] = piece.create_piece(value)
            self[position].keep_reference(self)
        self.player_turn = 'white'

    def get_piece_at(self, position):
        return self.get(position)

    def get_alphanumeric_position(self, rowcol):
        if self.is_on_board(rowcol):
            row, col = rowcol
            return "{}{}".format(X_AXIS_LABELS[col], Y_AXIS_LABELS[row])

    def is_on_board(self, rowcol):
        row, col = rowcol
        return 0 <= row <= 7 and 0 <= col <= 7

    def get_alphanumeric_position_of_king(self, color):
        for position in self.keys():
            this_piece = self.get_piece_at(position)
            if isinstance(this_piece, piece.King) and this_piece.color == color:
                return position

    def is_king_under_check(self, color):
        position_of_king = self.get_alphanumeric_position_of_king(color)
        opponent = ('black' if color == 'white' else 'white')
        return position_of_king in self.get_all_available_moves(opponent)
