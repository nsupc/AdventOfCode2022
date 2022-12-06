def part_one():
    with open("input.txt", "r") as in_file:
        buffer = in_file.read()

        for idx, _ in enumerate(buffer):
            slice = buffer[idx:idx+4]

            if len(slice) == len(set(slice)):
                print(idx+4)
                return


def part_two():
    with open("input.txt", "r") as in_file:
        buffer = in_file.read()

        for idx, _ in enumerate(buffer):
            slice = buffer[idx:idx+14]

            if len(slice) == len(set(slice)):
                print(idx+14)
                return


#part_one()
part_two()