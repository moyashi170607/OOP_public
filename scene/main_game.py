import sys
import pygame
from chara.enemy import Enemy
from chara.player import Player
from config import SCREEN_SIZE,isSoundEnable
import config
from scene.scene import Scene
from system.levelup import LevelUP
from system.score import ScoreCounter

import random

ENEMY_COOLTIME = 1.3 * config.FPS

BGM_PATH = "./sound/bgm/iwashiro_kumitechan.ogg"
LEVELUP_SE_PATH = "./sound/se/warp.ogg"
GAMEOVER_SE_PATH = "./sound/se/doon.ogg"


class MainGame(Scene):
    
    def __init__(self,scene_managaer,screen):
        super().__init__(scene_managaer,screen)
        #背景の色
        self.background_color = (0, 0, 0)

        self.sprites = pygame.sprite.Group()
        #敵を管理するためのグループ
        self.enemy_group = pygame.sprite.Group()

        self.enemy_speed = 3
        self.level = 1
        

        if(isSoundEnable):
            self.levelup_se = pygame.mixer.Sound(LEVELUP_SE_PATH)
            self.levelup_se.set_volume(1)

            self.gameover_se = pygame.mixer.Sound(GAMEOVER_SE_PATH)
            self.gameover_se.set_volume(1)

    #シーン開始時に呼び出される
    def start(self):
        self.fps_counter = config.FPS
        self.enemy_speed = 3
        self.level = 1
        self.player = Player(self.screen,SCREEN_SIZE[0]/2,900,"./img/player/player.png",0.5)
        self.sprites.add(self.player)

        self.score_counter = ScoreCounter(self.screen,30,30,30)

        self.levelup_text = LevelUP(self.screen,config.SCREEN_SIZE[0],200,"./img/levelup.png",1,10)

        if(isSoundEnable):
            # BGMの読み込み（ファイル名を指定）
            pygame.mixer.music.load(BGM_PATH) 
            # 音量の設定（0.0〜1.0）
            pygame.mixer.music.set_volume(0.5)
            # BGMの再生（ループ再生）
            pygame.mixer.music.play(-1)

        self.score_counter.reset()





    def draw(self):
        pass
        #self.all_sprite.draw()

    #毎フレーム呼び出される
    def update(self):
        # 背景色で画面を塗りつぶす
        self.screen.fill(self.background_color)

        self.score_counter.update()

        self.sprites.update()
        self.enemy_group.update()

        self.levelup_text.update()

        self.sprites.draw(self.screen)
        self.enemy_group.draw(self.screen)


        # イベント処理
        for event in pygame.event.get():
            self.check_quit(event)
            self.player.check_event(event)
        
        # 衝突した敵のリストを取得する
        hits_sprites = pygame.sprite.spritecollide(self.player, self.enemy_group, False)

        #当たり判定の処理
        if hits_sprites:
            for sprite in self.enemy_group:
                sprite.kill()
            self.player.kill()
            pygame.mixer.music.stop()
            self.scene_manager.set_score(self.score_counter.score)
            self.scene_manager.change_scene("result")
            if(isSoundEnable):
                self.gameover_se.play()

        #敵の出現
        self.fps_counter += 1
        if self.fps_counter >= ENEMY_COOLTIME - (self.level-1)*10:
            self.fps_counter = 0
            self.spawn_enemy(random.randint(0,config.SCREEN_SIZE[0]),10,self.enemy_speed)

        #スコア50ごとに難易度アップ
        if(self.score_counter.score >= self.level*50):
            self.levelup()

    #指定した位置に敵を出現させる
    def spawn_enemy(self,x,y,speed):
        self.enemy_group.add(Enemy(x,y,"./img/enemy/enemy.png",0.4,speed))

    def levelup(self):
        self.level += 1
        self.enemy_speed += 1

        self.levelup_text.activate()
        self.levelup_se.play()
