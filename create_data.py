def read_file(fname):
    f = open(fname, 'r')
    cur_str = ''
    section_list = []
    for line in f.readlines():
        line_fix = line.replace('\n', '')
        if line_fix == '':
            section_list += [cur_str]
            cur_str = ''
        cur_str += line_fix + '\n'
    return section_list


def pokemon_stat_list(pokemon_str):
    pokemon_list = []
    data_list = pokemon_str.split('\n')
    for pokemon in data_list:
        if 'Base Stats' in pokemon or 'NUM|NAME' in pokemon or pokemon is '':
            continue
        poke_data = pokemon.split('|')
        num = int(poke_data[0])
        name = poke_data[1].replace(' ', '')
        t = poke_data[2].split('/')
        if len(t) < 2:
            types = (t[0].replace(' ', ''), 'NONE')
        else:
            types = (t[0].replace(' ', ''), t[1].replace(' ', ''))
        abilities = (poke_data[9].replace(' ', ''), poke_data[10].replace(' ', ''))
        items = poke_data[11].split(', ')
        pokemon_list += [[num, name, types, int(poke_data[3]), int(poke_data[4]), int(poke_data[5]),
                          int(poke_data[6]), int(poke_data[7]), int(poke_data[8]),
                         abilities, items]]
    return pokemon_list


def classify_moves(data_str):
    pokemon_moves = {}
    data_list = data_str.split('\n')
    for line in data_list:
        if 'Pokemon Movesets' in line or line is '':
            continue
        tokens = line.split(':')[0].split(' ')
        name = tokens[1]
        for i in range(2, len(tokens)):
            name += tokens[i]
        pokemon_moves[name] = []
        moves = line.split(':')[1].split(',')
        for move in moves:
            mv = move.split(' at level ')
            pokemon_moves[name] += [(mv[0], mv[1])]
    return pokemon_moves


def combine_data(stat_list, moves_list):
    pokemon_ovr = []
    for pokemon in stat_list:
        pokemon_data = [pokemon[i] for i in range(0, len(pokemon))]
        pokemon_data += [moves_list[pokemon[1]]]
        pokemon_ovr += [pokemon_data]
    return pokemon_ovr
