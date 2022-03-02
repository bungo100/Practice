def linear_search(numbers, value):
    for i in range(len(numbers)):
        if numbers[i] == value:
            return i
    return "Not found!"

def binary_search(numbers, value):
    left, right = 0, len(numbers)-1
    while left < right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return "Not found!"


def binary_search_recursive(numbers, value):
    def _binary_search_recursive(numbers, value, left, right):
        if left > right:
            return "Not found!"

        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_search_recursive(numbers, value, mid+1, right)
        else:
            return _binary_search_recursive(numbers, value, left, mid-1)

    return _binary_search_recursive(numbers, value, 0, len(numbers)-1)


if __name__ == "__main__":
    num = [0,1,5,7,9,11,15,20,24]
    print(binary_search_recursive(num, 15))