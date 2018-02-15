import pafy
info = pafy.new("vYlgTIS7mVg")
bigthumbhd = info.bigthumbhd
print(bigthumbhd)
watchid = info.videoid
playlist = pafy.get_playlist("RD"+str(watchid))
print(playlist['pafy'])
