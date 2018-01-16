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
            check_keydown_events(event, human, trees, suitcases, ai_settings)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, human, suitcases)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, bgs, trees, suitcases, targets, play_button, mouse_x, mouse_y)

def get_locations(group):
    locations = list()
    for sprite in group:
        locations.append([sprite.rect.x, sprite.rect.y])
    return locations

def get_nearby_location(sprite, location):
    left = sprite.rect.x-sprite.rect.width
    right = sprite.rect.x+sprite.rect.width
    top = sprite.rect.y-sprite.rect.height
    bottom = sprite.rect.y+sprite.rect.height
    if location == 'left':
        return [left, sprite.rect.y]
    elif location == 'right':
        return [right, sprite.rect.y]
    elif location == 'top':
        return [sprite.rect.x, top]
    elif location == 'bottom':
        return [sprite.rect.x, bottom]

def check_collide(sprite, groups):
    locations = get_locations(groups)
    if get_nearby_location(sprite, 'left') in locations:
        sprite.moving_left = False
    if get_nearby_location(sprite, 'right') in locations:
        sprite.moving_right = False
    if get_nearby_location(sprite, 'top') in locations:
        sprite.moving_top = False
    if get_nearby_location(sprite, 'bottom') in locations:
        sprite.moving_bottom = False

def get_nearby_suitcase(sprite, groups, location):
    for group in groups:
        locations = get_nearby_location(sprite, location)
        x, y = locations[0], locations[1]
        if x == group.rect.x and y == group.rect.y:
            return group
    return None

def get_nearby_suitcases(sprite, groups):
    left = sprite.rect.x-sprite.rect.width
    right = sprite.rect.x+sprite.rect.width
    top = sprite.rect.y-sprite.rect.height
    bottom = sprite.rect.y+sprite.rect.height
    suitcases = list()
    for group in groups:
        if left == group.rect.x and group.rect.y == sprite.rect.y:
            suitcases.append(group)
        if right == group.rect.x and group.rect.y == sprite.rect.y:
            suitcases.append(group)
        if group.rect.x == sprite.rect.x and top == group.rect.y:
            suitcases.append(group)
        if group.rect.x == sprite.rect.x and bottom == group.rect.y:
            suitcases.append(group)
    return suitcases

def check_game_over(suitcases, ai_settings):
    case_locations = list()
    for suitcase in suitcases:
        case_locations.append([suitcase.rect.x, suitcase.rect.y])
    target_locations = list()
    for target in ai_settings.target_location:
        target_locations.append([(target[0]-1)*34, (target[1]-1)*34])
    for location in case_locations:
        if location not in target_locations:
            return False
    return True


def show_action(obj, name='human'):
    print('_____________%s__________________' %name)
    if not obj.moving_left:
        print('can not moving left')
    if not obj.moving_right:
        print('can not moving right')
    if not obj.moving_top:
        print('can not moving top')
    if not obj.moving_bottom:
        print('can not moving bottom')

def check_keydown_events(event, human, trees, suitcases, ai_settings):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_LEFT:
        human.moving_left = True
        suitcase = get_nearby_suitcase(human, suitcases, 'left')
        if suitcase:
            suitcase.moving_left = True
            check_collide(suitcase, trees)
            if not suitcase.moving_left:
                human.moving_left = False
    elif event.key == pygame.K_RIGHT:
        human.moving_right = True
        suitcase = get_nearby_suitcase(human, suitcases, 'right')
        if suitcase:
            suitcase.moving_right = True
            check_collide(suitcase, trees)
            if not suitcase.moving_right:
                human.moving_right = False
    elif event.key == pygame.K_UP:
        human.moving_top = True
        suitcase = get_nearby_suitcase(human, suitcases, 'top')
        if suitcase:
            suitcase.moving_top = True
            check_collide(suitcase, trees)
            if not suitcase.moving_top:
                human.moving_top = False
    elif event.key == pygame.K_DOWN:
        human.moving_bottom = True
        suitcase = get_nearby_suitcase(human, suitcases, 'bottom')
        if suitcase:
            suitcase.moving_bottom = True
            check_collide(suitcase, trees)
            if not suitcase.moving_bottom:
                human.moving_bottom = False
    check_collide(human, trees)
    human.update()
    suitcases.update()


def check_keyup_events(event, human, suitcases):
    if event.key == pygame.K_LEFT:
        human.moving_left = False
        for suitcase in suitcases:
            suitcase.moving_left = False
    elif event.key == pygame.K_RIGHT:
        human.moving_right = False
        for suitcase in suitcases:
            suitcase.moving_right = False
    elif event.key == pygame.K_UP:
        human.moving_top = False
        for suitcase in suitcases:
            suitcase.moving_top = False
    elif event.key == pygame.K_DOWN:
        human.moving_bottom = False
        for suitcase in suitcases:
            suitcase.moving_bottom = False

def check_play_button(ai_settings, screen, stats, bgs, trees, suitcases, targets, play_button, mouse_x, mouse_y):
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
        targets.draw(screen)
        suitcases.draw(screen)
        human.blit()
    else:
        screen.fill(ai_settings.bg_color)
        play_button.draw_button()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
    if check_game_over(suitcases, ai_settings):
        stats.game_active = False



