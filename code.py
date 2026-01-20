import ugame
import stage
import time
import random
import constants
import supervisor

def splash_scene():
    # this function is for the main game splash_scene

    # image banks for CircuitPython stores the images in bmp file
    # an image bank for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    # sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_mt_background,constants.SCREEN_X,constants.SCREEN_Y)

    # used this program to split the image into tile:
    # https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)   # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)   # blank white


    background.tile(2, 3, 0)   # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)   # blank white


    background.tile(2, 4, 0)   # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)   # blank white


    background.tile(2, 5, 0)   # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)   # blank white

    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites, items show up in order
    game.layers = [background]
    # render all sprites
    # most likely you will only render the background  once per game scene
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # wait for 2 seconds and then goes to the menu scene, 
        # it'll be a blank white scene
        time.sleep(2.0)
        menu_scene()

def menu_scene():
    # this function is for the main game game_scene

    # image banks for CircuitPython stores the images in bmp file
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)


    # set the background to image 0 in the image bank
    # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites, items show up in order
    game.layers = text + [background]
    # render all sprites
    # most likely you will only render the background  once per game scene
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()
 
        #redraw sprite
        # redraws game sprites
        game.tick()

def game_scene():
    # this function is for the main game game_scene

    # for score
    score = 0
    # score settings: this will print and show player their score
    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))
    # function loops through all aliens and checks if an alien
    # has a position of < 0 and if it does ands takes it and puts it in a
    # random x position, and y will be at the top

    # for lives
    lives = 5
    # lives settings: this will print and show player their score
    lives_text = stage.Text(width=29, height=14)
    lives_text.clear()
    lives_text.cursor(0, 0)
    lives_text.move(95, 1)
    lives_text.text("Lives: {}".format(lives))


    def show_alien():
        # this function takes an alien from off screen and moves it on screen
        # this function takes an alien from off screen and moves it on screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(
                    random.randint(0, constants.SCREEN_X - constants.SPRITE_SIZE),
                    constants.OFF_TOP_SCREEN
                )
                break
    # image banks for CircuitPython stores the images in bmp file
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("pew.wav",'rb')
    coin_sound = open("coin.wav", 'rb')
    boom_sound = open("boom.wav", 'rb')
    crash_sound = open("crash.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    # set the background to image 0 in the image bank
    # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    # i have two for loops for x and y axis, I start at 0 and go to the grid size
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            # this will now create a different background
            background.tile(x_location, y_location, tile_picked)

    # this is my ship sprite that can be moved, I subtract the sprite size x 2 from the screen so
    # the sprite starts at the bottom
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - ( 2 * constants.SPRITE_SIZE))

    # create list of aliens for when we shoot
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprites,9,constants.OFF_SCREEN_X,constants.OFF_SCREEN_Y)

        aliens.append(a_single_alien)
    show_alien()
    
    # create list of lasers for when we shoot
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites,10,constants.OFF_SCREEN_X,constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)
    game = stage.Stage(ugame.display, constants.FPS)

    # set the layers of all sprites, items show up in order
    game.layers = [score_text, lives_text] + aliens + lasers + [ship] + [background]
    # render all sprites
    # most likely you will only render the background  once per game scene
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # speed boost when B button is pressed is held
        if keys & ugame.K_X != 0:
            speed = 10
        else:
            speed = constants.SPRITE_MOVEMENT_SPEED

        # A button to fire
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            pass
        if keys & ugame.K_RIGHT != 0:
            # this code makes the sprite have boundaries, if it reaches the sides 
            # of the grid
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + speed, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT != 0:
            if ship.x >= 0:
                ship.move(ship.x - speed, ship.y)
            else:
                ship.move(0, ship.y)

        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            ship.move(ship. x, ship.y + 1)
        # update game logic
        if a_button == constants.button_state["button_just_pressed"]:
                # fire a laser
                for laser_number in range(len(lasers)):
                    if lasers[laser_number].x < 0:
                        lasers[laser_number].move(ship.x, ship.y)
                        sound.play(pew_sound)
                        break
        # each frame move the lasers that have been fired up
        # checks every laser and if it is on the screen, moves it up, then checks if 
        # if it goes off the top screen moves it back to holding.
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x,lasers[laser_number].y - constants.LASER_SPEED)

                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X,constants.OFF_SCREEN_Y)

        # each frame move the aliens down, that are on the screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(
                aliens[alien_number].x,
                aliens[alien_number].y + constants.ALIEN_SPEED
            )

                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X,constants.OFF_SCREEN_Y)
                    show_alien()
                    score -= 1
                    if score < 0:
                        score = 0

                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("My Score: {0}".format(score))

        # each frame check if any of the lasers are touching any of the aliens
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2,
                                        lasers[laser_number].x + 11, lasers[laser_number].y + 12,
                                        aliens[alien_number].x + 1, aliens[alien_number].y + 1,
                                        aliens[alien_number].x + 15, aliens[alien_number].y + 15):
                            # you hit an alien
                            aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            # get sound ready
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            score = score + 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("My Score: {0}".format(score))
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                if stage.collide(aliens[alien_number].x + 1,aliens[alien_number].y, aliens[alien_number].x + 15,
                                aliens[alien_number].y + 15,
                                ship.x,ship.y,ship.x + 15,ship.y + 15):
                    # alien hit the ship
                    sound.stop()
                    sound.play(crash_sound)

                    # ONE life lost every time user collides
                    lives = lives - 1
                    
                    # clear and redraw lives text
                    lives_text.clear()
                    lives_text.cursor(0, 0)
                    lives_text.move(95, 1)

                    # update the lives, if lives is 1 it'll give the user a warning
                    if lives == 1:
                        lives_text.text("Lives: 1!")
                    else:
                        lives_text.text("Lives: {}".format(lives))

                    game.render_block()

                    time.sleep(0.5)
                    # if all lives are lost, THEN it is a game over
                    if lives <= 0:
                        game_over_scene(score)
                    else:
                        aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        #redraw sprite
        # redraws game sprites
        game.render_sprites( aliens + lasers + [ship])
        game.tick()

def game_over_scene(final_score):
    # this function is the game over scene

    # image banks for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the image bank
    background = stage.Grid(
        image_bank_2,
        constants.SCREEN_GRID_X,
        constants.SCREEN_GRID_Y
    )

    # add text objects
    text = []

    text1 = stage.Text(
        width=29,
        height=14,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None
    )
    text1.move(22, 20)
    text1.text("Final Score: {:02d}".format(final_score))
    text.append(text1)

    text2 = stage.Text(
        width=29,
        height=14,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None
    )
    text2.move(43, 60)
    text2.text("GAME OVER")
    text.append(text2)

    text3 = stage.Text(
        width=29,
        height=14,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None
    )
    text3.move(32, 110)
    text3.text("PRESS SELECT")
    text.append(text3)

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set the layers, items show up in order
    game.layers = text + [background]

    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # Start button selected
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()

        # update game logic
        game.tick()  # wait until refresh rate finishes
        
if __name__ == "__main__":
    splash_scene()
