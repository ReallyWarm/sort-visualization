import pygame
from .constant import *

class ArrayBar:
    def __init__(self, index, val, size):
        self.color = WHITE
        self.index = index
        self.val = val
        self.x = (WIDTH // size) * self.index
        self.y = HEIGHT - ((VIS_H // size) * val)
        self.width = WIDTH // size
        self.height = (VIS_H // size) * val

    def get_height(self):
        return self.height

    def get_x(self):
        return self.x

    def get_index(self):
        return self.index

    def get_val(self):
        return self.val

    def bar_check(self):
        self.color = RED

    def bar_move(self):
        self.color = BLUE

    def bar_mark(self):
        self.color = YELLOW

    def bar_done(self):
        self.color = WHITE

    def draw(self, SCREEN):
        pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.width, self.height))


