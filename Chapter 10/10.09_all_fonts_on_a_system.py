"""
Code illustration: 10.09
        Fetching tuple of all fonts installed on a system
Tkinter GUI Application Development Blueprints
"""
from tkinter import Tk, font
root = Tk()
all_fonts = font.families()
print(all_fonts)
