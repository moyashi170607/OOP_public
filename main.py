# -*- coding:utf-8 -*-
import sys
import pygame
from pygame.locals import *
from pygame.locals import QUIT

from config import FPS, SCREEN_SIZE
from scene.license import LicenseViwer
from scene.main_game import MainGame
from scene.result import Result
from scene.title import Title



## シーン管理
class SceneManager:

    def __init__(self,sceren):
        self.score = 0

        self.scene_list = {
            "title": Title(self,sceren),
            "main_game": MainGame(self,sceren),
            "result": Result(self,sceren),
            "license":LicenseViwer(self,sceren)
        }

        self.current_scene = self.scene_list["title"]


    def change_scene(self,key):
        self.current_scene = self.scene_list[key]
        self.current_scene.start()

    def update(self):
        self.current_scene.update()
    
    def draw(self):
        self.current_scene.draw()

    def set_score(self,score):
        self.score = score

    def get_score(self):
        return self.score

##ゲームが実行中か
running = False


#起動時に実行される関数
def main():
    # Pygameの初期化
    pygame.init()

    #ミキサーの初期化
    pygame.mixer.init()

    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("バグヨケール")

    #シーンを管理
    scene_manager = SceneManager(screen)

    clock = pygame.time.Clock()
    running = True

    scene_manager.change_scene("title")

    while running:
        # 画面を黒色(#000000)に塗りつぶし
        screen.fill((0, 0, 0))

        scene_manager.update()
        scene_manager.draw()

        # 画面を更新
        pygame.display.flip()
        clock.tick(FPS)




if __name__ == "__main__":
    main()