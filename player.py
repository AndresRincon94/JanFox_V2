"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame
import constants
import os

from platforms import MovingPlatform
# # from spritesheet_functions import SpriteSheetk

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0

    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames = []
    dying_frames = []

    # What direction is the player facing?
    direction = "R"
    velocity = 6

    # Items of dead
    countDeadFrame = 0
    countReviveFrame = 0
    indexDead = 0    
    isDead = False

    # List of sprites we can bump against
    level = None

    # Set score
    score = 0

    # items dead health
    countHealthFrame = 0
    health = 100
    lifes = 3

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        
        self.salto = pygame.mixer.Sound("Assets/Sound/jumpSound1.ogg") 
        self.recoger = pygame.mixer.Sound("Assets/Sound/pickupSound1.ogg")    
             
        # self.walking_frames_l = [pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (1).png'),pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (2).png'),pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (3).png'),pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (4).png'),pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (5).png'),pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (6).png'),pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (7).png'),pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (8).png'),pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (9).png'),pygame.image.load('spritesheet_example/Assets/Sprites/personage/Fox/Walk/Walk (10).png')]
        self.walking_frames = constants.PLAYER_WALKING_FRAMES
        self.dying_frames = constants.PLAYER_DYING_FRAMES

        # Set the image the player starts with
        self.image = pygame.transform.scale(self.walking_frames[0], (70, 100))

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
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

        if not self.isDead:                        
            # Move left/right
            self.rect.x += self.change_x
            pos = self.rect.x + self.level.world_shift
            if self.direction == "R":
                frame = (pos // 30) % len(self.walking_frames)
                self.image = pygame.transform.scale(self.walking_frames[frame], (70, 100))
            else:
                frame = (pos // 30) % len(self.walking_frames)
                self.image = pygame.transform.flip(pygame.transform.scale(self.walking_frames[frame], (70, 100)), True, False)

            # See if we hit anything
            block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            for block in block_hit_list:
                # If we are moving right,
                # set our right side to the left side of the item we hit
                if self.change_x > 0:
                    self.rect.right = block.rect.left
                elif self.change_x < 0:
                    # Otherwise if we are moving left, do the opposite.
                    self.rect.left = block.rect.right

            # Check and see if we hit good Object
            good_object_hit_list = pygame.sprite.spritecollide(self, self.level.good_object_list, True)
            for good_object in good_object_hit_list:
                # Add score
                self.score += 100
                self.health += 5
                if self.health > 100:
                    self.health = 100
                self.recoger.play()

            # Check and see if we hit bad Object
            enemy_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
            for enemy in enemy_hit_list:
                # Player die
                self.loseHealth(10)
                
            # Check and see if we hit bad Object
            bad_object_hit_list = pygame.sprite.spritecollide(self, self.level.bad_object_list, False)
            for bad_object in bad_object_hit_list:
                # Player die
                if not self.isDead:
                    self.loseHealth(self.health)
        else:
            self.dead()
        
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
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10
            self.salto.play()

    def loseHealth(self, lose):
        self.countHealthFrame += 1
        if self.countHealthFrame == 1:
            self.health -= lose
        elif self.countHealthFrame > 20:
            self.countHealthFrame = 0

        if self.health == 0:
            self.dead()

    # Player-controlled movement:
    def dead(self):
        if not self.isDead:
            self.lifes -= 1

        if self.indexDead < len(self.dying_frames):
            self.countDeadFrame += 1
            if self.countDeadFrame > 4:
                self.image = pygame.transform.scale(self.dying_frames[self.indexDead], (115, 115))        
                self.indexDead += 1
                self.countDeadFrame = 0
            self.isDead = True

        if self.isDead and self.indexDead == len(self.dying_frames) - 1:
            if self.lifes > 0:
                self.indexDead = 0
                self.rect.x = 0
                self.rect.y = 0
                self.health = 100
                self.isDead = False

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = self.velocity * -1
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = self.velocity
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
