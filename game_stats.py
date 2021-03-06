# -*- coding:utf-8 -*-
"""
    game score
"""


class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings =ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_level = 19

    def reset_stats(self):
        """初始化在游戏运行期间可能编号的统计信息"""
        self.level = 1

    def level_up(self):
        """下一关"""
        if self.level < self.high_level:
            self.level += 1

    def get_level(self):
        return self.level