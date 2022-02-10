from typing import List



def quick_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    i = -1
    j = 0
    for a in range(len_numbers):
        if numbers[a] < numbers[-1]:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
        j += 1
    return numbers







if __name__ == "__main__":
    import random
    num = [random.randint(0, 1000) for _ in range(10)]
    print(quick_sort(num))

