def mcd(n1, n2):
    if n1 > n2:
        n = n1
    else:
        n = n2
    while n > 0:
        if (n2 % n == 0 and n1 % n == 0):
            return n
        n -= 1
