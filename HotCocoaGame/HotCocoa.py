import pygame as pg
import random
import time
import pandas as pd
import cProfile

from settings import *
from ui import canvas, titleAnimation, playButton, scores, endGame
from sprites import Sprite, objectsSprite
from sounds import *


def shapeImages(image, scaling_factor):
    original_image = pg.image.load(image).convert_alpha()

    # Get original dimensions
    original_rect = original_image.get_rect()
    original_width = original_rect.width
    original_height = original_rect.height

    # Calculate new dimensions
    new_width = int(original_width * scaling_factor)
    new_height = int(original_height * scaling_factor)
    
    # Scale the image to the new size while maintaining aspect ratio
    image = pg.transform.scale(original_image, (new_width, new_height))

    return image, new_width, new_height


##  FUNCTION : SAVES SCORES IN DF  ##
def saveScore(score, name):
    global df
    #Saving the score in the dataframe
    newScore = pd.DataFrame({'SCORES': [score], 'NAME': [name]})
    df = pd.concat([df, newScore], ignore_index=True)
    df = df.sort_values(by='SCORES', ascending=False)
    df.to_excel('HotCocoaScoresheet.xlsx', index=False)

##  FUNCTION : SHOWS SCORE IN GAME  ##
def show_score(score, x,y):
    score = scoreFont.render('Score: ' + str(score), True, 'white')
    text_width, text_height = score.get_size()

    # Calculate text position for centering
    text_x = x + (150 - text_width) // 2
    text_y = y + (40 - text_height) // 2

    button_rect = pg.rect.Rect((x, y), (150, 40))

    pg.draw.rect(canvas, '#F09F90', button_rect, 0, 5)
    pg.draw.rect(canvas, 'white', button_rect, 2, 5)
    canvas.blit(score, (text_x, text_y))


##  FUNCTION : SPRITE CREATIO AND LEVEL LOGIC  ##
# Creates object sprites based on probability, with specific movement patterns based on advancement in game
def create_object_sprites(score, probability):
    global win_menu
    global game_menu
    global spriteInterval

    sprite_type = 'mainMarsh' if probability <= 0.9 else 'badMarsh'
    movement_type = 'straight'
    if score < 10:
        spriteInterval = 1.5
    if 10 <= score < 20:
        spriteInterval = 1
    if 20 <= score <= 30:
        spriteInterval = 0.75
    if 30 <= score < 50:
        movement_type = 'sinus'
    if 50 <= score < 70:
        movement_type = 'sinus2'
    if 70 <= score:
        spriteInterval = 0.5
    if score == 1000:
        win_menu = True
        game_menu = False

    # Sprite Creation
    if sprite_type == 'mainMarsh':
        new_sprite = objectsSprite(mainMarshImage, random.randint(0, 430), -100, sprite_type, movement_type)
    if sprite_type == 'badMarsh':
        new_sprite = objectsSprite(badMarshImage, random.randint(0, 430), -100, sprite_type, movement_type)
    objectSpriteList.add(new_sprite)


###       VARIABLES       ##
## IMAGES
mainMarshImage, mainMarshWidth, mainMarshHeight = shapeImages("/Users/erantroshani/Documents/CODING_PROJECTS/HotCocoaGame/images/mainMarshmellow1.png", 0.03)
badMarshImage, badMarshWidth, badMarshHeight    = shapeImages("/Users/erantroshani/Documents/CODING_PROJECTS/HotCocoaGame/images/bomb.png", 0.02)
cocoaImage, cocoaWidth, cocoaHeight             = shapeImages("/Users/erantroshani/Documents/CODING_PROJECTS/HotCocoaGame/images/hotCocoaIcon.png", 0.15)

##  MAIN SPRITE  ##
# Cocoa Sprite instance
cocoaSprite = Sprite(cocoaImage, 0, 0, cocoaWidth, cocoaHeight)
cocoaWidth  = cocoaSprite.rect.width
# Positioning the sprite
cocoaSprite.rect.x = 250 - (cocoaWidth/2)
cocoaSprite.rect.y = 570
# Creating sprites group
objectSpriteList    = pg.sprite.Group()
mainSpriteList      = pg.sprite.Group()
mainSpriteList.add(cocoaSprite)

## BUTTONS
play_button     = playButton('PLAY', 150, 320, True, '#B96A59' )
scores_button   = playButton('SCORES', 150, 390, True, '#B96A59' )
quit_button     = playButton('QUIT', 150, 460, True, '#B96A59' )
restartButton   = playButton('RESTART', 150, 350, True, '#B96A59' )
mainMenuButton  = playButton('MAIN MENU', 150, 420, True, '#B96A59' )
nameButton      = playButton('START', 150, 425, True, '#B96A59')

##  DATAFRAME FOR SCORES  ##
df = pd.read_excel("HotCocoaScoresheet.xlsx")

## SCORECARD (in scores_menu)
scoreRect           = pg.rect.Rect((50, 50), (400, 500))
scoreMainMenuButton = playButton('MAIN MENU', 150, 590, True, '#B96A59' )



###     GAME LOOP     ###
while exit: 

    #F6C6BD
    canvas.fill("#F6C6BD")

    # APPENDING THE IMAGE TO THE BACK 
    # OF THE SAME IMAGE 
    i = 0
    while(i < tiles):
        position =  scroll - bg.get_height() + bg.get_height()*i
        canvas.blit(bg, (-15, position))
        i += 1
    # FRAME FOR SCROLLING 
    scroll += 0.2

    # RESET THE SCROLL FRAME 
    if abs(scroll) > bg.get_height(): 
        scroll = 0


    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pg.mouse.get_pos()

    ####    MUSIC    ####
    if main_menu or name_menu or scores_menu:
        if current_song != "menu":
            pg.mixer.music.load(songs['menu'])
            pg.mixer.music.play(loops=-1, fade_ms=1500)
            pg.mixer.music.set_volume(0.5)
            current_song = "menu"

    if game_menu:
        if current_song != "gameplay":
            pg.mixer.music.load(songs['gameplay'])
            pg.mixer.music.play(loops=-1, fade_ms=3000)
            pg.mixer.music.set_volume(0.8)
            current_song = "gameplay"

            

    ####    SCREENS    ####
    if main_menu == True:

        # TITLE
        title = titleAnimation("Fill My", "Hot Cocoa")
        title.animation()
        play_button.draw()
        scores_button.draw()
        quit_button.draw()


        ###  MAIN SPRITE CONTROL  ###
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            cocoaSprite.moveLeft()
        if keys[pg.K_RIGHT]:
            cocoaSprite.moveRight()
        # Wrapping the sprite around the screen
        cocoaSprite.wrapAroundScreen(WIDTH, cocoaWidth)

        mainSpriteList.update()
        mainSpriteList.draw(canvas)


    if name_menu == True:
        title = titleAnimation("Fill My", "Hot Cocoa")
        title.animation()

        if active:
            color = colorActive
        else:
            color = colorPassive

        pg.draw.rect(canvas, '#F09F90', outerRect, 0, 5)
        pg.draw.rect(canvas, 'white', outerRect, 5, 5)
        pg.draw.rect(canvas, color, inputRect, 0, 5)
        textSurface = textFont.render("Enter your name", True, (255, 255, 255))
        textSurface_width, textSurface_height = textSurface.get_size() 
        canvas.blit(textSurface, (WIDTH/2 - textSurface_width/2, inputRect.y-40)) 
        inputSurface = scoreFont.render(userText, True, "#B96A59") 
        canvas.blit(inputSurface, (inputRect.x+5, inputRect.y + 8)) 
        nameButton.draw()

        ###  MAIN SPRITE CONTROL  ###
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            cocoaSprite.moveLeft()
        if keys[pg.K_RIGHT]:
            cocoaSprite.moveRight()
        # Wrapping the sprite around the screen
        cocoaSprite.wrapAroundScreen(WIDTH, cocoaWidth)

        mainSpriteList.update()
        mainSpriteList.draw(canvas)


    if game_menu == True:
        if cocoaLives > 0:
            ###  SPRITE COLLISIONS  ###
            for sprite in objectSpriteList:
                
                # Regular marshmellow hits cup
                if sprite.type == 'mainMarsh' and sprite.rect.colliderect(cocoaSprite.hitbox):
                    goodMarsh_sfx.play()
                    sprite.kill()
                    cocoaScore += 1
                    print(cocoaScore)
                
                # Bad marshmellow hits cup
                if sprite.type == 'badMarsh' and sprite.rect.colliderect(cocoaSprite.hitbox):
                    badMarsh_sfx.play()
                    sprite.kill()
                    cocoaLives -= 1
                    print("Lives: " + str(cocoaLives))
                
                # Regular marshmellow misses the cup
                if sprite.type == "mainMarsh" and sprite.rect.y >= HEIGHT:
                    badMarsh_sfx.play()
                    sprite.kill()
                    cocoaLives -= 1
                    print("Lives: " + str(cocoaLives))

            ###  LEVELS  ###
            #   ROUND 1   #
            if round1 == True:
                ###  OBJECT SPRITES CREATION  ###
                currentTime = time.time()
                if currentTime - spriteCreationTime >= spriteInterval:
                    spriteCreationTime = currentTime
                    probability = random.random()
                    create_object_sprites(cocoaScore, probability)

                # Update based on the level
                for sprite in objectSpriteList:
                    sprite.update_based_on_level(cocoaScore)

                # Update and draw object sprites
                objectSpriteList.draw(canvas)
                show_score(cocoaScore,10,10)


            ###  MAIN SPRITE CONTROL  ###
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                cocoaSprite.moveLeft()
            if keys[pg.K_RIGHT]:
                cocoaSprite.moveRight()
            # Wrapping the sprite around the screen
            cocoaSprite.wrapAroundScreen(WIDTH, cocoaWidth)

            mainSpriteList.update()
            mainSpriteList.draw(canvas)


        else:
            lost_menu = True


    if scores_menu == True:
        pg.draw.rect(canvas, '#B96A59', scoreRect, 0, 5)
        pg.draw.rect(canvas, 'white', scoreRect, 5, 5)
        scoreMainMenuButton.draw()
        scoreText = fontSubTitle.render("SCORECARD", True, (255, 255, 255))
        scoreText_width, scoreText_height = scoreText.get_size() 
        canvas.blit(scoreText, (WIDTH/2 - scoreText_width/2, scoreRect.y+30)) 

        # Dataframe for scores
        df = pd.read_excel("HotCocoaScoresheet.xlsx")

        #TOP 5
        name1, score1 = df["NAME"][0], df["SCORES"][0] 
        top1 = scores(name1, score1, 75, 150, "#F6C6BD")
        name2, score2 = df["NAME"][1], df["SCORES"][1] 
        top2 = scores(name2, score2, 75, (top1.y_pos + top1.height + 10), "#F6C6BD")
        name3, score3 = df["NAME"][2], df["SCORES"][2]
        top3 = scores(name3, score3, 75, (top2.y_pos + top2.height + 10), "#F6C6BD") 
        name4, score4 = df["NAME"][3], df["SCORES"][3] 
        top4 = scores(name4, score4, 75, (top3.y_pos + top3.height + 10), "#F6C6BD") 
        name5, score5 = df["NAME"][4], df["SCORES"][4] 
        top5 = scores(name5, score5, 75, (top4.y_pos + top4.height + 10), "#F6C6BD") 
        
        #TOP 5 display
        top1.draw()
        top2.draw()
        top3.draw()
        top4.draw()
        top5.draw()


    if lost_menu == True:
        lostMessage = endGame("YOU LOST", str(cocoaScore))
        lostMessage.display()
        restartButton.draw()
        mainMenuButton.draw()
        pg.mixer.music.stop()


    if win_menu == True:
        winMessage = endGame("YOU WON!!", str(cocoaScore))
        winMessage.display()
        restartButton.draw()
        mainMenuButton.draw()
        if win_sound == False:
            pg.mixer.music.stop()
            win_sfx.play()
            win_sound = True


    #####    EVENT HANDLER    #####
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            exit = False
        if main_menu == True:
            if play_button.collidepoint(mouse):
                play_button = playButton('PLAY', 150, 310, True, '#F09F90' )
                play_button.draw()

            else:
                play_button = playButton('PLAY', 150, 310, True, '#B96A59' )
                play_button.draw()

            if scores_button.collidepoint(mouse):
                scores_button = playButton('SCORES', 150, 380, True, '#F09F90' )
                scores_button.draw()
            else:
                scores_button = playButton('SCORES', 150, 380, True, '#B96A59' )
                scores_button.draw()

            if quit_button.collidepoint(mouse):
                quit_button = playButton('QUIT', 150, 450, True, '#F09F90' )
                quit_button.draw()
            else:
                quit_button = playButton('QUIT', 150, 450, True, '#B96A59' )
                quit_button.draw()

            if event.type == pg.MOUSEBUTTONDOWN:
                if play_button.collidepoint(mouse):
                    button_sfx.play()
                    main_menu = False
                    name_menu = True


                if scores_button.collidepoint(mouse):
                    button_sfx.play()
                    main_menu   = False
                    scores_menu = True

                if quit_button.collidepoint(mouse):
                    button_sfx.play()
                    exit = False
        
        if name_menu == True:
            if nameButton.collidepoint(mouse):
                nameButton = playButton('START', 150, 425, True, '#F09F90')
                nameButton.draw()
            else:
                nameButton = playButton('START', 150, 425, True, '#B96A59')
                nameButton.draw()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    if charCount > 0:
                        userText = userText[:-1]
                        charCount -= 1
                else:
                    if charCount < limitCount:
                        userText += event.unicode
                        charCount += 1
            
            if event.type == pg.MOUSEBUTTONDOWN: 
                if inputRect.collidepoint(mouse):
                    active = True
                else:
                    active = False
                
                if nameButton.collidepoint(mouse):
                    button_sfx.play()
                    name_menu = False
                    game_menu = True

        if scores_menu == True:
            if scoreMainMenuButton.collidepoint(mouse):
                scoreMainMenuButton = playButton('MAIN MENU', 150, 590, True, '#F09F90' )
                scoreMainMenuButton.draw()
            else:
                scoreMainMenuButton = playButton('MAIN MENU', 150, 590, True, '#B96A59' )
                scoreMainMenuButton.draw()

            if event.type == pg.MOUSEBUTTONDOWN: 
                if scoreMainMenuButton.collidepoint(mouse):
                    button_sfx.play()
                    main_menu = True
                    scores_menu = False


        if lost_menu == True or win_menu == True:
            if event.type == pg.QUIT:
                #Saves the score
                saveScore(cocoaScore, userText) 
                exit = False
            if restartButton.collidepoint(mouse):
                restartButton = playButton('RESTART', 150, 350, True, '#F09F90' )
                restartButton.draw()
            else:
                restartButton = playButton('RESTART', 150, 350, True, '#B96A59' )
                restartButton.draw()

            if mainMenuButton.collidepoint(mouse):
                mainMenuButton = playButton('MAIN MENU', 150, 420, True, '#F09F90' )
                mainMenuButton.draw()
            else:
                mainMenuButton = playButton('MAIN MENU', 150, 420, True, '#B96A59' )
                mainMenuButton.draw()

            if event.type == pg.MOUSEBUTTONDOWN:
                if restartButton.collidepoint(mouse):
                    button_sfx.play()
                    main_menu   = False
                    game_menu   = True
                    lost_menu   = False
                    win_menu    = False
                    win_sound   = False
                    current_song = ""

                if mainMenuButton.collidepoint(mouse):
                    button_sfx.play()
                    main_menu   = True
                    game_menu   = False
                    lost_menu   = False
                    win_menu    = False
                    win_sound   = False
                    current_song = ""

                #Saves the score
                saveScore(cocoaScore, userText)

                #Reset
                objectSpriteList.empty()
                cocoaLives, cocoaScore = 1, 0
                spriteInterval, spriteCreationTime = 1, 2
                cocoaSprite.rect.x = 250 - (cocoaWidth/2)

        if game_menu == True:
            if event.type == pg.QUIT: 
                exit = False


    # Update the GUI
    pg.display.update()


pg.quit()

