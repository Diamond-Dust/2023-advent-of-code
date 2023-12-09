def digitise_line(line):
    return [int(val) for val in line.split(' ')]


def get_prefirst_value(values_list):
    if [values_list[0]] * len(values_list) == values_list:
        return values_list[0]
    higher_order_values_list = [second - first for first, second in zip(values_list[:-1], values_list[1:])]
    last_value = values_list[0] - get_prefirst_value(higher_order_values_list)
    return last_value


def get_total_prefirst_values(document):
    values = [get_prefirst_value(digitise_line(line)) for line in document.split('\n')]
    return sum(values)


if __name__ == '__main__':

    with open('data/day_9.in', 'r') as file:
        data = file.read()

    print(get_total_prefirst_values(data))
