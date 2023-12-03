def is_neighbouring_part(lines, idy, idx, length):
    neighbouring = False
    if idy > 0:
        upper_line_idx = max(0, idx - 1)
        while upper_line_idx < min(idx + length + 2, len(lines[idy - 1])):
            if not lines[idy - 1][upper_line_idx].isdigit() and lines[idy - 1][upper_line_idx] != '.':
                neighbouring = True
            upper_line_idx += 1
    if idy < len(lines) - 1:
        lower_line_idx = max(0, idx - 1)
        while lower_line_idx < min(idx + length + 2, len(lines[idy + 1])):
            if not lines[idy + 1][lower_line_idx].isdigit() and lines[idy + 1][lower_line_idx] != '.':
                neighbouring = True
            lower_line_idx += 1
    if idx > 0:
        if not lines[idy][idx - 1].isdigit() and lines[idy][idx - 1] != '.':
            neighbouring = True
    if idx + length < len(lines[idy]) - 1:
        if not lines[idy][idx + length + 1].isdigit() and lines[idy][idx + length + 1] != '.':
            neighbouring = True
    return neighbouring


def select_part_numbers(lines):
    part_numbers = []
    for idy, line in enumerate(lines):
        i = 0
        while i < len(line):
            if line[i].isdigit():
                k = 0
                while i + k + 1 < len(line) and line[i + k + 1].isdigit():
                    k += 1
                num = int(line[i:i+k+1])
                if is_neighbouring_part(lines, idy, i, k):
                    part_numbers.append(num)
                i += k
            i += 1
    return part_numbers


def get_part_number_sum(document):
    lines = document.split('\n')
    part_numbers = select_part_numbers(lines)
    return sum(part_numbers)


if __name__ == '__main__':

    with open('data/day_3.in', 'r') as file:
        data = file.read()

    print(get_part_number_sum(data))
