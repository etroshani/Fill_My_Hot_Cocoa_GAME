import pygame as pg
import math
import time

from settings import *


# TITLES ANIMATION CLASS
class titleAnimation:
    def __init__(self, title1, title2):
        self.title1 = title1
        self.title2 = title2
        self.amplitude = 15
        self.frequency = 4
        self.speed     = 0.8

    def animation(self):
        # rendering a TITLE
        title1 = font.render(self.title1, True, "white")
        title2 = fontTitle.render(self.title2, True, "white")
        
        # Get the size of the rendered text
        title1_width, title1_height = title1.get_size()
        title2_width, title2_height = title2.get_size()

        # Create rectangles for the titles
        titleRect1 = pg.rect.Rect((0, 0), (title1_width, title1_height))
        titleRect1.center = (97, 125)

        titleRect2 = pg.rect.Rect((0, 0), (title2_width, title2_height))
        titleRect2.center = (250, 180)

        # Calculate sinusoidal movement
        sinusMovement = int(self.amplitude * math.sin(self.frequency * (self.speed * time.time())))

        # Apply sinusoidal movement to title rectangles
        titleRect1.centery += sinusMovement
        titleRect2.centery += sinusMovement

        # Blit the titles with the updated positions
        canvas.blit(title1, titleRect1.topleft)
        canvas.blit(title2, titleRect2.topleft)



# BUTTONS CLASS
class playButton:
    def __init__(self, text, x_pos, y_pos, enabled, color):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.button_width = 200
        self.button_height = 60
        self.color = color

    def draw(self):
        button_text = font.render(self.text, True, 'white')
        text_width, text_height = button_text.get_size()

        # Calculate text position for centering
        text_x = self.x_pos + (self.button_width - text_width) // 2
        text_y = self.y_pos + (self.button_height - text_height) // 2

        button_rect = pg.rect.Rect((self.x_pos, self.y_pos), (self.button_width, self.button_height))

        pg.draw.rect(canvas, self.color, button_rect, 0, 5)
        pg.draw.rect(canvas, 'white', button_rect, 2, 5)
        canvas.blit(button_text, (text_x, text_y))
    
    def collidepoint(self, point):
        x_pos, y_pos = point
        return self.x_pos <= x_pos <= self.x_pos + self.button_width and self.y_pos <= y_pos <= self.y_pos + self.button_height


#SCORES CLASS
class scores:
    def __init__(self, name, score, x_pos, y_pos, color):
        self.name = name
        self.score = str(score)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.width = 350
        self.height = 60

    def draw(self):
        topScoresName = font.render(self.name, True, 'black')
        topScoresScore = font.render(self.score, True, 'black')
        topScoresText_width, topScoresText_height = topScoresScore.get_size()

        # Calculate text position for centering
        textName_x = self.x_pos + 20
        textScore_x = self.x_pos + self.width - (topScoresText_width + 20)
        text_y = self.y_pos + (self.height - topScoresText_height) // 2

        button_rect = pg.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))

        pg.draw.rect(canvas, self.color, button_rect, 0, 5)
        pg.draw.rect(canvas, 'white', button_rect, 2, 5)
        canvas.blit(topScoresName, (textName_x, text_y))
        canvas.blit(topScoresScore, (textScore_x, text_y))


class endGame:
    def __init__(self, message, score):
        self.message = message
        self.score = score
    
    def display(self):
        message = fontTitle.render(self.message, True, '#eb7e6a')
        message_width, message_height = message.get_size()
        messageRect = pg.rect.Rect((0, 0), (message_width, message_height))
        messageRect.center = (250, 160)
        scoreMessage = fontSubTitle.render('You scored: ' + str(self.score), True, '#eb7e6a')
        score_width, score_height = scoreMessage.get_size()
        scoreRect = pg.rect.Rect((0, 0), (score_width, score_height))
        scoreRect.center = (250, 240)
        canvas.blit(message, messageRect)
        canvas.blit(scoreMessage, scoreRect)