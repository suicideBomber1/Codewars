def filter_list(l):
    'return a new list with the strings filtered out'
    result = []
    for i in l:
        try:
            if i >= 0:
                result.append(i)
        except TypeError:
            pass

    return result


r = filter_list([1, 'a', 'b', 0, 15])
print(r)
