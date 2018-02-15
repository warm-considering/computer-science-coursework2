import pyglet

player = pyglet.media.Player()
shiawase = pyglet.media.load("Fuwa fuwa time - Yui Hirasawa VERSION + Lyrics (192kbit_AAC).mp3")
player.queue(shiawase)
print(shiawase.duration)
player.play()
print(player.time)
pyglet.app.run()
print(player.time)

