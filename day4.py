import functools
import operator


def has_full_overlap(elf1, elf2):
    print(elf1)
    print(elf2)
    if set(elf1).issubset(set(elf2)) or set(elf1).issuperset(set(elf2)):
        return True
    return False


def make_elf(proposed_elf):
    t = proposed_elf.split("-")
    if int(t[0]) == int(t[1]):
        return [int(t[0])]
    r = range(int(t[0]), int(t[1]))
    return [*r, int(t[1])]


if __name__ == '__main__':
    with open('input_day4.txt') as f:
        pairs = f.read().splitlines()
    f.close()
    overlaps = 0

    # e1, e2 = "1 - 81, 82 - 82".split(",")
    # print(has_full_overlap(make_elf(e1), make_elf(e2)))
    #
    # e1, e2 = "17 - 97, 96 - 97".split(",")
    # print(has_full_overlap(make_elf(e1), make_elf(e2)))
    #
    # e1, e2 = "5 - 7, 6 - 79".split(",")
    # print(has_full_overlap(make_elf(e1), make_elf(e2)))
    #
    # e1, e2 = "5 - 7, 5 - 7".split(",")
    # print(has_full_overlap(make_elf(e1), make_elf(e2)))
    #
    #
    for pair in pairs:
        e1, e2 = pair.split(",")
        elf1 = make_elf(e1)
        elf2 = make_elf(e2)
        if has_full_overlap(elf1, elf2):
            overlaps += 1

    print(overlaps)
