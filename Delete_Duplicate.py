l = [1,3,3,5,5,7,7,7,10,12,12,15]
# ll = set(l)
# lll = list(ll)
# print(list(dict.fromkeys(l)))
# print([n for i, n in enumerate(l) if n not in l[:i]])

def delete_duplicate_v1(numbers):
    tmp = []
    for i in numbers:
        if i not in tmp:
            tmp.append(i)
    numbers[:] = tmp

def delete_duplicate_v2(numbers):
    i = len(numbers)-1
    while i > 0:
        if numbers[i] == numbers[i-1]:
            numbers.pop(i)
        i -= 1


if __name__ == "__main__":
    l = [1,3,3,5,5,7,7,7,10,12,12,15]
    delete_duplicate_v2(l)
    print(l)