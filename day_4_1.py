def get_card(card_line):
    numbers_string = card_line.split(': ')[1]
    numbers_strings = numbers_string.split(' | ')
    card = {
        'winning_numbers': [int(num) for num in filter(None, numbers_strings[0].split(' '))],
        'scratch_numbers': [int(num) for num in filter(None, numbers_strings[1].split(' '))]
    }
    return card


def fast_exponentiation(base, exp):
    # Assumes base in N, exponent in N_0
    if exp <= 0:
        return 1
    original_base = base
    result = 1
    while exp > 0:
        if exp % original_base:
            result *= base
        base *= base
        exp //= original_base
    return result


def hits_to_points(hits):
    if hits == 0:
        return 0
    return fast_exponentiation(2, hits - 1)


def get_winnings(card_line):
    card = get_card(card_line)
    hits = sum([scratch in card['winning_numbers'] for scratch in card['scratch_numbers']])
    return hits_to_points(hits)


def get_total_winnings(document):
    winnings = [get_winnings(card_line) for card_line in document.split('\n')]
    return sum(winnings)


if __name__ == '__main__':

    with open('data/day_4.in', 'r') as file:
        data = file.read()

    print(get_total_winnings(data))
