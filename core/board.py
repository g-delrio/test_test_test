from pieces.piece import Piece


class Board:

    def __init__(self):
        i = 1
        self.board = dict()

        while i < 9:
            j = 1
            while j < 9:
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                    colour = 'Black'
                else:
                    colour = 'White'
                square = {'file': chr(96 + i),
                          'rank': j,
                          'colour': colour,
                          'piece': None
                          }
                self.board.update({'{0}{1}'.format(square['file'], square['rank']): square})
                j += 1
            i += 1
        self.position = dict()

    def setup(self):
        """
        Sets the board in its initial position.
        :return:
        """
        # Set up white pieces
        num_file = 1
        num_rank = 1
        while num_file < 9:
            file = chr(96 + num_file)
            if file == 'a' or file == 'h':
                self.board['{0}{1}'.format(file, num_rank)]['piece'] = Piece(colour='White',
                                                                             piece_type='rook',
                                                                             file=file,
                                                                             rank=num_rank)
            elif file == 'b' or file == 'g':
                self.board['{0}{1}'.format(file, num_rank)]['piece'] = Piece(colour='White',
                                                                             piece_type='knight',
                                                                             file=file,
                                                                             rank=num_rank)
            elif file == 'c' or file == 'f':
                self.board['{0}{1}'.format(file, num_rank)]['piece'] = Piece(colour='White',
                                                                             piece_type='bishop',
                                                                             file=file,
                                                                             rank=num_rank)
            elif file == 'd':
                self.board['{0}{1}'.format(file, num_rank)]['piece'] = Piece(colour='White',
                                                                             piece_type='queen',
                                                                             file=file,
                                                                             rank=num_rank)
            elif file == 'e':
                self.board['{0}{1}'.format(file, num_rank)]['piece'] = Piece(colour='White',
                                                                             piece_type='king',
                                                                             file=file,
                                                                             rank=num_rank)
            num_file += 1

        num_rank = 2
        num_file = 1
        while num_file < 9:
            file = chr(96 + num_file)
            self.board['{0}{1}'.format(file, num_rank)]['piece'] = Piece(colour='White',
                                                                         piece_type='pawn',
                                                                         file=file,
                                                                         rank=num_rank)
            num_file += 1

        # Set up black pieces
        num_rank = 7
        num_file = 1
        while num_file < 9:
            file = chr(96 + num_file)
            self.board['{0}{1}'.format(file, num_rank)]['piece'] = Piece(colour='Black',
                                                                         piece_type='pawn',
                                                                         file=file,
                                                                         rank=num_rank)
            num_file += 1

        num_file = 1
        num_rank = 8
        while num_file < 9:
            file = chr(96 + num_file)
            if file == 'a' or file == 'h':
                self.board['{0}{1}'.format(file, num_rank)]['piece'] = Piece(colour='Black',
                                                                             piece_type='rook',
                                                                             file=file,
                                                                             rank=num_rank)
            elif file == 'b' or file == 'g':
                self.board['{0}{1}'.format(file, num_rank)]['piece'] = Piece(colour='Black',
                                                                             piece_type='knight',
                                                                             file=file,
                                                                             rank=num_rank)
            elif file == 'c' or file == 'f':
                self.board['{0}{1}'.format(file, num_rank)]['piece'] = Piece(colour='Black',
                                                                             piece_type='bishop',
                                                                             file=file,
                                                                             rank=num_rank)
            elif file == 'd':
                self.board['{0}{1}'.format(file, num_rank)]['piece'] = Piece(colour='Black',
                                                                             piece_type='queen',
                                                                             file=file,
                                                                             rank=num_rank)
            elif file == 'e':
                self.board['{0}{1}'.format(file, num_rank)]['piece'] = Piece(colour='Black',
                                                                             piece_type='king',
                                                                             file=file,
                                                                             rank=num_rank)
            num_file += 1

        self.update()

    def update(self, old_position, new_position):
        """
        Updates the position on the board after a move is made
        :param old_position:
        :param new_position:
        :return:
        """

    def assess_position(self, position):
        """
        Evaluates if the position is OK, check, or mate
        :param position:
        :return:
        """


if __name__ == '__main__':
    board = Board()
