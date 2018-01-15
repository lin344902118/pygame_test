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
        self.screen_width = 544
        self.screen_height = 544
        self.bg_color = (255, 255, 255)
        self.speed = 34

        self.tree_location = [[5,8],[5,9],[5,10],[6,8],[6,10],[7,5],[7,6],
                              [7,7],[7,8],[7,10],[8,5],[8,10],[8,11],[8,12],
                              [9,5],[9,6],[9,7],[9,12],[10,7],[10,9],[10,10],
                              [10,11],[10,12],[11,7],[11,9],[12,7],[12,8],[12,9]]

        self.target_location = [[6,9],[8,6],[9,11],[11,8]]

        self.suitcase_location = [[8,8],[8,9],[10,8],[9,10]]

        self.human_location = [9,9]