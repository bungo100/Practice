

def find_pair(taple_list):
    cache = {}
    for pair in taple_list:
        first, second = pair
        value = cache.get(second)
        if not value:
            cache[first] = second
        elif first == value:
            yield pair


if __name__ == "__main__":
    l = [(1,2), (3,5), (4,7), (5,3), (7,4)]
    for i in find_pair(l):
        print(i)


