# l = [1,2,3]
# print(int(''.join([str(i) for i in l])) + 1 )

def list_to_int(numbers):
    sum_numbers = 0
    for i, num in enumerate(reversed(numbers)):
        sum_numbers += num * (10**i)
    return sum_numbers


def remove_zero(numbers):
    if numbers[0] == 0:
        numbers.pop(0)
        remove_zero(numbers)

def list_to_int_plusone(numbers):
    i = len(numbers) - 1
    numbers[i] += 1
    while 0 < i:
        if numbers[i] != 10:
            remove_zero(numbers)
            break
        else:
            numbers[i] = 0
            numbers[i-1] += 1
        i -= 1
    else:
        if numbers[0] == 10:
            numbers[0] = 1
            numbers.append(0)

    return list_to_int(numbers)

if __name__ == "__main__":

    print(list_to_int_plusone([0,0,8,6,9,9]))