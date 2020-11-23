def factor(n):
    factors = []
    k = 2
    while k <= n:
        if n % k == 0:
            factors.append(k)
            n /= k
        else:
            k += 1
    return factors