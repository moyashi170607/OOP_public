import pygame
SCREEN_SIZE = (576, 1024)

class Enemy(pygame.sprite.Sprite):
    # 敵の初期設定
    def __init__(self, x,y, image_path,scale,speed = 3):
        super().__init__() # 初期化メソッド

        self.x = x
        self.y = y

        # 敵画像を読み込む
        original_image = pygame.image.load(image_path).convert_alpha()
        # 倍率を指定してリサイズ
        self.image = pygame.transform.rotozoom(original_image, 0, scale)

        # サーフェスの短形を取得
        self.rect = self.image.get_rect(center=(self.x, self.y))
        # # 短形の左上を引数として渡されたx,yに設定
        # self.rect.topleft = (x, y) # 横:x 縦:y
        # 敵の移動速度
        self.speed = speed

    # 位置を更新
    def update(self):
         # 現在の速度で下方向へ移動する
        self.rect.y += self.speed

        # 画面外に出たら削除
        if self.rect.top > SCREEN_SIZE[1]:
            self.kill()

        # # 画面の端に達すると折り返す
        # if self.rect.right >= SCREEN_SIZE[0] or self.rect.left <= 0:
        #     # 移動方向を反転
        #     self.speed = -self.speed
        #     # 40ピクセル下に移動    
        #     self.rect.y += 40

"""
class Enemy(pygame.sprite.Sprite):
    #ゲームに追加されたときに動く関数
    def __init__(self,screen, x, y, image_path, scale):
        super().__init__()

        self.screen = screen

        self.x = x
        self.y = y
        
        #画像を読み込む
        original_image = pygame.image.load(image_path).convert_alpha()
        # 倍率を指定してリサイズ
        self.image = pygame.transform.rotozoom(original_image, 0, scale)
        
        #描画位置の設定
        self.rect = self.image.get_rect(center=(self.x, self.y))


    #毎フレーム呼び出される関数
    #center=(x, y)の値を変えるとキャラの位置が変わる
    def update(self):
        #画像の描画
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.screen.blit(self.image, self.rect)
"""
