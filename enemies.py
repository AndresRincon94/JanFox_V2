"""
This module is used to hold the Enemy class. The Enemy represents the user-
controlled sprite on the screen.
"""
import pygame
import constants
import os

from platforms import MovingPlatform
# # from spritesheet_functions import SpriteSheetk

DESERT_ENEMY = 1
JUNGLE_ENEMY = 2
SNOW_ENEMY   = 3

class Enemy(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the enemy
    controls. """

    # -- Attributes
    # Set speed vector of enemy
    change_x = 0
    change_y = 0

    #Set width and height
    height = 0
    width = 0

    # This holds all the images for the animated walk left/right
    # of our enemy
    walking_frames_l = []
    walking_frames_r = []

    # What direction is the enemy facing?
    direction = "R"
    goRight = True
    calc_distance = 0

    # List of sprites we can bump against
    level = None
    player = None

    # -- Methods
    def __init__(self, enemy_type, distance):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        self.distance = distance

        if enemy_type == DESERT_ENEMY:  
            self.walking_frames = constants.ENEMY_DESERT_WALKING_FRAMES
            self.width = 70
            self.height = 100
        elif enemy_type ==  JUNGLE_ENEMY:  
            self.walking_frames = constants.ENEMY_JUNGLE_WALKING_FRAMES
            self.width = 100
            self.height = 100
        elif enemy_type ==  SNOW_ENEMY:  
            self.walking_frames = constants.ENEMY_SNOW_WALKING_FRAMES
            self.width = 70
            self.height = 100

        # Set the image the enemy starts with
        self.image = pygame.transform.scale(self.walking_frames[0], (self.width, self.height))

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the enemy. """
        # Gravity
        self.calc_grav()

        # Move
        self.move()
        # pos = self.rect.x + self.player.level.world_shift

        # Animation
        if self.direction == "R":
            frame = (self.rect.x // 30) % len(self.walking_frames)
            self.image = pygame.transform.scale(self.walking_frames[frame], (self.width, self.height))
        else:
            frame = (self.rect.x // 30) % len(self.walking_frames)
            self.image = pygame.transform.flip(pygame.transform.scale(self.walking_frames[frame], (self.width, self.height)), True, False)

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.player.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.player.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    # movimiento del enemigo
    def move(self):
        if self.goRight:
            if self.calc_distance > self.distance: 
                self.goRight = False
                self.calc_distance = 0
        else:
            if self.calc_distance < self.distance * -1:  
                self.goRight = True
                self.calc_distance = 0

        if self.goRight:
            self.go_right()
        else:
            self.go_left()

        self.rect.x += self.change_x
        self.calc_distance += self.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    # Enemy-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -2
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 2
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
