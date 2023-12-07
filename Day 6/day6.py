def part1(data):
    f = open(data, "r")
    data = f.read()
    lines = data.split('\n')

    times = [int(x) for x in lines[0].split(':')[-1].split()]
    distances = [int(x) for x in lines[1].split(':')[-1].split()]

    best_score = 1

    for idx, time in enumerate(times):
        no_of_ways = 0
        for ms in range(time // 2):
            if ms * (time - ms) > distances[idx]:
                no_of_ways = (time - ms) - ms + 1
                break

        best_score *= no_of_ways

    return best_score


def part2(data):
    f = open(data, "r")
    data = f.read()
    lines = data.split('\n')

    time = int(lines[0].split(':')[-1].replace(' ', ''))
    distance = int(lines[1].split(':')[-1].replace(' ', ''))

    no_of_ways = 0
    for ms in range(time // 2):
        if ms * (time - ms) > distance:
            no_of_ways = (time - ms) - ms + 1
            break

    return no_of_ways


if __name__ == "__main__":
    input_data = "day6.txt"
    # input_data = 'sample_input.txt'

    print("********Solution for Part 1********")
    print(part1(input_data))
    print('\n')

    print("********Solution to Part 2********")
    print(part2(input_data))
