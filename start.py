# -*- coding:utf-8 -*-

import pygame
from pygame.sprite import Group

from human import Human
import game_functions as gf
from settings import Settings
from button import Button
from game_stats import GameStats

# def run_game():
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption('测试')
#     play_button = Button(ai_settings, screen, "Play")
#     # 创建一个用于存储游戏统计信息的实例
#     stats = GameStats(ai_settings)
#     human = Human(ai_settings, screen)
#     bg = Group()
#     while True:
#         gf.check_events(ai_settings, screen, stats, play_button, human, bg)
#         if stats.game_active:
#             human.update()
#         gf.update_screen(ai_settings, screen, stats, human, bg, play_button)

def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption(u'推箱子')
    stats = GameStats(ai_setting)
    play_button = Button(ai_setting, screen, 'Play')
    human = Human(ai_setting, screen)
    bgs = Group()
    trees = Group()
    suitcases = Group()
    targets = Group()
    while True:
        gf.check_events(ai_setting, screen, stats, play_button, human, bgs, trees, suitcases, targets)
        # if stats.game_active:
        #     human.update()
        gf.update_screen(ai_setting, screen, stats, human, bgs, trees, suitcases, targets, play_button)


if __name__ == '__main__':
    run_game()