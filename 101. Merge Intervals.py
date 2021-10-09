def merge(interval):
    i, j = 0, 1
    while j < len(interval):
        if interval[i][1] >= interval[j][0]:
            a = [interval[i][0], interval[j][1]]
            del(interval[i:j+1])
            interval.insert(i, a)
        else:
            i += 1
            j += 1
    return interval