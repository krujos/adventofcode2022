import functools
import operator


def has_any_overlap(elf1, elf2):
    if set(elf1) & set(elf2):
        return True
    return False

def has_full_overlap(elf1, elf2):
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
    full_overlaps = 0
    any_overlaps = 0

    for pair in pairs:
        e1, e2 = pair.split(",")
        elf1 = make_elf(e1)
        elf2 = make_elf(e2)
        if has_full_overlap(elf1, elf2):
            full_overlaps += 1
        if has_any_overlap(elf1, elf2):
            any_overlaps += 1

    print("Full overlap = ",  full_overlaps)
