import pygame
from pygame.color import Color
from animation import Animation
from stone import Stone
from const import *

class Catapult(Animation):
    def __init__(self, stone):
        self.sprite_image = 'catapult.png'
        self.sprite_width = 32
        self.sprite_height = 32
        self.sprite_columns = 5
        self.fps = 30
        self.stone = stone
        self.state = CATAPULT_READY
        self.init_animation()

    def update(self):
        if self.state == CATAPULT_FIRE:
            self.clac_next_frame()

            if self.current_frame == self.sprite_columns:
                self.current_frame = 0
                self.state = CATAPULT_READY
                self.stone.setup(
                    (self.rect.x, self.rect.y),
                    self.power, self.direction)
            else:
                self.current_frame = 0

            rect = (self.sprite_width*self.current_frame, 0,
                    self.sprite_width, self.sprite_height)
            self.image.blit( self.sprite_sheet, (0, 0), rect)
            self.image.set_colorkey(Color(255, 0, 255))

        def forward(self):
            if self.rect.x > 0:
                self.rect.x -= 1

        def fire(self, power, direction):
            self.state = CATAPULT_FIRE
            self.power = power
            self.direction = direction
