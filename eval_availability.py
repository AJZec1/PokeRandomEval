cool_early_pokemon = ['BULBASAUR', 'CHARMANDER', 'SQUIRTLE', 'PIDGEY', 'EKANS', 'PIKACHU', 'SANDSHREW', 'NIDORAN',
                      'VULPIX', 'ODDISH', 'VENONAT', 'DIGLETT', 'POLIWAG', 'ABRA', 'MACHOP', 'BELLSPROUT', 'GEODUDE',
                      'PONYTA', 'SLOWPOKE', 'MAGNEMITE', 'SEEL', 'SHELLDER', 'GASTLY', 'DROWZEE', 'KRABBY', 'VOLTORB',
                      'EXEGGCUTE', 'CUBONE', 'RHYHORN', 'HORSEA', 'STARYU', 'OMANYTE', 'KABUTO', 'AERODACTYL',
                      'DRATINI', 'CHIKORITA', 'CYNDAQUIL', 'TOTODILE', 'HOOTHOOT', 'NATU', 'MAREEP', 'WOOPER',
                      'HOUNDOUR', 'LARVITAR', 'TREECKO', 'TORCHIC', 'MUDKIP', 'POOCHYENA', 'LOTAD', 'SEEDOT',
                      'TAILLOW', 'WINGULL', 'RALTS', 'SHROOMISH', 'MAKUHITA', 'MEDITITE', 'ELECTRIKE', 'CARVANHA',
                      'NUMEL', 'TRAPINCH', 'SWABLU', 'BARBOACH', 'BALTOY', 'LILEEP', 'ANORITH', 'SHUPPET', 'DUSKULL',
                      'TROPIUS', 'SPHEAL', 'BAGON', 'BELDUM']
hoenn_locs = ['ROUTE 101 ', 'ROUTE 102 ', 'ROUTE 103 ', 'ROUTE 104 ', 'PETALBURG WOODS ', 'ROUTE 116 ', 'GRANITE CAVE ',
              'ROUTE 110 ', 'ROUTE 117 ']
kanto_locs = ['ROUTE 1 ', 'ROUTE 22 ', 'ROUTE 2 ', 'VIRIDIAN FOREST ', 'ROUTE 3 ', 'MT. MOON ', 'ROUTE 4 ', 'ROUTE 24 ',
              'ROUTE 25 ', 'ROUTE 5 ', 'ROUTE 6 ', 'ROUTE 11 ', 'DIGLETT\'S CAVE ']


def read_wild_pkmn(wild_pkmn_str):
    all_wild_pkmn = {}
    wild_pkmn_data = wild_pkmn_str.split('\n')
    for line in wild_pkmn_data:
        if 'Wild Pokemon' in line or line == '':
            continue
        data = line.split(' - ')
        name_data = data[1].split(' ')
        loc_name = ''
        for token in name_data[:-2]:
            loc_name += token + ' '
        if 'Grass/Cave' not in name_data[-2]:
            continue
        wild_pkmn = data[2].split(', ')
        wild_set = []
        for pkmn in wild_pkmn:
            tokens = pkmn.split(' ')
            pkmn_data = (tokens[0], tokens[1].replace(' ', ''))
            wild_set += [pkmn_data]
        all_wild_pkmn[loc_name] = wild_set
    return all_wild_pkmn


def evaluate_availability(wild_pkmn_str, region='HOENN'):
    all_wild_pkmn = read_wild_pkmn(wild_pkmn_str)
    summary = ''
    if region is 'HOENN':
        areas = hoenn_locs
    else:
        areas = kanto_locs
    unique_pkmn = []
    for area in areas:
        for loc in all_wild_pkmn:
            if area in loc:
                summary += loc + ': '
                current_pkmn = []
                for pkmn in all_wild_pkmn[loc]:
                    if pkmn[0] in cool_early_pokemon and pkmn[0] not in current_pkmn:
                        summary += pkmn[0] + ' ' + pkmn[1] + ', '
                        current_pkmn += [pkmn[0]]
                        if pkmn[0] not in unique_pkmn:
                            unique_pkmn += [pkmn[0]]
                summary = summary[:-2] + '\n'
    summary += 'Num good pokemon: ' + str(len(unique_pkmn))
    return summary
