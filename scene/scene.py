from abc import abstractmethod
import sys

import pygame


class Scene:
    def __init__(self,scene_manager,screen):
        self.scene_manager = scene_manager
        self.screen = screen

    #シーン開始時に実行される
    @abstractmethod
    def start(self):
        raise NotImplementedError
    
    #シーンの更新処理
    @abstractmethod
    def update(self):
        raise NotImplementedError
    
    @abstractmethod
    def draw(self):
        raise NotImplementedError

    #終了ボタンが押されたか確認
    def check_quit(self,event):
        if event.type == pygame.QUIT:
            self.quit_game()

    #ゲームを終了させる
    def quit_game(self):
        pygame.quit()
        sys.exit()