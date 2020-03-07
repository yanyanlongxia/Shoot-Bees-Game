#导入支持模块
import sys
import pygame

#从自定义的模块中导入自定义的类或函数
from settings import Settings
from airship import AirShip
import game_functions as gf
#从Pygame的Sprite模块中导入Group群组类
from pygame.sprite import Group


#定义运行游戏函数
def run_game():
    #初始化Pygame模块
    pygame.init()
    #定义一个变量保存创建的 Settings 实例
    sb_settings = Settings()
    #定义一个变量保存显示窗口大小
    screen = pygame.display.set_mode((sb_settings.screen_width,
        sb_settings.screen_height))
    #定义窗口标题
    pygame.display.set_caption("打蜜蜂 V0.1")
    #创建一艘飞船
    airship = AirShip(screen)
    #创建一个用于存储子弹的群组
    bullets = Group()

    #开始游戏主循环
    while True:
        #调用检测键盘、鼠标事件的函数
        gf.check_events(sb_settings, screen, airship, bullets)
        #更新飞船坐标
        airship.update()
        #更新子弹
        gf.update_bullets(bullets)

        #更新屏幕显示
        gf.update_screen(sb_settings, screen, airship, bullets)

#执行自定义函数，运行游戏
run_game()
