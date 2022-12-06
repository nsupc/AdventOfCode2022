def part_one():
    values = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    with open("input.txt", "r") as in_file:
        rucksacks = in_file.read().split("\n")

    sum = 0

    for rucksack in rucksacks:
        slice = int(len(rucksack)/2)

        compartment_one = rucksack[:slice]
        compartment_two = rucksack[slice:]

        for char in compartment_one:
            if char in compartment_two:
                sum += values.index(char)
                break

    print(sum)
    

def part_two():
    values = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    with open("input.txt", "r") as in_file:
        rucksacks = in_file.read().split("\n")

    sum = 0

    for i in range(0, len(rucksacks), 3):
        bag_a, bag_b, bag_c = rucksacks[i: i + 3]

        for char in bag_a:
            if char in bag_b and char in bag_c:
                sum += values.index(char)
                break

    print(sum)

#part_one()
part_two()