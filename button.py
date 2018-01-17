# -*- coding:utf-8 -*-
"""
    buttons
"""

import pygame.font


class Button():

    def __init__(self, screen, msg, width=200, height=50, button_color=(0, 255, 0), text_color=(255, 255, 255), x=None, y=None):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width , self.height = width, height
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, 48)


        self.rect  = pygame.Rect(0, 0, self.width, self.height)
        if x and y:
            self.rect.x = x
            self.rect.y = y
        else:
            self.rect.center = self.screen_rect.center

        # 按钮的标签只需创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染成图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制一个用颜色填充的按钮，在绘制文本"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)