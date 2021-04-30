import pygame

import constants
import platforms
import enemies
import objects


class Level:
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None
    good_object_list = None
    bad_object_list = None
    standard_object_list = None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.good_object_list = pygame.sprite.Group()
        self.bad_object_list = pygame.sprite.Group()
        self.standard_object_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
        self.good_object_list.update()
        self.bad_object_list.update()
        self.standard_object_list.update()
        pygame.display.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.WHITE)
        screen.blit(self.background, (self.world_shift // 3, 0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.good_object_list.draw(screen)
        self.bad_object_list.draw(screen)
        self.standard_object_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for obj in self.good_object_list:
            obj.rect.x += shift_x

        for obj in self.bad_object_list:
            obj.rect.x += shift_x

        for obj in self.standard_object_list:
            obj.rect.x += shift_x


# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor

        Level.__init__(self, player)
        self.background = pygame.image.load("Assets/Levels/Jungle/Bg/Jungle.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -4500

        # Array with type of platform, and x, y location of the platform.
        platform_array = [[constants.JUNGLE_STONE_PLATFORM_TOP_LEFT_1, 0, 530],
                          [constants.JUNGLE_STONE_PLATFORM_TOP_MIDDLE, 70, 460],
                          [constants.JUNGLE_STONE_PLATFORM_TOP_RIGHT_1, 570, 449],
                          [constants.DESERT_GRASS_LEFT, 800, 400],
                          [constants.DESERT_GRASS_MIDDLE, 870, 400],
                          [constants.DESERT_GRASS_RIGHT, 940, 400],
                          [constants.DESERT_GRASS_LEFT, 1100, 500],
                          [constants.DESERT_GRASS_MIDDLE, 1170, 500],
                          [constants.DESERT_GRASS_RIGHT, 1240, 500],
                          [constants.DESERT_STONE_PLATFORM_TOP_LEFT, 1120, 280],
                          [constants.DESERT_STONE_PLATFORM_TOP_MIDDLE, 1190, 280],
                          [constants.DESERT_STONE_PLATFORM_TOP_RIGHT, 1260, 280],
                          ]



        # Go through the array above and add platforms
        for platform in platform_array:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Array with type of enemy, and x, and distance of the enemy.
        enemy_array = [[enemies.JUNGLE_ENEMY, 430, 435, 245],
                       [enemies.JUNGLE_ENEMY, 580, 435, 120],
                       [enemies.JUNGLE_ENEMY, 780, 300, 150]
                       ]

        # Go through the array above and add enemies
        for enemy in enemy_array:
            enem = enemies.Enemy(enemy[0], enemy[3])
            enem.rect.x = enemy[1]
            enem.rect.y = enemy[2]
            enem.player = self.player
            self.enemy_list.add(enem)

        # Array with type x and y of good object.
        good_object_array = [[constants.BLACKBERRY, 480, 285],
                             [constants.BLACKBERRY, 1020, 280],
                             [constants.BLACKBERRY, 1800, 280],
                             [constants.BLACKBERRY, 1810, 290],
                             [constants.BLACKBERRY, 1820, 280],
                             [constants.BLACKBERRY, 1900, 280],
                             [constants.BLACKBERRY, 1910, 290],
                             [constants.BLACKBERRY, 1920, 280],
                             [constants.BLACKBERRY, 2000, 280],
                             [constants.BLACKBERRY, 2010, 290],
                             [constants.BLACKBERRY, 2020, 280]
                             ]

        # Array with type x and y of bad object.
        bad_object_array = [[constants.DESERT_CACTUS, 900, 320]]

        # Array with type x and y of standard object.
        standard_object_array = [[constants.DESERT_STONE, 640, 460],
                                 [constants.DESERT_CACTUS_2, 430, 430],
                                 [constants.DESERT_SKELETON, 1130, 470],
                                 ]

        # Go through the array above and add good object
        for good_object in good_object_array:
            obj = objects.Object(good_object[0])
            obj.rect.x = good_object[1]
            obj.rect.y = good_object[2]
            obj.player = self.player
            self.good_object_list.add(obj)

        # Go through the array above and add bad object
        for bad_object in bad_object_array:
            obj = objects.Object(bad_object[0])
            obj.rect.x = bad_object[1]
            obj.rect.y = bad_object[2]
            obj.player = self.player
            self.bad_object_list.add(obj)

        # Go through the array above and add standard object
        for standard_object in standard_object_array:
            obj = objects.Object(standard_object[0])
            obj.rect.x = standard_object[1]
            obj.rect.y = standard_object[2]
            obj.player = self.player
            self.standard_object_list.add(obj)

        # Add a custom moving platform
        block = platforms.MovingPlatform(constants.DESERT_STONE_PLATFORM_TOP_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


# Create platforms for the level 2
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 2. """

        # Call the parent constructor
        Level.__init__(self, player)


        self.background = pygame.image.load("Assets/Levels/Desert/Bg/Desert.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        platform_array = [[constants.DESERT_GRASS_LEFT, 430, 500],
                          [constants.DESERT_GRASS_MIDDLE, 500, 500],
                          [constants.DESERT_GRASS_MIDDLE, 570, 500],
                          [constants.DESERT_GRASS_RIGHT, 640, 500],
                          [constants.DESERT_GRASS_LEFT, 800, 400],
                          [constants.DESERT_GRASS_MIDDLE, 870, 400],
                          [constants.DESERT_GRASS_RIGHT, 940, 400]
                          ]

        # Go through the array above and add platforms
        for platform in platform_array:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Array with type of enemy, and x, and patrol distance of the enemy.
        enemy_array = [[enemies.DESERT_ENEMY, 430, 435, 245],
                       [enemies.SNOW_ENEMY, 580, 435, 120]
                       ]

        # Go through the array above and add enemies
        for enemy in enemy_array:
            enem = enemies.Enemy(enemy[0], enemy[3])
            enem.rect.x = enemy[1]
            enem.rect.y = enemy[2]
            enem.player = self.player
            self.enemy_list.add(enem)

        # Array with type x and y of good object.
        good_object_array = [[constants.BLACKBERRY, 480, 285],
                             [constants.BLACKBERRY, 1020, 280],
                             [constants.BLACKBERRY, 1800, 280],
                             [constants.BLACKBERRY, 1810, 290],
                             [constants.BLACKBERRY, 1820, 280]
                             ]

        # Array with type x and y of bad object.
        bad_object_array = [[constants.DESERT_CACTUS, 900, 320]]

        # Array with type x and y of standard object.
        standard_object_array = [[constants.DESERT_STONE, 640, 460],
                                 [constants.DESERT_CACTUS_2, 430, 430],
                                 ]

        # Go through the array above and add good object
        for good_object in good_object_array:
            obj = objects.Object(good_object[0])
            obj.rect.x = good_object[1]
            obj.rect.y = good_object[2]
            obj.player = self.player
            self.good_object_list.add(obj)

        # Go through the array above and add bad object
        for bad_object in bad_object_array:
            obj = objects.Object(bad_object[0])
            obj.rect.x = bad_object[1]
            obj.rect.y = bad_object[2]
            obj.player = self.player
            self.bad_object_list.add(obj)

        # Go through the array above and add standard object
        for standard_object in standard_object_array:
            obj = objects.Object(standard_object[0])
            obj.rect.x = standard_object[1]
            obj.rect.y = standard_object[2]
            obj.player = self.player
            self.standard_object_list.add(obj)

        # Add a custom moving platform
        block = platforms.MovingPlatform(constants.DESERT_STONE_PLATFORM_TOP_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


# Create platforms for the level 2
class Level_03(Level):
    """ Definition for level 3. """

    def __init__(self, player):
        """ Create level 3. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("Assets/Levels/Snow/Bg/Snow.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        platform_array = [[constants.DESERT_GRASS_LEFT, 430, 500],
                          [constants.DESERT_GRASS_MIDDLE, 500, 500],
                          [constants.DESERT_GRASS_MIDDLE, 570, 500],
                          [constants.DESERT_GRASS_RIGHT, 640, 500],
                          [constants.DESERT_GRASS_LEFT, 800, 400],
                          [constants.DESERT_GRASS_MIDDLE, 870, 400],
                          [constants.DESERT_GRASS_RIGHT, 940, 400],
                          ]

        # Go through the array above and add platforms
        for platform in platform_array:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Array with type of enemy, and x, and patrol distance of the enemy.
        enemy_array = [[enemies.DESERT_ENEMY, 430, 435, 245]
                       ]

        # Go through the array above and add enemies
        for enemy in enemy_array:
            enem = enemies.Enemy(enemy[0], enemy[3])
            enem.rect.x = enemy[1]
            enem.rect.y = enemy[2]
            enem.player = self.player
            self.enemy_list.add(enem)

        # Array with type x and y of good object.
        good_object_array = [[constants.BLACKBERRY, 480, 285],
                             [constants.BLACKBERRY, 1020, 280],
                             [constants.BLACKBERRY, 1800, 280],
                             [constants.BLACKBERRY, 1810, 290],
                             [constants.BLACKBERRY, 1910, 290],
                             [constants.BLACKBERRY, 1920, 280],
                             [constants.BLACKBERRY, 2000, 280],
                             [constants.BLACKBERRY, 2010, 290],
                             [constants.BLACKBERRY, 2020, 280]
                             ]

        # Array with type x and y of bad object.
        bad_object_array = [[constants.DESERT_CACTUS, 900, 320]]

        # Array with type x and y of standard object.
        standard_object_array = [[constants.DESERT_STONE, 640, 460],
                                 [constants.DESERT_CACTUS_2, 430, 430],
                                 [constants.DESERT_SKELETON, 1130, 470],
                                 ]

        # Go through the array above and add good object
        for good_object in good_object_array:
            obj = objects.Object(good_object[0])
            obj.rect.x = good_object[1]
            obj.rect.y = good_object[2]
            obj.player = self.player
            self.good_object_list.add(obj)

        # Go through the array above and add bad object
        for bad_object in bad_object_array:
            obj = objects.Object(bad_object[0])
            obj.rect.x = bad_object[1]
            obj.rect.y = bad_object[2]
            obj.player = self.player
            self.bad_object_list.add(obj)

        # Go through the array above and add standard object
        for standard_object in standard_object_array:
            obj = objects.Object(standard_object[0])
            obj.rect.x = standard_object[1]
            obj.rect.y = standard_object[2]
            obj.player = self.player
            self.standard_object_list.add(obj)

        # Add a custom moving platform
        block = platforms.MovingPlatform(constants.DESERT_STONE_PLATFORM_TOP_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)