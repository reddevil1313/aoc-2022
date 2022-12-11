from collections import deque
import math

def LCMofArray(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//math.gcd(lcm, a[i])
  return lcm

def create_monkeys():
    curr_index = -1
    items = []
    operations = {}
    rules = []
    truth = {}
    outputs = {}

    with open('input.txt') as f:
        for line in f:
            clean = line.strip().split()
            if not clean == []:
                if clean[0] == "Monkey":
                    curr_index +=1
                elif clean[0] == "Starting":
                    new_q = deque()
                    for i in range(2,len(clean)):
                        num = clean[i].split(',')
                        new_q.append(int(num[0]))
                    items.append(new_q)
                elif clean[0] == "Operation:":
                    operator = clean[4]
                    num = clean[5]
                    if operator == "*":
                        if clean[5] == "old":
                            operations[curr_index] = (lambda x: x*x)
                        else:
                            val = int(num)
                            operations[curr_index] = (lambda x, val=val: x*val)
                    elif operator == "+":
                        if clean[5] == "old":
                            operations[curr_index] = (lambda x: x+x)
                        else:
                            val = int(num)
                            operations[curr_index] = (lambda x, val=val: x+val)
                elif clean[0] == "Test:":
                    divisor = clean[3]
                    rules.append(int(divisor))
                elif clean[1] == "true:":
                    mky = clean[5]
                    truth[curr_index] = int(mky)
                elif clean[1] == "false:":
                    val1 = truth[curr_index]
                    val2 = rules[curr_index]
                    val3 = int(clean[5])
                    outputs[curr_index] = (lambda x, val1=val1, val2=val2, val3=val3: val1 if x % val2 == 0 else val3)
    
    return items, operations, outputs, LCMofArray(rules)


def part1():

    items, operations, div, lcm = create_monkeys()
    total = [0 for i in range(len(items))]
    
    for i in range(20):
        for j in range(len(items)):
            total[j] += len(items[j])
            while items[j]:
                item = items[j].popleft()
                worry = math.floor(operations[j](item)/3)
                monkey = div[j](worry)
                items[monkey].append(worry)

    total.sort(reverse=True)
    return total[0]*total[1]

def part2():
    items, operations, div, lcm = create_monkeys()
    total = [0 for i in range(len(items))]
    
    for i in range(10000):
        for j in range(len(items)):
            total[j] += len(items[j])
            while items[j]:
                item = items[j].popleft()
                worry = math.floor(operations[j](item)%lcm)
                monkey = div[j](worry)
                items[monkey].append(worry)

    total.sort(reverse=True)
    return total[0]*total[1]


print("Part 1:", part1())
print("Part 2:", part2())