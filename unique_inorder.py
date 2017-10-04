def unique_in_order(iterable):
    l = iterable
    n = len(l)
    u = []
    i = 0
    while i < n:
        j = i + 1
        while j < n and l[i] == l[j]:
            j += 1
        u.append(l[i])
        i = j
    return u


result = unique_in_order('AAAABBBCCDAABBB')
print(result)
