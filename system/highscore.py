import pygame

import config

FILE_PATH = "./highscore_data/highscore.txt"

class HighScore():
    def __init__(self,screen,x,y,font_size):
        self.screen = screen
        self.x = x
        self.y = y
        self.size = font_size

        self.highscore = self.get_highscore()

        #フォントを指定
        self.font = pygame.font.SysFont("MS Gothic", font_size)
        
        self.surface = self.font.render(f"SCORE:{self.highscore}", True, (255,255,255))
        self.rect = self.surface.get_rect(topleft=(self.x, self.y))
        
        self.count = 0

    def start(self):
        self.highscore = self.get_highscore()

    def get_highscore(self):
        try:
            with open(FILE_PATH) as file:
                for line in file.read().splitlines():
                    if (line.isdecimal()):
                        return int(line)
            
            return 0

        except FileNotFoundError:
            f = open(FILE_PATH, 'w')
            f.close()
            return 0
        
        except :
            return 0


    def set_highscore(self,score):
        try:
            f = open(FILE_PATH, 'w')
            f.write(str(score) + "\n")
            f.close()

            return True


        except:
            return False

    def update(self):
        self.surface = self.font.render(f"HIGH SCORE:{self.highscore}", True, (255,255,255))
        self.screen.blit(self.surface, self.rect)


