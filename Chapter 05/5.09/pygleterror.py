import pyglet

audio_file = 'test.mp3'
player = pyglet.media.Player()
source = pyglet.media.load(audio_file)
player.queue(source)
player.play()
