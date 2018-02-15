import pafy
import pyglet
from random import randint
import time
videourl = input("Please input the video url: ")
myvid = pafy.new(videourl)
playlist = myvid.mix
print(playlist)
stream = myvid.getbestaudio(preftype="m4a")
songname = myvid.title.replace("/", "").replace(":", "").replace("\\", "").replace("*", "").replace("?","").replace('"', '').replace("<", "").replace(">","").replace("|","")
try:
    stream.download("songs\\"+songname+'.m4a', quiet=True)
except:
    print("file already exists")
time.sleep(0.4)
song = pyglet.media.load("songs\\"+songname+'.m4a')
player = pyglet.media.Player()
player.queue(song)
player.play()
pyglet.app.run()
