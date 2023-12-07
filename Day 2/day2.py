import re

def part1(data):
    f = open(data, "r")
    data = f.read()
    data = data.split('\n')

    game_possible = True
    game_sum = 0

    for game in data:

        red = re.compile(r'\d+(?= red)')
        all_red = red.findall(game)
        game_possible = all(int(num) <= 12 for num in all_red)

        if game_possible:
            green = re.compile(r'\d+(?= green)')
            all_green = green.findall(game)
            game_possible = all(int(num) <= 13 for num in all_green)

        if game_possible:
            blue = re.compile(r'\d+(?= blue)')
            all_blue = blue.findall(game)
            game_possible = all(int(num) <= 14 for num in all_blue)

        if game_possible:
            find_game = re.compile(r'Game \d+')
            game_no = find_game.match(game).group(0).split(' ')[-1]
            game_sum += int(game_no)

    return game_sum


def part2(data):
    f = open(data, "r")
    data = f.read()
    data = data.split('\n')

    game_sum = 0

    for game in data:
        red = re.compile(r'\d+(?= red)')
        all_red = red.findall(game)
        max_red = max(int(num) for num in all_red)

        green = re.compile(r'\d+(?= green)')
        all_green = green.findall(game)
        max_green = max(int(num) for num in all_green)

        blue = re.compile(r'\d+(?= blue)')
        all_blue = blue.findall(game)
        max_blue = max(int(num) for num in all_blue)

        game_sum += max_red * max_green * max_blue

    return game_sum

if __name__ == "__main__":
    input_path = "day2.txt"
    print("********Solution for Part 1********")
    print(part1(input_path))
    print('\n')

    print("********Solution to Part 2********")
    print(part2(input_path))