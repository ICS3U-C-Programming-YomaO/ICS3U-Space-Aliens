#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: January, 2025
# This program holds all my constants

SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 5
TOTAL_NUMBER_OF_LASERS = 5
FPS = 60
SPRITE_MOVEMENT_SPEED = 1
SHIP_SPEED = 1
ALIEN_SPEED = 1
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
LASER_SPEED = 2
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
# using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
}
# new palette for red filled text (RGB565 format, 16 colors = 32 bytes)
# Each color is 2 bytes: R5G6B5 format
RED_PALETTE = (
    # Color 0 (transparent/background)
    b'\xff\xff'  # Color 0: white (0xFFFF)
    b'\x00\x00'  # Color 1: black (0x0000)
    b'\x1f\x00'  # Color 2: red (0xF800)
    b'\x00\xf8'  # Color 3: green (0x07E0)
    b'\x00\x1f'  # Color 4: blue (0x001F)
    b'\xff\x00'  # Color 5: yellow (0xFFE0)
    b'\x00\xff'  # Color 6: cyan (0x07FF)
    b'\xff\xff'  # Color 7: white (duplicate)
    b'\x80\x00'  # Color 8: dark red (0x8000)
    b'\x00\x80'  # Color 9: dark green (0x0400)
    b'\x00\x80'  # Color 10: dark blue (0x0010)
    b'\xf8\x00'  # Color 11: bright red (0xF800)
    b'\x07\xe0'  # Color 12: bright green (0x07E0)
    b'\x00\x1f'  # Color 13: bright blue (0x001F)
    b'\xff\xe0'  # Color 14: bright yellow (0xFFE0)
    b'\xff\xff'  # Color 15: bright white (0xFFFF)
)
