def find(buffer, len_to_find):

    for i, v in enumerate(buffer):
        s = set()
        for r in range(len_to_find):
            s.add(buffer[r+i])
        if len_to_find == len(s):
            print(i+len_to_find)
            return


if __name__ == '__main__':
    with open('input_day6.txt') as f:
        b = f.read().splitlines()
    f.close()

    find(b[0],4)
    find(b[0],14)
