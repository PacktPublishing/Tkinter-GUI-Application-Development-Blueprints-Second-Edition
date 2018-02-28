from tkinter import *
import itertools

class ScoreMaker:

  NOTES = ['C1','D1', 'E1', 'F1', 'G1','A1', 'B1', 'C2','D2', 'E2', 'F2', 'G2','A2', 'B2']
  

  def __init__(self, container):
    self.canvas = Canvas(container,  width=500, height = 110)
    self.canvas.grid(row=0, column = 1)
    container.update_idletasks() 
    self.canvas_width = self.canvas.winfo_width()
    self.sharp_image = PhotoImage(file='../pictures/sharp.gif')
    self.treble_clef_image = PhotoImage(file='../pictures/treble-clef.gif')
    self.x_counter = itertools.count(start=50, step=30)
    
    
  def _clean_score_sheet(self):
    self.x_counter = itertools.count(start=50, step=30)
    self.canvas.delete("all")
    
  
  def _create_treble_staff(self):
    self._draw_five_lines()
    self.canvas.create_image(10, 20, image=self.treble_clef_image, anchor=NW)
    

  def draw_chord(self, chord):
    self._clean_score_sheet()
    self._create_treble_staff()
    for note in chord:
      self._draw_single_note(note, is_in_chord=True)

    
  def _draw_five_lines(self):
    w = self.canvas_width
    self.canvas.create_line(0,40,w,40, fill="#555")
    self.canvas.create_line(0,50,w,50, fill="#555")
    self.canvas.create_line(0,60,w,60, fill="#555")
    self.canvas.create_line(0,70,w,70, fill="#555")
    self.canvas.create_line(0,80,w,80, fill="#555")
      

  def draw_notes(self, notes):
    self._clean_score_sheet()
    self._create_treble_staff()
    for note in notes:
      self._draw_single_note(note)

  def _draw_single_note(self, note, is_in_chord=False):
    is_sharp = "#" in note   
    note = note.replace("#","")
    radius = 9
    if is_in_chord:
      x = 75
    else:  
      x = next(self.x_counter)
    i =  self.NOTES.index(note)
    y = 85-(5*i)
    self.canvas.create_oval(x,y,x+radius, y+ radius, fill="#555")
    if is_sharp:
      self.canvas.create_image(x-10,y, image=self.sharp_image, anchor=NW)
    if note=="C1":
       self.canvas.create_line(x-5,90,x+15, 90, fill="#555")
    elif note=="G2":
       self.canvas.create_line(x-5,35,x+15, 35, fill="#555")
    elif note=="A2":
       self.canvas.create_line(x-5,35,x+15, 35, fill="#555")
    elif note=="B2":
       self.canvas.create_line(x-5,35,x+15, 35, fill="#555")
       self.canvas.create_line(x-5,25,x+15, 25, fill="#555") 



if __name__ == "__main__":
  root = Tk()
  s = ScoreMaker(root)
  #notes = ['C1','D1', 'E1', 'F1', 'G1','A1', 'B1', 'C2','D2', 'E2', 'F2', 'G2','A2', 'B2']
  #s.draw_notes(notes)
  chord = ['C1', 'E1', 'G1', ]
  s.draw_chord(chord)
  root.mainloop()
