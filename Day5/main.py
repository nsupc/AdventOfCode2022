import re

def part_one():
    with open("input.txt", "r") as in_file:
        structure, steps = in_file.read().split('\n\n')
    
    num_columns = len(structure.split('\n')[-1].strip().split("   "))

    data = {}

    for num in range(1, num_columns+1):
        data[num] = []

    columns = structure.split('\n')[:-1]

    for column in columns:
        for idx, i in enumerate(range(0, len(column), 4)):
            chunk = column[i:i+4].strip()
            if chunk:
                temp = data[idx+1]
                temp.append(chunk[1])

                data[idx+1] = temp
    
    steps = steps.split('\n')
    
    for step in steps:
        count, origin, target = map(int, re.findall("\d+", step))

        for _ in range(0, count):
            item = data[origin].pop(0)

            temp = data[target]
            temp.insert(0, item)

            data[target] = temp

    result = []

    for col in data:
        result.append(data[col][0])

    print("".join(result))


def part_two():
    with open("input.txt", "r") as in_file:
        structure, steps = in_file.read().split('\n\n')
    
    num_columns = len(structure.split('\n')[-1].strip().split("   "))

    data = {}

    for num in range(1, num_columns+1):
        data[num] = []

    columns = structure.split('\n')[:-1]

    for column in columns:
        for idx, i in enumerate(range(0, len(column), 4)):
            chunk = column[i:i+4].strip()
            if chunk:
                temp = data[idx+1]

                temp.append(chunk[1])

                data[idx+1] = temp
    
    steps = steps.split('\n')
    
    for step in steps:
        count, origin, target = map(int, re.findall("\d+", step))

        data[target] = data[origin][0:count] + data[target]
        data[origin] = data[origin][count:]

    result = []

    for col in data:
        result.append(data[col][0])

    print("".join(result))


#part_one()
part_two()