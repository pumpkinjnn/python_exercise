def trim(str):
    ret = str
    while (ret != '')and(ret[0] == ' '):
        ret = ret[1:]
    while (ret != '')and(ret[-1] == ' '):
        ret = ret[:-1]
    return ret
