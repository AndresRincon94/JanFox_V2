import pygame
from pygame.locals import *
import os

# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width=800
screen_height=600

screen=pygame.display.set_mode((screen_width, screen_height))

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText

# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(125, 206, 160)
green2 = (20, 90, 50)

# Game Fonts
font = "Dynamix.ttf"
Bg = pygame.image.load("Assets/Levels/Menu.png")
Piso1 = pygame.image.load('Assets/Levels/Desert/Tile/2.png')
Tree = pygame.image.load('Assets/Levels/jungle/Object/Tree_3.png')
Piso2 = pygame.image.load('Assets/Levels/Desert/Tile/2.png')
Piso3 = pygame.image.load('Assets/Levels/Desert/Tile/3.png')
Fox = pygame.image.load('Assets/Sprites/personage/Fox/Idle/Idle (1).png')

size = (screen_width,screen_height) 
Bg = pygame.transform.scale(Bg, size)


# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Main Menu
def main_menu():

    menu=True
    selected="start"

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        from platform_scroller import main
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        # screen.fill(green)
        screen.blit(Bg, (0,0))
        # screen.blit(pygame.transform.scale(Piso1, (650, 40)), (90,500))
        # screen.blit(pygame.transform.scale(Tree, (120, 170)), (620,330))
        screen.blit(pygame.transform.scale(Fox, (120, 150)), (100,360))

        title=text_format("JANFOX", font, 90, green2)
        if selected=="start":
            text_start=text_format("START", font, 50, white)
        else:
            text_start = text_format("START", font, 50, black)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 50, white)
        else:
            text_quit = text_format("QUIT", font, 50, black)

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 280))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")

#Initialize the Game
main_menu()
pygame.quit()
quit()
