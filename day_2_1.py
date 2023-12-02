def dictify_round(game_str):
    result = {}
    cubes_strs = game_str.split(', ')
    for cube_str in cubes_strs:
        split_cube = cube_str.split(' ')
        result[split_cube[1]] = int(split_cube[0])
    return result


def dictify_game(line):
    result = {}
    split_line = line.split(': ')
    result['id'] = int(split_line[0][5:])
    split_games = split_line[1].split('; ')
    result['rounds'] = [dictify_round(game) for game in split_games]
    return result


def check_if_possible(game_dict, max_red=12, max_green=13, max_blue=14):
    for round_dict in game_dict['rounds']:
        if 'red' in round_dict and round_dict['red'] > max_red:
            return False
        if 'green' in round_dict and round_dict['green'] > max_green:
            return False
        if 'blue' in round_dict and round_dict['blue'] > max_blue:
            return False
    return True


def determine_possible_ids(document):
    games = [dictify_game(line) for line in document.split('\n')]
    ids = [game['id'] for game in games if check_if_possible(game)]
    return ids


def determine_possible_id_sum(document):
    ids = determine_possible_ids(document)
    return sum(ids)


if __name__ == '__main__':

    with open('data/day_2.in', 'r') as file:
        data = file.read()

    print(determine_possible_id_sum(data))
