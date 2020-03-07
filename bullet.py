#导入模块
import pygame
#导入精灵类
from pygame.sprite import Sprite

class Bullet(Sprite):
    """飞船发射的子弹类"""
    def __init__(self, sb_settings, screen, airship):
        """在飞船所在位置创建子弹对象"""
        #继承 Sprite 精灵类
        super().__init__()
        self.screen = screen

        #先在（0,0）处创建子弹矩形，再设置其正确位置
        self.rect = pygame.Rect(0, 0, sb_settings.bullet_width,
            sb_settings.bullet_height)
        self.rect.centerx = airship.rect.centerx
        self.rect.top = airship.rect.top

        #子弹位置用 y 坐标表示，强制为浮点数类型
        self.y = float(self.rect.y)

        #获取参数设置里的颜色及速度设置值
        self.color = sb_settings.bullet_color
        self.speed = sb_settings.bullet_speed

    def update(self):
        """向上移动子弹"""
        #更新子弹位置值
        self.y -= self.speed
        
        #更新子弹rect的位置
        self.rect.y = self.y
        
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        