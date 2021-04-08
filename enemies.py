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

    # List of sprites we can bump against
    level = None
    player = None

    # -- Methods
    def __init__(self, enemy_type):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # self.walking_frames_r = [pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (1).png'), pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (2).png'), pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (3).png'), pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (4).png'), pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (5).png'), pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (6).png'), pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (7).png'), pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (8).png'), pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (9).png'), pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (10).png')]
        # self.walking_frames_l = [pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (1).png'), pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (2).png'), pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (3).png'), pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (4).png'), pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (5).png'), pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (6).png'), pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (7).png'), pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (8).png'), pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (9).png'), pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (10).png')]

        if enemy_type == DESERT_ENEMY:  
            self.walking_frames = [pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_000.png"))    ,pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_001.png")),    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_002.png")),    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_003.png")),    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_004.png")),    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_005.png")),    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_006.png")),    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_007.png")),    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_008.png")),    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_009.png"))]
            self.width = 70
            self.height = 100
        elif enemy_type ==  JUNGLE_ENEMY:  
            self.walking_frames = [pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_000.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_001.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_002.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_003.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_004.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_005.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_006.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_007.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_008.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_009.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_010.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_011.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_012.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_013.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_014.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_015.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_016.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_017.png"))]
            self.width = 100
            self.height = 100
        elif enemy_type ==  SNOW_ENEMY:  
            self.walking_frames = [pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_000.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_001.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_002.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_003.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_004.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_005.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_006.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_007.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_008.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_009.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_010.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_011.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_012.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_013.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_014.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_015.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_016.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_017.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_018.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_019.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_020.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_021.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_022.png")), pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_023.png"))]
            self.width = 70
            self.height = 100

        # sprite_sheet = SpriteSheet("p1_walk.png")
        # # Load all the right facing images into a list
        # image = sprite_sheet.get_image(0, 0, 66, 90)
        # self.walking_frames_r.append(image)
        # image = sprite_sheet.get_image(66, 0, 66, 90)
        # self.walking_frames_r.append(image)
        # image = sprite_sheet.get_image(132, 0, 67, 90)
        # self.walking_frames_r.append(image)
        # image = sprite_sheet.get_image(0, 93, 66, 90)
        # self.walking_frames_r.append(image)
        # image = sprite_sheet.get_image(66, 93, 66, 90)
        # self.walking_frames_r.append(image)
        # image = sprite_sheet.get_image(132, 93, 72, 90)
        # self.walking_frames_r.append(image)
        # image = sprite_sheet.get_image(0, 186, 70, 90)
        # self.walking_frames_r.append(image)

        # Load all the right facing images, then flip them
        # to face left.
        # image = sprite_sheet.get_image(0, 0, 66, 90)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)
        # image = sprite_sheet.get_image(66, 0, 66, 90)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)
        # image = sprite_sheet.get_image(132, 0, 67, 90)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)
        # image = sprite_sheet.get_image(0, 93, 66, 90)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)
        # image = sprite_sheet.get_image(66, 93, 66, 90)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)
        # image = sprite_sheet.get_image(132, 93, 72, 90)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)
        # image = sprite_sheet.get_image(0, 186, 70, 90)
        # image = pygame.transform.flip(image, True, False)
        # self.walking_frames_l.append(image)

        # Set the image the enemy starts with
        self.image = pygame.transform.scale(self.walking_frames[0], (self.width, self.height))

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the enemy. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.player.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames)
            self.image = pygame.transform.scale(self.walking_frames[frame], (self.width, self.height))
        else:
            frame = (pos // 30) % len(self.walking_frames)
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

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.player.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10

    # Enemy-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
