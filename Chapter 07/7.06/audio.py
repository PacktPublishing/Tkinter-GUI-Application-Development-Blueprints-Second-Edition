import simpleaudio as sa
from _thread import start_new_thread
import time

def play_note(note_name):
  wave_obj = sa.WaveObject.from_wave_file('../sounds/' + note_name + '.wav')
  wave_obj.play()

def play_scale(scale):
  for note in scale:
    play_note(note)
    time.sleep(0.5)

def play_scale_in_new_thread(scale):
  start_new_thread(play_scale,(scale,))

def play_chord(scale):
  for note in scale:
    play_note(note)

def play_chord_in_new_thread(chord):
  start_new_thread(play_chord,(chord,))
