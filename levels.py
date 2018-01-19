# -*- encoding:utf-8 -*-
"""
    author:lgh
"""

from positions.locations import *


class Level():

    def __init__(self, level):
        self.tree_location = eval('level_%s_tree_location' %level)
        self.target_location = eval('level_%s_target_location' %level)
        self.suitcase_location = eval('level_%s_suitcase_location' %level)
        self.human_location = eval('level_%s_human_location' %level)

    def get_tree_location(self):
        return self.tree_location

    def get_target_location(self):
        return self.target_location

    def get_suitcase_location(self):
        return self.suitcase_location

    def get_human_location(self):
        return self.human_location

