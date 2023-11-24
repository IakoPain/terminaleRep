def genereDecrementation(n):
    if n==0:
        return [0]
    else:
        return genereDecrementation(n-1)+[n]
print(genereDecrementation(10))
