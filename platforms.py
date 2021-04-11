"""
Module for managing platforms.
"""
import pygame
import os

from spritesheet_functions import SpriteSheet

# These constants define our platform types:
#   Name of file
#   Path location of sprite
#   Width of sprite
#   Height of sprite
DESERT_GRASS_LEFT   = (os.path.join("Assets", "Levels/Desert/Tile/14.png"), 70, 50)
DESERT_GRASS_MIDDLE  = (os.path.join("Assets", "Levels/Desert/Tile/15.png"), 70, 50)
DESERT_GRASS_RIGHT = (os.path.join("Assets", "Levels/Desert/Tile/16.png"), 70, 50)
DESERT_STONE_PLATFORM_TOP_LEFT   = (os.path.join("Assets", "Levels/Desert/Tile/1.png"), 70, 70)
DESERT_STONE_PLATFORM_TOP_MIDDLE = (os.path.join("Assets", "Levels/Desert/Tile/2.png"), 70, 70)
DESERT_STONE_PLATFORM_TOP_RIGHT  = (os.path.join("Assets", "Levels/Desert/Tile/3.png"), 70, 70)
DESERT_STONE_PLATFORM_MIDDLE   = (os.path.join("Assets", "Levels/Desert/Tile/5.png"), 70, 70)
DESERT_STONE_PLATFORM_BOTTOM_LEFT   = (os.path.join("Assets", "Levels/Desert/Tile/12.png"), 70, 70)
DESERT_STONE_PLATFORM_BOTTOM_MIDDLE = (os.path.join("Assets", "Levels/Desert/Tile/9.png"), 70, 70)
DESERT_STONE_PLATFORM_BOTTOM_RIGHT  = (os.path.join("Assets", "Levels/Desert/Tile/13.png"), 70, 70)


class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("tiles_spritesheet.png")
        # Grab the image for this platform
        self.image = pygame.transform.scale(pygame.image.load(sprite_sheet_data[0]), (sprite_sheet_data[1], sprite_sheet_data[2]))

        self.rect = self.image.get_rect()


class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move. """
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
