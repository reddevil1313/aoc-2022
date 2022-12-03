# Batch reading using itertools
from itertools import islice

def part1():
    with open('input.txt') as f:
        sum = 0
        for line in f:
            firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
            common_charac = ''.join(set(firstpart).intersection(secondpart))
            if ord(common_charac) > 96:
                sum += ord(common_charac) - 96
            else:
                sum += ord(common_charac) - 64 + 26
    return sum

def part2():
    with open('input.txt') as f:
        sum = 0
        count = 0
        for n_lines in iter(lambda: tuple(islice(f, 3)), ()):
            common_charac = ''.join(set(n_lines[0].strip()).intersection(n_lines[1].strip()).intersection(n_lines[2].strip()))
            if ord(common_charac) > 96:
                sum += ord(common_charac) - 96
            else:
                sum += ord(common_charac) - 64 + 26
            count += 1
    return sum

print("Part 1:", part1())
print("Part 2:", part2())
