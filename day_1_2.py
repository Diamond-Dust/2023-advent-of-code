def translate_digits(line):
    digit_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    digit_length_map = {len(k): [] for k in digit_map.keys()}
    for k in digit_map.keys():
        digit_length_map[len(k)].append(k)

    translated_line = ''
    last_uncovered = 0
    first_uncovered = 0
    for i in range(len(line)):
        for k, v in digit_length_map.items():
            text_to_consider = line[i:i+k]
            if text_to_consider in v:
                translated_line += line[first_uncovered:last_uncovered] + digit_map[text_to_consider]
                first_uncovered = i+k
                last_uncovered = first_uncovered
                break
        else:
            last_uncovered += 1
    translated_line += line[first_uncovered:last_uncovered]

    return translated_line


def get_calibration_value(line):
    translated_line = translate_digits(line)
    digits = list(filter(str.isdigit, translated_line))
    return int(digits[0] + digits[-1])


def get_calibration_values(document):
    return [get_calibration_value(line) for line in document.split('\n')]


def get_calibration_sum(document):
    values = get_calibration_values(document)
    return sum(values)


if __name__ == '__main__':

    with open('data/day_1.in', 'r') as file:
        data = file.read()

    print(get_calibration_sum(data))
