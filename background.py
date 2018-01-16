# -*- encoding:utf-8 -*-
"""
    创建一个背景类
    author:lgh
"""

import pygame
from pygame.sprite import Sprite


class BaseSprite(Sprite):

    def __init__(self, ai_settings, screen, img_dir):
        super(BaseSprite, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load(img_dir)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blit(self):
        self.screen.blit(self.image, self.rect)

class Background(BaseSprite):

    def __init__(self, ai_settings, screen):
        BaseSprite.__init__(self, ai_settings, screen, 'images/bg.png')


class Target(BaseSprite):

    def __init__(self, ai_settings, screen):
        BaseSprite.__init__(self, ai_settings, screen, 'images/target.png')


class Tree(BaseSprite):

    def __init__(self, ai_settings, screen):
        BaseSprite.__init__(self, ai_settings, screen, 'images/tree.png')


class SuitCase(BaseSprite):

    def __init__(self, ai_settings, screen):
        BaseSprite.__init__(self, ai_settings, screen, 'images/suitcase.png')
        self.moving_left = False
        self.moving_right = False
        self.moving_top = False
        self.moving_bottom = False
        self.speed = self.ai_settings.speed

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
        elif self.moving_top and self.rect.top > 0:
            self.rect.y -= self.speed
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.speed
