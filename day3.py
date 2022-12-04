import functools
import operator


def find_common_items(bags):
    return set(set(bags[0]) & set(bags[1]) & set(bags[2])).pop()


def find_duplicate_items(bag):
    size = len(bag)
    half = int(size/2)
    return set(set(bag[0:half]) & set(bag[half:size])).pop()


def get_item_priority(item):
    ordinal = ord(item)
    if ordinal >= 97:
        return ordinal - 96

    if ordinal >= 65:
        return ordinal - 38

    exit(1)


if __name__ == '__main__':
    dups = []
    with open('input_day3.txt') as f:
        bags = f.readlines()
    f.close()

    #get the sum of the bag priority
    [dups.append(find_duplicate_items(bag.strip())) for bag in bags]
    sum_of_priority = functools.reduce(operator.add, map(get_item_priority, dups))
    print(sum_of_priority)

    bps = []
    for n in range(0, len(bags), 3):
        b = bags[n].strip(), bags[n+1].strip(), bags[n+2].strip()
        bps.append(get_item_priority(find_common_items(b)))

    sum_of_bage_priority = functools.reduce(operator.add, bps)
    print(sum_of_bage_priority)
