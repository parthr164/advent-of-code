def part1(data):
    f = open(data, "r")
    data = f.read()
    lines = data.split('\n')

    steps = lines[0]
    moves = {}

    for move in lines[2:]:
        moves[move.split('=')[0].strip()] = move.split('=')[1].strip()[1:-1].split(", ")

    current_move = 'AAA'
    no_of_steps = 0
    idx = 0

    while True:
        step = steps[idx]
        if current_move == 'ZZZ':
            return no_of_steps
        if step == 'L':
            current_move = moves[current_move][0]
        elif step == 'R':
            current_move = moves[current_move][1]
        else:
            print("Whoops!!!")

        no_of_steps += 1

        if idx == len(steps)-1:
            idx = 0
        else:
            idx += 1


if __name__ == "__main__":
    input_data = "day8.txt"

    print("********Solution for Part 1********")
    print(part1(input_data))
