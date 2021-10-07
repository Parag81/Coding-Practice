def count(arr):
    d = {}
    for ele in arr:
        if ele not in d:
            d[ele] = 1
        else:
            return ele
    return -1