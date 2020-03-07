import sys
import pygame
from bullet import Bullet

#定义一个响应键盘、鼠标事件的函数，参数指向指定的飞船
def check_events(sb_settings, screen, airship, bullets):
    #监听键盘和鼠标事件
    for event in pygame.event.get():
        #判断用户是否点击关闭按钮
        if event.type == pygame.QUIT:
            #sys.exit()
            pygame.quit()
        #判断用户是否按下键盘上某个按键
        if event.type == pygame.KEYDOWN:
            #判断是否按下 右光标 键
            if event.key == pygame.K_RIGHT:
                #设置飞船右移标记为真，同时左移标记为假
                airship.move_right = True
                airship.move_left = False
            #判断是否按下 左光标 键
            elif event.key == pygame.K_LEFT:
                #设置飞船左移标记为真，同时右移标记为假
                airship.move_left = True
                airship.move_right = False
            elif event.key == pygame.K_SPACE:
                #发射子弹
                fire_bullet(sb_settings, screen, airship, bullets)
            else:
                #若没有按下左、右光标键，则设置飞船左移、右移标记均为假
                airship.move_right = False
                airship.move_left = False

#定义屏幕更新函数，注意添加三个参数
def update_screen(sb_settings, screen, airship, bullets):
    #绘制屏幕
    screen.fill(sb_settings.bg_color)
    #绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    airship.blitme()

    #更新显示内容
    pygame.display.flip()

#定义子弹更新函数
def update_bullets(bullets):
    #更新子弹坐标
    bullets.update()
    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

#定义发射子弹函数
def fire_bullet(sb_settings, screen, airship, bullets):
    # 创建一个子弹，并将其加入到编组 bullets 中
    new_bullet = Bullet(sb_settings, screen, airship)
    bullets.add(new_bullet)
    