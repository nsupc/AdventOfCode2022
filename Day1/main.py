def part_one():
    with open("input.txt", "r") as in_file:
        elves = in_file.read().strip().split('\n\n')

    max = 0

    for elf in elves:
        calories = sum(map(int, elf.split('\n')))

        if calories > max:
            max = calories
    
    print(max)

def part_two():
    with open("input.txt", "r") as in_file:
        elves = in_file.read().strip().split('\n\n')

    capacities = []

    for elf in elves:
        calories = elf.split('\n')
        sum = 0

        for item in calories:
            sum += int(item)

        capacities.append(sum)

    capacities.sort(reverse=True)

    sum = 0
    for capacity in capacities[0:3]:
        sum += int(capacity)

    print(sum)

#part_one()
part_two()