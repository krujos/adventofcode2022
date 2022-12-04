import functools
import operator


def find_common_items(bags_to_search):
    return set(set(bags_to_search[0]) & set(bags_to_search[1]) & set(bags_to_search[2])).pop()


def find_duplicate_items(bag):
    size = len(bag)
    half = int(size/2)
    return set(set(bag[0:half]) & set(bag[half:size])).pop()


def get_item_priority(item):
    ordinal = ord(item)

    if item.islower():
        return ordinal - 96

    if item.isupper():
        return ordinal - 38

    exit(1)


if __name__ == '__main__':
    dups = []
    with open('input_day3.txt') as f:
        bags = f.read().splitlines()
    f.close()

    [dups.append(find_duplicate_items(bag)) for bag in bags]
    sum_of_priority = functools.reduce(operator.add, map(get_item_priority, dups))
    print(sum_of_priority)

    badge_priorities = []
    for n in range(0, len(bags), 3):
        badge_priorities.append(get_item_priority(find_common_items([bags[n], bags[n+1], bags[n+2]])))

    sum_of_badge_priority = functools.reduce(operator.add, badge_priorities)
    print(sum_of_badge_priority)
