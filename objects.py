"""
This module is used to hold the Object class. The Object represents the user-
controlled sprite on the screen.
"""
import pygame
import constants
import os

from platforms import MovingPlatform
# # from spritesheet_functions import SpriteSheetk

BLACKBERRY   = (os.path.join("Assets", "Sprites/Objects/Fruits/shadow/32.png"), 70, 70)
DESERT_CACTUS  = (os.path.join("Assets", "Levels/Desert/Objects/Cactus (1).png"), 79, 80)
DESERT_CACTUS_2  = (os.path.join("Assets", "Levels/Desert/Objects/Cactus (3).png"), 67, 73)
DESERT_STONE = (os.path.join("Assets", "Levels/Desert/Objects/Stone.png"), 68, 40)
DESERT_SKELETON = (os.path.join("Assets", "Levels/Desert/Objects/Skeleton.png"), 90, 32)

class Object(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the object
    controls. """

    # -- Attributes
    # Set speed vector of object
    change_x = 0
    change_y = 0

    #Set width and height
    height = 0
    width = 0

    # This holds all the images for the animated walk left/right
    # of our object
    walking_frames_l = []
    walking_frames_r = []

    # What direction is the object facing?
    direction = "R"
    # goRight = True
    # calc_distance = 0

    # List of sprites we can bump against
    level = None
    player = None

    # -- Methods
    def __init__(self, sprite_sheet_data):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(pygame.image.load(sprite_sheet_data[0]), (sprite_sheet_data[1], sprite_sheet_data[2]))

        self.rect = self.image.get_rect()
        # Set the image the object starts with

    