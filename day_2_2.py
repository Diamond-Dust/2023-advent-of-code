from functools import reduce


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


def minimise_game(game_dict):
    game_dict['minima'] = {
        'red': max([round_dict.get('red', 0) for round_dict in game_dict['rounds']]),
        'green': max([round_dict.get('green', 0) for round_dict in game_dict['rounds']]),
        'blue': max([round_dict.get('blue', 0) for round_dict in game_dict['rounds']]),
    }
    return game_dict


def determine_set_powers(document):
    games = [dictify_game(line) for line in document.split('\n')]
    minimised_games = [minimise_game(game) for game in games]
    powers = [reduce(lambda x, y: x*y, game['minima'].values()) for game in minimised_games]
    return powers


def determine_possible_id_sum(document):
    powers = determine_set_powers(document)
    return sum(powers)


if __name__ == '__main__':

    with open('data/day_2.in', 'r') as file:
        data = file.read()

    print(determine_possible_id_sum(data))
