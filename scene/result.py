import pygame
from config import SCREEN_SIZE
from scene.scene import Scene
from system.highscore import HighScore


class Result(Scene):
    background_color = (0, 0, 0)
    def __init__(self,scene_manager,screen):
        super().__init__(scene_manager,screen)

        self.scene_manager = scene_manager

        self.score = scene_manager.get_score()

        self.font = pygame.font.SysFont("MS Gothic", 55)

        self.gameover = pygame.image.load("img/gameover.png").convert_alpha()
        self.gameover_rect = self.gameover.get_rect()
        self.gameover_rect.center = (SCREEN_SIZE[0]/2, 200)

        self.score_text = self.font.render(f"SCORE:{self.score}", True, (255, 255, 255))

        self.push = pygame.image.load("img/push.png").convert_alpha()
        self.push_rect = self.push.get_rect()
        self.push_rect.center = (SCREEN_SIZE[0]/2, 500)

        self.highscore_text = HighScore(self.screen,120,600,50)

        self.gameover_player = pygame.image.load("img/player_gameover.png").convert_alpha()
        # 倍率を指定してリサイズ
        self.player_image = pygame.transform.rotozoom(self.gameover_player, 0, 0.5)
        self.gameover_player_rect = self.player_image.get_rect()
        self.gameover_player_rect.center = (SCREEN_SIZE[0]/2, 900)



        self.all_sprites = pygame.sprite.Group()


    def start(self):
        self.score = self.scene_manager.get_score()

        self.score_text = self.font.render(f"SCORE:{self.scene_manager.get_score()}", True, (255, 255, 255))

        if(self.score > self.highscore_text.get_highscore() ):
            self.highscore_text.set_highscore(self.score)
        
        self.highscore_text.start()

    def draw(self):
        pass

    def update(self):
        # 背景色で画面を塗りつぶす
        self.screen.fill(self.background_color)

        self.screen.blit(self.gameover, self.gameover_rect)

        self.screen.blit(self.score_text, [120,350])

        self.highscore_text.update()

        self.screen.blit(self.player_image, self.gameover_player_rect)
        self.screen.blit(self.push, self.push_rect)

        for event in pygame.event.get():
            self.check_quit(event)
            if event.type == pygame.KEYDOWN:
                #エンターキーでゲーム開始
                if event.key == pygame.K_RETURN:
                    self.scene_manager.change_scene("title")