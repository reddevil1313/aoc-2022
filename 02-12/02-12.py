# There should be a better way than to just store the values in a matrix

def part1():
    dic = {
        "A": 0,
        "B": 1,
        "C": 2,
        "X": 0,
        "Y": 1,
        "Z": 2
    }

    outcomes = [[3,6,0],[0,3,6],[6,0,3]]
    with open('input.txt') as f:
        sum = 0
        for line in f:
            opp, player = line.split()
            out = outcomes[dic[opp]][dic[player]] + dic[player] + 1
            sum += out
    return sum

def part2():
    dic = {
        "A": 0,
        "B": 1,
        "C": 2,
        "X": 0,
        "Y": 1,
        "Z": 2
    }

    # Change the Outcomes for this Part
    outcomes = [[3,4,8],[1,5,9],[2,6,7]]
    with open('input.txt') as f:
        sum = 0
        for line in f:
            opp, player = line.split()
            out = outcomes[dic[opp]][dic[player]]
            sum += out
    return sum

print("Part 1:", part1())
print("Part 2:", part2())