

if __name__ == '__main__':
    elf = 0
    calories = [0]

    with open('input_day1.txt') as f:
        lines = f.readlines()
    f.close()

    for line in lines:
        if "\n" != line:
            calories[elf] += int(line)
        else:
            elf += 1
            calories.append(0)

    calories.sort(reverse=True)
    print(sum(calories[0:3]))
