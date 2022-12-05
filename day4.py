def has_any_overlap(elf1, elf2):
    if set(elf1) & set(elf2):
        return True
    return False


def has_full_overlap(elf1, elf2):
    if set(elf1).issubset(set(elf2)) or set(elf1).issuperset(set(elf2)):
        return True
    return False


def make_elf(proposed_elf):
    start, end = map(eval, proposed_elf.split("-"))
    return [start] if start == end else [*range(start, end), end]


if __name__ == '__main__':
    with open('input_day4.txt') as f:
        pairs = f.read().splitlines()
    f.close()
    any_overlaps = 0
    full_overlaps = 0

    for pair in pairs:
        elf1, elf2 = map(make_elf, pair.split(","))
        if has_full_overlap(elf1, elf2):
            full_overlaps += 1
        if has_any_overlap(elf1, elf2):
            any_overlaps += 1

    print("Full overlap = ",  full_overlaps)
    print("Partial overlap = ", any_overlaps)
