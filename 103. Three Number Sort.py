def threeNumberSort(array, order):
    if len(array) <= 1:
        return array
    d = {}
    for ele in array:
        if ele not in d:
            d[ele] = 1
        else:
            d[ele] += 1
    i = 0
    for e in order:
        if e not in d:
            continue
        j = d[e]
        while i < len(array) and j > 0:
            array[i] = e
            j -= 1
            i += 1
    return array