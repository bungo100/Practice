def factorial(num):

    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

def fibonacci_recursive(num):
    if num < 2:
        return num
    else:
        return fibonacci_recursive(num-2) + fibonacci_recursive(num-1)

def plus(num):
    if num < 1:
        return 0
    return num + plus(num-1)

def double_list(lst):
    if lst == []:
        return []
    first = lst[0]
    rest = lst[1:]
    return [first*2] + double_list(rest)



if __name__ == "__main__":
    # print(factorial(4))
    # print(fibonacci_recursive(6))
    # print(plus(19))
    # print(double_list([1,2,3]))