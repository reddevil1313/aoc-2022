def create_matrix():
    matrix = []
    with open('input.txt') as f:
        for line in f:
            matrix.append(list(line.strip()))
    
    return matrix

def part1():
    matrix  = create_matrix()
    visible = [x[:] for x in matrix]

    for idx, itemx in enumerate(matrix):
        left_min = -1
        right_min = -1
        for idy, itemy in enumerate(itemx):
            if int(itemy) > left_min:
                left_min = int(itemy)
                visible[idx][idy] =  'X'
        
        for idy, itemy in reversed(list(enumerate(itemx))):
            if int(itemy) > right_min:
                right_min = int(itemy)
                visible[idx][idy] =  'X'
    
    transposed = list(zip(*matrix))

    for idx, itemx in enumerate(transposed):
        left_min = -1
        right_min = -1
        for idy, itemy in enumerate(itemx):
            
            if int(itemy) > left_min:
                left_min = int(itemy)
                visible[idy][idx] =  'X'
        
        for idy, itemy in reversed(list(enumerate(itemx))):
            if int(itemy) > right_min:
                right_min = int(itemy)
                visible[idy][idx] =  'X'
        
    total = 0
    for i in visible:
        for j in i:
            if j == 'X':
                total += 1
                    
    return total

def part2():
    matrix  = create_matrix()
    output = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            val = matrix[i][j]
            score = 1

            # Left Score
            for x in range(1,j+1):
                if matrix[i][j-x] >= val:
                    score = x
                    break

                if x == j:
                    score = x

            # Right Score
            for x in range(1, len(matrix[0])-j):
                if matrix[i][j + x] >= val:
                    score *= x
                    break
                
                if x == len(matrix[0])-j-1:
                    score *= x

            # Top Score
            for x in range(1, i+1):
                if matrix[i - x][j] >= val:
                    score *= x
                    break

                if x == i:
                    score *= x
           
            # Bottom Score
            for x in range(1, len(matrix[0])-i):
                if matrix[i + x][j] >= val:
                    score *= x
                    break

                if x == len(matrix[0])-i-1:
                    score *= x

            output = max(output, score)
                    
    return output
         


print("Part 1:", part1())
print("Part 2:", part2())