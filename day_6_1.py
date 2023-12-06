import math
from functools import reduce


class Race:
    def __init__(self, time, record):
        self.time = time
        self.record = record
        self.ways = None

    def count_ways(self):
        if self.ways is not None:
            return self.ways
        # a * ([self.time] - a) > [self.record]
        # -a^2 + [self.time]a - [self.record] > 0
        b = self.time
        c = -self.record
        # ax^2 + bx + c > 0, x \in [0, self.time]
        # x = (-b ± sqrt(b^2 - 4ac)) / (2a)
        # x = (-b ± sqrt(b^2 + 4c)) / -2
        # x_1 = (b + sqrt(b^2 + 4c)) / 2
        # x_2 = (b - sqrt(b^2 + 4c)) / 2
        # solution: (x_1, x_2) ∩ [0, self.time]
        x_1 = (b - math.sqrt(b*b + 4*c)) / 2
        x_2 = (b + math.sqrt(b*b + 4*c)) / 2
        left_start = 0 if x_1 < 0 else int(math.floor(x_1 + 1))
        right_end = self.time if x_2 > self.time else int(math.ceil(x_2 - 1))
        ways = right_end - left_start + 1
        self.ways = ways
        return self.ways


def get_times_distances(document):
    time_line, distance_line = document.split('\n')
    time_counts = [int(time) for time in filter(None, time_line.split(': ')[1].split(' '))]
    distance_counts = [int(time) for time in filter(None, distance_line.split(': ')[1].split(' '))]
    return zip(time_counts, distance_counts)


def get_ways(document):
    times_distances = get_times_distances(document)
    races = [Race(time, distance) for time, distance in times_distances]
    ways = [race.count_ways() for race in races]
    return ways


def get_ways_product(document):
    ways = get_ways(document)
    return reduce(lambda x, y: x * y, ways)


if __name__ == '__main__':

    with open('data/day_6.in', 'r') as file:
        data = file.read()

    print(get_ways_product(data))
