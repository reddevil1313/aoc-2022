def part1():
    with open('input.txt') as f:
        # Attempt using pointers and dictionary
        output = 0
        store = {}
        left_ptr = 0
        right_ptr = 0
        for line in f:
            input = [*line]
            for idx, i in enumerate(input):
                if i in store:
                    left_ptr = max(store[i] + 1, left_ptr)
                store[i]= idx

                if right_ptr - left_ptr >= 3:
                    output = right_ptr + 1
                    break
                right_ptr += 1
                    
    return output

def part2():
    with open('input.txt') as f:
        # Attempt using pointers and dictionary
        output = 0
        store = {}
        left_ptr = 0
        right_ptr = 0
        for line in f:
            input = [*line]
            for idx, i in enumerate(input):
                if i in store:
                    left_ptr = max(store[i] + 1, left_ptr)
                store[i]= idx

                if right_ptr - left_ptr >= 13:
                    output = right_ptr + 1
                    break
                right_ptr += 1
                    
    return output


print("Part 1:", part1())
print("Part 2:", part2())