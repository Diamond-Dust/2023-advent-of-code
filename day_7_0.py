"""
For the 'typical' poker rules:
"""

from enum import Enum
from collections import Counter


# https://docs.python.org/3/howto/enum.html#orderedenum
class OrderedEnum(Enum):
    # https://stackoverflow.com/a/42397017
    def __init__(self, *args):
        try:
            # attempt to initialize other parents in the hierarchy
            super().__init__(*args)
        except TypeError:
            # ignore -- there are no other parents
            pass
        ordered = len(self.__class__.__members__) + 1
        self._order = ordered

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self._order >= other._order
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self._order > other._order
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self._order <= other._order
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self._order < other._order
        return NotImplemented


class Card(OrderedEnum):
    Two = '2'
    Three = '3'
    Four = '4'
    Five = '5'
    Six = '6'
    Seven = '7'
    Eight = '8'
    Nine = '9'
    Ten = 'T'
    Jack = 'J'
    Queen = 'Q'
    King = 'K'
    Ace = 'A'


class Type(OrderedEnum):
    High = 'High Card'
    Pair = 'Pair'
    TwoPair = 'Two Pair'
    Three = 'Three of a Kind'
    Full = 'Full House'
    Caret = 'Four of a Kind'
    Poker = 'Poker'


class HandType:
    def __init__(self, commons):
        self.commons = commons
        self.type = None
        self.type_cards = []
        self.determine(commons)

    def __lt__(self, other):
        return self.type < other.type

    def determine(self, commons):
        if commons[0][1] == 5:
            self.type = Type.Poker
            self.type_cards = [Card(commons[0][0])]
        elif commons[0][1] == 4:
            self.type = Type.Caret
            self.type_cards = [Card(commons[0][0])]
        elif commons[0][1] == 3:
            twos = list(filter(lambda t: t[1] == 2, commons))
            if twos:
                self.type = Type.Full
                self.type_cards = [Card(commons[0][0]), Card(twos[0][0])]
            else:
                self.type = Type.Three
                self.type_cards = [Card(commons[0][0])]
        elif commons[0][1] == 2:
            twos = list(filter(lambda t: t[1] == 2, commons))
            twos = [Card(two[0]) for two in twos]
            twos.sort(reverse=True)
            if len(twos) == 2:
                self.type = Type.TwoPair
                self.type_cards = [twos[0], twos[1]]
            else:
                self.type = Type.Pair
                self.type_cards = [Card(twos[0])]
        elif commons[0][1] == 1:
            ones = [Card(one[0]) for one in commons]
            ones.sort(reverse=True)
            self.type = Type.High
            self.type_cards = [ones[0]]
        else:
            raise ValueError('I forgor 💀')


class Hand:
    def __init__(self, line):
        self.line = line
        self.type = self.determine_hand_type(line)
        self.cards = [Card(c) for c in self.line]
        self.cards.sort(reverse=True)

    def __lt__(self, other):
        if self.type.type == other.type.type:
            if self.type.type_cards == other.type.type_cards:
                return self.cards < other.cards
            return self.type.type_cards < other.type.type_cards
        return self.type < other.type

    @staticmethod
    def determine_hand_type(line):
        c = Counter(line)
        mc = c.most_common()
        return HandType(mc)


class Game:
    def __init__(self, line):
        self.line = line
        hand_line, bid_line = line.split(' ')
        self.hand = Hand(hand_line)
        self.bid = int(bid_line)

    def __lt__(self, other):
        return self.hand < other.hand

    def __repr__(self):
        return f'<Hand: {"".join([card.value for card in self.hand.cards])} Bid: {self.bid} Type: {self.hand.type.type.value}> '


def get_total_winnings(document):
    games = [Game(line) for line in document.split('\n')]
    games.sort()
    winnings = [game.bid * (idx + 1) for idx, game in enumerate(games)]
    return sum(winnings)


if __name__ == '__main__':

    with open('data/day_7.in', 'r') as file:
        data = file.read()

    print(get_total_winnings(data))
