def get_seeds(seed_line):
    seeds = seed_line.split(': ')[1]
    seeds = seeds.split(' ')
    seeds = zip(seeds[::2], seeds[1::2])
    return [(int(seed), int(length)) for seed, length in seeds]


class EntryLine:
    def __init__(self, line):
        split_line = line.split(' ')
        self.dest = int(split_line[0])
        self.source = int(split_line[1])
        self.length = int(split_line[2])
        self.src_end = self.source + self.length - 1
        self.dst_end = self.dest + self.length - 1

    def transform(self, src_val_start, length):
        transformed_start = self.dest + src_val_start - self.source
        src_val_end = src_val_start + length - 1
        # Wholly outside
        if src_val_end < self.source or src_val_start > self.src_end:
            return [(src_val_start, length)], []
        # Wholly inside
        if self.source <= src_val_start <= self.src_end and self.source <= src_val_end <= self.src_end:
            return [], [(transformed_start, length)]
        # Wholly encompassing
        if src_val_start < self.source and src_val_end > self.src_end:
            return [
                (src_val_start, self.source - src_val_start),
                (self.source + self.length, length - (self.source - src_val_start) - self.length)
            ],\
                   [(self.dest, self.length)]
        # Right-side overlap
        if self.source <= src_val_start <= self.src_end:
            transformed_length = self.length - (src_val_start - self.source)
            return [(src_val_start + transformed_length, length - transformed_length)],\
                   [(transformed_start, self.length - (src_val_start - self.source))]
        # Left-side overlap
        if self.source <= src_val_end <= self.src_end:
            transformed_length = src_val_start + length - self.source
            return [(src_val_start, length - transformed_length)],\
                   [(transformed_start + length - transformed_length, transformed_length)]
        raise ValueError('i forgor 💀')


class Entry:
    def __init__(self, entry_block):
        split_entry = entry_block.split('\n')
        self.lines = [EntryLine(line) for line in split_entry[1:]]

    def transform(self, src_val, length, lines=None):
        if lines is None:
            lines = self.lines
        if not lines:
            return [(src_val, length)]
        res = []
        unchanged, changed = lines[0].transform(src_val, length)
        if changed:
            res.extend(changed)
        for unchanged_interval in unchanged:
            res.extend(self.transform(unchanged_interval[0], unchanged_interval[1], lines=lines[1:]))
        return res


def get_location(seed, entries):
    new_location = []
    if not entries:
        return [seed]
    new_seeds = entries[0].transform(seed[0], seed[1])
    for new_seed in new_seeds:
        new_location.extend(get_location(new_seed, entries[1:]))
    return new_location


def get_closest_seed(document):
    entries = document.split('\n\n')
    seeds = get_seeds(entries[0])
    entries = [Entry(entry) for entry in entries[1:]]
    locations = {seed: get_location(seed, entries) for seed in seeds}
    return min([seed for sublist in locations.values() for seed, range in sublist])


if __name__ == '__main__':

    with open('data/day_5.in', 'r') as file:
        data = file.read()

    print(get_closest_seed(data))
