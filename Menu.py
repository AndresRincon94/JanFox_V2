import pygame
import os
import platform_scroller

# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width=1000
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
    pygame.mixer.music.load("Assets/Sound/Menu.mp3")
    pygame.mixer.music.play(9)
    
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
                        platform_scroller.main()
                        
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.blit(Bg, (0,0))
        screen.blit(pygame.transform.scale(Fox, (160, 150)), (100,340))

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
        pygame.display.set_caption("JANFOX")


#Initialize the Game
main_menu()
pygame.quit()
quit()
