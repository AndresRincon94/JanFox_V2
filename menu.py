import pygame
import os
import init
import constants

# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))


# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (125, 206, 160)
green2 = (20, 90, 50)

# Game Fonts
font = "Dynamix.ttf"
menuImg = pygame.image.load("Assets/Levels/Menu/Menu.png")
foxImg = pygame.image.load('Assets/Sprites/personage/Fox/Jump/Jump(4).png')

size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
menuImg = pygame.transform.scale(menuImg, size)

# Game Framerate
clock = pygame.time.Clock()
FPS = 30


# Main Menu
def main_menu():
    menu = True
    # selected="start"
    pygame.mixer.music.load("Assets/Sound/Menu.mp3")
    pygame.mixer.music.play(3)

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    init.main()
                if event.key == pygame.K_c:
                    pygame.quit()
                    quit()

        # Main Menu UI
        screen.blit(menuImg, (0, 0))
        screen.blit(pygame.transform.scale(foxImg, (260, 250)), (100, 240))

        title = text_format("JANFOX", font, 90, green2)
        text_start = text_format("INICIAR 'I'", font, 50, black)
        text_quit = text_format("CERRAR 'C'", font, 50, black)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (constants.SCREEN_WIDTH / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_start, (constants.SCREEN_WIDTH / 2 - (start_rect[2] / 2), 280))
        screen.blit(text_quit, (constants.SCREEN_WIDTH / 2 - (quit_rect[2] / 2), 360))
        pygame.display.update()
        pygame.display.set_caption("JANFOX")


# Initialize the Game
main_menu()
