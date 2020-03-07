#定义一个游戏参数设置类
class Settings():
    #类的描述
    """存储《打蜜蜂》游戏的所有设置的类"""

    #定义类的初始化方法，在创建实例时自动调用，注意是两个连续的下划线
    #缺省参数 self 指向实例自身
    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (250,250,250)

        #子弹设置
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        