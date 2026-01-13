import ugame
import stage

import constants
def game_scene():
    # this function is for the main game game_scene

    # image banks for CircuitPython stores the images in bmp file
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # set the background to image 0 in the image bank
    # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    # this is my ship sprite that can be moved, I subtract the sprite size x 2 from the screen so
    # the sprite starts at the bottom
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - ( 2 * constants.SPRITE_SIZE))
    # create a stage for the background to show up on
    # and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites, items show up in order
    game.layers = [ship] + [background]
    # render all sprites
    # most likely you will only render the background  once per game scene
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            # this code makes the sprite have boundaries, if it reaches the sides 
            # of the grid
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)

        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            ship.move(ship. x, ship.y + 1)
        # update game logic

        #redraw sprite
        # redraws game sprites
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()
