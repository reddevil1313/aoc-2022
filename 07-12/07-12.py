class Node:
    def __init__(self, val, parent=None):
        self.val = val
        self.parent = parent
        self.sum = 0


def part1():
    with open('input.txt') as f:
        current_node = Node(None)
        total = 0
        for line in f:
            command = line.split(" ")
            if command[0] == "$":
                if command[1] == "cd":
                    if command[2] != "..\n":
                        temp = current_node
                        current_node = Node(command[2], temp)
                    else:
                        if current_node.sum <= 100000:
                            total += current_node.sum
                        current_node.parent.sum += current_node.sum
                        current_node = current_node.parent

            elif command[0] != "dir":
                size = int(command[0])
                current_node.sum += size
                    
    return total

def part2():
    with open('input.txt') as f:
        root = Node("/\n", None)
        current_node = root
        store = []
        for line in f:
            command = line.split(" ")
            if command[0] == "$":
                if command[1] == "cd":
                    if command[2] == "/\n":
                        current_node = root
                    elif command[2] != "..\n":
                        temp = current_node
                        current_node = Node(command[2], temp)
                    else:
                        current_node.parent.sum += current_node.sum
                        store.append(current_node.sum)
                        current_node = current_node.parent

            elif command[0] != "dir":
                size = int(command[0])
                current_node.sum += size

        while current_node.parent is not None:
            current_node.parent.sum += current_node.sum
            current_node = current_node.parent
        
        minimum = min(i for i in store if i >= (root.sum - 40000000))
                    
    return minimum


print("Part 1:", part1())
print("Part 2:", part2())