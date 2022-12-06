import re

def part_one():
    with open("input.txt", "r") as in_file:
        pairs = in_file.read().split('\n')

    count = 0

    for pair in pairs:
        r1_start, r1_stop, r2_start, r2_stop = map(int, re.findall('\d+', pair))
        range_1, range_2 = set(range(r1_start, r1_stop + 1)), set(range(r2_start, r2_stop + 1))

        if range_1.issubset(range_2) or range_2.issubset(range_1):
            count += 1

    print(count)


def part_two():
    with open("input.txt", "r") as in_file:
        pairs = in_file.read().split('\n')

    count = 0

    for pair in pairs:
        r1_start, r1_stop, r2_start, r2_stop = map(int, re.findall('\d+', pair))
        range_1, range_2 = range(r1_start, r1_stop + 1), range(r2_start, r2_stop + 1)

        if (r1_start in range_2 or r1_stop in range_2) or (r2_start in range_1 or r2_stop in range_1):
            count += 1

    print(count)


#part_one()
part_two()
