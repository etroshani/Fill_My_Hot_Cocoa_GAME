import pygame as pg


## SOUNDS AND MUSIC ##
pg.mixer.init()
button_sfx = pg.mixer.Sound("/Users/erantroshani/Documents/CODING_PROJECTS/HotCocoaGame/sound/buttonsfx.wav")
goodMarsh_sfx = pg.mixer.Sound("/Users/erantroshani/Documents/CODING_PROJECTS/HotCocoaGame/sound/goodMarshsfx.mp3")
badMarsh_sfx = pg.mixer.Sound("/Users/erantroshani/Documents/CODING_PROJECTS/HotCocoaGame/sound/badMarshsfx.mp3")
win_sfx = pg.mixer.Sound("/Users/erantroshani/Documents/CODING_PROJECTS/HotCocoaGame/sound/gamewinsfx.mp3")
win_sound = False

songs = {
    "menu": "/Users/erantroshani/Documents/CODING_PROJECTS/HotCocoaGame/sound/musicsfx.mp3",
    "gameplay": "/Users/erantroshani/Documents/CODING_PROJECTS/HotCocoaGame/sound/gamemusicsfx.mp3",
}
current_song = ""