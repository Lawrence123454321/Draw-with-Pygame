import pygame

pygame.init()


size = (700, 500)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("Game")


class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50


my_group = pygame.sprite.Group()
my_sprite = MySprite()
my_group.add(my_sprite)


clock = pygame.time.Clock()


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
                print("Press" + str(my_sprite.rect.y))

    screen.fill((255, 255, 255))


    my_group.draw(screen)


    pygame.display.update()

    # 控制游戏帧率
    clock.tick(60)

# 退出Pygame
pygame.quit()
