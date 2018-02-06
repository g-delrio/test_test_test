import pygame
import sys
from main_exec import MainExec
from config.player_config import config_players

white = [255, 255, 255]
black = [0, 0, 0]
dark = [168, 134, 48]
light = [234, 209, 145]


class UI:

    def __init__(self, total_size):
        self.size = total_size
        self.square_size = int(total_size) / 9
        self.game_over = False
        pygame.init()

        # Iniciamos clase principal
        new_game_players = config_players()
        new_game = MainExec(players=new_game_players)
        # main loop
        while not self.game_over:
            self.screen = pygame.display.set_mode((self.size, self.size))
            pygame.display.set_caption("Test title")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.game_over = self.play(new_game)

    def udpate_ui(self, position):
        self.screen.fill(black)
        pos = position.copy()

        for coor, square in pos.items():
            if square['colour'] == 'white':
                colour = light
            else:
                colour = dark
            square['surface'] = pygame.Surface((self.square_size, self.square_size))
            square['surface'].fill(colour)
            self.screen.blit(square['surface'],
                             (self.square_size * (ord(square['file'])-96),
                              self.square_size*square['rank']))

        pygame.display.update()
        return

    def play(self, game):
        """
        Main function of the game. While the game is not over, the player whose turn it is makes a ply.
        When the game is over, it exits.
        :return: 0
        """
        last_turn = None
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Update UI with current position

            self.udpate_ui(game.board.board)
            # Set whose turn it is
            if last_turn == 'Black' or last_turn is None:
                turn = 'White'
            else:
                turn = 'Black'
            game.ply(turn=turn)

        return True



if __name__ == '__main__':
    test = UI(400)
