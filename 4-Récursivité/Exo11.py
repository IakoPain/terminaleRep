def puissance(a, n):
    if n == 0:
        return 1
    else:
        return a*puissance(a,n-1)

print(puissance(2,4))