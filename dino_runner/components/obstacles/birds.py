import pygame
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH

class Birds(Obstacle):
    def _init_(self):
        self.image = BIRD[0]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = SCREEN_WIDTH
        self.bird_rect.y = 210
        self.step_index = 0
        self.bird = False

    def update(self):
        if self.bird:
            self.at()
            
        if self.step_index >= 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, (self.bird_rect.x, self.bird_rect.y))
        
    def at(self):
        if self.step_index <= 5:
            self.image = BIRD[0]
        else:
            self.image = BIRD[1]

        self.bird_rect.x = 800
        self.bird_rect.y = 310
        self.step_index += 1
        self.bird = False