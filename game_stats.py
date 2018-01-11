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
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能编号的统计信息"""
        self.love_left = self.ai_settings.love_limit
        self.score = 0
        self.level = 1