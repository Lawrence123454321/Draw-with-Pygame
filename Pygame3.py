import pygame

# 初始化Pygame
pygame.init()

# 设置窗口大小
size = (700, 500)
screen = pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption("My Game")

# 创建精灵
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

# 添加精灵到组中
my_group = pygame.sprite.Group()
my_sprite = MySprite()
my_group.add(my_sprite)

# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环
done = False
gravity = 1
stop = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_sprite.rect.x -= 10
            elif event.key == pygame.K_RIGHT:
                my_sprite.rect.x += 10
            elif event.key == pygame.K_UP:
                my_sprite.rect.y -= 10
            elif event.key == pygame.K_DOWN:
                my_sprite.rect.y += 10
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("鼠标点击" + str(my_sprite.rect.y))
    # 处理事件

    # 绘制背景
    screen.fill((255, 255, 255))

    # 绘制精灵
    my_group.draw(screen)

    # 更新窗口
    pygame.display.update()

    # 控制游戏帧率
    clock.tick(60)

# 退出Pygame
pygame.quit()