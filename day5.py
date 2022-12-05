def make_containers(lines):
    ctr = [[],[],[],[],[],[],[],[],[]]
    for l in reversed(lines):
        arr = [v for i, v in enumerate(list(l)) if i % 2 != 0]
        arr = [v for i, v in enumerate(list(arr)) if i % 2 == 0]
        for i,v in enumerate(list(arr)):
            if v == " ":
                continue
            ctr[i].append(v)

    return ctr

if __name__ == '__main__':
    with open('input_day5.txt') as f:
        input_lines = f.read().splitlines()
    f.close()

    containers = make_containers(input_lines[0:8])

    for line in input_lines[10:]:
        instruction = line.split()
        num = int(instruction[1])
        f = int(instruction[3])-1
        t = int(instruction[5])-1
        length = len(containers[f])

        for i, v in enumerate(containers[f][length-num:length]):
            containers[t].append(v)
        containers[f] = containers[f][0:length-num]

    for r in containers:
        print(r)