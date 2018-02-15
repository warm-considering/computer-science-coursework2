import pyglet
import time
import threading

def playshiawase():
    player = pyglet.media.Player()
    shiawase = pyglet.media.load("D:\\lads\\K-ON! Music History's Box [FLAC]\\Disc 07 - Image Song Season Two [Yui, Mio, Ritsu, Tsumugi, Azusa]\\02 - Hirasawa Yui - Shiawase Hiyori.flac")
    player.queue(shiawase)
    player.play()
    pyglet.app.run()

thread = threading.Thread(target=playshiawase, args=())
thread.daemon = True
thread.start()
