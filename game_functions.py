# -*- coding:utf-8 -*-
import sys

from time import sleep
import pygame
from mouse import Mouse


def get_number_rows(ai_settings, love_height, mouse_height):
    """计算屏幕可以容纳多少行老鼠"""
    available_space_y = (ai_settings.screen_height - (3 * mouse_height) - love_height)
    number_rows = int(available_space_y / (2 * love_height))
    return number_rows

def get_number_mouses_x(ai_settings, mouse_width):
    """计算可以容纳的老鼠"""
    available_space_x = ai_settings.screen_width - 2 * mouse_width
    number_mouses_x = int(available_space_x / (2 * mouse_width))
    return number_mouses_x

def create_mouse(ai_settings, screen, mouses, mouse_number, row_number):
    mouse = Mouse(ai_settings, screen)
    mouse_width = mouse.rect.width
    mouse.x = mouse_width + 2 * mouse_width * mouse_number
    mouse.rect.x = mouse.x
    mouse.rect.y = mouse.rect.height + 2 * mouse.rect.height * row_number
    mouses.add(mouse)

def create_fleet(ai_settings, screen, love, mouses):
    """创建老鼠群"""
    mouse = Mouse(ai_settings, screen)
    number_mouses_x = get_number_mouses_x(ai_settings, mouse.rect.width)
    number_rows = get_number_rows(ai_settings, love.rect.height, mouse.rect.height)

    for row_number in range(number_rows):
        for mouse_number in range(number_mouses_x):
            create_mouse(ai_settings, screen, mouses, mouse_number, row_number)

def check_events(ai_settings, screen, stats, sb, play_button, love, mouses):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, love)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, love)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, love, mouses, mouse_x, mouse_y)


def check_keydown_events(event, love):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_LEFT:
        love.moving_left = True
    elif event.key == pygame.K_RIGHT:
        love.moving_right = True
    elif event.key == pygame.K_UP:
        love.moving_top = True
    elif event.key == pygame.K_DOWN:
        love.moving_bottom = True


def check_keyup_events(event, love):
    if event.key == pygame.K_LEFT:
        love.moving_left = False
    elif event.key == pygame.K_RIGHT:
        love.moving_right = False
    elif event.key == pygame.K_UP:
        love.moving_top = False
    elif event.key == pygame.K_DOWN:
        love.moving_bottom = False

def check_play_button(ai_settings, screen, stats, sb, play_button, love, mouses, mouse_x, mouse_y):
    """在玩家单机play按钮开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_loves()

        mouses.empty()

        create_fleet(ai_settings, screen, love, mouses)

def update_screen(ai_settings, screen, stats, sb, love, mouses, play_button):
    # 每次循环重绘屏幕
    screen.fill(ai_settings.bg_color)
    love.blit()
    mouses.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def love_hit(ai_settings, screen, stats, sb, love, mouses):
    """响应被老鼠撞到的哆啦A梦"""
    if stats. love_left > 0:
        stats.love_left -= 1
        sb.prep_loves()
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    mouses.empty()
    create_fleet(ai_settings, screen, love, mouses)
    sleep(0.5)

def check_mouses_bottom(ai_settings, screen, stats, sb, love, mouses):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for mouse in mouses.sprites():
        if mouse.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            love_hit(ai_settings, screen, stats, sb, love, mouses)
            break
            
def update_mouses(ai_settings, screen, stats, sb, love, mouses):
    # 更新老鼠群的位置
    mouses.update()

    # 检测老鼠和哆啦A梦之间的碰撞
    if pygame.sprite.spritecollideany(love, mouses):
        love_hit(ai_settings, screen, stats, sb, love, mouses)
    # 检查是否有老鼠到达屏幕底端
    check_mouses_bottom(ai_settings, screen, stats, sb, love, mouses)
