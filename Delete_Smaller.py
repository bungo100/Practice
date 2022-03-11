from collections import Counter

def min_count_remove(x,y):
    # count_x = {}
    # count_y = {}
    # for i in x:
    #     count_x[i] = count_x.get(i, 0) + 1
    # for ii in y:
    #     count_y[ii] = count_y.get(ii, 0) + 1
    #

    count_x = Counter(x)
    count_y = Counter(y)

    for key_x, value_x in count_x.items():
        value_y = count_y.get(key_x)
        if value_y:
            if value_x < value_y:
                x[:] = [i for i in count_x if i != key_x]
            elif value_x > value_y:
                y[:] = [i for i in count_y if i != key_x]





if __name__ == "__main__":
    x = [1,2,3,4,4,5,5,8,10]
    y = [4,5,5,5,6,7,8,8,10]
    print('x = ', x)
    print('y = ', y)
    min_count_remove(x,y)
    print('x = ', x)
    print('y = ', y)