"""
Code illustration: 5.07

@Tkinter GUI Application Development Blueprints
"""

import pyglet

FORWARD_REWIND_JUMP_TIME = 20


class Player:

    def __init__(self):
        self.player = pyglet.media.Player()
        self.player.volume = 0.6

    def play_media(self, audio_file):
        self.reset_player()
        self.player = pyglet.media.Player()
        self.source = pyglet.media.load(audio_file)
        self.player.queue(self.source)
        self.player.play()

    def reset_player(self):
        self.player.pause()
        self.player.delete()
        
    def is_playing(self):
        try:
            elapsed_time = int(self.player.time)
            is_playing =  elapsed_time < int(self.track_length)
        except:
            is_playing = False
        return is_playing

    def seek(self, time):
        try:
            self.player.seek(time)
        except AttributeError:
            pass

    @property
    def track_length(self):
        try:
            return self.source.duration
        except AttributeError:
            return 0

    @property
    def volume(self):
        return self.player.volume

    @property
    def elapsed_play_duration(self):
        return self.player.time

    @volume.setter
    def volume(self, volume):
        self.player.volume = volume

    def unpause(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.reset_player()

    def mute(self):
        self.player.volume = 0.0

    def unmute(self, newvolume_level):
        self.player.volume = newvolume_level

    def fast_forward(self):
        time = self.player.time + FORWARD_REWIND_JUMP_TIME
        try:
            if self.source.duration > time:
                self.seek(time)
            else:
                self.seek(self.source.duration)
        except AttributeError:
            pass

    def rewind(self):
        time = self.player.time - FORWARD_REWIND_JUMP_TIME
        try:
            self.seek(time)
        except:
            self.seek(0)
