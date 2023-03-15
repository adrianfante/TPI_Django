def mcm(n1, n2):
    max = n1 * n2
    if n1 > n2:
        min = n1
    else:
        min = n2
    while min < max:
        if (min % n1 == 0 and min % n2 == 0):
            return min
        min += 1
    return max

