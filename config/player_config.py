def config_players():
    empty_players = {
                'White': {
                    'name': 'Anon',
                    'ELO': None
                },
                'Black': {
                    'name': 'Anon',
                    'ELO': None
                }
            }
    new_players = empty_players
    print('=========\nNew game:\n=========\n')
    print('Enter configuration for the players.')
    print('White:\n------\n')
    print("Enter the player's name:\n")
    name = input()
    if name != '':
        new_players['White']['name'] = name
    invalid_elo = True
    elo = None
    while invalid_elo:
        elo = input_elo()
        if elo or elo == '':
            invalid_elo = False
    if elo == '':
        new_players['White']['ELO'] = None
    else:
        new_players['White']['ELO'] = elo

    print('Black:\n------\n')
    print("Enter the player's name:\n")
    name = input()
    if name != '':
        new_players['Black']['name'] = name
    invalid_elo = True
    while invalid_elo:
        elo = input_elo()
        if elo or elo == '':
            invalid_elo = False
    if elo == '':
        new_players['Black']['ELO'] = None
    else:
        new_players['Black']['ELO'] = elo

    return new_players


def input_elo():
    print("Enter the player's ELO:\n")
    elo = input()
    if elo == '':
        num_elo = None
        return ''
    else:
        try:
            num_elo = int(elo)
        except ValueError:
            return False
        return num_elo


if __name__ == '__main__':

    players = config_players()
    assert 1 == 1
