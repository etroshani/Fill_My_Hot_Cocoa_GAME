import pygame as pg
import random
import math
import time

##   MAIN SPRITE CLASS   ##
class Sprite(pg.sprite.Sprite):
    def __init__(self, image, x, y, new_width, new_height):
        super().__init__()
 
        self.image = image
        self.new_width = new_width
        self.new_height = new_height
        
        # Get the rectangle that encloses the image
        self.rect = pg.Rect(self.image.get_rect().left , self.image.get_rect().top, new_width, new_height)

        # Positioning the sprite
        self.rect.x = x
        self.rect.y = y

        # COLLISION HITBOX
        self.offset = 30
        hitbox_width = new_width - self.offset
        hitbox_height = new_height - self.offset

        self.hitbox = pg.Rect(x + self.offset / 2, y + self.offset / 2, hitbox_width, hitbox_height)
 
        # MOVEMENT VARIABLES
        self.velocity_x = 0
        self.acceleration_x = 0
        self.max_speed = 3
        self.friction = 0.92

    def moveRight(self):
        self.acceleration_x = 0.1

    def moveLeft(self):
        self.acceleration_x = -0.1

    def update(self):
        # Apply acceleration to velocity
        self.velocity_x += self.acceleration_x
        # Apply friction
        self.velocity_x *= self.friction
        # Limit velocity to max speed
        self.velocity_x = max(-self.max_speed, min(self.velocity_x, self.max_speed))
        # Update position
        self.rect.x += self.velocity_x

        # Update hitbox position to follow the sprite
        self.hitbox.x = self.rect.x + self.offset / 2
        self.hitbox.y = self.rect.y + self.offset / 2

        # Reset acceleration
        self.acceleration_x = 0

    def wrapAroundScreen(self, WIDTH, cocoaWidth):
        # Wrapping the sprite around the screen
        if self.rect.x > WIDTH:
            self.rect.x = (0 - cocoaWidth)
        if self.rect.x < (0 - cocoaWidth):
            self.rect.x = WIDTH


##   OBJECT SPRITE CLASS   ##
class objectsSprite(pg.sprite.Sprite):
    def __init__(self, image, x, y, type, movement_type):
        super().__init__()

        self.image = image

        # Get the rectangle that encloses the image
        self.rect = self.image.get_rect()

        # Positioning the sprite
        self.rect.x = x
        self.rect.y = y
        self.float_y = float(self.rect.y)      # Float position for smooth movement

        # Setting the type
        self.type = type

        # Setting the movement type
        self.movement_type = movement_type

        self.phase_offset = random.uniform(0, 10 * math.pi)


    def update_based_on_level(self, score):
        if score < 30:
            if self.movement_type == 'straight':
                self.float_y += 0.5  # Vertical movement
                self.rect.y = int(self.float_y)

        # For sinusoidal movement
        if 30 <= score < 50:
            if self.movement_type == 'sinus':

                self.float_y += 0.85  # Vertical movement
                self.rect.y = int(self.float_y)
                """ 
                frequency = 2
                amplitude = 1.2
                self.rect.x += int(amplitude * math.sin(frequency * (3 * time.time()) + self.phase_offset))
                """
            else:
                self.float_y += 0.85  # Vertical movement
                self.rect.y = int(self.float_y)

        # For a more complex sinusoidal movement
        if 50 <= score <= 1000:
            if self.movement_type == 'sinus2':
                self.float_y += 1  # Vertical movement
                self.rect.y = int(self.float_y)

                """
                frequency = 2
                amplitude = 1.2
                self.rect.x += int(amplitude * math.sin(frequency * (4 * time.time()) + self.phase_offset))
                """
            else:
                self.float_y += 1  # Vertical movement
                self.rect.y = int(self.float_y)

                
                #self.rect.x += int(amplitude * math.sin(frequency * (3 * time.time()) + self.phase_offset))
