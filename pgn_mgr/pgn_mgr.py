import re
# from . import PGNCodes


class PGNCodes:
    OK = 0
    NO_OK = 1


class PGN:
    def __init__(self, information=None, file=None):

        self.information = dict()
        if information is None:
            information = dict()
        self.params = ['Event', 'Site', 'Date', 'Round', 'White', 'Black', 'Result', 'Moves']
        if file is not None:
            try:
                with open(file, 'r') as f:
                    read_data = f.read()
                f.close()
            except TypeError or ValueError:
                print('Could not open PGN. Wrong format or directory')
            information = self.parse_pgn(pgn_string=read_data)

        if information.get('Event'):
            self.information['Event'] = information.get('Event')
        else:
            self.information['Event'] = None

        if information.get('Site'):
            self.information['Site'] = information.get('Site')
        else:
            self.information['Site'] = None

        if information.get('Date'):
            self.information['Date'] = information.get('Date')
        else:
            self.information['Date'] = None

        if information.get('Round'):
            self.information['Round'] = information.get('Round')
        else:
            self.information['Round'] = None

        if information.get('White'):
            self.information['White'] = information.get('White')
        else:
            self.information['White'] = None

        if information.get('Black'):
            self.information['Black'] = information.get('Black')
        else:
            self.information['Black'] = None

        if information.get('Result'):
            self.information['Result'] = information.get('Result')
        else:
            self.information['Result'] = None

        self.information = information

    def parse_pgn(self, pgn_string):
        """
        Parses a string read from a PGN text file to extract information
        :param pgn_string:
        :return:
        """
        i = 0
        while i <= len(pgn_string):
            char = pgn_string[i]
            if char == '[':
                j = i+1
                while j < len(pgn_string):
                    nxt_char = pgn_string[j]
                    if nxt_char == ']':
                        info = ''.join(pgn_string[i + 1:j - 1])
                        pro = self.process_info(info=info)
                        if pro.get('code', PGNCodes.NO_OK) != PGNCodes.OK:
                            return {'code': PGNCodes.NO_OK}
                        j += 1
                    else:
                        j += 1
            i += 1
        return {}

    def process_info(self, info):
        split_info = info.split(' ', 1)
        if split_info[0] not in self.params:
            print('Error parsing PGN. ')
            return {'code': PGNCodes.NO_OK}
        else:
            value = split_info[1].split('"')[1]
            print(split_info[0]+':')
            print(split_info[1])
            self.information.update({split_info[0]: value})
            return {'code': PGNCodes.OK, 'parameter': split_info[0], 'value': split_info[1]}


if __name__ == '__main__':
    pgn = PGN()
    pgn.parse_pgn(pgn_string='[Event "London Chess Classic"]')