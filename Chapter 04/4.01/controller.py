"""
Code illustration: 4.01

@ Tkinter GUI Application Development Blueprints
"""
from configurations import *
import model


class Controller():

    def __init__(self):
        self.init_model()

    def init_model(self):
        self.model = model.Model()
