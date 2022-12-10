def part1():
    count = 1
    cycle = 0
    total = 0

    with open('input.txt') as f:
        for line in f:
            arr = [20,60,100,140,180,220]
            

            if line.startswith("noop"):
                cycle += 1
                if cycle in arr:
                    print(cycle, count)
                    total += cycle*count
            else:
                command = line.strip().split()
                num = int(command[1])
                for i in range(2):
                    cycle += 1
                    if cycle in arr:
                        print(cycle, count)
                        total += cycle*count
                count += num

    return total

def part2():
    position = 1
    cycle = 0

    with open('input.txt') as f:
        for line in f:
            if line.startswith("noop"):
                if cycle == 40:
                    cycle -= 40
                    print("\n")
                if abs(position-cycle) <= 1:
                    print("#", end="")
                else:
                    print(" ", end="")
                cycle += 1
            else:
                command = line.strip().split()
                num = int(command[1])
                for i in range(2):
                    if cycle == 40:
                        cycle -= 40
                        print("\n")
                    if abs(position-cycle) <= 1:
                        print("#", end="")
                    else:
                        print(" ", end="")
                    cycle += 1
                position += num

    return True


print("Part 1:", part1())
part2()