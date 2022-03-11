from functools import lru_cache

# @lru_cache()
# def long_func(num):
#     r = 0
#     for i in range(10000000):
#         r += num * i
#
#     return r

def deco(func):
    cache = {}
    def wrapper(num):
        if num not in cache:
            cache[num] = func(num)
        return cache[num]
    return wrapper


@deco
def long_func(num):
    r = 0
    for i in range(10000000):
        r += num * i
    return r



if __name__ == "__main__":
    for i in range(5):
        print(long_func(i))

    for i in range(5):
        print(long_func(i))