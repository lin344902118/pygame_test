# -*- coding:utf-8 -*-
import pygame
from pygame.sprite import Group

from love import Love
import game_functions as gf
from settings import Settings
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('测试')
    play_button = Button(ai_settings, screen, "Play")
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    love = Love(ai_settings, screen)
    mouses = Group()
    gf.create_fleet(ai_settings, screen, love, mouses)
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, love, mouses)
        if stats.game_active:
            love.update()
            gf.update_mouses(ai_settings, screen, stats, sb, love, mouses)
        gf.update_screen(ai_settings, screen, stats, sb, love, mouses, play_button)

if __name__ == '__main__':
    run_game()