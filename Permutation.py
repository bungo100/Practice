# from itertools import permutations
# for i in permutations([1,2,3]):
#     print(i)

def all_perms(elements):
    result = []

    if len(elements) <= 1:
        return [elements]

    for perm in all_perms(elements[1:]):
        for i in range(len(elements)):
            result.append((perm[:i] + elements[0:1] + perm[i:]))

    return result


def all_perms2(elements):
    if len(elements) <= 1:
        yield elements

    else:
        for perm in all_perms2(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


if __name__ == "__main__":
    for i in all_perms2([1,2,3]):
        print(i)


