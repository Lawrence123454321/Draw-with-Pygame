import pygame
from random import randint
# 初始化程序
pygame.init()
screen = pygame.display.set_mode((450,400))
pygame.display.set_caption("Draw")
# 更新显示
pygame.display.flip()
while True:
    #等待事件发生
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        exit("成功退出")
    if event.type == pygame.MOUSEBUTTONDOWN:
        # pos 获取鼠标当前位置
        print('    ', event.pos)
        mx, my = event.pos
        # 随机生成 RGB 颜色值
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        pygame.draw.circle(screen, (r, g, b,), (mx, my), 10)
        # 处理完，更新显示
        pygame.display.update()
    if event.type == pygame.MOUSEBUTTONUP:
        pass
    if event.type == pygame.MOUSEMOTION:
        pass
    