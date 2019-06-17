cool_items = [('MASTER BALL', 5), ('ULTRA BALL', 1), ('FULL RESTORE', 2), ('MAX POTION', 2), ('MAX REVIVE', 3),
              ('SACRED ASH', 4), ('HP UP', 5), ('PP UP', 4), ('PP MAX', 5), ('RARE CANDY', 5), ('SUN STONE', 2),
              ('MOON STONE', 3), ('NUGGET', 2), ('TM', 1)]


def evaluate_items(poke_list):
    summary = ''
    for item in cool_items:
        summary += item[0] + ': '
        for pkmn in poke_list:
            for held_item in pkmn[-2]:
                if item[0] in held_item:
                    summary += pkmn[1] + ', '
        summary = summary[:-2] + '\n'
    return summary
