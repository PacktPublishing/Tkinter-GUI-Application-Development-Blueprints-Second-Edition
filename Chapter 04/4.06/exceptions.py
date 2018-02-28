"""
Code illustration: 4.06

    New classes added here:
        InvalidMove(ChessError)
        CheckMate(ChessError)
        Draw(ChessError)
        NotYourTurn(ChessError)
        InvalidCoord(ChessError)

@ Tkinter GUI Application Development Blueprints
"""
class ChessError(Exception): pass
class Check(ChessError): pass
class InvalidMove(ChessError): pass
class CheckMate(ChessError): pass
class Draw(ChessError): pass
class NotYourTurn(ChessError): pass
class InvalidCoord(ChessError): pass
