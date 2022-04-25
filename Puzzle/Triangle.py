import random

def generate_numbers(depth, max_num):
    return [[random.randint(0, max_num) for _ in range(i)] for i in range(1, depth+1)]

def generate_triangle(data):
    max_digit = len(str(max([max(i) for i in data])))
    width = max_digit + (max_digit % 2) + 2
    for index, lines in enumerate(data):
        numbers = "".join([str(i).center(width, ' ') for i in lines])
        print(" " * int(width/2) * (len(data) - index), numbers)

def sum_min_path(triangle):
    tree = triangle[:]
    j, len_triangle = 1, len(triangle)
    if not len_triangle:
        return

    while j < len_triangle:
        line = triangle[j]
        line_path_sum = []
        for i, value in enumerate(line):
            if i == 0:
                sum_value = line[i] + tree[j-1][0]
            elif i == len(line) - 1:
                sum_value = line[i] + tree[j-1][i-1]
            else:
                min_value = min(tree[j-1][i-1], tree[j-1][i])
                sum_value = line[i] + min_value
            line_path_sum.append(sum_value)
        tree[j] = line_path_sum
        j += 1

    return min(tree[-1])




if __name__ == "__main__":
    data = generate_numbers(5,9)

    generate_triangle(data)
    print(sum_min_path(data))
