def order_change_by_index_v1(wording, index):
    tmp = [None]*len(wording)
    for i, v in enumerate(index):
        tmp[v] = wording[i]
    return ''.join(tmp)

def order_change_by_index_v2(wording, index):
    i, len_index = 0, len(index)-1
    while i < len_index:
        while i != index[i]:
            ind = index[i]
            wording[ind], wording[i] = wording[i], wording[ind]
            index[ind], index[i] = index[i], index[ind]
        i += 1
    return ''.join(wording)



if __name__ == "__main__":
    w = ["h","y","n","p","t","o"]
    i = [3,1,5,0,2,4]
    print(order_change_by_index_v2(w,i))