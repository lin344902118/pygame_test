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
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        self.moving_left = False
        self.moving_right = False
        self.moving_top = False
        self.moving_bottom = False
        self.speed = self.ai_settings.speed

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.center -= self.speed
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.speed
        elif self.moving_top and self.rect.top > 0:
            self.bottom -= self.speed
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.speed
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom