from config.player_config import config_players
from core.board import Board


class MainExec:

    def __init__(self, players=None):

        if players is None:
            players = {
                'White': {
                    'name': 'Anon',
                    'ELO': None
                },
                'Black': {
                    'name': 'Anon',
                    'ELO': None
                }
            }
        else:
            self.players = players
        self.board = Board()

        self.board.setup()

    def ply(self, turn):
        """
        Processes a move of a player. After the move is made, it assesses if its legal (when in check).
        If the move is legal, it updates the board position. The function does not return until a valid move is made.
        Resigning counts as a valid move.
        :param turn:
        :return:
        """
        legal_move = False
        while not legal_move:
            legal_move = self.move(turn=turn)
        self.board.update()

    def move(self, turn):
        old_position = self.board.board

        player_move = input()
        # Assess the move. Get the square of origin and the piece associated.


if __name__ == '__main__':
    new_game_players = config_players()
    new_game = MainExec(players=new_game_players)
    new_game_exec = new_game.play()
