import pygame
import config

class ScoreCounter:
    def __init__(self,screen,x,y,font_size):
        self.screen = screen
        
        #スコアを保存する変数
        self.score = 0
        
        self.x = x
        self.y = y
        self.size = font_size
        
        #フォントを指定
        self.font = pygame.font.SysFont("MS Gothic", font_size)
        
        self.surface = self.font.render(f"SCORE:{self.score}", True, (255,255,255))
        self.rect = self.surface.get_rect(topleft=(self.x, self.y))
        
        self.count = 0
    
    def reset(self):
        self.count = 0
        self.score = 0

    def update(self):
        self.count = self.count + 1
        if self.count == config.FPS:
            self.score += 5
            self.count = 0
            
        self.surface = self.font.render(f"SCORE:{self.score}", True, (255,255,255))
        self.screen.blit(self.surface, self.rect)
