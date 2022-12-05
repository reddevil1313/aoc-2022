# Used Dequeues to have a FIFO structure 
from collections import deque

def create_stacks(lst, num):
    arr = [deque() for i in range(num)]

    for i in lst:
        for j, item in enumerate(i):
            if item != "":
                arr[j].append(item)
    
    return arr

def create_rows(lst):
    output = []
    count = 0
    for i in lst:
        if i != '':
            output.append(i[1])
        else:
            count+=1
        
        if count % 4 == 3:
            output.append("")
    return output

def part1():
    queues = []

    def update_stacks(amount, src, dst):
        for i in range(amount):
            queues[dst].appendleft(queues[src].popleft())
    
    with open('input.txt') as f:
        rows = []
        moving = False
        for line in f:
            if line.startswith(' 1'):
                queues = create_stacks(rows, len(rows[0]))
                moving = True
            elif line.startswith('move'):
                instruction = line.split()
                update_stacks(int(instruction[1]), int(instruction[3])-1, int(instruction[5])-1)
            elif not moving:
                crates = line.split(' ')
                rows.append(create_rows(crates))
    
    output = ""
    for i in queues:
        output += i[0]

    return output

def part2():
    queues = []

    def update_stacks(amount, src, dst):
        store = []
        for i in range(amount):
            store.append(queues[src].popleft())
        for i in reversed(store):
            queues[dst].appendleft(i)
    
    with open('input.txt') as f:
        rows = []
        moving = False
        for line in f:
            if line.startswith(' 1'):
                queues = create_stacks(rows, len(rows[0]))
                moving = True
            elif line.startswith('move'):
                instruction = line.split()
                update_stacks(int(instruction[1]), int(instruction[3])-1, int(instruction[5])-1)
            elif not moving:
                crates = line.split(' ')
                rows.append(create_rows(crates))
    
    output = ""
    for i in queues:
        output += i[0]

    return output

print("Part 1:", part1())
print("Part 2:", part2())