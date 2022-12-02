def you_play_rock(play):
    return play == "X"


def you_play_paper(play):
    return play == "Y"


def you_play_scissors(play):
    return play == "Z"


def they_play_rock(play):
    return play == "A"


def they_play_paper(play):
    return play == "B"


def they_play_scissors(play):
    return play == "C"


def play_game(you, them):
    win = 6
    tie = 3
    loss = 0
    if you_play_rock(you):
        if they_play_paper(them):
            return loss
        if they_play_rock(them):
            return tie
        if they_play_scissors(them):
            return win

    if you_play_paper(you):
        if they_play_paper(them):
            return tie
        if they_play_rock(them):
            return win
        if they_play_scissors(them):
            return loss

    if you_play_scissors(you):
        if they_play_paper(them):
            return win
        if they_play_rock(them):
            return loss
        if they_play_scissors(them):
            return tie

    exit(1)


if __name__ == '__main__':
    score = 0

    with open('input_day2.txt') as f:
        lines = f.readlines()
    f.close()

    for line in lines:
        them, you = line.split()

        match you:
            case "X":
                score += 1
            case "Y":
                score += 2
            case "Z":
                score += 3
            case _:
                print("invalid value")
                exit(1)

        score += play_game(you, them)

    print(score)
