# Second Part required manual storing of lines in variables, there must be a way of readin lines in batches

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
        line1 = ""
        line2 = ""
        line3 = ""
        for line in f:
            if count % 3 == 0:
                line1 = line.strip()
            elif count % 3 == 1:
                line2 = line.strip()
            elif count % 3 == 2:
                line3 = line.strip()
                common_charac = ''.join(set(line1).intersection(line2).intersection(line3))
                if ord(common_charac) > 96:
                    sum += ord(common_charac) - 96
                else:
                    sum += ord(common_charac) - 64 + 26
            count += 1
    return sum

print("Part 1:", part1())
print("Part 2:", part2())