from functools import reduce


def get_neighbouring_part_numbers(digitised_lines, idx, idy):
    part_numbers = []
    # Line above current
    if idy > 0:
        left_side_idx_limit = max(0, idx - 1)
        right_side_idx_limit = min(idx + 2, len(digitised_lines[idy - 1]))
        upper_line_idx = left_side_idx_limit
        while upper_line_idx < right_side_idx_limit:
            k = 1
            if isinstance(digitised_lines[idy - 1][upper_line_idx], int):
                part_numbers.append(digitised_lines[idy - 1][upper_line_idx])
                # Go right until a break is found
                while upper_line_idx + k < right_side_idx_limit:
                    if not isinstance(digitised_lines[idy - 1][upper_line_idx + k], int):
                        break
                    k += 1
            upper_line_idx += k
    # Line below current
    if idy > 0:
        left_side_idx_limit = max(0, idx - 1)
        right_side_idx_limit = min(idx + 2, len(digitised_lines[idy + 1]))
        lower_line_idx = left_side_idx_limit
        while lower_line_idx < right_side_idx_limit:
            k = 1
            if isinstance(digitised_lines[idy + 1][lower_line_idx], int):
                part_numbers.append(digitised_lines[idy + 1][lower_line_idx])
                # Go right until a break is found
                while lower_line_idx + k < right_side_idx_limit:
                    if not isinstance(digitised_lines[idy + 1][lower_line_idx + k], int):
                        break
                    k += 1
            lower_line_idx += k
    # On the left
    if idx > 0:
        if isinstance(digitised_lines[idy][idx - 1], int):
            part_numbers.append(digitised_lines[idy][idx - 1])
    # On the right
    if idx < len(digitised_lines[idy]) - 1:
        if isinstance(digitised_lines[idy][idx + 1], int):
            part_numbers.append(digitised_lines[idy][idx + 1])
    return part_numbers


def get_gear_ratios(digitised_lines):
    gear_ratios = []
    for idy, line in enumerate(digitised_lines):
        for idx, c in enumerate(line):
            if c == '*':
                neighbouring_part_numbers = get_neighbouring_part_numbers(digitised_lines, idx, idy)
                if len(neighbouring_part_numbers) == 2:
                    gear_ratios.append(reduce(lambda x, y: x*y, neighbouring_part_numbers))
    return gear_ratios


def digitise_line(line):
    digitised_line = [None] * len(line)
    i = 0
    while i < len(line):
        if line[i].isdigit():
            k = 0
            while i + k + 1 < len(line) and line[i + k + 1].isdigit():
                k += 1
            num = int(line[i:i+k+1])
            for j in range(i, i+k+1):
                digitised_line[j] = num
            i += k
        else:
            digitised_line[i] = line[i]
        i += 1
    return digitised_line


def get_gear_ratio_sum(document):
    lines = document.split('\n')
    digitised_lines = [digitise_line(line) for line in lines]
    gear_ratios = get_gear_ratios(digitised_lines)
    return sum(gear_ratios)


if __name__ == '__main__':

    with open('data/day_3.in', 'r') as file:
        data = file.read()

    print(get_gear_ratio_sum(data))
