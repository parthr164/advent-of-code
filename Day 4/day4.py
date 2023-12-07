

def part1(lines):
    total_winnings = 0

    for line in lines:
        winning_cards = {int(num) for num in line.split(':')[-1].split('|')[0].split()}
        my_cards = {int(num) for num in line.split(':')[-1].split('|')[1].split()}

        points = len(winning_cards & my_cards)

        if points == 0:
            total_winnings += 0
        else:
            total_winnings += 2 ** (points - 1)

    return total_winnings

def part2(lines):
    total_cards = [1] * len(lines)

    for idx, line in enumerate(lines):
        winning_cards = {int(num) for num in line.split(':')[-1].split('|')[0].split()}
        my_cards = {int(num) for num in line.split(':')[-1].split('|')[1].split()}

        matches = len(winning_cards & my_cards)

        for index in range(matches):
            total_cards[idx+index+1] += 1*total_cards[idx]

    return sum(total_cards)

if __name__ == "__main__":
    input_data = "day4.txt"
    f = open(input_data, "r")
    data = f.readlines()

    print("********Solution for Part 1********")
    print(part1(data))
    print('\n')

    print("********Solution to Part 2********")
    print(part2(data))