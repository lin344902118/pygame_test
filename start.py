# -*- coding:utf-8 -*-

import pygame
from pygame.sprite import Group

from human import Human
import game_functions as gf
from settings import Settings
from button import Button
from game_stats import GameStats

def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption(u'推箱子')
    stats = GameStats(ai_setting)
    play_button = Button(screen, 'Play')
    next_button = Button(screen, 'Next', x=172, y=300)
    human = Human(ai_setting, screen)
    bgs = Group()
    trees = Group()
    suitcases = Group()
    targets = Group()
    while True:
        gf.check_events(ai_setting, screen, stats, play_button, next_button, human, bgs, trees, suitcases, targets)
        gf.update_screen(ai_setting, screen, stats, human, bgs, trees, suitcases, targets, play_button, next_button)


if __name__ == '__main__':
    run_game()