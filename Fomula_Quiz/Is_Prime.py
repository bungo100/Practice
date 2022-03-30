import math

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def is_prime_v2(num):
    if num <= 1:
        return False

    for i in range(2, math.floor(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def is_prime_v3(num):
    if num <= 1:
        return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def is_prime_v4(num):
    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, math.floor(math.sqrt(num)+1), 2):
        if num % i == 0:
            return False


    # i = 3
    # while i * i <= num:
    #     if num % i == 0:
    #         return False
    #     i += 2
    return True

def is_prime_v5(num):
    if num <= 1:
        return False

    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    # for i in range(5, math.floor(math.sqrt(num)+1), 6):
    #     if num % i == 0 or num % (i+2):
    #         return False


    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    # print(is_prime(5))[i for in in range(math.floor(math.sqrt(37))+1)]
    # print([i for i in range(2, math.floor(math.sqrt(37)) + 1)])
    import time
    import random
    number = [random.randint(1, 100) for i in range(100000)]

    start = time.time()
    for num in number:
        is_prime(num)
    print(f'v1 took {time.time() - start}')

    start = time.time()
    for num in number:
        is_prime_v2(num)
    print(f'v2 took {time.time() - start}')

    start = time.time()
    for num in number:
        is_prime_v4(num)
    print(f'v4 took {time.time() - start}')

    start = time.time()
    for num in number:
        is_prime_v5(num)
    print(f'v5 took {time.time() - start}')
