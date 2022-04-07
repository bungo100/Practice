def fermat_last_theorem_v1(max_num, square_num):
    result = []
    if square_num < 2:
        return result

    z_max = int(pow(pow(max_num - 1, square_num) + pow(max_num, square_num), 1/square_num))
    for x in range(1, max_num+1):
        for y in range(x+1, max_num+1):
            for z in range(y+1,z_max):
                if pow(x, square_num) + pow(y, square_num) == pow(z, square_num):
                    result.append((x,y,z))

    return result

if __name__ == "__main__":
    print('v', fermat_last_theorem_v1(10,2))