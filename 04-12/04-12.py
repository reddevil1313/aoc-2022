# Tried using range() but did not work

def part1():
    with open('input.txt') as f:
        sum = 0
        for line in f:
            
            first, second = line.split(',')[0], line.split(',')[1]
            first_start, first_end, second_start, second_end = int(first.split('-')[0]), int(first.split('-')[1]), int(second.split('-')[0]), int(second.split('-')[1])
            
            if (first_start <= second_start and first_end >= second_end) or (second_start <= first_start and second_end >= first_end):
                sum += 1
    return sum

def part2():
    with open('input.txt') as f:
        sum = 0
        for line in f:
            first, second = line.split(',')[0], line.split(',')[1]
            first_start, first_end, second_start, second_end = int(first.split('-')[0]), int(first.split('-')[1]), int(second.split('-')[0]), int(second.split('-')[1])
            
            if (first_start <= second_start and second_start <= first_end) or (first_start <= second_end and second_end <= first_end) or (second_start <= first_start and first_start <= second_end) or (second_start <= first_end and first_end <= second_end):
                sum += 1
    return sum

print("Part 1:", part1())
print("Part 2:", part2())