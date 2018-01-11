# -*- coding:utf-8 -*-

import pygame
from pygame.sprite import Sprite


class Mouse(Sprite):

    def __init__(self, ai_settings, screen):
        super(Mouse, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/tom.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """如果位于屏幕边缘，返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left < 0:
            return True

    def update(self):
        """向右移动"""
        self.y += (self.ai_settings.mouse_speed_factor * self.ai_settings.fleet_direction)
        self.rect.y = self.y