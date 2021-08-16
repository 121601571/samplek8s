import itertools


class valStruct:
    def __init__(self, value, valueL, valueR, operator):
        self.value = value
        self.valueL = valueL
        self.operator = operator
        self.valueR = valueR

    def __repr__(self):
        return str(self.value) + '->' + str(self.valueL) + '->' +str(self.operator) + '->' +str(self.valueR)

    def __str__(self):
        return self.__repr__()


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


def yValueStruct(a: valStruct, b: valStruct):
    vlist = set()
    if type(b) == tuple:
        b = b[0]
    vlist.add(valStruct(value=a.value + b.value, valueL= a, valueR=b, operator='+' ))
    vlist.add(valStruct(value=a.value - b.value, valueL=a, valueR=b, operator='-'))
    vlist.add(valStruct(value=a.value * b.value, valueL= a, valueR=b, operator='*' ))
    vlist.add(valStruct(value=b.value - a.value, valueL= b, valueR=a, operator='-' ))

    if b.value != 0:
        vlist.add(valStruct(value=a.value / b.value, valueL=a, valueR=b, operator='/'))

    if a.value != 0:
        vlist.add(valStruct(value=b.value / a.value, valueL=b, valueR=a, operator='/'))

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
        yield v, res3[k]


def yieldValues(ll):
    #ll list of vStruct.
    if len(ll) == 1:
        yield ll[0]
    if len(ll) == 2:
        for i in yValue(ll[0], ll[1]):
            yield i
    for tt in getCb(ll):
        for j in yieldValues(list(tt[0])):  # j tuple(v, formula)
            for k in yValue(j, tt[1]):
                yield k


def yieldStructValues(ll):
    #ll list of vStruct.
    if len(ll) == 1:
        yield ll[0]
    if len(ll) == 2:
        for i in yValueStruct(ll[0], ll[1]):
            yield i
    for tt in getCb(ll):
        for j in yieldStructValues(list(tt[0])):  # j tuple(v, formula)
            for k in yValueStruct(j, tt[1]):
                yield k

def isOK(ll, target):
    for i in yieldValues(ll):
        if i == target:
            return True
    return False

def isStructOK(ll, target):
    for i in yieldStructValues(ll):
        if i.value == target:
            return True, i
    return False, None

if __name__ == '__main__':
    pass
    ll = [1,2,3,4]
    # a = valStruct(value=1, valueL=None,valueR=None,operator=None)
    # b = valStruct(value=2, valueL=None, valueR=None, operator=None)
    # for i in yValueStruct(a,b):
    #     print(i)
    # res = isOK(ll, 24)
    # print(res)
    a = [ valStruct(value=i, valueL=None,valueR=None,operator=None)  for i in ll]
    ok, res = isStructOK(a, 10)
    print(res)
