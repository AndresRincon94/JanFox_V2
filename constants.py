import os
import pygame

"""
Global constants
"""

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (52, 152, 219)
GREEN = (46, 204, 113)
YELLOW = (241, 196, 15)
RED = (231, 76, 60)

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# Paths images
"""
Player
"""
# Face
PLAYER_FACE = pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Face.png"))

# Walk
PLAYER_WALKING_FRAMES = [pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk(1).png")),
                         pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk(2).png")),
                         pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk(3).png")),
                         pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk(4).png")),
                         pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk(5).png")),
                         pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk(6).png")),
                         pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk(7).png")),
                         pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk(8).png")),
                         pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk(9).png")),
                         pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk(10).png"))
                         ]

# Dead
PLAYER_DYING_FRAMES = [pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead(1).png")),
                       pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead(2).png")),
                       pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead(3).png")),
                       pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead(4).png")),
                       pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead(5).png")),
                       pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead(6).png")),
                       pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead(7).png")),
                       pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead(8).png")),
                       pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead(9).png")),
                       pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead(10).png"))
                       ]

# Jump
PLAYER_JUMPYNG_FRAMES = [pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Jump/Jump(1).png")),
                         pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Jump/Jump(2).png")),
                         pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Jump/Jump(3).png")),
                         pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Jump/Jump(4).png")),
                         pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Jump/Jump(5).png")),
                         pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Jump/Jump(6).png")),
                         pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Jump/Jump(7).png")),
                         pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Jump/Jump(8).png"))
                         ]

# Idle
PLAYER_IDLE_FRAMES = [pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Idle/Idle(1).png")),
                      pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Idle/Idle(2).png")),
                      pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Idle/Idle(3).png")),
                      pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Idle/Idle(4).png")),
                      pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Idle/Idle(5).png")),
                      pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Idle/Idle(6).png")),
                      pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Idle/Idle(7).png")),
                      pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Idle/Idle(8).png")),
                      pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Idle/Idle(9).png")),
                      pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Idle/Idle(10).png"))
                      ]

# Fall
PLAYER_FALL_FRAMES = [pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Fall/Fall(1).png")),
                      pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Fall/Fall(2).png")),
                      pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Fall/Fall(3).png")),
                      pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Fall/Fall(4).png")),
                      pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Fall/Fall(5).png")),
                      pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Fall/Fall(6).png")),
                      pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Fall/Fall(7).png")),
                      pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Fall/Fall(8).png"))
                      ]

"""
Enemies
"""
# Walk
ENEMY_DESERT_WALKING_FRAMES = [
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(1).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(2).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(3).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(4).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(5).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(6).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(7).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(8).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(9).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(10).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(11).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(12).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(13).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(14).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(15).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(16).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(17).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(18).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(19).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(20).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(21).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(22).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(23).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Walking/Walking(24).png"))
]

ENEMY_JUNGLE_WALKING_FRAMES = [
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Jungle_Enemy/Walking/Walking(1).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Jungle_Enemy/Walking/Walking(2).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Jungle_Enemy/Walking/Walking(3).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Jungle_Enemy/Walking/Walking(4).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Jungle_Enemy/Walking/Walking(5).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Jungle_Enemy/Walking/Walking(6).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Jungle_Enemy/Walking/Walking(7).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Jungle_Enemy/Walking/Walking(8).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Jungle_Enemy/Walking/Walking(9).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Jungle_Enemy/Walking/Walking(10).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Jungle_Enemy/Walking/Walking(11).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Jungle_Enemy/Walking/Walking(12).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Jungle_Enemy/Walking/Walking(13).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Jungle_Enemy/Walking/Walking(14).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Jungle_Enemy/Walking/Walking(15).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Jungle_Enemy/Walking/Walking(16).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Jungle_Enemy/Walking/Walking(17).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Jungle_Enemy/Walking/Walking(18).png"))
]

ENEMY_SNOW_WALKING_FRAMES = [
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(1).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(2).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(3).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(4).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(5).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(6).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(7).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(8).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(9).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(10).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(11).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(12).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(13).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(14).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(15).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(16).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(17).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(18).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(19).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(20).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(21).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(22).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(23).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Walking/Walking(24).png"))
]

# Run_Slashing

ENEMY_DESERT_SlASHING_FRAMES = [
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Run_Slashing/Slashing(1).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Run_Slashing/Slashing(2).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Run_Slashing/Slashing(3).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Run_Slashing/Slashing(4).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Run_Slashing/Slashing(5).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Run_Slashing/Slashing(6).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Run_Slashing/Slashing(7).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Run_Slashing/Slashing(8).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Run_Slashing/Slashing(9).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Run_Slashing/Slashing(10).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Run_Slashing/Slashing(11).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert_Enemy/Run_Slashing/Slashing(12).png"))
]

ENEMY_SNOW_SlASHING_FRAMES = [
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Run_Slashing/Slashing(1).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Run_Slashing/Slashing(2).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Run_Slashing/Slashing(3).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Run_Slashing/Slashing(4).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Run_Slashing/Slashing(5).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Run_Slashing/Slashing(6).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Run_Slashing/Slashing(7).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Run_Slashing/Slashing(8).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Run_Slashing/Slashing(9).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Run_Slashing/Slashing(10).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Run_Slashing/Slashing(11).png")),
    pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow_Enemy/Run_Slashing/Slashing(12).png"))
]

"""
Platforms
"""
# These constants define our platform types:
#   Path location of sprite
#   Width scale of sprite
#   Height scale of sprite

# Desert
DESERT_STONE_PLATFORM_FLAT = (os.path.join("Assets", "Levels/Desert/Bg/Desert_flat.png"), 8200, 25)
DESERT_STONE_PLATFORM_TOP_LEFT = (os.path.join("Assets", "Levels/Desert/Tiles/1.png"), 70, 70)
DESERT_STONE_PLATFORM_TOP_MIDDLE = (os.path.join("Assets", "Levels/Desert/Tiles/2.png"), 70, 70)
DESERT_STONE_PLATFORM_TOP_RIGHT = (os.path.join("Assets", "Levels/Desert/Tiles/3.png"), 70, 70)
DESERT_STONE_PLATFORM_MIDDLE = (os.path.join("Assets", "Levels/Desert/Tiles/5.png"), 70, 70)
DESERT_STONE_PLATFORM_BOTTOM_MIDDLE = (os.path.join("Assets", "Levels/Desert/Tiles/9.png"), 70, 70)
DESERT_STONE_PLATFORM_BOTTOM_LEFT = (os.path.join("Assets", "Levels/Desert/Tiles/12.png"), 70, 70)
DESERT_STONE_PLATFORM_BOTTOM_RIGHT = (os.path.join("Assets", "Levels/Desert/Tiles/13.png"), 70, 70)
DESERT_GRASS_LEFT = (os.path.join("Assets", "Levels/Desert/Tiles/14.png"), 70, 50)
DESERT_GRASS_MIDDLE = (os.path.join("Assets", "Levels/Desert/Tiles/15.png"), 70, 50)
DESERT_GRASS_RIGHT = (os.path.join("Assets", "Levels/Desert/Tiles/16.png"), 70, 50)

# Jungle
JUNGLE_STONE_PLATFORM_FLAT = (os.path.join("Assets", "Levels/Jungle/Bg/Jungle_flat.png"), 8200, 25)
JUNGLE_STONE_PLATFORM_TOP_LEFT_1 = (os.path.join("Assets", "Levels/Jungle/Tiles/1.png"), 70, 80)
JUNGLE_STONE_PLATFORM_TOP_LEFT_2 = (os.path.join("Assets", "Levels/Jungle/Tiles/11.png"), 80, 60)
JUNGLE_STONE_PLATFORM_TOP_LEFT_3 = (os.path.join("Assets", "Levels/Jungle/Tiles/13.png"), 70, 40)
JUNGLE_STONE_PLATFORM_TOP_MIDDLE = (os.path.join("Assets", "Levels/Jungle/Tiles/2.png"), 80, 60)
JUNGLE_STONE_PLATFORM_TOP_RIGHT_1 = (os.path.join("Assets", "Levels/Jungle/Tiles/3.png"), 70, 80)
JUNGLE_STONE_PLATFORM_TOP_RIGHT_2 = (os.path.join("Assets", "Levels/Jungle/Tiles/7.png"), 80, 60)
JUNGLE_STONE_PLATFORM_TOP_RIGHT_3 = (os.path.join("Assets", "Levels/Jungle/Tiles/15.png"), 70, 40)

JUNGLE_STONE_PLATFORM_MIDDLE_1 = (os.path.join("Assets", "Levels/Jungle/Tiles/5.png"), 70, 50)
JUNGLE_STONE_PLATFORM_MIDDLE_2 = (os.path.join("Assets", "Levels/Jungle/Tiles/8.png"), 70, 70)
JUNGLE_STONE_PLATFORM_MIDDLE_3 = (os.path.join("Assets", "Levels/Jungle/Tiles/10.png"), 70, 50)
JUNGLE_STONE_PLATFORM_MIDDLE_LEFT = (os.path.join("Assets", "Levels/Jungle/Tiles/4.png"), 70, 30)
JUNGLE_STONE_PLATFORM_MIDDLE_RIGHT = (os.path.join("Assets", "Levels/Jungle/Tiles/6.png"), 70, 30)

JUNGLE_STONE_PLATFORM_BOTTOM_MIDDLE_1 = (os.path.join("Assets", "Levels/Jungle/Tiles/9.png"), 70, 70)
JUNGLE_STONE_PLATFORM_BOTTOM_MIDDLE_2 = (os.path.join("Assets", "Levels/Jungle/Tiles/14.png"), 100, 60)
JUNGLE_STONE_PLATFORM_BOTTOM_MIDDLE_3 = (os.path.join("Assets", "Levels/Jungle/Tiles/14.png"), 70, 40)
JUNGLE_STONE_PLATFORM_BOTTOM_LEFT = (os.path.join("Assets", "Levels/Jungle/Tiles/12.png"), 70, 70)
JUNGLE_STONE_PLATFORM_BOTTOM_RIGHT = (os.path.join("Assets", "Levels/Jungle/Tiles/16.png"), 70, 50)

JUNGLE_STONE_PLATFORM_WAVES = (os.path.join("Assets", "Levels/Jungle/Tiles/17.png"), 70, 30)
JUNGLE_STONE_PLATFORM_WATER = (os.path.join("Assets", "Levels/Jungle/Tiles/18.png"), 70, 30)


# Snow
SNOW_STONE_PLATFORM_FLAT = (os.path.join("Assets", "Levels/Snow/Bg/Snow_flat.png"), 8200, 25)
SNOW_STONE_PLATFORM_TOP_LEFT = (os.path.join("Assets", "Levels/Snow/Tiles/1.png"), 70, 70)
SNOW_STONE_PLATFORM_TOP_MIDDLE = (os.path.join("Assets", "Levels/Snow/Tiles/2.png"), 70, 70)
SNOW_STONE_PLATFORM_TOP_RIGHT = (os.path.join("Assets", "Levels/Snow/Tiles/3.png"), 70, 70)
SNOW_STONE_PLATFORM_MIDDLE_LEFT = (os.path.join("Assets", "Levels/Snow/Tiles/4.png"), 70, 70)
SNOW_STONE_PLATFORM_MIDDLE = (os.path.join("Assets", "Levels/Snow/Tiles/5.png"), 70, 70)
SNOW_STONE_PLATFORM_MIDDLE_RIGHT = (os.path.join("Assets", "Levels/Snow/Tiles/6.png"), 70, 70)
SNOW_STONE_PLATFORM_TOP_RIGHT_2 = (os.path.join("Assets", "Levels/Snow/Tiles/7.png"), 70, 70)
SNOW_STONE_PLATFORM_MIDDLE_2 = (os.path.join("Assets", "Levels/Snow/Tiles/8.png"), 70, 70)
SNOW_STONE_PLATFORM_BOTTOM_MIDDLE = (os.path.join("Assets", "Levels/Snow/Tiles/9.png"), 70, 70)
SNOW_STONE_PLATFORM_MIDDLE_3 = (os.path.join("Assets", "Levels/Snow/Tiles/10.png"), 70, 70)
SNOW_STONE_PLATFORM_TOP_LEFT_2 = (os.path.join("Assets", "Levels/Snow/Tiles/11.png"), 70, 70)
SNOW_STONE_PLATFORM_BOTTOM_LEFT = (os.path.join("Assets", "Levels/Snow/Tiles/12.png"), 70, 70)
SNOW_STONE_PLATFORM_BOTTOM_RIGHT = (os.path.join("Assets", "Levels/Snow/Tiles/13.png"), 70, 70)
SNOW_GRASS_LEFT = (os.path.join("Assets", "Levels/Snow/Tiles/14.png"), 70, 50)
SNOW_GRASS_MIDDLE = (os.path.join("Assets", "Levels/Snow/Tiles/15.png"), 70, 50)
SNOW_GRASS_RIGHT = (os.path.join("Assets", "Levels/Snow/Tiles/16.png"), 70, 50)
SNOW_STONE_PLATFORM_WAVES = (os.path.join("Assets", "Levels/Snow/Tiles/17.png"), 70, 35)
SNOW_STONE_PLATFORM_WATER = (os.path.join("Assets", "Levels/Snow/Tiles/18.png"), 70, 35)

# These constants define our platform types:
#   Path location of sprite
#   Width scale of sprite
#   Height scale of sprite


# Desert
DESERT_CACTUS = (os.path.join("Assets", "Levels/Desert/Objects/Cactus(1).png"), 79, 80)
DESERT_CACTUS_4 = (os.path.join("Assets", "Levels/Desert/Objects/Cactus(1).png"), 100, 200)
DESERT_CACTUS_2 = (os.path.join("Assets", "Levels/Desert/Objects/Cactus(3).png"), 67, 73)
DESERT_CACTUS_3 = (os.path.join("Assets", "Levels/Desert/Objects/Cactus(2).png"), 50, 32)
DESERT_STONE = (os.path.join("Assets", "Levels/Desert/Objects/Stone.png"), 68, 40)
DESERT_SKELETON = (os.path.join("Assets", "Levels/Desert/Objects/Skeleton.png"), 90, 32)
DESERT_SIGNARROW = (os.path.join("Assets", "Levels/Desert/Objects/SignArrow.png"), 130, 100)
DESERT_BUSH = (os.path.join("Assets", "Levels/Desert/Objects/Bush(1).png"), 150, 100)
DESERT_BUSH_2 = (os.path.join("Assets", "Levels/Desert/Objects/Bush(2).png"), 68, 40)
DESERT_GRASS_1 = (os.path.join("Assets", "Levels/Desert/Objects/Grass(1).png"), 68, 40)
DESERT_GRASS_2 = (os.path.join("Assets", "Levels/Desert/Objects/Grass(2).png"), 68, 40)
DESERT_TREE = (os.path.join("Assets", "Levels/Desert/Objects/Tree.png"), 400, 200)
DESERT_CRATE = (os.path.join("Assets", "Levels/Desert/Objects/Crate.png"), 60, 60)
DESERT_SIGN = (os.path.join("Assets", "Levels/Desert/Objects/Sign.png"), 60, 60)

"""
Objects Fruits Desert
"""

BLACKBERRY = (os.path.join("Assets", "Levels/Desert/Objects/Blackberry.png"), 70, 70)
NUT = (os.path.join("Assets", "Levels/Objects/Fruits/shadow/9.png"), 80, 80)

# Jungle
JUNGLE_BUSH_1 = (os.path.join("Assets", "Levels/Jungle/Objects/Bush(1).png"), 50, 40)
JUNGLE_BUSH_2 = (os.path.join("Assets", "Levels/Jungle/Objects/Bush(2).png"), 70, 40)
JUNGLE_BUSH_3 = (os.path.join("Assets", "Levels/Jungle/Objects/Bush(3).png"), 50, 30)
JUNGLE_BUSH_4 = (os.path.join("Assets", "Levels/Jungle/Objects/Bush(4).png"), 50, 32)
JUNGLE_TREE_1 = (os.path.join("Assets", "Levels/Jungle/Objects/Tree_1.png"), 70, 30)
JUNGLE_TREE_2 = (os.path.join("Assets", "Levels/Jungle/Objects/Tree_2.png"), 250, 300)
JUNGLE_TREE_3 = (os.path.join("Assets", "Levels/Jungle/Objects/Tree_3.png"), 250, 300)
JUNGLE_SIGN_1 = (os.path.join("Assets", "Levels/Jungle/Objects/Sign_1.png"), 50, 50)
JUNGLE_SIGN_2 = (os.path.join("Assets", "Levels/Jungle/Objects/Sign_2.png"), 79, 80)
JUNGLE_MUSHROOM_1 = (os.path.join("Assets", "Levels/Jungle/Objects/Mushroom_1.png"), 50, 30)
JUNGLE_MUSHROOM_2 = (os.path.join("Assets", "Levels/Jungle/Objects/Mushroom_2.png"), 50, 30)
JUNGLE_STONE = (os.path.join("Assets", "Levels/Jungle/Objects/Stone.png"), 70, 40)
JUNGLE_CRATE = (os.path.join("Assets", "Levels/Jungle/Objects/Crate.png"), 80, 80)

"""
Objects Fruits Jungle
"""

# BLACKBERRY = (os.path.join("Assets", "Levels/Desert/Objects/Blackberry.png"), 70, 70)


# Snow
SNOW_CRATE = (os.path.join("Assets", "Levels/Snow/Objects/Crate.png"), 60, 60)
SNOW_CRYSTAL = (os.path.join("Assets", "Levels/Snow/Objects/Crystal.png"), 50, 50)
SNOW_IGLOO = (os.path.join("Assets", "Levels/Snow/Objects/Igloo.png"), 150, 50)
SNOW_ICEBOX = (os.path.join("Assets", "Levels/Snow/Objects/IceBox.png"), 80, 80)
SNOW_SIGN = (os.path.join("Assets", "Levels/Snow/Objects/Sign_1.png"), 60, 60)
SNOW_SIGNARROW = (os.path.join("Assets", "Levels/Snow/Objects/Sign_2.png"), 130, 100)
SNOW_SNOWMAN = (os.path.join("Assets", "Levels/Snow/Objects/SnowMan.png"), 200, 120)
SNOW_STONE = (os.path.join("Assets", "Levels/Snow/Objects/Stone.png"), 90, 32)
SNOW_TREE_1 = (os.path.join("Assets", "Levels/Snow/Objects/Tree_1.png"), 200, 300)
SNOW_TREE_2 = (os.path.join("Assets", "Levels/Snow/Objects/Tree_2.png"), 120, 180)

"""
Objects Fruits Snow
"""

# BLACKBERRY = (os.path.join("Assets", "Levels/Desert/Objects/Blackberry.png"), 70, 70)
