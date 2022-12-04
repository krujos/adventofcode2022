import functools
import operator


def find_duplicate_items(bag):
    size = len(bag)
    half = int(size/2)
    return set(set(bag[0:half]) & set(bag[half:size])).pop()


def get_item_priortiy(item):
    ascii =  ord(item)
    if ascii >= 97:
        return ascii - 96

    if ascii >= 65:
        return ascii - 38

    exit(1)


if __name__ == '__main__':
    dups = []
    with open('input_day3.txt') as f:
        bags = f.readlines()
    f.close()

    [dups.append(find_duplicate_items(bag.strip())) for bag in bags]
    sum_of_priority = functools.reduce(operator.add, map(get_item_priortiy, dups))
    print(sum_of_priority)
