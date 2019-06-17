good_starters = ['BULBASAUR', 'CHARMANDER', 'SQUIRTLE', 'PIDGEY', 'NIDORAN♀', 'NIDORAN♂', 'ZUBAT', 'ODDISH', 'POLIWAG',
                 'ABRA', 'MACHOP', 'BELLSPROUT', 'GEODUDE', 'GASTLY', 'HORSEA', 'DRATINI', 'CHIKORITA', 'CYNDAQUIL',
                 'TOTODILE', 'MAREEP', 'HOPPIP', 'LARVITAR', 'TREECKO', 'TORCHIC', 'MUDKIP', 'LOTAD', 'SEEDOT',
                 'RALTS', 'SLAKOTH', 'WHISMUR', 'ARON', 'TRAPINCH', 'SPHEAL', 'BAGON', 'BELDUM']


def evaluate_starters(starter_str):
    starter_data = starter_str.split('\n')
    summary = ''
    n_good_ones = 0
    for line in starter_data:
        if 'Starters' in line:
            continue
        tokens = line.split(' ')
        full_name = ''
        for token in tokens[4:]:
            full_name += token
        if full_name in good_starters:
            n_good_ones += 1
        summary += full_name + ', '
    return summary[:-2] + '\nGood Starters: ' + str(n_good_ones)

