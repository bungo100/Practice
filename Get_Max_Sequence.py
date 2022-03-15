def get_max_min_sequence(numbers, operator=max):
    result_sequence, sum_sequence = 0,0
    for num in numbers:
        sum_sequence = operator(num, sum_sequence + num)
        result_sequence = operator(result_sequence, sum_sequence)
    return result_sequence

def find_max_circular_sequence(numbers):
    max_sequence = get_max_min_sequence(numbers)
    max_sequence_wrap = sum(numbers) - get_max_min_sequence(numbers, operator=min)
    return max(max_sequence, max_sequence_wrap)


if __name__ == "__main__":
    listA = [1,-2,3,6,-1,2,4,-5,2]
    listB = [2,1,-2,3,6,-1,2,4]
    print(get_max_min_sequence(listA))
    print(find_max_circular_sequence(listA))