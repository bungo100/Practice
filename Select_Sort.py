from typing import List

def select_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_ind = i
        for j in range(i+1, len_numbers):
            if numbers[min_ind] > numbers[j]:
                min_ind = j
        numbers[i],numbers[min_ind] = numbers[min_ind], numbers[i]
    return numbers

if __name__ == "__main__":
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(select_sort(nums))