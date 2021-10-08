def winner(array, point):
    d = {}
    for i in range(len(array)):
        if point[i] == 1:
            val = array[i][0]
            if val not in d:
                d[val] = 3
            else:
                d[val] += 3
        else:
            val = array[i][1]
            if val not in d:
                d[val] = 3
            else:
                d[val] += 3
    name, p = "", -1
    for ele in d:
        if d[ele] > p:
            name = ele
            p = d[ele]
    return nam