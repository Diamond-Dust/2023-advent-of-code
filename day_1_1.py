def get_calibration_value(line):
    digits = list(filter(str.isdigit, line))
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
