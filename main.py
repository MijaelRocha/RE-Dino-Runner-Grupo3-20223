from dino_runner.components.game import Game

if __name__ == "__main__":
    game = Game()

    while game.running :
        if not game.playing : #si el False llama al metodo
            game.show_menu(game.death_count) # muestra el menu cuando pierde todos sus corazones