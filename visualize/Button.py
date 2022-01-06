# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_ui_elements.md

import pygame
from .constant import *

class Font:
    def __init__(self, font, antialias, color, text, x, y):
        self.font = font
        self.antialias = antialias
        self.text = text
        self.color = color
        self.x = x
        self.y = y

    def draw(self, SCREEN):
        SCREEN.blit(self.font.render(self.text, self.antialias, self.color), (self.x, self.y))
# 

class Button:
    def __init__(self, x, y, width, height, color, text, size):
        self.color = color
        self.text = text
        self.t_size = size
        self.b_font = pygame.font.SysFont("Courier", self.t_size)
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, SCREEN, pos):
        b_color = self.color[1] if self.rect.collidepoint(pos) else self.color[0]
        pygame.draw.rect(SCREEN, b_color, (self.rect))

        t_width, t_height = self.b_font.size(self.text)
        t_x, t_y = self.rect.centerx - t_width // 2, self.rect.centery - t_height // 2

        b_text = Font(self.b_font, True, WHITE, self.text, t_x, t_y)
        b_text.draw(SCREEN)

    def is_click(self, pos, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return self.rect.collidepoint(pos)
# 

class Dropdown:
    def __init__(self, x, y, width, height, color_m, color_op, main, options, size):
        self.color_m = color_m
        self.color_op = color_op
        self.main = main
        self.options = options
        self.t_size = size
        self.b_font = [pygame.font.SysFont("Courier", self.t_size)] * (len(self.options) + 1)
        self.rect = pygame.Rect(x, y, width, height)
        self.active = False
        self.draw_options = False
        self.selected = -1

    def draw(self, SCREEN, pos):
        self.update_font()
        mb_color = self.color_m[1] if self.rect.collidepoint(pos) else self.color_m[0]
        pygame.draw.rect(SCREEN, mb_color, (self.rect))

        t_width, t_height = self.b_font[0].size(self.main)
        t_x, t_y = self.rect.centerx - t_width // 2, self.rect.centery - t_height // 2
        
        mb_text = Font(self.b_font[0], True, WHITE, self.main, t_x, t_y)
        mb_text.draw(SCREEN)

        if self.draw_options:
            for i, option in enumerate(self.options):
                rect_op = self.rect.copy()
                rect_op.y += (i + 1) * self.rect.height
                
                opb_color = self.color_op[1] if rect_op.collidepoint(pos) else self.color_op[0]
                pygame.draw.rect(SCREEN, opb_color, (rect_op))
                
                t_width, t_height = self.b_font[i + 1].size(option)
                t_x, t_y = rect_op.centerx - t_width // 2, rect_op.centery - t_height // 2

                opb_text = Font(self.b_font[i + 1], True, WHITE, option, t_x, t_y)
                opb_text.draw(SCREEN)

    def is_choose(self, pos, event_list):
        self.active = self.rect.collidepoint(pos)

        self.selected = -1
        for i in range(len(self.options)):
            op_rect = self.rect.copy()
            op_rect.y += (i + 1) * self.rect.height

            if op_rect.collidepoint(pos):
                self.selected = i
                break

        if not self.active and self.selected == -1:
            self.draw_options = False

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.active:
                    self.draw_options = not self.draw_options

                elif self.draw_options and self.selected != -1:
                    self.draw_options = False
                    return self.selected

        return -1

    def update_font(self):
        # Find the font size that does not exceed the box.
        self.b_font[0] = pygame.font.SysFont("Courier", self.t_size)
        x = 1
        t_width, _ = self.b_font[0].size(self.main)

        while t_width + 6 > self.rect.width:
            self.b_font[0] = pygame.font.SysFont("Courier", self.t_size - x)
            t_width, _ = self.b_font[0].size(self.main)
            x += 1

        for i, option in enumerate(self.options):  
            self.b_font[i + 1] = pygame.font.SysFont("Courier", self.t_size)
            x = 1
            t_width, _ = self.b_font[i].size(option)

            while t_width + 6 > self.rect.width:
                self.b_font[i + 1] = pygame.font.SysFont("Courier", self.t_size - x)
                t_width, _ = self.b_font[i + 1].size(option)
                x += 1
# 

# https://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

class Slider:
    def __init__(self, x, y, width, height, t_box_width, color, b_color, mini, maxi, val, text, size, val_size):
        self.val = val
        self.mini = mini
        self.maxi = maxi
        self.color = color
        self.b_color = b_color
        self.active = False
        self.hold = False # Mouse click and hold

        # Text box
        self.text = text
        self.t_size = size
        self.t_font = pygame.font.SysFont("Courier", self.t_size)
        self.t_rect = pygame.Rect(x, y, t_box_width, height)

        # Slider box background
        self.main_sli_rect = pygame.Rect(self.t_rect.right + 3, y, width, height)
        self.sli_w = width - 18
        self.sli_h = height // 5
        self.sli_rect = pygame.Rect(self.main_sli_rect.centerx - self.sli_w // 2, self.t_rect.centery - self.sli_h // 2, self.sli_w, self.sli_h)

        # Val box
        self.v_size = val_size
        self.v_font = pygame.font.SysFont("Courier", self.v_size)
        self.v_rect = pygame.Rect(self.main_sli_rect.right + 3, y, t_box_width, height)    

    def draw(self, SCREEN, pos):
        # Text box, Slider box, Val box
        pygame.draw.rect(SCREEN, self.color, (self.t_rect))
        pygame.draw.rect(SCREEN, self.color, (self.main_sli_rect))
        pygame.draw.rect(SCREEN, WHITE, (self.sli_rect))
        pygame.draw.rect(SCREEN, self.color, (self.v_rect))

        # Text box's font
        t_width, t_height = self.t_font.size(self.text)
        t_x, t_y = self.t_rect.centerx - t_width // 2, self.t_rect.centery - t_height // 2

        box_text = Font(self.t_font, True, WHITE, self.text, t_x, t_y)
        box_text.draw(SCREEN)

        # Val box's font
        v_width, v_height = self.v_font.size(str(self.val))
        v_x, v_y = self.v_rect.centerx - v_width // 2, self.v_rect.centery - v_height // 2

        box_val = Font(self.v_font, True, WHITE, str(self.val), v_x, v_y)
        box_val.draw(SCREEN)

        # Button position
        button_pos = (self.sli_rect.left + int((self.val - self.mini) / (self.maxi - self.mini) * self.sli_w), self.sli_rect.centery)
        self.button = pygame.draw.circle(SCREEN, self.b_color, (button_pos), 6)

        if self.hold:
            self.val = int((pos[0] - self.sli_rect.left) / self.sli_w * (self.maxi - self.mini) + self.mini)
            
            if self.val < self.mini:
                self.val = self.mini

            if self.val > self.maxi:
                self.val = self.maxi

    def is_hold(self, pos, event_list):
        self.active = self.button.collidepoint(pos)

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.active:
                    self.hold = not self.hold

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.hold = False

    def get_val(self):
        return self.val
