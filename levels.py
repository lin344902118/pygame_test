# -*- encoding:utf-8 -*-
"""
    author:lgh
"""


class Level():

    def __init__(self, level):
        if level == 1:
            self.tree_location = [[5, 8], [5, 9], [5, 10], [6, 8], [6, 10], [7, 5], [7, 6],
                                  [7, 7], [7, 8], [7, 10], [8, 5], [8, 10], [8, 11], [8, 12],
                                  [9, 5], [9, 6], [9, 7], [9, 12], [10, 7], [10, 9], [10, 10],
                                  [10, 11], [10, 12], [11, 7], [11, 9], [12, 7], [12, 8], [12, 9]]
            self.target_location = [[6, 9], [8, 6], [9, 11], [11, 8]]
            self.suitcase_location = [[8, 8], [8, 9], [10, 8], [9, 10]]
            self.human_location = [9, 9]
        elif level == 2:
            self.tree_location = [[5,4],[5,5],[5,6],[5,7],[5,8],[6,4],[6,8],[6,9],[6,10],
                                  [6,11],[6,12],[7,4],[7,8],[7,9],[7,12],[8,4],[8,12],[9,4],
                                  [9,5],[9,6],[9,7],[9,8],[9,12],[10,8],[10,10],[10,11],
                                  [10,12],[11,6],[11,7],[11,8],[11,11],[12,6],[12,11],
                                  [13,6],[13,7],[13,8],[13,9],[13,10],[13,11]]
            self.target_location = [[12, 7], [12, 8], [12, 9]]
            self.suitcase_location = [[7, 6], [8, 6], [7, 7]]
            self.human_location = [6, 5]

    def get_tree_location(self):
        return self.tree_location

    def get_target_location(self):
        return self.target_location

    def get_suitcase_location(self):
        return self.suitcase_location

    def get_human_location(self):
        return self.human_location

