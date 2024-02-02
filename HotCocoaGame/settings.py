import pygame as pg
import math

pg.init()

## SCREEN SIZING ##
WIDTH = 500
HEIGHT = 700

## CREATING CANVAS ##
canvas = pg.display.set_mode((500, 700), pg.DOUBLEBUF)

## CANVAS LOGO AND TITLE ##
pg.display.set_caption("Fill My Hot Cocoa") 
icon = pg.image.load("/Users/erantroshani/Documents/CODING_PROJECTS/HotCocoaGame/images/hotCocoaIcon.png")
pg.display.set_icon(icon)

## SCROLLING BACKGROUND ##
# IMAGE 
bg = pg.image.load("/Users/erantroshani/Documents/CODING_PROJECTS/HotCocoaGame/images/scrollingbg.png").convert_alpha()
# Scale the image to the new size while maintaining aspect ratio
bg = pg.transform.scale(bg, (WIDTH, HEIGHT))
bg.set_alpha(40)
# scroll variable 
scroll = 0
# CHANGE THE BELOW 1 TO UPPER NUMBER IF YOU GET BUFFERING OF THE IMAGE HERE 1 IS THE CONSTATNT FOR REMOVING BUFFERING 
tiles = math.ceil(WIDTH / bg.get_width()) + 1

## FONTS ##
font = pg.font.SysFont('Lucida Console', 33)
scoreFont = pg.font.SysFont('Lucida Console', 25)
textFont = pg.font.SysFont('Lucida Console', 28, bold = True)
fontTitle = pg.font.SysFont('Impact', 110)
fontSubTitle = pg.font.SysFont('Lucida Console', 40)

##  MAIN VARIABLES  ##
#Screens
main_menu       = True
name_menu       = False
game_menu       = False
scores_menu     = False
win_menu        = False
lost_menu       = False
exit            = True

#Object variables
cocoaLives  = 1
cocoaScore  = 0

#Timing variables
spriteInterval      = 1
spriteCreationTime  = 1

#ROUNDS
round1 = True
round2 = False


##  ELEMENTS  ##
## Name Input Box variables
userText        = ""
colorActive     = pg.Color('white')
colorPassive    = pg.Color('#F6C6BD')
color           = colorPassive
inputRect       = pg.rect.Rect((150, 370), (200, 40))
outerRect       = pg.rect.Rect((100, 310), (300, 200))
active          = False
charCount       = 0
limitCount      = 12


