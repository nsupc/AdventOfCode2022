shape_scores = {
    "A": 1,
    "B": 2,
    "C": 3
}


def part_one():
    rps = {
        "X": "A",
        "Y": "B",
        "Z": "C"
    }

    with open("input.txt", "r") as in_file:
        rounds = in_file.read().split('\n')

    score = 0

    for round in rounds: 
        opponent, action = round[0], rps[round[2]]

        score += shape_scores[action]

        if opponent == action:
            score += 3
        elif (action == "A" and opponent == "C") or (action == "B" and opponent == "A") or (action == "C" and opponent == "B"):
            score += 6
    
    print(score)


def part_two():
    result_scores = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }

    with open("input.txt", "r") as in_file:
        rounds = in_file.read().split('\n')

    score = 0

    for round in rounds:
        opponent, result = round.split()

        score += result_scores[result]

        match result:
            case "X":
                if opponent == "A":
                    score += 3
                elif opponent == "B":
                    score += 1
                else:
                    score += 2
            case "Y":
                score += shape_scores[opponent]
            case "Z":
                if opponent == "A":
                    score += 2
                elif opponent == "B":
                    score += 3
                else:
                    score += 1

    print(score)


#part_one()
part_two()