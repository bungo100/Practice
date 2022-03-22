def order_even_first_odd_last(numbers):
    even = []
    odd = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    numbers[:] = even + odd

def order_even_first_odd_last2(numbers):
    i, j = 0, len(numbers)-1
    while i < j:
        if numbers[i] % 2 == 0:
            i += 1
        else:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j -= 1

        # print(numbers)


if __name__ == "__main__":
    l = [0,1,3,4,2,4,5,1,6,9,8]
    order_even_first_odd_last2(l)
    print(l)
