import pygame
from dino_runner.components.obstacles.birds import Birds
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.largecactus import LargeCactus
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:
    def __init__(self) -> None:
        self.obstacle = []
        
    def update(self, game):
        if len(self.obstacle) == 0:
            self.obstacle.append(Cactus(SMALL_CACTUS))
        for obstacle in self.obstacle:
            obstacle.update(game.game_speed, self.obstacle)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break
            
        if len(self.obstacle) == 0:
            self.obstacle.append(LargeCactus(LARGE_CACTUS))
        for obstacle in self.obstacle:
            obstacle.update(game.game_speed, self.obstacle)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break
            
        # if len(self.obstacle) == 0:
        #     self.obstacle.append(Birds())
        # for obstacle in self.obstacle:
        #     obstacle.update(game.game_speed, self.obstacle)
        #     if game.player.dino_rect.colliderect(obstacle.rect):
        #         pygame.time.delay(1000)
        #         game.playing = False
        #         break
    
    def draw(self, screen):
        for obstacle in self.obstacle:
            obstacle.draw(screen)