import random 

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self):
        self.type = 0
        self.fly = 0 #indicador de vuelo
        super().__init__(BIRD, self.type)
        self.rect.y = random.randint(100, 310)


    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed #se actualiza restando la velocidad del juego
        self.obs_to_draw = BIRD[0] if self.fly < 10 else BIRD[1] #alas
        self.fly += 1
        if self.fly >= 20:
            self.fly = 0
        
        if self.rect.x < -self.rect.width:
            obstacles.pop() #se elimina de la lista de obstaculos 