import create_data as cd
from eval_availability import evaluate_availability
from eval_items import evaluate_items
from eval_moves import evaluate_movesets
from eval_starters import evaluate_starters
from eval_trainers import evaluate_trainers

sec_titles = ['Patching for National Dex at Start of Game', 'Pokemon Base Stats & Types', 'Removing Trade Evolutions',
              'Condensed Level Evolutions', 'Random 2-Evolution Starters', 'Move Data', 'Pokemon Movesets',
              'Trainers Pokemon', 'Static Pokemon', 'Wild Pokemon', 'TM Moves', 'Move Tutor Moves', 'In-Game Trades']
hoenn = 'HOENN'
kanto = 'KANTO'


def read_file(fname):
    f = open(fname, 'r')
    cur_str = ''
    section_list = []
    for line in f.readlines():
        line_fix = line.replace('\n', '')
        if line_fix == '':
            section_list += [cur_str]
            cur_str = ''
        else:
            cur_str += line_fix + '\n'
    return section_list


def count_lines(data_string):
    return len(data_string.split('\n')) > 1


def evaluate():
    section_list = read_file('log_files/FireRed-Tweak1.gba.log')
    outfile = open('out.txt', 'w+')
    stat_list = cd.pokemon_stat_list(section_list[1])
    move_list = cd.classify_moves(section_list[6])
    poke_list = cd.combine_data(stat_list, move_list)
    for section in section_list:
        if sec_titles[4] in section:
            outfile.write(evaluate_starters(section) + '\n')
        if sec_titles[5] in section:
            outfile.write(evaluate_items(poke_list) + '\n')
        if sec_titles[6] in section:
            outfile.write(evaluate_movesets(poke_list) + '\n')
        if sec_titles[7] in section:
            outfile.write(evaluate_trainers(section, kanto) + '\n')
        if sec_titles[9] in section:
            outfile.write(evaluate_availability(section, kanto) + '\n')
    outfile.close()


evaluate()
