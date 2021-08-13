import sys, os
import itertools


def yValue(a, b):
    if b == None:
        return
    if b == ():
        return
    if type(b) == tuple:
        b= b[0]
    vlist = set()
    vlist.add((a + b))
    vlist.add((a - b))
    vlist.add((a * b))
    vlist.add((b - a))
    if b != 0:
        vlist.add(a / b)
    if a != 0:
        vlist.add(b / a)
    for i in vlist:
        yield i


def getCb(ll):
    cz = len(ll) - 1
    if cz == 0:
        return
    res = itertools.combinations(ll, cz)
    res1 = [i for i in res]
    tmp = ll
    tmp.reverse()
    res2 = itertools.combinations(tmp, 1)
    res3 = [i for i in res2]
    for k, v in enumerate(res1):
        yield (v, res3[k])

def yieldValues(ll ):
    if len(ll) == 1:
        yield ll[0]
    if len(ll) == 2:
        for i in yValue(ll[0], ll[1]):
            yield i
    for tt in getCb(ll):
        for j in yieldValues(list(tt[0])):
            for k in yValue(j, tt[1]):
                yield k

def isOK(ll, target):
    for i in yieldValues(ll):
        if i == target:
            return True
    return False

if __name__ == '__main__':
    pass
    ll = [3,3,7,7]
    print(isOK(ll,24))
