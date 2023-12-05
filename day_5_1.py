def get_seeds(seed_line):
    seeds = seed_line.split(': ')[1]
    return [int(seed) for seed in seeds.split(' ')]


class EntryLine:
    def __init__(self, line):
        split_line = line.split(' ')
        self.dest = int(split_line[0])
        self.source = int(split_line[1])
        self.length = int(split_line[2])

    def transform(self, src_val):
        if self.source <= src_val < self.source + self.length:
            return self.dest + src_val - self.source
        return src_val


class Entry:
    def __init__(self, entry_block):
        split_entry = entry_block.split('\n')
        self.lines = [EntryLine(line) for line in split_entry[1:]]

    def transform(self, src_val):
        res = src_val
        for line in self.lines:
            res = line.transform(src_val)
            if res != src_val:
                break
        return res


def get_location(seed, entries):
    for entry in entries:
        seed = entry.transform(seed)
    return seed


def get_closest_seed(document):
    entries = document.split('\n\n')
    seeds = get_seeds(entries[0])
    entries = [Entry(entry) for entry in entries[1:]]
    locations = {seed: get_location(seed, entries) for seed in seeds}
    return min(locations.values())


if __name__ == '__main__':

    with open('data/day_5.in', 'r') as file:
        data = file.read()

    print(get_closest_seed(data))
