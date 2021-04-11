import pygame,sys
import pygame

import constants
import levels

from player import Player
#from Menu import main_menu

def main():
    """ Main Program """
    pygame.init()
    pygame.mixer.music.load("Assets/Sound/backgroundSound2.mp3")
    pygame.mixer.music.play(3)

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
   
    pygame.display.set_caption("JANFOX")

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 240
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_ESCAPE:
                    pausa()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_ESCAPE:
                    pausa()

            

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


def pausa():
    
    font = "Dynamix.ttf"
    green2 = (20, 90, 50)
    black=(0, 0, 0)

    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    bg = pygame.image.load('Assets/Levels/Menu.png')
    bg = pygame.transform.scale(bg, size)

    win = pygame.display.set_mode(size)
    pausado = True
    while pausado:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pausado = False
                if event.key == pygame.K_r:
                    from Menu import main_menu

        pausaText = text_format("PAUSA", font, 50, green2)
        continuarText = text_format("CONTINUAR 'C'", font, 35, black)
        quitarText =text_format("QUITAR 'R'", font, 35, black)
        
        win.blit(bg, (0,0))
        win.blit(pausaText,(320,150))
        win.blit(continuarText,(280,300))
        win.blit(quitarText,(320,350))

        pygame.display.update()


def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText


if __name__ == "__main__":
    main()
