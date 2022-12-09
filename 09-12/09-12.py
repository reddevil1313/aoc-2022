def part1():
    store = {}
    store[(0,0)] = 1
    H_x = 0
    H_y = 0
    T_x = 0
    T_y = 0

    with open('input.txt') as f:
        for line in f:
            command = line.strip().split()
            dir, num = command[0], command[1]

            for i in range(1, int(num)+1):

                # Move Head
                if dir == 'U':
                    H_y += 1
                elif dir == 'D':
                    H_y -= 1
                elif dir == 'L':
                    H_x -= 1
                elif dir == 'R':
                    H_x += 1

                # Move Tail
                if not (abs(H_x - T_x) <= 1 and abs(H_y - T_y) <= 1):
                    if H_x == T_x:
                        if H_y > T_y:
                            T_y += 1
                        else:
                            T_y -= 1
                    elif H_y == T_y:
                        if H_x > T_x:
                            T_x += 1
                        else:
                            T_x -= 1
                    else:
                        if H_y > T_y and H_x > T_x:
                            T_y += 1
                            T_x += 1
                        elif H_y > T_y and H_x < T_x:
                            T_y += 1
                            T_x -= 1
                        elif H_y < T_y and H_x < T_x:
                            T_y -= 1
                            T_x -= 1
                        elif H_y < T_y and H_x > T_x:
                            T_y -= 1
                            T_x += 1
                
                store[(T_x, T_y)] = 1

    total = len(store)
    return total

def part2():
    store = {}
    store[(0,0)] = 1
    rope = [[0,0] for i in range(10)]

    with open('input.txt') as f:
        for line in f:
            command = line.strip().split()
            dir, num = command[0], command[1]

            for i in range(1, int(num)+1):

                # Move Head
                if dir == 'U':
                    rope[0][1] += 1
                elif dir == 'D':
                    rope[0][1] -= 1
                elif dir == 'L':
                    rope[0][0] -= 1
                elif dir == 'R':
                    rope[0][0] += 1

                for i in range(1,10):

                    # Move Each
                    if not (abs(rope[i-1][0] - rope[i][0]) <= 1 and abs(rope[i-1][1] - rope[i][1]) <= 1):
                        print("Hi")
                        if rope[i-1][0] == rope[i][0]:
                            if rope[i-1][1] > rope[i][1]:
                                rope[i][1] += 1
                            else:
                                rope[i][1] -= 1
                        elif rope[i-1][1] == rope[i][1]:
                            if rope[i-1][0] > rope[i][0]:
                                rope[i][0] += 1
                            else:
                                rope[i][0] -= 1
                        else:
                            if rope[i-1][1] > rope[i][1] and rope[i-1][0] > rope[i][0]:
                                rope[i][1] += 1
                                rope[i][0] += 1
                            elif rope[i-1][1] > rope[i][1] and rope[i-1][0] < rope[i][0]:
                                rope[i][1] += 1
                                rope[i][0] -= 1
                            elif rope[i-1][1] < rope[i][1] and rope[i-1][0] < rope[i][0]:
                                rope[i][1] -= 1
                                rope[i][0] -= 1
                            elif rope[i-1][1] < rope[i][1] and rope[i-1][0] > rope[i][0]:
                                rope[i][1] -= 1
                                rope[i][0] += 1
                
                store[(rope[9][0], rope[9][1])] = 1

    total = len(store)
    return total
         


print("Part 1:", part1())
print("Part 2:", part2())