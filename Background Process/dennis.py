import threading
from pydub import AudioSegment
from pydub.playback import play
import time
def shiawasehiyori():
    song = AudioSegment.from_file("D:\\lads\\K-ON! Music History's Box [FLAC]\\Disc 07 - Image Song Season Two [Yui, Mio, Ritsu, Tsumugi, Azusa]\\02 - Hirasawa Yui - Shiawase Hiyori.flac", "flac")
    play(song)
thread = threading.Thread(target=shiawasehiyori, args=())
thread.daemon = True
thread.start()
time.sleep(5)
print('''
Uraraka osanpo hiyori mune ippai shinkokyuu hiyori 
Ichi jikan hayaku natta mezamashi ga kureta chiisai odekake taimu

Glorious, perfect weather for a stroll, perfect weather to fill your lungs with air 
The alarm clock went off an hour early so there's a little time to go out

Fukufuku koinu fuwafuwa na kumo purantaa no hana ni mo ne 
Egao ga koborechau yo doushite ka na? 
Wakannai demo ne... ufufu

Sniffing puppy, fluffy clouds, and the flowers in the pot 
I can't stop smiling, I wonder why? 
I don't know but... tehehe

Nikkori to ne "ohayou" shiranai hito ni mo "ohayou" 
Ikiterutte ii na hayaokitte ii na ohirune mo ii kedo ne 
Ranra

I say "Good morning" with a happy smile, say "Good morning" to a person I don't know 
It's nice to be alive, it's nice to be up early, though afternoon naps are nice too 
Lanla

Ippo niho osanpo hiyori uta utatte hamingu hiyori 
Dare to mo yakusoku shite nakutemo heiki jiyuu na odekake taimu

One step, two steps, perfect weather for a stroll, perfect weather for singing and humming 
Even if I don't have plans with someone it's fine, there's time to go out where ever I like

Sunaba no oshiro kankeri suberidai buranko wa junbanmachi 
Miteta hazu ga sanka shiteru doushite ka na? 
Wakannai yappashi... ufufu

Sand castles, kick the can, the slide, waiting for a turn at the swing 
I want to try them, I wonder why? 
I don't know after all, tehehe

Sakki no koinu... koinu na no ka naa 
Moshikashite chiisai inu no, otona datta no kamo... 
Haa~ kawaikatta naa.

That puppy from earlier... was he really a puppy? 
Maybe he was just a little dog, but a grown-up dog... 
Ah~ he sure was cute.

Otona demo kodomo demo inu wa inu hito wa hito watashi wa watashi 
Tanoshii wa tanoshii da ne itsudemo 
Wakatteru yo chanto... ufufu

Whether they're an adult or child, a dog is a dog, a person is a person, and I am me 
Fun things are fun, no matter what 
I'll always know that... tehehe

Uraraka osanpo hiyori mune ippai shinkokyuu hiyori 
Ichi jikan hayaku natta mezamashi ga kureta ooki na shiawase taimu 
Lanla

Glorious, perfect weather for a stroll, perfect weather to fill your lungs with air 
The alarm clock went off an hour early so there's a ton of time time to be happy 
Lanla
''')
