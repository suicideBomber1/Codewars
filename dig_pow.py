def dig_pow(n, p):
    a = [int(d) for d in str(n)]
    sum = 0
    for i in range(len(a)):
        sum += (a[i] ** (p + i))
    if sum % n == 0:
        return sum // n
    else:
        return -1
