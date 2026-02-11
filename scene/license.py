import sys
import pygame
from chara.enemy import Enemy
from chara.player import Player
from config import SCREEN_SIZE
import config
from scene.scene import Scene
from system.levelup import LevelUP
from system.score import ScoreCounter

class LicenseViwer(Scene):
    def __init__(self, scene_manager, screen):
        super().__init__(scene_manager, screen)
        
        #背景の色
        self.background_color = (0, 0, 0)

        self.push = pygame.image.load("img/push.png").convert_alpha()
        self.push_rect = self.push.get_rect()
        self.push_rect.center = (SCREEN_SIZE[0]/2, 900)


    def start(self):
        self.license = pygame.image.load("./img/license.png").convert_alpha()
        self.license_rect = self.license.get_rect(topleft=(0, 0))

    def update(self):
        # 背景色で画面を塗りつぶす
        self.screen.fill(self.background_color)
        self.screen.blit(self.license, self.license_rect)

        self.screen.blit(self.push, self.push_rect)

        for event in pygame.event.get():
            self.check_quit(event)
            if event.type == pygame.KEYDOWN:
                #エンターキーでゲーム開始
                if event.key == pygame.K_RETURN:
                    self.scene_manager.change_scene("title")

    def draw(self):
        pass
