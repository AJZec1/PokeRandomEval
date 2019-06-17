hoenn_leaders = ['ROXANNE', 'BRAWLY', 'WATTSON', 'FLANNERY', 'NORMAN', 'WINONA', 'TATE&LIZA', 'WALLACE', 'JUAN']
kanto_leaders = ['BROCK', 'MISTY', 'LT. SURGE', 'ERIKA', 'KOGA', 'SABRINA', 'BLAINE', 'GIOVANNI']


def evaluate_trainers(trainer_str, region='HOENN'):
    trainer_data = trainer_str.split('\n')
    summary = ''
    if region is 'HOENN':
        leaders = hoenn_leaders
    else:
        leaders = kanto_leaders
    for line in trainer_data:
        if 'Trainers Pokemon' in line or line is '':
            continue
        tokens = line.split(' - ')
        trainer_name_part = tokens[0].split('(')
        trainer_name_part_2 = trainer_name_part[1].split(')')
        trainer_name = trainer_name_part_2[0]
        if 'LEADER' in trainer_name and ''.join(trainer_name.split(' ')[1:]) in leaders:
            summary += trainer_name + ' - ' + tokens[1] + '\n'
    return summary
