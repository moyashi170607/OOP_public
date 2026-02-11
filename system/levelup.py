import pygame

import config


class LevelUP(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, image_path, scale,speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.scale = scale

        self.active = False

        # 画像を読み込む
        original_image = pygame.image.load(image_path).convert_alpha()
        # 倍率を指定してリサイズ
        self.image = pygame.transform.rotozoom(original_image, 0, scale)

        # サーフェスの短形を取得
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        # # 短形の左上を引数として渡されたx,yに設定
        # self.rect.topleft = (x, y) # 横:x 縦:y
        # 敵の移動速度
        self.speed = speed

    def update(self):
        if(self.active):
            self.x -= self.speed
            self.rect.x = self.x
            self.screen.blit(self.image, self.rect)

        if(self.x < -500):
            self.active = False
            self.x = config.SCREEN_SIZE[0]
            self.rect = self.image.get_rect(topleft=(self.x, self.y))
            self.screen.blit(self.image, self.rect)
    
    def activate(self):
        self.active = True