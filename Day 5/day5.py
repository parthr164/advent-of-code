def process_input(input_data):
    f = open(input_data, "r")
    data = f.read()
    data = data.split('\n')

    # seeds
    seeds = [int(seed) for seed in data[0].split(':')[-1].split()]

    idx = 3
    s2s = {}
    s2f = {}
    f2w = {}
    w2l = {}
    l2t = {}
    t2h = {}
    h2l = {}

    # seed to soil map
    while any(x.isnumeric() for x in data[idx].split()):
        line = [int(x) for x in data[idx].split()]
        s2s[line[1]] = (line[0], line[2])
        idx += 1

    idx += 2
    while any(x.isnumeric() for x in data[idx].split()):
        line = [int(x) for x in data[idx].split()]
        s2f[line[1]] = (line[0], line[2])
        idx += 1

    idx += 2
    while any(x.isnumeric() for x in data[idx].split()):
        line = [int(x) for x in data[idx].split()]
        f2w[line[1]] = (line[0], line[2])
        idx += 1

    idx += 2
    while any(x.isnumeric() for x in data[idx].split()):
        line = [int(x) for x in data[idx].split()]
        w2l[line[1]] = (line[0], line[2])
        idx += 1

    idx += 2
    while any(x.isnumeric() for x in data[idx].split()):
        line = [int(x) for x in data[idx].split()]
        l2t[line[1]] = (line[0], line[2])
        idx += 1

    idx += 2
    while any(x.isnumeric() for x in data[idx].split()):
        line = [int(x) for x in data[idx].split()]
        t2h[line[1]] = (line[0], line[2])
        idx += 1

    idx += 2
    while idx < len(data) and any(x.isnumeric() for x in data[idx].split()):
        line = [int(x) for x in data[idx].split()]
        h2l[line[1]] = (line[0], line[2])
        idx += 1

    return seeds, s2s, s2f, f2w, w2l, l2t, t2h, h2l


def part1(data):
    seeds, s2s, s2f, f2w, w2l, l2t, t2h, h2l = process_input(data)
    locations = []

    for seed in seeds:
        soil = 0
        fertilizer = 0
        water = 0
        light = 0
        temp = 0
        humidity = 0

        for key, val in s2s.items():
            if key <= seed < key + val[1]:
                soil = val[0] + (seed - key)
                # print(key, val[0], seed, (seed-key), soil)
                break
        else:
            soil += seed

        for key, val in s2f.items():
            if soil >= key and soil < key + val[1]:
                fertilizer = val[0] + (soil - key)
                break
        else:
            fertilizer += soil

        for key, val in f2w.items():
            if fertilizer >= key and fertilizer < key + val[1]:
                water = val[0] + (fertilizer - key)
                break
        else:
            water += fertilizer

        for key, val in w2l.items():
            if water >= key and water < key + val[1]:
                light = val[0] + (water - key)
                break
        else:
            light += water

        for key, val in l2t.items():
            if light >= key and light < key + val[1]:
                temp = val[0] + (light - key)
                break
        else:
            temp += light

        for key, val in t2h.items():
            if temp >= key and temp < key + val[1]:
                humidity = val[0] + (temp - key)
                break
        else:
            humidity += temp

        for key, val in h2l.items():
            if humidity >= key and humidity < key + val[1]:
                locations.append(val[0] + (humidity - key))
                break
        else:
            locations.append(humidity)

    return min(locations)


if __name__ == "__main__":
    input_data = "day5.txt"
    # input_data = 'sample_input.txt'

    print("********Solution for Part 1********")
    print(part1(input_data))