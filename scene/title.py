from config import SCREEN_SIZE,isSoundEnable
from scene.scene import Scene
import sys
import pygame
from pygame.locals import *

PLAY_SE_PATH ="./sound/se/play.ogg"

class Title(Scene):
    #背景の色
    background_color = (0, 0, 0)
    def __init__(self,scene_manager,screen):
        super().__init__(scene_manager,screen)

        self.title= pygame.image.load("img/title3.png").convert_alpha()
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (SCREEN_SIZE[0]/2, 200)


        self.push = pygame.image.load("img/push.png").convert_alpha()
        self.push_rect = self.push.get_rect()
        self.push_rect.center = (SCREEN_SIZE[0]/2, 500)

        self.Lpush = pygame.image.load("img/push_L.png").convert_alpha()
        self.Lpush_rect = self.Lpush.get_rect()
        self.Lpush_rect.center = (SCREEN_SIZE[0]/2, 600)

        self.all_sprites = pygame.sprite.Group()
        

        self.player = pygame.image.load("img/player/player.png").convert_alpha()
        self.player_rect = self.player.get_rect()
        self.player_rect.center = (SCREEN_SIZE[0]/2, 800)

        if(isSoundEnable):
            self.start_se = pygame.mixer.Sound(PLAY_SE_PATH)
            self.start_se.set_volume(1)


    def start(self):
        pass

    def draw(self):
        pass

    def update(self):
        # 背景色で画面を塗りつぶす
        self.screen.fill(self.background_color)

        self.screen.blit(self.title,self.title_rect)
        self.screen.blit(self.push, self.push_rect)
        self.screen.blit(self.Lpush,self.Lpush_rect)
        self.screen.blit(self.player, self.player_rect)

        for event in pygame.event.get():
            self.check_quit(event)
            if event.type == KEYDOWN:
                #エンターキーでゲーム開始
                if event.key == K_RETURN:
                    self.scene_manager.change_scene("main_game")
                    if(isSoundEnable):
                        self.start_se.play()
                elif event.key == K_l:
                    self.scene_manager.change_scene("license")
