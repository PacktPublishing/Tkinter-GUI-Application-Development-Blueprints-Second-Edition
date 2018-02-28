"""
Code illustration: 9.05
    urllib demo
Tkinter GUI Application Development Blueprints
"""
import urllib.request
with urllib.request.urlopen('http://www.packtpub.com/') as f:
    print(f.read())
