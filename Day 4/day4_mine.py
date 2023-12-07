

def part1(lines):
    total_winnings = 0

    for line in lines:
        winning_cards = sorted([int(num) for num in line.split(':')[-1].split('|')[0].split()])
        my_cards = sorted([int(num) for num in line.split(':')[-1].split('|')[1].split()])

        ptr1 = 0
        ptr2 = 0
        points = 1

        while ptr1<len(winning_cards) and ptr2<len(my_cards):
            if winning_cards[ptr1] == my_cards[ptr2]:
                points*=2
                ptr1+=1
                ptr2+=1
            elif winning_cards[ptr1] < my_cards[ptr2]:
                if ptr1 == len(winning_cards)-1:
                    break
                else:
                    ptr1+=1
            elif winning_cards[ptr1] > my_cards[ptr2]:
                if ptr2 == len(my_cards)-1:
                    break
                else:
                    ptr2+=1

        total_winnings += points//2

    return total_winnings

def part2(lines):

    total_cards = [1] * len(lines)

    for idx, line in enumerate(lines):
        winning_cards = sorted([int(num) for num in line.split(':')[-1].split('|')[0].split()])
        my_cards = sorted([int(num) for num in line.split(':')[-1].split('|')[1].split()])
        # break
        ptr1 = 0
        ptr2 = 0
        matches = 0

        while ptr1<len(winning_cards) and ptr2<len(my_cards):
            if winning_cards[ptr1] == my_cards[ptr2]:
                matches+=1
                ptr1+=1
                ptr2+=1
            elif winning_cards[ptr1] < my_cards[ptr2]:
                if ptr1 == len(winning_cards)-1:
                    break
                else:
                    ptr1+=1
            elif winning_cards[ptr1] > my_cards[ptr2]:
                if ptr2 == len(my_cards)-1:
                    break
                else:
                    ptr2+=1

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