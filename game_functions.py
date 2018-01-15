# -*- coding:utf-8 -*-
import sys

import pygame
from background import Background, Tree, SuitCase, Target

def create_bg(ai_settings, screen, x, y, bgs):
    bg = Background(ai_settings, screen)
    bg_width = bg.rect.width
    bg_height = bg.rect.height
    bg.rect.x = bg_width * x
    bg.rect.y = bg_height * y
    bgs.add(bg)


def create_bgs(ai_settings, screen, bgs):
    bg = Background(ai_settings, screen)
    number_bg_x = ai_settings.screen_width // bg.rect.width
    number_bg_y = ai_settings.screen_height // bg.rect.height
    for x in range(number_bg_x):
        for y in range(number_bg_y):
            create_bg(ai_settings, screen, x, y, bgs)

def create_tree(ai_settings, screen, x, y, trees):
    tree = Tree(ai_settings, screen)
    tree_width = tree.rect.width
    tree_height = tree.rect.height
    tree.rect.x = tree_width * x
    tree.rect.y = tree_height * y
    trees.add(tree)

def create_trees(ai_settings,screen, trees):
    for location in ai_settings.tree_location:
        x, y = location[0]-1, location[1]-1
        create_tree(ai_settings, screen, x, y, trees)

def create_suitcase(ai_settings, screen, x, y, suitcases):
    suitcase = SuitCase(ai_settings, screen)
    suitcase_width = suitcase.rect.width
    suitcase_height = suitcase.rect.height
    suitcase.rect.x = suitcase_width * x
    suitcase.rect.y = suitcase_height * y
    suitcases.add(suitcase)

def create_suitcases(ai_settings,screen, suitcases):
    for location in ai_settings.suitcase_location:
        x, y = location[0]-1, location[1]-1
        create_suitcase(ai_settings, screen, x, y, suitcases)

def create_target(ai_settings, screen, x, y, targets):
    target = Target(ai_settings, screen)
    target_width = target.rect.width
    target_height = target.rect.height
    target.rect.x = target_width * x
    target.rect.y = target_height * y
    targets.add(target)

def create_targets(ai_settings,screen, targets):
    for location in ai_settings.target_location:
        x, y = location[0]-1, location[1]-1
        create_target(ai_settings, screen, x, y, targets)

def check_events(ai_settings, screen, stats, play_button, human, bgs, trees, suitcases, targets):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, human)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, human)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, human, bgs, trees, suitcases, targets, play_button, mouse_x, mouse_y)


def check_keydown_events(event, human):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_LEFT:
        human.moving_left = True
        human.update()
    elif event.key == pygame.K_RIGHT:
        human.moving_right = True
        human.update()
    elif event.key == pygame.K_UP:
        human.moving_top = True
        human.update()
    elif event.key == pygame.K_DOWN:
        human.moving_bottom = True
        human.update()


def check_keyup_events(event, human):
    if event.key == pygame.K_LEFT:
        human.moving_left = False
    elif event.key == pygame.K_RIGHT:
        human.moving_right = False
    elif event.key == pygame.K_UP:
        human.moving_top = False
    elif event.key == pygame.K_DOWN:
        human.moving_bottom = False

def check_play_button(ai_settings, screen, stats, human, bgs, trees, suitcases, targets, play_button, mouse_x, mouse_y):
    """在玩家单机play按钮开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True
        bgs.empty()
        trees.empty()
        suitcases.empty()
        targets.empty()
        create_bgs(ai_settings, screen, bgs)
        create_trees(ai_settings, screen, trees)
        create_suitcases(ai_settings, screen, suitcases)
        create_targets(ai_settings, screen, targets)

def update_screen(ai_settings, screen, stats, human, bgs, trees, suitcases, targets, play_button):
    if stats.game_active:
        bgs.draw(screen)
        trees.draw(screen)
        suitcases.draw(screen)
        targets.draw(screen)
        human.blit()
    else:
        screen.fill(ai_settings.bg_color)
        play_button.draw_button()
    # 让最近绘制的屏幕可见
    pygame.display.flip()



