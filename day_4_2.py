def get_card(card_line):
    numbers_string = card_line.split(': ')[1]
    numbers_strings = numbers_string.split(' | ')
    card = {
        'winning_numbers': [int(num) for num in filter(None, numbers_strings[0].split(' '))],
        'scratch_numbers': [int(num) for num in filter(None, numbers_strings[1].split(' '))]
    }
    return card


def get_hits(card_line):
    card = get_card(card_line)
    return sum([scratch in card['winning_numbers'] for scratch in card['scratch_numbers']])


def get_total_cards(document):
    winnings = [get_hits(card_line) for card_line in document.split('\n')]
    cards = [1] * len(winnings)
    for idx, win in enumerate(winnings):
        for i in range(1, win + 1):
            cards[idx + i] += cards[idx]
    return sum(cards)


if __name__ == '__main__':

    with open('data/day_4.in', 'r') as file:
        data = file.read()

    print(get_total_cards(data))
