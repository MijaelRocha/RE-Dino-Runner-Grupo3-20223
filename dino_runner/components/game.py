import pygame
from dino_runner.components.dino import Dino
from dino_runner.components.obstacles.obstaclemanager import ObstacleManager
from dino_runner.components import text_utils
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, GAME_OVER, GAME_START, GAME_DEAD
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 0
        self.y_pos_cloud = 180
        self.points = 0
        self.running = True
        self.death_count = 0
        self.player = Dino()
        self.obstacle_manager = ObstacleManager()
        self.player_heart_manager = PlayerHeartManager()
        self.power_up_manager = PowerUpManager()

    def run(self):
        self.run = 0
        self.create_components()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def create_components(self):
        self.power_up_manager.reset_power_ups(self.points)
        # self.obstacle_manager.reset_obstacles()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        self.obstacle_manager.update(self)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_cloud()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.player_heart_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score()
        self.player.check_lives()

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
    def draw_cloud(self): #NUBE
        image_height = CLOUD.get_height()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        self.screen.blit(CLOUD, (image_height + self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_height:
            self.screen.blit(CLOUD, (image_height + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = 1000
        self.x_pos_cloud -= self.game_speed
    
    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        text, text_rect = text_utils.get_score_element(self.points)
        self.player.check_invincibility(self.screen)
        self.screen.blit(text, text_rect)
        
    
    def show_menu(self, death_count):
        self.running = True
        
        self.screen.fill((255, 255, 255))
        self.print_menu_elements(self.death_count)
        pygame.display.update()
        self.handle_key_events_on_menu()

    def print_menu_elements(self, death_count = 0):
        half_screen_height = SCREEN_HEIGHT // 2
        
        if death_count == 0:
            text, text_rect = text_utils.get_centered_message('Press any Key to start')
            self.screen.blit(text, text_rect)
            
            text_rect_dino = text_utils.get_dino_elemen()
            self.screen.blit(GAME_START  , text_rect_dino)
            
        elif death_count > 0:
            text, text_rect = text_utils.get_centered_message("Press any Key to Restart")
            score, score_rect = text_utils.get_centered_message("Your score was: " + str(self.points), height = half_screen_height + 50)

            text_death , text_death_rect = text_utils.get_number_dead(self.death_count )
            self.screen.blit(text_death, text_death_rect)

            text_game = text_utils.get_game_over()
            self.screen.blit(GAME_OVER  , text_game)

            text_rect_dino = text_utils.get_dino_elemen()
            self.screen.blit(GAME_DEAD  , text_rect_dino)
            
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.points = 0
                self.run()