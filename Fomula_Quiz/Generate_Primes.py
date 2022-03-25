def generate_primes_v1(number):
    prime = []

    for x in range(2, number+1):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            prime.append(x)


    return prime

def generate_primes_v2(number):
    prime = []
    cache = {}
    i = 0
    for x in range(2, number+1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue
        prime.append(x)
        for y in range(x*2, number+1, x):
            cache[y] = False
            i += 1
    print(f'This is v2 = {i}')
    print(prime)

def generate_primes_v3(number):
    cache = {}
    for x in range(2, number+1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue
        yield x
        for y in range(x*2, number+1, x):
            cache[y] = False


if __name__ == "__main__":
    import time
    start = time.time()
    print(generate_primes_v1(50))
    finish = time.time()
    print(f'It took {finish-start}')

    start = time.time()
    generate_primes_v2(50)
    print(time.time()-start)

    start = time.time()
    print([i for i in generate_primes_v3(50)])
    print(time.time()-start)


