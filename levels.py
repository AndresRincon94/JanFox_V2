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
        self.level_limit = -6000

        # Array with type of platform, and x, y location of the platform.
        platform_array = [[constants.JUNGLE_STONE_PLATFORM_FLAT, -450, 575],

                          [constants.JUNGLE_STONE_PLATFORM_TOP_MIDDLE, 200, 430],
                          [constants.JUNGLE_STONE_PLATFORM_TOP_MIDDLE, 280, 430],

                          [constants.JUNGLE_STONE_PLATFORM_TOP_MIDDLE, 480, 310],
                          [constants.JUNGLE_STONE_PLATFORM_TOP_MIDDLE, 560, 310],

                          [constants.JUNGLE_STONE_PLATFORM_TOP_MIDDLE, 760, 430],
                          [constants.JUNGLE_STONE_PLATFORM_TOP_MIDDLE, 840, 430],

                          [constants.JUNGLE_STONE_PLATFORM_TOP_LEFT_1, 1500, 540],
                          [constants.JUNGLE_STONE_PLATFORM_TOP_RIGHT_1, 2270, 540],

                          [constants.JUNGLE_STONE_PLATFORM_TOP_LEFT_3, 2800, 450],
                          [constants.JUNGLE_STONE_PLATFORM_TOP_RIGHT_3, 2870, 450],

                          [constants.JUNGLE_STONE_PLATFORM_TOP_LEFT_3, 3020, 350],
                          [constants.JUNGLE_STONE_PLATFORM_BOTTOM_MIDDLE_3, 3090, 350],
                          [constants.JUNGLE_STONE_PLATFORM_TOP_RIGHT_3, 3160, 350],

                          [constants.JUNGLE_STONE_PLATFORM_TOP_LEFT_3, 3310, 250],
                          [constants.JUNGLE_STONE_PLATFORM_BOTTOM_MIDDLE_3, 3380, 250],
                          [constants.JUNGLE_STONE_PLATFORM_BOTTOM_MIDDLE_3, 3450, 250],
                          [constants.JUNGLE_STONE_PLATFORM_TOP_RIGHT_3, 3520, 250],

                          [constants.JUNGLE_STONE_PLATFORM_TOP_LEFT_3, 3800, 250],
                          [constants.JUNGLE_STONE_PLATFORM_TOP_RIGHT_3, 3870, 250],

                          [constants.JUNGLE_STONE_PLATFORM_TOP_LEFT_3, 4150, 250],
                          [constants.JUNGLE_STONE_PLATFORM_BOTTOM_MIDDLE_3, 4220, 250],
                          [constants.JUNGLE_STONE_PLATFORM_BOTTOM_MIDDLE_3, 4290, 250],
                          [constants.JUNGLE_STONE_PLATFORM_TOP_RIGHT_3, 4360, 250],

                          [constants.JUNGLE_STONE_PLATFORM_TOP_LEFT_3, 4640, 250],
                          [constants.JUNGLE_STONE_PLATFORM_TOP_RIGHT_3, 4710, 250],

                          [constants.JUNGLE_STONE_PLATFORM_TOP_LEFT_3, 4990, 250],
                          [constants.JUNGLE_STONE_PLATFORM_BOTTOM_MIDDLE_3, 5060, 250],
                          [constants.JUNGLE_STONE_PLATFORM_BOTTOM_MIDDLE_3, 5130, 250],
                          [constants.JUNGLE_STONE_PLATFORM_TOP_RIGHT_3, 5200, 250],

                          [constants.JUNGLE_STONE_PLATFORM_TOP_LEFT_3, 5350, 350],
                          [constants.JUNGLE_STONE_PLATFORM_BOTTOM_MIDDLE_3, 5420, 350],
                          [constants.JUNGLE_STONE_PLATFORM_TOP_RIGHT_3, 5490, 350],

                          [constants.JUNGLE_STONE_PLATFORM_TOP_LEFT_3, 5640, 450],
                          [constants.JUNGLE_STONE_PLATFORM_TOP_RIGHT_3, 5710, 450],

                          [constants.JUNGLE_STONE_PLATFORM_TOP_LEFT_3, 6600, 430],
                          [constants.JUNGLE_STONE_PLATFORM_BOTTOM_MIDDLE_3, 6670, 430],
                          [constants.JUNGLE_STONE_PLATFORM_TOP_RIGHT_3, 6740, 430],

                          ]

        # Go through the array above and add platforms
        for platform in platform_array:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Array with type of enemy, and x, and distance of the enemy.
        enemy_array = [[enemies.JUNGLE_ENEMY, 600, 310, 120],
                       [enemies.JUNGLE_ENEMY, 1060, 435, 200],
                       [enemies.JUNGLE_ENEMY, 3020, 450, 500],
                       [enemies.JUNGLE_ENEMY, 4220, 400, 400],
                       [enemies.JUNGLE_ENEMY, 5060, 400, 400],
                       ]

        # Go through the array above and add enemies
        for enemy in enemy_array:
            enem = enemies.Enemy(enemy[0], enemy[3])
            enem.rect.x = enemy[1]
            enem.rect.y = enemy[2]
            enem.player = self.player
            self.enemy_list.add(enem)

        # Array with type x and y of good object.
        good_object_array = [[constants.BLACKBERRY, 520, 80],
                             [constants.BLACKBERRY, 530, 80],
                             [constants.BLACKBERRY, 1150, 280],
                             [constants.BLACKBERRY, 1170, 280],
                             [constants.BLACKBERRY, 1800, 280],
                             [constants.BLACKBERRY, 1810, 290],
                             [constants.BLACKBERRY, 1820, 280],
                             [constants.BLACKBERRY, 1900, 280],
                             [constants.BLACKBERRY, 1910, 290],
                             [constants.BLACKBERRY, 1920, 280],
                             [constants.BLACKBERRY, 2000, 280],
                             [constants.BLACKBERRY, 2010, 290],
                             [constants.BLACKBERRY, 2020, 280],
                             [constants.JUNGLE_MUSHROOM_1, 3100, 320],
                             [constants.JUNGLE_MUSHROOM_1, 3130, 320],
                             [constants.JUNGLE_MUSHROOM_1, 3160, 320],
                             [constants.BLACKBERRY, 3655, 30],
                             [constants.BLACKBERRY, 3665, 40],
                             [constants.BLACKBERRY, 4005, 30],
                             [constants.BLACKBERRY, 4015, 40],
                             [constants.BLACKBERRY, 4495, 30],
                             [constants.BLACKBERRY, 4505, 40],
                             [constants.BLACKBERRY, 4845, 30],
                             [constants.BLACKBERRY, 4855, 40],
                             [constants.JUNGLE_MUSHROOM_1, 3830, 220],
                             [constants.JUNGLE_MUSHROOM_1, 5060, 220],
                             [constants.JUNGLE_MUSHROOM_1, 5090, 220],
                             [constants.JUNGLE_MUSHROOM_1, 5110, 220],
                             [constants.BLACKBERRY, 6915, 210],
                             [constants.BLACKBERRY, 6925, 200],
                             [constants.BLACKBERRY, 6935, 210],
                             [constants.BLACKBERRY, 6945, 200],
                             [constants.BLACKBERRY, 6955, 210],
                             [constants.JUNGLE_MUSHROOM_1, 6670, 540],
                             [constants.JUNGLE_MUSHROOM_1, 6720, 540],
                             [constants.JUNGLE_MUSHROOM_1, 6770, 540],
                             ]

        # Go through the array above and add good object
        for good_object in good_object_array:
            obj = objects.Object(good_object[0])
            obj.rect.x = good_object[1]
            obj.rect.y = good_object[2]
            obj.player = self.player
            self.good_object_list.add(obj)

            # Array with type x and y of bad object.
        bad_object_array = [[constants.JUNGLE_STONE_PLATFORM_WAVES, 1570, 540],
                            [constants.JUNGLE_STONE_PLATFORM_WATER, 1570, 570],
                            [constants.JUNGLE_STONE_PLATFORM_WAVES, 1640, 540],
                            [constants.JUNGLE_STONE_PLATFORM_WATER, 1640, 570],
                            [constants.JUNGLE_STONE_PLATFORM_WAVES, 1710, 540],
                            [constants.JUNGLE_STONE_PLATFORM_WATER, 1710, 570],
                            [constants.JUNGLE_STONE_PLATFORM_WAVES, 1780, 540],
                            [constants.JUNGLE_STONE_PLATFORM_WATER, 1780, 570],
                            [constants.JUNGLE_STONE_PLATFORM_WAVES, 1850, 540],
                            [constants.JUNGLE_STONE_PLATFORM_WATER, 1850, 570],
                            [constants.JUNGLE_STONE_PLATFORM_WAVES, 1920, 540],
                            [constants.JUNGLE_STONE_PLATFORM_WATER, 1920, 570],
                            [constants.JUNGLE_STONE_PLATFORM_WAVES, 1990, 540],
                            [constants.JUNGLE_STONE_PLATFORM_WATER, 1990, 570],
                            [constants.JUNGLE_STONE_PLATFORM_WAVES, 2060, 540],
                            [constants.JUNGLE_STONE_PLATFORM_WATER, 2060, 570],
                            [constants.JUNGLE_STONE_PLATFORM_WAVES, 2130, 540],
                            [constants.JUNGLE_STONE_PLATFORM_WATER, 2130, 570],
                            [constants.JUNGLE_STONE_PLATFORM_WAVES, 2200, 540],
                            [constants.JUNGLE_STONE_PLATFORM_WATER, 2200, 570],
                            ]

        # Go through the array above and add bad object
        for bad_object in bad_object_array:
            obj = objects.Object(bad_object[0])
            obj.rect.x = bad_object[1]
            obj.rect.y = bad_object[2]
            obj.player = self.player
            self.bad_object_list.add(obj)

        # Array with type x and y of standard object.
        standard_object_array = [[constants.JUNGLE_MUSHROOM_2, 770, 400],
                                 [constants.JUNGLE_SIGN_2, 20, 500],
                                 [constants.JUNGLE_BUSH_1, 220, 390],
                                 [constants.JUNGLE_CRATE, 420, 490],
                                 [constants.JUNGLE_STONE, 480, 530],
                                 [constants.JUNGLE_BUSH_3, 540, 540],
                                 [constants.JUNGLE_BUSH_3, 570, 540],
                                 [constants.JUNGLE_BUSH_3, 600, 540],
                                 [constants.JUNGLE_TREE_1, 1000, 540],
                                 [constants.JUNGLE_TREE_1, 1200, 540],
                                 [constants.JUNGLE_TREE_1, 1400, 540],
                                 [constants.JUNGLE_SIGN_1, 1510, 490],
                                 [constants.JUNGLE_STONE, 2400, 530],
                                 [constants.JUNGLE_TREE_3, 2410, 270],
                                 [constants.JUNGLE_BUSH_2, 2820, 410],
                                 [constants.JUNGLE_STONE, 3300, 530],
                                 [constants.JUNGLE_BUSH_2, 3340, 530],
                                 [constants.JUNGLE_STONE, 3380, 530],
                                 [constants.JUNGLE_TREE_2, 3400, 270],
                                 [constants.JUNGLE_TREE_1, 5460, 320],
                                 [constants.JUNGLE_STONE, 5660, 410],
                                 [constants.JUNGLE_BUSH_3, 5680, 420],
                                 [constants.JUNGLE_TREE_3, 6050, 270],
                                 [constants.JUNGLE_TREE_3, 6100, 270],
                                 [constants.JUNGLE_TREE_3, 6150, 270],
                                 [constants.JUNGLE_BUSH_2, 6050, 530],
                                 [constants.JUNGLE_STONE, 6100, 530],
                                 [constants.JUNGLE_BUSH_2, 6150, 530],
                                 [constants.JUNGLE_BUSH_1, 6670, 390],
                                 [constants.JUNGLE_STONE, 6690, 390],
                                 [constants.JUNGLE_BUSH_2, 6870, 530],
                                 [constants.JUNGLE_STONE, 6880, 530],
                                 [constants.JUNGLE_STONE, 6920, 530],
                                 [constants.JUNGLE_SIGN_2, 6960, 490],
                                 [constants.JUNGLE_MUSHROOM_2, 3400, 220],
                                 [constants.JUNGLE_MUSHROOM_2, 3430, 220],
                                 [constants.JUNGLE_MUSHROOM_2, 3430, 220],
                                 [constants.JUNGLE_MUSHROOM_2, 4220, 220],
                                 [constants.JUNGLE_MUSHROOM_2, 4250, 220],
                                 [constants.JUNGLE_MUSHROOM_2, 5410, 320],


                                 ]

        # Go through the array above and add standard object
        for standard_object in standard_object_array:
            obj = objects.Object(standard_object[0])
            obj.rect.x = standard_object[1]
            obj.rect.y = standard_object[2]
            obj.player = self.player
            self.standard_object_list.add(obj)

        # Add a custom moving platform
        block = platforms.MovingPlatform(constants.JUNGLE_STONE_PLATFORM_BOTTOM_MIDDLE_2)
        block.rect.x = 1650
        block.rect.y = 440
        block.boundary_left = 1600
        block.boundary_right = 1800
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block_1 = platforms.MovingPlatform(constants.JUNGLE_STONE_PLATFORM_BOTTOM_MIDDLE_2)
        block_1.rect.x = 1950
        block_1.rect.y = 440
        block_1.boundary_left = 1900
        block_1.boundary_right = 2100
        block_1.change_x = -2
        block_1.player = self.player
        block_1.level = self
        self.platform_list.add(block_1)

        block_2 = platforms.MovingPlatform(constants.JUNGLE_CRATE)
        block_2.rect.x = 3655
        block_2.rect.y = 200
        block_2.boundary_top = 30
        block_2.boundary_bottom = 560
        block_2.change_y = 2
        block_2.player = self.player
        block_2.level = self
        self.platform_list.add(block_2)

        block_3 = platforms.MovingPlatform(constants.JUNGLE_CRATE)
        block_3.rect.x = 4005
        block_3.rect.y = 400
        block_3.boundary_top = 30
        block_3.boundary_bottom = 560
        block_3.change_y = 2
        block_3.player = self.player
        block_3.level = self
        self.platform_list.add(block_3)

        block_4 = platforms.MovingPlatform(constants.JUNGLE_CRATE)
        block_4.rect.x = 4495
        block_4.rect.y = 200
        block_4.boundary_top = 30
        block_4.boundary_bottom = 560
        block_4.change_y = 2
        block_4.player = self.player
        block_4.level = self
        self.platform_list.add(block_4)

        block_5 = platforms.MovingPlatform(constants.JUNGLE_CRATE)
        block_5.rect.x = 4845
        block_5.rect.y = 400
        block_5.boundary_top = 30
        block_5.boundary_bottom = 560
        block_5.change_y = 2
        block_5.player = self.player
        block_5.level = self
        self.platform_list.add(block_5)


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
        platform_array = [[constants.DESERT_STONE_PLATFORM_FLAT, -450, 575],
                          [constants.DESERT_GRASS_LEFT, 430, 500],
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
        platform_array = [[constants.SNOW_STONE_PLATFORM_FLAT, -450, 575],
                          [constants.DESERT_GRASS_LEFT, 430, 500],
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
