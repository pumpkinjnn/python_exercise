def tri(line):
    prev = []
    count = 0
    while count < line:
        ret = []
        for x in range(count+1):
            if (x == 0) or (x == count):
                ret.append(1)
            else:
                ret.append(prev[x]+prev[x-1])
        count = count + 1
        prev = ret
        yield ret
