def you_lose(play):
    return play == "X"


def you_draw(play):
    return play == "Y"


def you_win(play):
    return play == "Z"


def they_play_rock(play):
    return play == "A"


def they_play_paper(play):
    return play == "B"


def they_play_scissors(play):
    return play == "C"


rock = 1
paper = 2
scissors = 3
win = 6
tie = 3
loss = 0


def play_game(them, outcome):
    if you_lose(outcome):
        if they_play_paper(them):
            return rock + loss
        if they_play_rock(them):
            return scissors + loss
        if they_play_scissors(them):
            return paper + loss

    if you_draw(outcome):
        if they_play_paper(them):
            return paper + tie
        if they_play_rock(them):
            return rock + tie
        if they_play_scissors(them):
            return scissors + tie

    if you_win(outcome):
        if they_play_paper(them):
            return scissors + win
        if they_play_rock(them):
            return paper + win
        if they_play_scissors(them):
            return rock + win

    print("bad outcome " + outcome)
    exit(1)


if __name__ == '__main__':
    score = 0

    with open('input_day2.txt') as f:
        lines = f.readlines()
    f.close()

    for line in lines:
        t, o = line.split()
        score += play_game(t, o)

    print(score)
