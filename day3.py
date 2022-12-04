import functools
import operator


def find_common_items(bags_to_search):
    return set(set(bags_to_search[0]) & set(bags_to_search[1]) & set(bags_to_search[2])).pop()


def find_duplicate_items(bag):
    size = len(bag)
    half = int(size/2)
    return set(set(bag[0:half]) & set(bag[half:size])).pop()


def get_item_priority(item):
    return ord(item) - 96 if item.islower() else ord(item) - 38


if __name__ == '__main__':
    with open('input_day3.txt') as f:
        bags = f.read().splitlines()
    f.close()

    print(sum(map(get_item_priority, list(map(find_duplicate_items, bags)))))

    badge_priorities = []
    for n in range(0, len(bags), 3):
        badge_priorities.append(get_item_priority(find_common_items([bags[n], bags[n+1], bags[n+2]])))

    print(sum(badge_priorities))
