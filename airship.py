import pygame

class AirShip():
    def __init__(self,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        #加载飞船图像并获取其外形矩形
        self.image = pygame.image.load('images/airship.png').convert_alpha()
        self.rect = self.image.get_rect()
        #获取屏幕矩形
        self.screen_rect = screen.get_rect()

        #将飞船放在屏幕底部中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #设置飞船可移动（左移、右移）标志，默认为不可移动
        self.move_right = False
        self.move_left = False

    def update(self):
        #根据飞船可移动标记更新飞船坐标
        #若飞船右移标记为真，且飞船矩形右侧未超出屏幕
        if self.move_right == True and self.rect.right < 1200:
            #设置飞船矩形中心点 x 坐标增加 1
            self.rect.centerx += 1
        #若飞船左移标记为真，且飞船矩形左侧未超出屏幕
        elif self.move_left == True and self.rect.left > 0:
            #设置飞船矩形中心点 x 坐标减少 1
            self.rect.centerx -= 1
        
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
