# f = open("day1.txt", "r")
# data = f.read()

def part1(data):
    f = open(data, "r")
    data = f.read()
    data = data.split('\n')

    final_list = []

    for val in data:
        temp_num = 0
        initial_ptr = 0
        final_ptr = len(val) - 1

        initial_num = 0
        final_num = 0

        initial_found = False
        final_found = False

        while (not initial_found or not final_found) and initial_ptr <= final_ptr:

            if not initial_found:
                if val[initial_ptr].isnumeric():
                    initial_num = int(val[initial_ptr])
                    initial_found = True
                initial_ptr += 1

            if not final_found:
                if val[final_ptr].isnumeric():
                    final_num = int(val[final_ptr])
                    final_found = True
                final_ptr -= 1

        if initial_found != final_found:
            initial_num, final_num = max(initial_num, final_num), max(initial_num, final_num)

        temp_num = initial_num * 10 + final_num
        final_list.append(temp_num)

    return sum(final_list)

def part2(data):
    f = open(data, "r")
    data = f.read()

    data = data.replace('one', 'o1e')
    data = data.replace('two', 't2o')
    data = data.replace('three', 'th3ee')
    data = data.replace('four', 'f4ur')
    data = data.replace('five', 'f5ve')
    data = data.replace('six', 's6x')
    data = data.replace('seven', 'se7en')
    data = data.replace('eight', 'ei8ht')
    data = data.replace('nine', 'n9ne')
    data = data.replace('zero', 'z0ro')

    data = data.split('\n')

    final_list = []

    for val in data:
        temp_num = 0
        initial_ptr = 0
        final_ptr = len(val) - 1

        initial_num = 0
        final_num = 0

        initial_found = False
        final_found = False

        while (not initial_found or not final_found) and initial_ptr <= final_ptr:

            if not initial_found:
                if val[initial_ptr].isnumeric():
                    initial_num = int(val[initial_ptr])
                    initial_found = True

                initial_ptr += 1

            if not final_found:
                if val[final_ptr].isnumeric():
                    final_num = int(val[final_ptr])
                    final_found = True

                final_ptr -= 1

        if initial_found != final_found:
            initial_num, final_num = max(initial_num, final_num), max(initial_num, final_num)

        temp_num = initial_num * 10 + final_num

        final_list.append(temp_num)

    return sum(final_list)


if __name__ == "__main__":
    input_path = "day1.txt"
    print("********Solution for Part 1********")
    print(part1(input_path))
    print('\n')

    print("********Solution to Part 2********")
    print(part2(input_path))