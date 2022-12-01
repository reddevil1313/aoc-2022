

def part1():
    val = 0
    with open('input.txt') as f:
        sum = 0
        for line in f:
            if len(line.strip()) == 0 :
                val = max(sum,val)
                sum = 0
            else:
                sum += int(line)
    return val

def part2():
    val1 = 0
    val2 = 0
    val3 = 0
    with open('input.txt') as f:
        sum = 0
        for line in f:
            if len(line.strip()) == 0 :
                if sum >= val1:
                    val3 = val2
                    val2 = val1
                    val1 = sum
                elif sum >= val2:
                    val3 = val2
                    val2 = sum
                elif sum >= val3:
                    val3 = sum
                sum = 0
            else:
                sum += int(line)
    return val1 + val2 + val3

print("Part 1:", part1())
print("Part 2:", part2())