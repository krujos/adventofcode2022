def find(buffer):
    last_seen = {}
    possible = 0

    for i, v in enumerate(buffer):
        s = {v, buffer[i+1], buffer[i+2], buffer[i+3]}
        if 4 == len(s):
            print(i+4)
            return


if __name__ == '__main__':
    with open('input_day6.txt') as f:
        b = f.read().splitlines()
    f.close()

    find(b[0])
