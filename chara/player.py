import pygame
import config  # 画面サイズを使う


class Player(pygame.sprite.Sprite):
    # ゲームに追加されたときに動く関数
    def __init__(self, screen, x, y, image_path, scale):
        super().__init__()

        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 10  # 移動スピード

        # 画像を読み込む
        original_image = pygame.image.load(image_path).convert_alpha()

        # 倍率を指定してリサイズ
        self.image = pygame.transform.rotozoom(original_image, 0, scale)

        # 描画位置の設定
        self.rect = self.image.get_rect(center=(self.x, self.y))

    # 毎フレーム呼び出される関数
    def update(self):
        keys = pygame.key.get_pressed()

        # 左に移動
        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        # 右に移動
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        # 画面外に出ないように制限（SCREEN_SIZE の width を使用）
        screen_width = config.SCREEN_SIZE[0]

        if self.x < 0:
            self.x = 0
        if self.x > screen_width:
            self.x = screen_width

        # 画像の描画位置を更新
        self.rect.center = (self.x, self.y)

    # プレイヤーの入力を調べる関数
    def check_event(self, event):
        pass
