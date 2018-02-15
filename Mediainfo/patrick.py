from pydub.utils import mediainfo
info = mediainfo("D:\\lads\\K-ON! Music History's Box [FLAC]\\Disc 07 - Image Song Season Two [Yui, Mio, Ritsu, Tsumugi, Azusa]\\02 - Hirasawa Yui - Shiawase Hiyori.flac")
tags = info.get("TAG")
album = tags.get("ALBUM")
print(album)
