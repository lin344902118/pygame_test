# -*- coding:utf-8 -*-


class Settings():
    """
        存储游戏的所有设置的类
    """
    def __init__(self):
        """
            初始化游戏的设置
        """
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)
        self.speed = 3
        self.love_limit = 3
        # 外星人设置
        self.fleet_drop_speed = 10
        # 什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.mouse_speed_factor = 1
        # fleet_direction为1表示向右移,-1表示向左移
        self.fleet_direction = 1
        self.mouse_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.mouse_speed_factor *= self.speedup_scale
        self.mouse_points = int(self.mouse_points * self.score_scale)