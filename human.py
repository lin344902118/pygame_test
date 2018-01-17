# -*- coding:utf-8 -*-
"""
    创建一个人物类
"""

import pygame
from pygame.sprite import Sprite


class Human(Sprite):
    def __init__(self, ai_settings, screen):
        super(Human, self).__init__()
        self.image = pygame.image.load('images/human.jpg')
        self.screen = screen
        self.ai_settings = ai_settings
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        x, y = ai_settings.human_location[0]-1, ai_settings.human_location[1]-1
        self.rect.x = self.rect.width * x
        self.rect.y = self.rect.height * y
        self.moving_left = False
        self.moving_right = False
        self.moving_top = False
        self.moving_bottom = False
        self.speed = self.ai_settings.speed

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
        elif self.moving_top and self.rect.top > 0:
            self.rect.y -= self.speed
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.speed