import collections


def longest(s1, s2):
    s = s1 + s2
    l = []
    c = collections.Counter(s)
    for i in c.keys():
        l.append(i)
    l.sort()
    return ''.join(l)


a = "xyaabbbccccdefww"
b1 = "xxxxyyyyabklmopq"
longest(a, b1)
