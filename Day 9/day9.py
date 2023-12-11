def part1(data):
    f = open(data, "r")
    data = f.read()
    lines = data.split('\n')

    final_ans = 0

    def pattern(series):
        new_series = [series[i + 1] - series[i] for i in range(len(series) - 1)]
        if all(x == 0 for x in new_series):
            return series[-1]
        else:
            return series[-1] + pattern(new_series)

    for line in lines:
        current_line = [int(x) for x in line.split()]

        final_ans += pattern(current_line)

    return final_ans

def part2(data):
    f = open(data, "r")
    data = f.read()
    lines = data.split('\n')

    final_ans = 0

    def pattern(series):
        new_series = [series[i + 1] - series[i] for i in range(len(series) - 1)]
        if all(x == 0 for x in new_series):
            return series[0]
        else:
            return series[0] - pattern(new_series)

    for line in lines:
        current_line = [int(x) for x in line.split()]

        final_ans += pattern(current_line)

    return final_ans


if __name__ == "__main__":
    input_data = "day9.txt"
    # input_data = 'sample_input.txt'

    print("********Solution for Part 1********")
    print(part1(input_data))
    print('\n')

    print("********Solution for Part 2********")
    print(part2(input_data))
